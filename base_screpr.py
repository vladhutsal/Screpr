#!/usr/bin/env python3

import re
import os
import shutil
import json
import argparse
import jsonschema


class Screpr:
    def __init__(self, workdir_path, cfg_path, mode, log):
        self.work_dir_path = workdir_path
        self.cfg_path = cfg_path
        self.mode = mode
        self.log = log

        self.user_cfg = self.load_cfg()
        self.screpr_cfg = self.user_cfg_to_dict()

    def load_cfg(self):
        with open(self.cfg_path, 'r') as read_file:
            config = json.load(read_file)
            validation_fail = self.json_validation(config)
            if validation_fail:
                raise Exception

            return config

    def user_cfg_to_dict(self):
        screpr_cfg = {}
        for path, values in self.user_cfg.items():
            for value in values:
                screpr_cfg[value] = path

        return screpr_cfg

    def json_validation(self, config):
        validator = {
            "patternProperties": {
                ".+": {"type": "array"}
            }
        }
        return jsonschema.validate(config, validator)


def check_folders(config):
    for new_folder_path in config.keys():
        if not os.path.isdir(new_folder_path):
            os.mkdir(new_folder_path)


def walk_trhough_files(screpr):
    for folder_path, _, files in os.walk(screpr.work_dir_path):
        if not files:
            raise Exception('Work folder is empty')

        for filename in files:
            dest = need_to_move(filename, screpr.screpr_cfg)
            if dest:
                do_the_job(screpr.mode, folder_path, dest, filename)


def need_to_move(filename, screpr_cfg):
    for key in screpr_cfg.keys():
        match = re.search(key, filename)
        if match:
            return screpr_cfg[key]


# function to copy or move files
def do_the_job(mode, folder_path, dest, filename):
    src = f'{folder_path}/{filename}'
    dst = f'{dest}/{filename}'

    if mode == 'safe':
        shutil.copyfile(src, dst)
    elif not mode or mode == 'move':
        shutil.move(src, dst)


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


def screpr(working_dir, config_path, *args, **kwargs):
    mode = kwargs.get('mode') or None
    log = kwargs.get('log') or False
    screpr = Screpr(working_dir, config_path, mode, log)
    check_folders(screpr.user_cfg)
    walk_trhough_files(screpr)
    return 'done?'
