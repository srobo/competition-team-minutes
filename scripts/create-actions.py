#!/usr/bin/env python3

import argparse

import make_github_issue


def process_actions(markdown_file: argparse.FileType, dry_run: bool) -> None:
    print("Processing {}...".format(markdown_file.name))


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
        type=argparse.FileType(mode='w+'),
    )
    return parser.parse_args()


def main(args):
    for markdown_file in args.actions_files:
        process_actions(markdown_file, args.dry_run)


if __name__ == '__main__':
    main(parse_args())
