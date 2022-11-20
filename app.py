#!/usr/bin/env python

import argparse
import logging
from gmail_dot_trick.util import serializer, generate_dot_trick, add_suffix, save_to_file, print_result


def setup_argparse():
    """
    Sets up the arguments for the program

    Returns:
        args (argparse.Namespace): parsed arguments
    """
    parser = argparse.ArgumentParser(
        description="Script to generate gmail addresses using dot trick")

    parser.add_argument("input", type=str,
                        help="email address or the handle (e.g. example@gmail.com or example)")
    parser.add_argument('-e', '--extra', action="store_true",
                        help='generate extra set of addresses with @googlemail.com')

    parser.add_argument('-d', '--debug', action="store_true",
                        help='set log level to DEBUG')
    parser.add_argument('-v', '--version', action='version',
                        version='%(prog)s 0.1.0')
    return parser.parse_args()


def setup_logging(debug):
    """
    Sets up logging module, setting log format and level

    Parameters:
        debug (bool): whether to show debug level in logs or not
    """
    log_level = logging.INFO
    if debug:
        log_level = logging.DEBUG
    logging.basicConfig(
        format="%(asctime)s [%(levelname)-8s] (%(funcName)s:%(lineno)d) %(message)s", level=log_level)


def main():
    args = setup_argparse()
    setup_logging(args.debug)

    logging.info("Script starting")
    logging.debug("Debug!")

    username = serializer(args.input)
    username_dotted = list(generate_dot_trick(username))
    result_list = sorted(
        list(add_suffix(username_dotted, args.extra)), key=len)
    save_to_file(result_list)

    logging.debug(print_result(result_list))
    logging.info("Finished running script, stored results in result.txt")


if __name__ == '__main__':
    main()
