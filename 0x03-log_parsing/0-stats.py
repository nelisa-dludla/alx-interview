#!/usr/bin/env python3
'''
This is my solution to a log parsing
interview question
'''

import sys


total_size = 0
status_counts = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
        }
line_count = 0


def process_line(line):
    '''
    Reads and processes stdin lines
    '''
    global total_size, line_count
    line_parts = line.split()

    if len(line_parts) < 9:
        return

    try:
        status_code = int(line_parts[7])
        file_size = int(line_parts[8])
    except (ValueError, IndexError):
        return

    total_size += file_size

    if status_code in status_counts:
        status_counts[status_code] += 1


def print_stats(total_size, status_counts):
    '''
    Prints the status stats
    '''
    print(f'File size: {total_size}')
    for code in sorted(status_counts):
        count = status_counts[code]
        if count > 0:
            print(f'{code}: {count}')

try:
    for line in sys.stdin:
        process_line(line)
        line_count += 1

        if line_count % 10 == 0:
            print_stats(total_size, status_counts)
except KeyboardInterrupt:
    print_stats(total_size, status_counts)
    sys.exit(0)
