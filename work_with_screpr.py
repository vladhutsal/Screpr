#!/usr/bin/env python3

from Screpr import Screpr
import os
import tempfile
import re

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
    move_dict = screpr.get_files_list(path, cfg_dict)
    print(screpr.move_dict)


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
