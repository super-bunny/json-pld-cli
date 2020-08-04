import argparse
import json
import os
import sys

import commands


def find_json_file() -> str:
    cwd = os.getcwd()
    for filename in os.listdir(cwd):
        ext = filename.split('.')[-1]
        if ext.lower() == 'json':
            return os.path.realpath(filename)


def read_file(file_path) -> str:
    f = open(file_path, 'r')
    file_content = f.read()
    f.close()
    return file_content


COMMAND_TABLE = {
    'duration': lambda arguments: commands.duration_cmd(pld_content, arguments.get('verbose', False)),
    'distribution': lambda arguments: commands.distribution_cmd(pld_content),
    'assignees': lambda arguments: commands.assignees_cmd(pld_content, arguments.get('user')),
    'test': lambda arguments: print(arguments)
}

json_file_path = find_json_file()
if json_file_path is None:
    print('No json file found')
    sys.exit(1)
pld_content = json.loads(read_file(json_file_path))

parser = argparse.ArgumentParser(description='CLI to generate and manipulate Project Log Document JSON')
subparsers = parser.add_subparsers(dest="command")
parser_duration = subparsers.add_parser('duration')
parser_duration.add_argument('-v', type=bool, dest='verbose', const=True, default=False, nargs='?',
                             help='print estimated duration for each user story')
parser_repartition = subparsers.add_parser('distribution')
parser_assignees = subparsers.add_parser('assignees')
parser_assignees.add_argument('user', type=str, default=None, help='user filter for assignees command')
parser_duration = subparsers.add_parser('test')

args = parser.parse_args()
if args.command in COMMAND_TABLE:
    COMMAND_TABLE[args.command](vars(args))
else:
    parser.print_help()
