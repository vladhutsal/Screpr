#!/usr/bin/env python3

import os
import json
import argparse


def load_config(config_path) -> dict():
    with open(config_path, 'r') as read_file:
        config_dict = json.load(read_file)

    format_to_path = dict()
    for path, formats in config_dict.items():
        for frmt in formats:
            format_to_path[frmt] = path
    return format_to_path


def walk(config, sort_path):
    for path, _, files in os.walk(sort_path):
        for filename in files:
            file_path = f'{path}/{filename}'
            do_the_move(config, file_path)


def do_the_move(config, file_path):
    file_format = file_path.split('.')[-1]
    file_name = file_path.split('/')[-1]
    if file_format in config.keys():
        destination = f'{config[file_format]}/{file_name}'
        print(f'{file_path} -->  {destination}')
        # os.rename(current_file_path, destination)


def main():
    try:
        config = load_config(config_path)
        walk(config, sort_path)
    except Exception as e:
        print(f'Wrong config file\n{e}')


def_config_name = '/screpr_config.json'
parser = argparse.ArgumentParser()
parser.add_argument('-c', default=os.getcwd() + def_config_name,
                          help='Config path(default: current dir)',
                          metavar='/home/../cfg.json',
                          type=str,
                          dest='config')

parser.add_argument('-sp', default=os.getcwd(), help='Sort folder path',
                    metavar='/home/../Folder/',
                    type=str,
                    dest='sp')
    
config_path = parser.parse_args().config
sort_path = parser.parse_args().sp

main()


