#!/usr/bin/env python3

import os
import json
import argparse


def load_config(config_path='screpr_config.json') -> dict():
    with open(config_path, 'r') as read_file:
        config_dict = json.load(read_file)

    format_to_path = dict()
    for path, formats in config_dict.items():
        for frmt in formats:
            format_to_path[frmt] = path
    return format_to_path


def walk(config):
    current_sort_path = os.getcwd()
    for path, _, files in os.walk(current_sort_path):
        for filename in files:
            current_file_path = f'{path}/{filename}'
            do_the_move(config, current_file_path, filename)


def do_the_move(config, path, filename):
    file_format = path.split('.')[-1]
    if file_format in config.keys():
        destination = f'{config[file_format]}/{filename}'
        print(f'{path} -->  {destination}')
        # os.rename(current_file_path, destination)


def main():
    try:
        config = load_config()
        walk(config)
    except Exception as e:
        print(str(e))

# input argparse
# validate json via json-scheme
# create dirs

main()