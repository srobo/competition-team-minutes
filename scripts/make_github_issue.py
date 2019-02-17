# Adapted from https://gist.github.com/JeffPaine/3145490/revisions#diff-6c74585fc93fb54ed50f85e4166e2fb4

import getpass
import json
import typing
from pathlib import Path

import requests

GitHubIdentity = typing.NewType('GitHubIdentity', str)

Issue = typing.NamedTuple('Issue', (
    ('id', int),
    ('url', str),
    ('assignees', typing.List[GitHubIdentity]),
    ('title', str),
))


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
    def __init__(self, repo_owner: str, repo_name: str) -> None:
        self.session = requests.Session()
        self.session.auth = get_credentials()

        self.issues_api_url = 'https://api.github.com/repos/{}/{}/issues'.format(
            repo_owner,
            repo_name,
        )

    def make_issue(self, title: str, body: str, assignee: GitHubIdentity) -> Issue:
        '''Create an issue on github.com using the given parameters.'''
        # Create our issue
        issue = {
            'title': title,
            'body': body,
            'assignee': assignee,
        }
        # Add the issue to our repository
        response = self.session.post(self.issues_api_url, json=issue)
        response.raise_for_status()
        if response.status_code != 201:
            raise FailedToCreateIssue(title, response)

        data = response.json()

        return Issue(
            data['number'],
            data['html_url'],
            [GitHubIdentity(x['login']) for x in data['assignees']],
            data['title'],
        )
