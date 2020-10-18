#!/usr/bin/env python3

from Screpr import Screpr
import os
import tempfile

path = os.path.join(os.getcwd() + '/SORTFOLDER')
config_path = ('screpr_config.json')

debug = False
create_files = False

screpr = Screpr(path, config_path)


def generate_tmpfiles():
    for frmt in range(3):
        tempfile.NamedTemporaryFile(suffix='',
                                    dir=path,
                                    delete=False)


def debuger(*args):
    if create_files:
        generate_tmpfiles()

    if debug:
        print('CONFIG FILE === ', cfg)
        print('CONFIG DICT === ', cfg_dict)


if __name__ == "__main__":
    cfg = screpr.load_cfg(config_path)
    cfg_dict = screpr.cfg_to_dict(cfg)

    file_list = []
    for path, _, files in os.walk(path):
        cur_dir_file_list = [os.path.join(path, file_path) for file_path in files]
        file_list.extend(cur_dir_file_list)

    print(file_list)

        # screpr.need_to_move_regex()
        # file_list = (file for file in files)
        # print(next(file_list))

    debuger(cfg, cfg_dict)

# screpr.move()


# working_dir, config_path = path, config
# config = load_config(config_path)
# config_dict = conf_to_dict(config)
# create_folders(config)
# walk_trhough_files(working_dir, config_dict, mode)


# 
# "mode": [
#     "regex", "format-sort"
# ],
