import re
import typing

Action = typing.NamedTuple('Action', (
    ('id', typing.Optional[int]),
    ('owner', str),
    ('title', str),
))

ACTION_POINT_REGEX = re.compile(r'[\*-]\s+(?P<owner>[-\w\s]+)( will|:) (?P<title>[^\.]+)')


def action_url(action_id: int) -> str:
    return 'https://github.com/srobo/core-team-minutes/issues/{}'.format(action_id)


def action_link(action_id: int) -> str:
    return "[#{}]({})".format(action_id, action_url(action_id))


def parse_action(line: str) -> typing.Optional[Action]:
    match = ACTION_POINT_REGEX.search(line)
    if match is not None:
        return Action(
            id=None,
            owner=match.group('owner'),
            title=match.group('title'),
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
        if action is not None:
            action_id = yield action
            if action_id is not None:
                line += " " + action_link(action_id)

    return lines


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('minutes_file', type=argparse.FileType())
    args = parser.parse_args()

    for action in process_actions(args.minutes_file.read()):
        print(action)
