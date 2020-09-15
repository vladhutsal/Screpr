#!/usr/bin/env python3

import unittest
import os
import json
import tempfile
import screpr_new
import shutil
import pprint

# json_schema validation:
#   string: list
# folder creation
# if it return 


def create_files(sort_tmpdir):
    with open('screpr_config.json', 'r') as read_config:
        config = json.load(read_config)
    
    formats = []
    for values in config.values():
        formats.extend(values)
    files_list = []
    for frmt in formats:
        tmp_file = tempfile.NamedTemporaryFile(suffix=f'.{frmt}', dir=sort_tmpdir,
                                             delete=False)
        file_name = tmp_file.name.split('/')[-1]
        files_list.append(file_name)
    return formats, files_list


def existence_check(files_list, src, dst):
    for file_name in files_list:
        src_check = os.path.exists(f'{src}/{file_name}')
        dst_check = os.path.exists(f'{dst}/{file_name}')
        if src_check == True or dst_check == False:
            return False
    return True


def main():
    sort_tmpdir = tempfile.mkdtemp()
    sorted_tmpdir = tempfile.mkdtemp()
    print('SORT:', sort_tmpdir)
    print('SORTED: ', sorted_tmpdir)

    formats, files_list = create_files(sort_tmpdir)
    config_dict = {}
    for frmt in formats:
        config_dict[frmt] = sorted_tmpdir

    screpr_new.walk(sort_tmpdir, config_dict)

    return existence_check(files_list, sort_tmpdir, sorted_tmpdir)
    

class TestBasic(unittest.TestCase):
    def test_move(self):
        res = main()
        self.assertEqual(res, True)


if __name__ == '__main__':
    unittest.main()













# def generate_cfg_dict(end_tmpdir):
#     config_path = '/home/rtdge/vscode/Screpr/screpr_config.json'
#     new_config_name = f'{end_tmpdir}/{config_path.split("/")[-1]}'
#     new_config_path = shutil.copyfile(config_path, new_config_name)

#     with open(new_config_path, 'r') as old_config:
#         config_dict = json.load(old_config)

#     new_config = dict()                         # important
#     for folder_path in config_dict.keys():
#         folder_name = folder_path.split('/')[-1]
#         new_folder_path = f'{end_tmpdir}/{folder_name}'
#         new_config[new_folder_path] = config_dict[folder_path]

#     with open(new_config_path, 'w') as config:
#         json.dump(new_config, config)
        
#     return new_config_path, new_config




# def generate_files(config_dict, sort_tmpdir):
#     format_list = []
#     for frmt_list in config_dict.values():
#         format_list.extend(frmt_list)

#     files_list = list()
#     for frmt in format_list:
#         filename = tempfile.NamedTemporaryFile(suffix=f'.{frmt}', dir=sort_tmpdir,
#                                             delete=False)
#         files_list.append(filename.name)

#     return files_list
