# Adapted from https://gist.github.com/JeffPaine/3145490/raw/8583a2f2fdc7d7e4dea1bcf9695bec6dba90c7d8/make_github_issue.py

import json
import getpass
import os.path
import requests


# The repository to add this issue to
REPO_OWNER = 'CHANGEME'
REPO_NAME = 'CHANGEME'


def get_credentials():
    my_dir = os.path.basename(__file__)
    config_file = os.path.join(my_dir, '..', '.config.json')

    data = {}
    username = None
    password = None

    if os.path.exists(config_file):
        with open(config_file, mode='r') as f:
            data = json.load(f)
            username = data['username']
            password = data.get('password')

            if password is not None:
                return username, password

    if username is None:
        username = input("GitHub Username: ")

    if password is None:
        password = getpass.getpass(
            "GitHub Password or Auth Token (for {}): ".format(username)
        )

        store = input("Store password? [y/N]: ")
        if store in ('Y', 'y'):
            data['password'] = password

    with open(config_file, mode='w') as f:
        json.dump(data, f)

    return username, password



def make_github_issue(title, body=None, assignee=None, milestone=None, labels=None):
    '''Create an issue on github.com using the given parameters.'''
    # Our url to create issues via POST
    url = 'https://api.github.com/repos/{}/{}/issues'.format(REPO_OWNER, REPO_NAME)
    # Create an authenticated session to create the issue
    session = requests.session(auth=(USERNAME, PASSWORD))
    # Create our issue
    issue = {'title': title,
             'body': body,
             'assignee': assignee,
             'milestone': milestone,
             'labels': labels}
    # Add the issue to our repository
    r = session.post(url, json.dumps(issue))
    if r.status_code == 201:
        print('Successfully created Issue "{}"'.format(title))
    else:
        print('Could not create Issue "{}"'.format(title))
        print('Response:', r.content)

make_github_issue('Issue Title', 'Body text', 'assigned_user', 3, ['bug'])