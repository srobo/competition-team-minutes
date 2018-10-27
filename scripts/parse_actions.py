import re
import typing

Action = typing.NamedTuple('Action', (
    ('id', typing.Optional[int]),
    ('owner', str),
    ('title', str),
))

# Matches markdown bullet points, like `* Dave will do a thing`
ACTION_POINT_REGEX = re.compile(r'[\*-]\s+(?P<owner>[-\w\s]+)( will|:) (?P<title>.+)')
ISSUE_LINK_REGEXT = re.compile(r'''
    \(
        \[\#\d+\]
        \(
            https://github.com/srobo/core-team-minutes/issues/(?P<id>\d+)
        \)
    \)
    ''',
    re.VERBOSE,
)


def action_url(action_id: int) -> str:
    return 'https://github.com/srobo/core-team-minutes/issues/{}'.format(action_id)


def action_link(action_id: int) -> str:
    return "[#{}]({})".format(action_id, action_url(action_id))


def parse_action(line: str) -> typing.Optional[Action]:
    match = ACTION_POINT_REGEX.search(line)
    if match is None:
        return

    title = match.group('title')
    if title.endswith('.'):
        title = title[:-1]

    id_ = None
    link_match = ISSUE_LINK_REGEXT.search(title)
    if link_match is not None:
        title = title[:link_match.start()]
        id_ = link_match.group('id')

    title = title.strip()
    title = title[0].upper() + title[1:]

    return Action(
        id=id_,
        owner=match.group('owner'),
        title=title,
    )


def process_actions(text: str) -> typing.Generator[
    Action, # The parsed action
    typing.Optional[int],  # If not `None`, the line will be updated with a link the issue with the given id
    typing.List[str],   # The possibly-updated lines of the document
]:
    lines = text.splitlines()

    action_points_index = lines.index("## Action Points")

    for line in lines[action_points_index:]:
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
            link = " " + action_link(action_id)
            if line.endswith('.'):
                line = line[:-1] + link + '.'
            else:
                line += link

    return lines


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('minutes_file', type=argparse.FileType())
    args = parser.parse_args()

    for action in process_actions(args.minutes_file.read()):
        print(action)
