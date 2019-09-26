#! /usr/bin/env python

""" j2cli main file """
from getversion import get_module_version
from j2cli.cli import main

__author__ = "Mark Vartanyan"
__email__ = "kolypto@gmail.com"
__version__ = get_module_version(j2cli)


if __name__ == '__main__':
    main()
