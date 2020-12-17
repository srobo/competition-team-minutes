# Competition Team Minutes

Minutes from the [Competition Team][competition-team] meetings.

The canonical instance of this repository is on github at
https://github.com/srobo/competition-team-minutes.

For the SR2019 season, this team was called the "Core Team".

## Agenda

The agenda doc lives in Google Drive, and is linked to the event in the [calendar].

To aid with converting the Google doc into markdown, it's recommended to use [this tool](https://github.com/Mr0grog/google-docs-to-markdown).

## Actions script

Actions from each meeting are recorded as [issues][github-issues] on the github
instance. There is a Python script to support this:
```
./scripts/create-actions.py 2018/2018-11-21.md
```
The script requires Python 3.5+ and the [requests][python-requests] library. It
uses the [GitHub REST API v3][github-rest-api], for which you should create a
[Personal Access Token][api-tokens] with scope `repo:public_repo`.

[competition-team]: https://opsmanual.studentrobotics.org/annual-robotics-competition/competition-programme-team
[github-issues]: https://github.com/srobo/competition-team-minutes/issues
[python-requests]: https://pypi.org/project/requests
[github-rest-api]: https://developer.github.com/v3/issues/
[api-tokens]: https://blog.github.com/2013-05-16-personal-api-tokens/
[calendar]: https://studentrobotics.org/runbook/volunteering/calendars/
