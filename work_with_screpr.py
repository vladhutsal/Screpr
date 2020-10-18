#!/usr/bin/env python3

import Screpr
import os
import tempfile
import re



# debug = False
# create_files = False

# def generate_tmpfiles():
#     for frmt in range(3):
#         tempfile.NamedTemporaryFile(suffix='',
#                                     dir=path,
#                                     delete=False)


# def debuger(*args):
#     if create_files:
#         generate_tmpfiles()

#     if debug:
#         print('CONFIG FILE === ', cfg)
#         print('CONFIG DICT === ', cfg_dict)


if __name__ == "__main__":
    path = os.path.join(os.getcwd() + '/SORTFOLDER')
    config_path = ('screpr_config.json')
    result = Screpr.safe(path, config_path)
    print(result)
