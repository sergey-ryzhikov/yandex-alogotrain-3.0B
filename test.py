#!/usr/bin/env python3

import sys
import argparse
from subprocess import Popen, PIPE, STDOUT

parser = argparse.ArgumentParser()
parser.add_argument('testfile', nargs='?', type=argparse.FileType('r'),
                    default=sys.stdin,
                    help='formatted file with test examples')
args = parser.parse_args()

if args.testfile == sys.stdin and sys.stdin.isatty():  # user forgot to provide testfile data
    parser.print_help()
    exit(0)


def parse_testfile(testfile, default_input_marker='===', default_output_marker='---'):
    """ Example:
    t1-2.py  === ---
    ===
    abc
    ---
    1
    ===
    Hello, 
    World!
    ---
    13
    42
    """
    file = testfile

    # first line is the program to test and (optionally) redifined markers
    firstline = file.readline().strip().rsplit(maxsplit=2)
    line = ['testme.py', default_input_marker, default_output_marker]
    line[:len(firstline)] = firstline  # update defaults with provided values
    prog, input_marker, output_marker = line

    # next lines are test examples
    tests = []
    lineno = 2  # line number: counts from 1, line 1 is a prog name

    eof = False

    while not eof:
        lines_in = []
        lines_out = []

        # reading input
        for line in file:
            lineno += 1
            line = str(line).rstrip('\n\r')  # strip EOL

            if line == input_marker:
                assert len(lines_in) == 0, \
                    f"Format error: no output before next input (line {lineno})"
                continue

            elif line == output_marker:
                break

            lines_in.append(line)
        else:
            raise ValueError(
                    f"Format error: no output for input (line {lineno})")

        # reading output
        for line in file:
            lineno += 1
            line = str(line).rstrip('\n\r')  # strip EOL

            if line == input_marker:
                break
            elif line == output_marker:
                raise ValueError(
                    f"Format error: output without input (line {lineno})")
            lines_out.append(line)
        else:
            eof = True


        # if lines_in and lines_out:
        test = '\n'.join(lines_in), '\n'.join(lines_out)
        tests.append(test)

    return prog, tests


prog, tests = parse_testfile(args.testfile)

prog_args = prog.split()
prog_args = ['python3'] + prog_args


for test in tests:
    vinput, voutput = test
    p = Popen(prog_args, stdout=PIPE, stdin=PIPE, stderr=PIPE)
    stdout_data, stderr_data = p.communicate(input=vinput.encode())

    got = stdout_data.decode().splitlines()
    expected = voutput.splitlines()
    
    if got != expected:
        print("<Input:>")
        print(vinput)
        if(stderr_data):
            print("<Debug:>")
            print(stderr_data.decode())
        print("<Expected:>")
        print('\n'.join(expected))
        print("<Got:>")
        print('\n'.join(got))
        print()

