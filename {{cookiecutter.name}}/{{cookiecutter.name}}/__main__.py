#!/usr/bin/env python3

"""Entry point of the project."""

import argparse

parser = argparse.ArgumentParser(description=__doc__)


def main(args=None):
    """Entry point of the script."""
    opts = parser.parse_args(args)

    print(opts)


if __name__ == "__main__":
    main()
