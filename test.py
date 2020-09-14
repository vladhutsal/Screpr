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


class TestOutput(unittest.TestCase):
    def test_main_func(self):
        pass


def generate_config_json():
    pass


def generate_files(config_dict, start_tmpdir):
    format_list = list()
    formats = config_dict.values()
    for frmt_list in formats:
        format_list.extend(frmt_list)

    files_list = list()
    for frmt in format_list:
        filename = tempfile.NamedTemporaryFile(suffix=f'.{frmt}', dir=start_tmpdir,
                                            delete=False)
        files_list.append(filename.name)
    return files_list


def main():
    config_path = "/home/rtdge/vscode/Screpr/screpr_config.json"

    with open(config_path, 'r') as read_file:
        config_dict = json.load(read_file)
        config_name = 'screpr_config.json'

    start_tmpdir = tempfile.mkdtemp()      # important
    end_tmpdir = tempfile.mkdtemp()

    files_list = generate_files(config_dict, start_tmpdir)
    
    new_config = dict()     # important
    for folder_path in config_dict.keys():
        folder_name = folder_path.split('/')[-1]
        new_folder_path = f'{end_tmpdir}/{folder_name}'
        new_config[new_folder_path] = config_dict[folder_path]

    new_config_path = f'{start_tmpdir}/{config_name}'
    with open(new_config_path, 'w') as create_new_config:
        json.dump(new_config, create_new_config)

    with open(new_config_path, 'r') as conf:
        config = json.load(conf)
    print(f'START _DIR: {start_tmpdir} START _DIR\n')
    print(f'END_DIR: {end_tmpdir} END_DIR\n')
    pprint.pprint(f'NEW_CONFIG_IS: {config} NEW_CONFIG_IS\n')
    print(f'CONFIG_PATH: {new_config_path} CONFIG_PATH\n')
    screpr_new.handler(start_tmpdir, new_config_path)




if __name__ == '__main__':
    main()





    # os.rmdir(tmpdir)
    # a = os.path.isdir(tmpdir)
    # print(a)

    

        
    
    
