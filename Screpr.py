import re
import os
import json
import jsonschema


class Screpr:
    def __init__(self, path, cfg):
        self.cfg = cfg
        self.path = path
        self.mode = None
        self.move_dict = {}

    def cfg_to_dict(self, cfg) -> dict():
        cfg_dict = dict()
        for path, values in cfg.items():
            for value in values:
                cfg_dict[value] = path
        return cfg_dict

    def load_cfg(self, cfg_path):
        with open(cfg_path, 'r') as read_file:
            cfg = json.load(read_file)
            validation_fail = self.json_validation(cfg)
            if validation_fail:
# ============= add validation error exception of jsonschema
                raise Exception
            else:
                return cfg

    def json_validation(self, cfg_dict):
        validator = {
            "patternProperties": {
                ".+": {"type": "array"}
            }
        }
        return jsonschema.validate(cfg_dict, validator)

    def create_folders(cfg):
        for new_folder_path in cfg.keys():
            if not os.path.isdir(new_folder_path):
                os.mkdir(new_folder_path)

    def get_files_list(self, working_dir, cfg_dict):
        for path, _, files in os.walk(working_dir):
            if not files:
                raise Exception(f'There is no files in {path} folder')

            for filename in files:
                curr_file_path = os.path.join(path, filename)
                file_dest = self.need_to_move(filename, cfg_dict)

                if file_dest in self.move_dict:
                    self.move_dict[file_dest].append(curr_file_path)
                else:
                    self.move_dict[file_dest] = [curr_file_path]

    def need_to_move(self, filename, cfg_dict):
        for key in cfg_dict.keys():
            match = re.search(key, filename)
            if match:
                return cfg_dict[key]

# ============= TODO:
    def need_to_move_format(cfg_dict, file_format):
        if file_format in cfg_dict.keys():
            return cfg_dict[file_format]
        return None

    def do_the_move(self, path, dest, filename):
        os.replace(f'{path}/{filename}', f'{dest}/{filename}')

    def screpr(self, working_dir, cfg):
        cfg_dict = self.conf_to_dict(cfg)
        self.create_folders(cfg)
        self.get_files_list(working_dir, cfg_dict)
        print('all done')

    def move(self):
        try:
            working_dir, cfg_path = self.path, self.cfg
            cfg = self.load_cfg(cfg_path)
            self.screpr(working_dir, cfg)
        except Exception as excpt:
            print(f'Something went wrong: {excpt}')
