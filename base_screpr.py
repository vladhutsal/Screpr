#!/usr/bin/env python3

import re
import os
import shutil

from Screpr import Screpr
from commandline_mode import arg_parsing


def check_folders(config):
    for new_folder_path in config.keys():
        if not os.path.isdir(new_folder_path):
            os.mkdir(new_folder_path)


def walk_trhough_files(screpr):
    for src_folder, _, files in os.walk(screpr.work_dir_path):
        if not files:
            raise Exception('Work folder is empty')

        for filename in files:
            dst_folder = need_to_move(filename, screpr.screpr_cfg)
            if dst_folder:
                do_the_job(screpr,
                           src_folder,
                           dst_folder,
                           filename)


def need_to_move(filename, screpr_cfg):
    for key in screpr_cfg.keys():
        match = re.search(key, filename)
        if match:
            return screpr_cfg[key]


# function to copy or move files
def do_the_job(screpr, src_folder, dst_folder, filename):
    mode = screpr.mode
    src = f'{src_folder}/{filename}'
    dst = f'{dst_folder}/{filename}'

    if mode == 'safe':
        shutil.copyfile(src, dst)
    elif mode == 'move':
        shutil.move(src, dst)


def clean_after_move(screpr):
    nonempty_folders = []
    for src_folder, _, _ in os.walk(screpr.work_dir_path):
        try:
            os.rmdir(src_folder)
        except OSError:
            nonempty_folders.append(f'{src_folder}\n')

    if nonempty_folders:
        print('There was attempt to delete not empty folders. Didn`t delete:')
    elif not nonempty_folders:
        print('Working dir is clean')


def screpr(work_dir, config_path, *args, **kwargs):
    screpr = Screpr(work_dir, config_path, *args, **kwargs)
    check_folders(screpr.user_cfg)
    walk_trhough_files(screpr)
    if screpr.clean:
        clean_after_move(screpr)
    return 'done'


if __name__ == "__main__":
    output = vars(arg_parsing())
    mode = output.get('mode')
    log = output.get('log')
    src = output.get('path')
    cfg = output.get('config')
    print(src, cfg, mode, log)
