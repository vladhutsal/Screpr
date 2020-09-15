#!/usr/bin/env python3

import os
import json
import argparse
import jsonschema
from pprint import pprint


def conf_to_dict(config) -> dict():
    config_dict = dict()
    for path, formats in config.items():
            for frmt in formats:
                config_dict[frmt] = path
    return config_dict


def load_config(config_path):
    with open(config_path, 'r') as read_file:
        config = json.load(read_file)
        validate_fail = json_validation(config)
    if not validate_fail:
        return config
    else:
        fails_handling(validate_fail)


def json_validation(config_dict):
    validator = {
    "patternProperties": {
        ".+": {"type": "array"}
    }
}
    return jsonschema.validate('config_dict', validator)


def create_folders(config):
    for new_folder_path in config.keys():
        # print(f'asking mysefl, is there is a dir? {os.path.isdir(new_folder_path)}\n')
        if os.path.isdir(new_folder_path) == False:
            # print(f'making a folder named {new_folder_path}\n')
            os.mkdir(new_folder_path)


def walk(sort_path, config_dict):
    for path, _, files in os.walk(sort_path):
        for filename in files:
            file_format = filename.split('.')[-1]
            dest = need_to_move(config_dict, file_format)
            if dest:
                src = f'{path}/{filename}'
                # print(f'SRC: {src}\n')
                dst = f'{dest}/{filename}'
                # print(f'DST: {dst}\n')
                do_the_move(src, dst)


def need_to_move(config_dict, file_format):
    if file_format in config_dict.keys():
        return config_dict[file_format]
    return None


def do_the_move(src, dst):
    # global res
    # res = (f'{src} => {dst}')
    # return res
    os.replace(src, dst)


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


def fails_handling(excpt):
    if excpt:
        return f'Something went wrong: {str(excpt)}'


def screpr(sort_path, config_dict):
    try:
        walk(sort_path, config_dict)
        print('all done')
    except Exception as excpt:
        print(fails_handling(excpt))


def main():
    config_path, sort_path = arg_parsing()
    config = load_config(config_path)
    config_dict = conf_to_dict(config)
    create_folders(config)

    screpr(sort_path, config_dict)


if __name__ == "__main__":
    main()



