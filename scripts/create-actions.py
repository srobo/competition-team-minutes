#!/usr/bin/env python3

import argparse
import ctypes
import functools
import json
import os.path
import platform
import subprocess
import typing
from pathlib import Path

from make_github_issue import GitHub, GitHubIdentity
from parse_actions import (
    REPO_NAME,
    REPO_OWNER,
    Action,
    NoActions,
    process_actions_returning_lines,
)


class FileIsNotInARepositoryError(Exception):
    def __init__(self, file_name: str) -> None:
        super().__init__(
            "The file '{}' is not within a git repository and cannot be "
            "annotated.".format(file_name),
        )
        self.file_name = file_name


def make_repo_relative_url(file_name: str) -> str:
    """
    Given a file name, computes the relative path to that file _from within
    the repo which contains it_.

    This copes with running this tool against files in _other_ repos.
    """
    file_path = Path(file_name).resolve()

    try:
        repo_root = subprocess.check_output(
            ['git', 'rev-parse', '--show-toplevel'],
            cwd=str(file_path.parent),
        ).decode('utf-8').strip()
    except subprocess.CalledProcessError as e:
        if e.returncode == 128:
            # Not a repo
            raise FileIsNotInARepositoryError(file_name) from e

        raise

    relative_path = str(file_path.relative_to(Path(repo_root)))
    relative_url = relative_path.replace(os.path.sep, '/')
    return relative_url


class ActionsProcessor:
    def __init__(
        self,
        api: GitHub,
        name_map: typing.Dict[str, GitHubIdentity],
        dry_run: bool,
        interactive: bool,
    ) -> None:
        self.api = api
        self.name_map = name_map
        self.dry_run = dry_run
        self.interactive = interactive

    def _process_action(
        self,
        action: Action,
        from_url: str,
    ) -> typing.Optional[int]:
        if action.id is not None:
            # Leave existing entries alone
            return None

        try:
            assignee = self.name_map[action.owner]
        except KeyError:
            print(
                "Unknown assignee {!r}. Either adjust the action or add them to"
                " the name map file".format(action.owner),
            )
            return None

        body = "From {}".format(from_url)
        body_for_print = "\n> " + ("\n> ".join(body.splitlines()))

        print()

        if self.interactive:
            response = 'unknown'
            yes_responses = ('y', '')
            while response not in yes_responses + ('n', 'e'):
                response = input("Create issue for @{} to {!r}? [Y/n/e]: ".format(
                    assignee,
                    action.title,
                )).lower()

            if response == 'e':
                existing_id = ''
                while not existing_id.isdigit():
                    existing_id = input("Enter the existing issue id: ").lower()

                return int(existing_id)

            if response not in yes_responses:
                return None

        if self.dry_run:
            print("Would create issue for @{} to {!r} with body:{}".format(
                assignee,
                action.title,
                body_for_print,
            ))
            return None

        print("Creating issue for @{} to {!r} with body:{}".format(
            assignee,
            action.title,
            body_for_print,
        ))

        issue = self.api.make_issue(action.title, body, assignee)

        print("Created issue {} assigned to @{}: {}".format(
            issue.id,
            ", @".join(issue.assignees),
            issue.title,
        ))

        return issue.id

    def process_actions(self, markdown_file: typing.TextIO) -> None:
        print("Processing {}...".format(markdown_file.name))
        from_url = 'https://github.com/{}/{}/blob/master/{}#specific'.format(
            REPO_OWNER,
            REPO_NAME,
            make_repo_relative_url(markdown_file.name),
        )

        markdown_file.seek(0)
        lines = process_actions_returning_lines(
            markdown_file.read(),
            functools.partial(self._process_action, from_url=from_url),
        )

        if not self.dry_run:
            newlines = markdown_file.newlines
            markdown_file.seek(0)
            markdown_file.write(newlines.join(lines))
            markdown_file.write(newlines)


def load_name_map() -> typing.Dict[str, GitHubIdentity]:
    name_map_file = Path(__file__).resolve().parent.parent / '.name_map.json'
    logins_to_names = json.loads(name_map_file.read_text())
    return {
        name: GitHubIdentity(login)
        for login, names in logins_to_names.items()
        for name in names
    }


class Formatter:
    ANSI_BOLD = '\033[1m'
    ANSI_RED = '\033[91m'
    ANSI_ENDC = '\033[0m'

    START = ANSI_BOLD + ANSI_RED

    FALLBACK_START = '** '
    FALLBACK_END = ' **'

    def __init__(self):
        super().__init__()

        self._start, self._end = self.START, self.ANSI_ENDC

        # Assume non-windows platforms will just work
        if platform.system() == 'Windows':
            try:
                self._enable_ansii_escapes()
            except Exception:
                self._start, self._end = self.FALLBACK_START, self.FALLBACK_END

    def _enable_ansii_escapes(self):
        if platform.win32_ver()[0] != '10':
            raise Exception("Windows versions before 10 don't support ANSII escapes")

        # From https://stackoverflow.com/a/36760881 - enable support for ANSII
        # escape sequences on Windows 10
        kernel32 = ctypes.windll.kernel32
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

    def as_error(self, message: str) -> None:
        return self._start + message + self._end


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--commit',
        dest='dry_run',
        default=True,
        action='store_false',
    )
    parser.add_argument(
        '-i',
        '--interactive',
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
    name_map = load_name_map()

    processor = ActionsProcessor(
        GitHub(REPO_OWNER, REPO_NAME),
        name_map,
        args.dry_run,
        args.interactive,
    )

    errors = []
    for markdown_file in args.actions_files:
        try:
            processor.process_actions(markdown_file)
        except NoActions:
            errors.append("WARNING: no actions were found in {!r}".format(
                markdown_file.name,
            ))

    if errors:
        formatter = Formatter()
        for message in errors:
            print(formatter.as_error(message))

    return 1 if errors else 0


if __name__ == '__main__':
    exit(main(parse_args()))
