import re
import typing
import urllib.parse

REPO_OWNER = 'srobo'
REPO_NAME = 'competition-team-minutes'

Action = typing.NamedTuple('Action', (
    ('id', typing.Optional[int]),
    ('owner', str),
    ('title', str),
))

ISSUES_URL = 'https://github.com/{}/{}/issues/'.format(REPO_OWNER, REPO_NAME)

# Matches markdown bullet points, like `* Dave will do a thing`
ACTION_POINT_REGEX = re.compile(r'[\*-]\s+(?P<owner>[-\w\s]+)( will|:) (?P<title>.+)')
ISSUE_LINK_REGEXT = re.compile(
    r'''
    \(
        \[\#\d+\]
        \(
            {issues_url}(?P<id>\d+)
        \)
    \)
    '''.format(issues_url=re.escape(ISSUES_URL)),
    re.VERBOSE,
)


class NoActions(Exception):
    pass


def action_url(action_id: int) -> str:
    return urllib.parse.urljoin(ISSUES_URL, str(action_id))


def action_link(action_id: int) -> str:
    return "[#{}]({})".format(action_id, action_url(action_id))


def sentence_case(string: str) -> str:
    """
    Capitalise the first character of a string.

    This approximates a conversion to "Sentence case" but intentionally
    _doesn't_ lowercase the string first, in order to copy with phrases which
    contain other proper nouns.
    """
    return string[0].upper() + string[1:]


def parse_action(line: str) -> typing.Optional[Action]:
    match = ACTION_POINT_REGEX.search(line)
    if match is None:
        return None

    title = match.group('title')
    if title.endswith('.'):
        title = title[:-1]

    id_ = None
    link_match = ISSUE_LINK_REGEXT.search(title)
    if link_match is not None:
        title = title[:link_match.start()]
        id_ = int(link_match.group('id'))

    title = sentence_case(title.strip())

    return Action(
        id=id_,
        owner=match.group('owner'),
        title=title,
    )


def process_actions(text: str) -> typing.Generator[
    Action,  # The parsed action
    typing.Optional[int],  # If not `None`, the line will be updated with a link to the issue with the given id
    typing.List[str],   # The possibly-updated lines of the document
]:
    lines = text.splitlines()

    try:
        action_points_index = lines.index("## Action Points")
    except ValueError:
        raise NoActions from None

    for idx, line in enumerate(
        lines[action_points_index:],
        start=action_points_index,
    ):
        action = parse_action(line)
        if action is None:
            continue

        action_id = yield action
        if action_id is not None:
            if action.id is not None:
                raise ValueError(
                    "Asked to add link which was already present for line:{}".format(
                        line,
                    ),
                )

            line = line.rstrip()
            link = " ({})".format(action_link(action_id))
            if line.endswith('.'):
                line = line[:-1] + link + '.'
            else:
                line += link

            lines[idx] = line

    return lines


def process_actions_returning_lines(
    text: str,
    callback: typing.Callable[[Action], typing.Optional[int]],
) -> typing.List[str]:
    generator = process_actions(text)
    value = next(generator)
    try:
        while True:
            value = generator.send(callback(value))
    except StopIteration as e:
        return e.args[0]


if __name__ == '__main__':
    import argparse
    import sys
    parser = argparse.ArgumentParser()
    parser.add_argument('minutes_file', type=argparse.FileType())
    args = parser.parse_args()

    def func(action: Action):
        print(action, file=sys.stderr)
        if action.id is None:
            return 0

    for line in process_actions_returning_lines(args.minutes_file.read(), func):
        print(line)
