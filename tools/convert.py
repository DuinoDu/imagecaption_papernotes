#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import argparse
import os

def convert(args):
    with open(args.input, 'r') as fid:
        lines = fid.readlines()

    new_lines = []
    start = False
    cur_seg = ""
    for enum, line in enumerate(lines):
        if line == '\n' and cur_seg != "":
            new_lines.append(cur_seg+'\n')
            cur_seg = ""
        if line != '\n':
            line = line.strip()
            if 'github' in line:
                cur_seg += '[code]({}) '.format(line[line.find('http'):])
            elif 'arxiv' in line or 'paper' in line:
                cur_seg += '[paper]({}) '.format(line[line.find('http'):])
            
            if enum > 0 and lines[enum-1] == '\n':
                cur_seg += '- '
                cur_seg += line
                cur_seg += ' '
    
    with open(args.ouput, 'w') as fid:
        for line in new_lines:
            fid.write(line)
    print('Saved')


def main(args):
    convert(args)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Save paper list in html to md')
    # addarg here
    parser.add_argument('--input', default=None, type=str, help='input file')
    parser.add_argument('--output', default='result.md', type=str, help='output file')
    args = parser.parse_args()
    main(args)

