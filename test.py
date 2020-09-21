#!/usr/bin/env python3

import unittest
import os
import json
import tempfile
import screpr_new
import shutil

# json_schema validation:
#   string: list
# folder creation
# if it return z


class MoveFunc(unittest.TestCase):
    def setUp(self):
        self.sort_tmpdir = tempfile.mkdtemp()
        self.sorted_tmpdir = tempfile.mkdtemp()

        print(f'User folder to sort: {self.sort_tmpdir},\nCreated Folder with sorted files: {self.sorted_tmpdir}')

        with open('screpr_config.json', 'r') as read_config:
            old_config = json.load(read_config)
# List of config values 
            old_config.pop('mode')
            self.values = []
            for value in old_config.values():
                self.values.extend(value)
# Creating temporary files for formats
            self.files_list = []
            for frmt in self.values:
                tmp_file = tempfile.NamedTemporaryFile(suffix=f'.{frmt}',
                                                dir=self.sort_tmpdir,
                                                delete=False)
                file_name = tmp_file.name.split('/')[-1]
                self.files_list.append(file_name)
# Creating config
        self.config = {
            f'{self.sorted_tmpdir}/nested': self.values,
            'mode': []}
        

    def tearDown(self):
        shutil.rmtree(self.sorted_tmpdir)
        shutil.rmtree(self.sort_tmpdir)
        print('Test folders deleted')


    def test_screpr_format(self):
        self.config['mode'].append('format-sort')
        screpr_new.screpr(self.sort_tmpdir, self.config)
        res = True
        for file_name in self.files_list:
            src_check = os.path.exists(f'{self.sort_tmpdir}/{file_name}')
            dst_check = os.path.exists(f'{self.sorted_tmpdir}/nested/{file_name}')
            if src_check == True or dst_check == False:
                res = False

        self.assertEqual(res, True)


    def test_screpr_regex(self):
        self.config['mode'].append('regex')
        print('CONF: ', self.config)
        screpr_new.screpr(self.sort_tmpdir, self.config)
        res = True
        for file_name in self.files_list:
            src_check = os.path.exists(f'{self.sort_tmpdir}/{file_name}')
            dst_check = os.path.exists(f'{self.sorted_tmpdir}/nested/{file_name}')
            if src_check == True or dst_check == False:
                res = False

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
#     for frmt_list in config_dict.formats():
#         format_list.extend(frmt_list)

#     files_list = list()
#     for frmt in format_list:
#         filename = tempfile.NamedTemporaryFile(suffix=f'.{frmt}', dir=sort_tmpdir,
#                                             delete=False)
#         files_list.append(filename.name)

#     return files_list
