import logging
import logging.handlers
import os
import sys
import argparse

logger = logging.getLogger(os.path.splitext(os.path.basename(sys.argv[0]))[0])


class CustomFormatter(argparse.RawDescriptionHelpFormatter,
                      argparse.ArgumentDefaultsHelpFormatter):
        pass

def parse_args(args=sys.argv[1:]):
    parser = argparse.ArgumentParser(
        description=sys.modules[__name__].__doc__,
        formatter_class=CustomFormatter
    )

    g = parser.add_argument_group('fizzbuzz settings')
    g = parser.add_mutually_exclusive_group()
    g.add_argument('--debug', '-d', action="store_true",
            default=False,
            help="enable debug")

    g.add_argument('--silent', '-s', action="store_true",
        default=False,
        help="don't log to console")

    g.add_argument('--fizz', metavar="N",
                    default=3,
                    type=int,
                    help="Modulo value for fizz"
    )
    g.add_argument('--buzz', metavar="N",
        default=5,
        type=int,
        help="Modulo value for buzz")
    
    parser.add_argument("start", type=int, help="Start value")
    parser.add_argument("end", type=int, help="Start value")

    return parser.parse_args(args)

options = parse_args()

def setup_logging(options):
    """Configure logging"""
    root = logging.getLogger("")
    root.setLevel(logging.WARNING)
    logger.setLevel(options.debug and logging.DEBUG or logging.INFO)
    if not options.silent:
        ch = logging.StreamHandler()
        ch.setFormatter(logging.Formatter(
            "%(levelname)s[%(name)s] %(message)s"))
        root.addHandler(ch)

    
if __name__ == '__main__':
    options = parse_args()
    setup_logging(options)

    try:
        logger.debug("compute fuzz buz from {} to {}".format(options.start, options.end))

        for n in range(options.start, options.end + 1):
            if n % 3 == 0 and n % 5 == 0:
                print('fizzbuzz')
            elif n % 3 == 0:
                print('fooz')
            elif n % 5 == 0:
                print('bazz')
            else:
                print(n)
    except Exception as e:
        logger.exception("%s", e)
        sys.exit(1)
    sys.exit(0)