#!/usr/bin/env python3

import argparse

import make_github_issue


def process_actions(markdown_file: argparse.FileType):
    print("Processing {}...".format(markdown_file.name))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'actions_files',
        metavar='MINUTES.md',
        nargs='+',
        type=argparse.FileType(mode='w+'),
    )
    return parser.parse_args()


def main(args):
    for markdown_file in args.actions_files:
        process_actions(markdown_file)


if __name__ == '__main__':
    main(parse_args())
