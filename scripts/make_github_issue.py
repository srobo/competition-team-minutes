# Adapted from https://gist.github.com/JeffPaine/3145490/raw/8583a2f2fdc7d7e4dea1bcf9695bec6dba90c7d8/make_github_issue.py

import json
import getpass
from pathlib import Path
import typing

import requests


# The repository to add this issue to
REPO_OWNER = 'srobo'
REPO_NAME = 'core-team-minutes'


def get_credentials() -> typing.Tuple[str, str]:
    config_file = Path(__file__).parent.parent / '.config.json'

    data = {}  # type: typing.Dict[str, str]
    username = None
    password = None

    if config_file.exists():
        with config_file.open() as f:
            data = json.load(f)
            username = data['username']
            password = data.get('password')

            if password is not None:
                return username, password

    if username is None:
        data['username'] = username = input("GitHub Username: ")

    if password is None:
        password = getpass.getpass(
            "GitHub Password or Auth Token (for {}): ".format(username)
        )

        store = input("Store password? [y/N]: ")
        if store in ('Y', 'y'):
            data['password'] = password

    with config_file.open(mode='w') as f:
        json.dump(data, f)

    return username, password


class FailedToCreateIssue(Exception):
    def __init__(self, title, response):
        super().__init__("Failed to created issue {!r}".format(title))
        self.response = response


class GitHub:
    URL = 'https://api.github.com/repos/{}/{}/issues'.format(
        REPO_OWNER,
        REPO_NAME,
    )

    def __init__(self) -> None:
        self.session = requests.Session()
        self.session.auth = get_credentials()

    def make_issue(self, title: str, body: str, assignee: str) -> None:
        '''Create an issue on github.com using the given parameters.'''
        # Create our issue
        issue = {
            'title': title,
            'body': body,
            'assignee': assignee,
        }
        # Add the issue to our repository
        response = self.session.post(self.URL, json=issue)
        response.raise_for_status()
        if response.status_code != 201:
            raise FailedToCreateIssue(title, response)
