#!/usr/bin/env python3

import argparse
import functools
import typing

from make_github_issue import GitHub, REPO_NAME, REPO_OWNER
from parse_actions import Action, process_actions_returning_lines


class ActionsProcessor:
    def __init__(self, api: GitHub, dry_run: bool) -> None:
        self.api = api
        self.dry_run = dry_run

    def _process_action(
        self,
        action: Action,
        from_url: str,
    ) -> typing.Optional[int]:
        if action.id is not None:
            # Leave existing entries alone
            return action.id

        # TODO: map from names to GitHub logins
        assignee = action.owner
        body = "From {}".format(from_url)

        if self.dry_run:
            print("Would create issue for {} to {!r} with body:{}".format(
                assignee,
                action.title,
                "\n> " + ("\n> ".join(body.splitlines())),
            ))
            return None

        issue = self.api.make_issue(action.title, body, assignee)

        print("Created issue {} assigned to {}: {}".format(
            issue.id,
            ", ".join(issue.assignees),
            issue.title,
        ))

        return issue.id

    def process_actions(self, markdown_file: typing.TextIO) -> None:
        print("Processing {}...".format(markdown_file.name))
        from_url = 'https://github.com/{}/{}/blob/master/{}#specific'.format(
            REPO_OWNER,
            REPO_NAME,
            markdown_file.name,
        )

        markdown_file.seek(0)
        lines = process_actions_returning_lines(
            markdown_file.read(),
            functools.partial(self._process_action, from_url=from_url),
        )

        if not self.dry_run:
            markdown_file.write("\n".join(lines))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--dry-run',
        default=False,
        action='store_true',
    )
    parser.add_argument(
        'actions_files',
        metavar='MINUTES.md',
        nargs='+',
        type=argparse.FileType(mode='r+'),
    )
    return parser.parse_args()


def main(args):
    processor = ActionsProcessor(GitHub(), args.dry_run)

    for markdown_file in args.actions_files:
        processor.process_actions(markdown_file)


if __name__ == '__main__':
    main(parse_args())
