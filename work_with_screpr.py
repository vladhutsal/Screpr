#!/usr/bin/env python3

import base_screpr
import os
import tempfile

debug = False
create_files = False


def generate_tmpfiles():
    files = ['jpg', 'jpeg', 'avi', 'mp3', 'doc', 'txt']
    for frmt in files:
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
    path = os.path.join(os.getcwd() + '/SORTFOLDER')
    config_path = ('screpr_config.json')
    result = base_screpr.screpr(path, config_path, mode='safe')
    print(result)
