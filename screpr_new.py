#!/usr/bin/env python3

import os
import json
import argparse
import jsonschema


def load_config(config_path) -> dict():
    with open(config_path, 'r') as read_file:
        config_dict = json.load(read_file)

    format_to_path = dict()
    for path, formats in config_dict.items():
        for frmt in formats:
            format_to_path[frmt] = path
    return format_to_path


def walk(config, sort_path):
    print('replacing files..')
    for path, _, files in os.walk(sort_path):
        for filename in files:
            file_format = filename.split('.')[-1]
            dest = need_to_move(config, file_format)
            if dest:
                src = f'{path}/{filename}'
                do_the_move(config, src, f'{dest}/{filename})


def need_to_move(config, file_format):
    if file_format in config.keys():
        return config[file_format]
    return None


def do_the_move(config, src, dst):
    pass


def maintance():
    def_config_name = '/screpr_config.json'

    parser = argparse.ArgumentParser()
    parser.add_argument('-c', default=os.getcwd() + def_config_name,
                help='Config path(default: current dir)',
                metavar='/home/../cfg.json',
                type=str,
                dest='config'
            )
    parser.add_argument('-sp', default=os.getcwd(), help='Sort folder path',
                metavar='/home/../Folder/',
                type=str,
                dest='sp'
            )
    return parser.parse_args().config, parser.parse_args().sp


def main():
    config_path, sort_path = maintance()
    try:
        config = load_config(config_path)
        print('Config is loaded..')
        walk(config, sort_path)
        print('done!')
    except Exception as e:
        print(f'Wrong config file: {str(e)}')


if __name__ == "__main__":
    main()



