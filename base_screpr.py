#!/usr/bin/env python3

import re
import os
import json
import argparse
import jsonschema


def conf_to_dict(config) -> dict():
    config_dict = dict()
    config.pop('mode')
    for path, values in config.items():
        for value in values:
            config_dict[value] = path
    return config_dict


def load_config(config_path):
    with open(config_path, 'r') as read_file:
        config = json.load(read_file)
        validation_fail = json_validation(config)
        if validation_fail:
            raise Exception
        else:
            return config


def json_validation(config_dict):
    validator = {
        "patternProperties": {
            ".+": {"type": "array"}
        }
    }
    return jsonschema.validate(config_dict, validator)


def create_folders(config):
    for new_folder_path in config.keys():
        if not os.path.isdir(new_folder_path):
            os.mkdir(new_folder_path)


def walk_trhough_files(working_dir, config_dict, mode):
    for path, _, files in os.walk(working_dir):
        if not files:
            raise Exception('Work folder is empty')
        for filename in files:
            if mode == 'regex':
                dest = need_to_move_regex(filename, config_dict)
            elif mode == 'format-sort':
                file_format = filename.split('.')[-1]
                dest = need_to_move_format(config_dict, file_format)
            else:
                raise Exception('Wrong config mode')
            if dest:
                do_the_move(path, dest, filename)


def need_to_move_regex(filename, config_dict):
    for key in config_dict.keys():
        match = re.search(key, filename)
        if match:
            return config_dict[key]


def need_to_move_format(config_dict, file_format):
    if file_format in config_dict.keys():
        return config_dict[file_format]
    return None


def do_the_move(path, dest, filename):
    os.replace(f'{path}/{filename}', f'{dest}/{filename}')


def arg_parsing():
    default_config_name = '/screpr_config.json'

    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='Folder to sort path',
                        metavar='/home/Folder/',
                        type=str,
                        dest='path',
                        # required=True
                        default='/home/rtdge/Documents/vscode/TESTFOLDER')

    parser.add_argument('-conf', default=os.getcwd() + default_config_name,
                        help='Config path(default: current dir)',
                        metavar='/home/cfg.json',
                        type=str,
                        dest='config')

    return parser.parse_args().path, parser.parse_args().config


def screpr(working_dir, config):
    mode = config.get('mode')[0]
    config_dict = conf_to_dict(config)
    create_folders(config)
    walk_trhough_files(working_dir, config_dict, mode)
    print('all done')


def main():
    try:
        working_dir, config_path = arg_parsing()
        config = load_config(config_path)
        screpr(working_dir, config)
    except Exception as excpt:
        print(f'Something went wrong: {excpt}')


if __name__ == "__main__":
    main()



