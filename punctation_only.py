#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import argparse
import re


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', required=True, help="Path to input file")
    parser.add_argument('-o', '--output', required=True, help="Path to output file")
    args = parser.parse_args()

    input_text = open(args.input).read()

    output_file = open(args.output, "w")
    output_text = re.sub("[^.,!?()\"]*", "", input_text)
    output_file.write(output_text)
    output_file.close()

    frequency = {x:output_text.count(x) for x in output_text}
    print frequency


