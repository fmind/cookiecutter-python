#!/usr/bin/env python3
"""Entry point of the project"""

import argparse

PARSER = argparse.ArgumentParser(description=__doc__)


def main(argv=None):
    """Entry point of the script."""
    args = PARSER.parse_args(argv)

    print(args)


if __name__ == "__main__":
    main()
