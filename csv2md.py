# -*- coding: utf-8 -*-
"""
@author: Andreas J. Poulsen
"""

import argparse
import codecs
import csv
import sys


def parse_args(args):
    parser = argparse.ArgumentParser(description="Convert CSV file to a MD table.")
    parser.add_argument("csv", type=str,
                        help="Location of CSV file for conversion into MD")
    parser.add_argument("-d", "--delimiter", type=str, default=',',
                        help="Delimiter for the CSV file.")
    parser.add_argument("-o", "--out", type=str,
                        help="Location of output file.")
    parser.add_argument("-H", "--header", action="store_true", default=False,
                        help="If sat will treat first row as a header")
    parser.add_argument("-a", "--no-align", action="store_true", default=False,
                        help="If sat the rows will not be aligned.")
    return parser.parse_args(args)


def get_max(lst):
    """Return maximum string length present in each column of a list of lists
    
    lst
        a list of lists containing only strings
    """
    lst = list(zip(*lst))  # Transposing the CSV
    lst = list(map(lambda x: list(map(len, x)), lst))  # len() on all elements
    return list(map(max, lst))  # Getting max of length of each column


def make_table(csv, maxes = [], header=False):
    """Returns a string with a markdown table corresponding to the csv given
    
    csv
        list of lists of strings corresponding to the csv
    maxes
        maximum space allocated to each element per column given as a list of
        integers. If an empty list is given no extra padding will be added and
        no aligning will occur. Must be same length as csv[0].
    header
        chooses if first row is treated as header
    """
    if len(maxes):
        line_string = "|" + "|".join(["{:" + str(maxx) + "}" for maxx in maxes]) + "|\n"
        header_seperator = "".join(["|" + "-" * maxx for maxx in maxes]) + "|\n"
    else:
        line_string = "|" + "|".join(["{}" for i in csv[0]]) + "|\n"
        header_seperator = "|-" * len(csv[0]) + "|\n"
    out = ""
    for i, row in enumerate(csv):
        out += line_string.format(*row)
        if i == 0 and header:
            out += header_seperator
    return out

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])

    with codecs.open(args.csv, 'r', "UTF-8") as file:
        reader = csv.reader(file, delimiter=args.delimiter)
        csv_file = list(reader)
    
    if args.no_align:
        maxes = []
    else:
        maxes = get_max(csv_file)
    
    out = make_table(csv_file, maxes, args.header)
    if args.out is None:
        print(out)
    else:
        with codecs.open(args.out, 'w', "UTF-8") as file:
            file.write(out)
            file.close()