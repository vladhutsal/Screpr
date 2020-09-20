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
    return jsonschema.validate(config_dict, validator)


def create_folders(config):
    for new_folder_path in config.keys():
        # print(f'asking mysefl, is there is a dir? {os.path.isdir(new_folder_path)}\n')
        if os.path.isdir(new_folder_path) == False:
            # print(f'making a folder named {new_folder_path}\n')
            os.mkdir(new_folder_path)


def move(working_dir, config_dict):
    for path, _, files in os.walk(working_dir):
        for filename in files:
            file_format = filename.split('.')[-1]
            dest = need_to_move(config_dict, file_format)
            if dest:
                src = f'{path}/{filename}'
                dst = f'{dest}/{filename}'
                do_the_move(src, dst)


def need_to_move(config_dict, file_format):
    if file_format in config_dict.keys():
        return config_dict[file_format]
    return None


def do_the_move(src, dst):
    os.replace(src, dst)


def arg_parsing():
    default_config_name = '/screpr_config.json'

    parser = argparse.ArgumentParser()
    parser.add_argument('-c', default=os.getcwd() + default_config_name,
                help='Config path(default: current dir)',
                metavar='/home/cfg.json',
                type=str,
                dest='config'
            )
    parser.add_argument('-sp', default=os.getcwd(), help='Sort folder path',
                metavar='/home/Folder/',
                type=str,
                dest='sp'
            )
    return parser.parse_args().config, parser.parse_args().sp


def fails_handling(excpt):
    if excpt:
        return f'Something went wrong: {str(excpt)}'


def screpr(working_dir, config):
    try:
        config_dict = conf_to_dict(config)
        create_folders(config)
        move(working_dir, config_dict)
        print('all done')
    except Exception as excpt:
        print(fails_handling(excpt))


def main():
    config_path, working_dir = arg_parsing()
    config = load_config(config_path)

    screpr(working_dir, config)


if __name__ == "__main__":
    main()



