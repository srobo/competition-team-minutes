# Core Team Minutes

Minutes from the [Core Team][core-team] meetings.

The canonical instance of this repository is on github at
https://github.com/srobo/core-team-minutes.

Actions from each meeting are recorded as [issues][github-issues] on the github
instance. There is a Python script to support this:
```
./scripts/create-actions.py 2018/2018-11-21.md
```
The script requires Python 3.5+ and the [requests][python-requests] library. It
uses the [GitHub REST API v3][github-rest-api], for which you should create a
[Personal Access Token][api-tokens] with scope `repo:public_repo` is _strongly_
recommended instead.

[core-team]: https://srobo.gitbook.io/ops-manual/annual-robotics-competition/core-team
[github-issues]: https://github.com/srobo/core-team-minutes/issues
[python-requests]: https://pypi.org/project/requests
[github-rest-api]: https://developer.github.com/v3/issues/
[api-tokens]: https://blog.github.com/2013-05-16-personal-api-tokens/
