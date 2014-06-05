import sys, os
import re
from pprint import pprint


def convert(number):
    ratio = float(number) / 640.0 * 100.0;
    return "{0:.1f}%".format(ratio)

def read_file(filename):
    f = open(filename)
    for line in f:
        results = re.findall("[0-9]+px", line)    
        pos = 0
        new_line = ""
        for match in results:
            new_pos = line.find(match, pos)
            new_line += line[pos : new_pos]
            new_pos += len(match)
            pos = new_pos
            ratio = convert(match[:-2])
            new_line += ratio

        new_line += line[pos : -1]
        print new_line

if __name__ == "__main__":
    #line = '<img src="/img/cancel.png" data-dismiss="modal" class="pull-right close" style="width: 50px; position:relative; left:35px; bottom:35px">'

    read_file(sys.argv[1])

