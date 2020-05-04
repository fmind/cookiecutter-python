#!/usr/bin/env python3

"""Main script of the project."""

import argparse

PARSER = argparse.ArgumentParser(description=__doc__)


def main(args=None):
    """Main script of the project."""
    opts = PARSER.parse_args(args)
    print(opts)


if __name__ == "__main__":
    main()
