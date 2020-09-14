#!/usr/bin/env python3

import os
import json
import argparse
import jsonschema
from pprint import pprint


def json_validation(config_dict):
    validator = {
    "patternProperties": {
        ".+": {"type": "array"}
    }
}
    return jsonschema.validate('config_dict', validator)


def load_config(config_path) -> dict():
    with open(config_path, 'r') as read_file:
        config_dict = json.load(read_file)
        validate_fail = json_validation(config_dict)
    if not validate_fail:
        format_to_path = dict()
        check_folders(config_dict)
        for path, formats in config_dict.items():
            for frmt in formats:
                format_to_path[frmt] = path
        return format_to_path
    else:
        exception_handling(validate_fail)


def check_folders(config_dict):
    for new_folder_path in config_dict.keys():
        if os.path.isdir(new_folder_path) == False:
             os.mkdir(new_folder_path)


def walk(config_dict, sort_path):
    for path, _, files in os.walk(sort_path):
        for filename in files:
            file_format = filename.split('.')[-1]
            dest = need_to_move(config_dict, file_format)
            if dest:
                src = f'{path}/{filename}'
                do_the_move(src, f'{dest}/{filename}')


def need_to_move(config_dict, file_format):
    if file_format in config_dict.keys():
        return config_dict[file_format]
    return None


def do_the_move(src, dst):
    print(f'{src} => {dst}')
    # os.replace(src, dst)


def arg_parsing():
    default_config_name = '/screpr_config.json'

    parser = argparse.ArgumentParser()
    parser.add_argument('-c', default=os.getcwd() + default_config_name,
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


def exception_handling(excpt):
    if excpt:
        return f'Something went wrong: {str(excpt)}'


def main():
    config_path, sort_path = arg_parsing()
    try:
        config_dict = load_config(config_path)
        walk(config_dict, sort_path)
    except Exception as excpt:
        print(exception_handling(excpt))


if __name__ == "__main__":
    main()



