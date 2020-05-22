#!/usr/bin/env python3

"""Main script of the project."""

import argparse

parser = argparse.ArgumentParser(description=__doc__)


def main(args=None):
    """Main script of the project."""
    opts = parser.parse_args(args)

    print(opts)


if __name__ == "__main__":
    main()
