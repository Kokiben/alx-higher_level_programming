#!/usr/bin/python3
"""Receives input from standard input and computes metrics.

After every ten lines or the upon of a keyboard interruption (CTRL + C),
outputs the following statistics:
    - Total size of the file processed thus far.
    - Number of status codes encountered up to that point.
"""


def pri_stats(siz, sttus_codes):
    """Print aggregated metrics.

    Args:
        siz (int): Aggregated read file size.
        sttus_codes (dict): Aggregated of status codes.
    """
    print("File size: {}".format(siz))
    for ky in sorted(sttus_codes):
        print("{}: {}".format(ky, sttus_codes[ky]))


if __name__ == "__main__":
    import sys

    siz = 0
    sttus_codes = {}
    vali_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    num = 0

    try:
        for line in sys.stdin:
            if num == 10:
                pri_stats(siz, sttus_codes)
                num = 1
            else:
                num += 1

            line = line.split()

            try:
                siz += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in vali_codes:
                    if sttus_codes.get(line[-2], -1) == -1:
                        sttus_codes[line[-2]] = 1
                    else:
                        sttus_codes[line[-2]] += 1
            except IndexError:
                pass

        pri_stats(siz, sttus_codes)

    except KeyboardInterrupt:
        pri_stats(siz, sttus_codes)
        raise
