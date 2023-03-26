from __future__ import annotations

import argparse
import re
import sys
from argparse import ArgumentParser
from collections.abc import Sequence
from pathlib import Path


ALLOW_HTTP_LATER_RE = re.compile(
    r'allow-http-in-([0-9]+)-lines'
)
ALLOW_HTTP_RE = re.compile(
    r'allow-http'
)


def main() -> int:
    args = parse_args()

    retval = 0
    for file in args.files:
        content = file.read_text()
        new_content = ''
        laters = []
        for line in content.splitlines(keepends=True):
            allow_later = ALLOW_HTTP_LATER_RE.search(line)
            if allow_later:
                laters.append(int(allow_later.group(1)))
            if ALLOW_HTTP_RE.search(line):
                new_content += line
                continue
            laters = [later - 1 for later in laters]
            if 0 in laters:
                laters.remove(0)
                new_content += line
                continue

            new_line = line.replace('http://', 'https://')  # allow-http
            new_content += new_line

        if new_content != content:
            file.write_text(new_content)
            retval = 1

    return retval


class Args(argparse.Namespace):
    files: Sequence[Path]


def parse_args() -> Args:
    parser = ArgumentParser('enforce-https')

    parser.add_argument(
        'files',
        nargs='+',
        type=Path,
    )

    return parser.parse_args(namespace=Args())


if __name__ == '__main__':
    sys.exit(main())
