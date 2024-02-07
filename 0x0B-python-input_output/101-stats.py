#!/usr/bin/python3
"""Receives input from standard input and computes metrics.

After every ten lines or the upon of a keyboard interruption (CTRL + C),
outputs the following statistics:
    - Total size of the file processed thus far.
    - Number of status codes encountered up to that point.
"""


def print_stats(size, status_codes):
    """Print aggregated metrics.

    Args:
        size (int): Aggregated read file size.
        status_codes (dict): Aggregated number of status codes.
    """
    print("File size: {}".format(size))
    for ky in sorted(status_codes):
        print("{}: {}".format(ky, status_codes[ky]))


if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    num = 0

    try:
        for line in sys.stdin:
            if num == 10:
                print_stats(size, status_codes)
                num = 1
            else:
                num += 1

            line = line.split()

            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_codes:
                    if status_codes.get(line[-2], -1) == -1:
                        status_codes[line[-2]] = 1
                    else:
                        status_codes[line[-2]] += 1
            except IndexError:
                pass

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
