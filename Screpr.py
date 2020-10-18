import re
import os
import json
import jsonschema
import shutil


class Screpr:
    def __init__(self, path, cfg, *args, **kwargs):
        self.work_dir_path = path
        self.cfg_path = cfg

        self.cfg_dict = {}
        self.cfg = None
        self.mode = None
        self.file_name = None
        self.curr_dir = None
        self.dest_dir = None

    def cfg_to_dict(self):
        for path, values in self.cfg.items():
            for value in values:
                self.cfg_dict[value] = path

# ============= Am I loading cfg?
    def load_cfg(self):
        with open(self.cfg_path, 'r') as read_file:
            self.cfg = json.load(read_file)

# ============= add validation error exception of jsonschema

# ============= validate user config
    def json_validation(self):
        validator = {
            "patternProperties": {
                ".+": {"type": "array"}
            }
        }
        return jsonschema.validate(self.cfg_dict, validator)

    def check_folder(self):
        if not os.path.isdir(self.dest_dir):
            os.mkdir(self.dest_dir)

    def walk_through_folders(self):
        for path, _, files in os.walk(self.work_dir_path):
            if not files:
                raise Exception(f'There is no files in {path} folder')

            for filename in files:
                self.file_name = filename
                self.curr_dir = path
                self.dest_dir = self.need_to_move()

                if self.dest_dir:
                    self.check_folder()
                    self.do_the_move()

    def need_to_move(self):
        for key in self.cfg_dict.keys():
            match = re.search(key, self.file_name)
            if match:
                return self.cfg_dict[key]

    def do_the_move(self):
        if not self.mode or self.mode == 'move':
            os.replace(
                f'{self.curr_dir}/{self.file_name}',
                f'{self.dest_dir}/{self.file_name}'
            )

        if self.mode == 'safe':
            shutil.copyfile(
                f'{self.curr_dir}/{self.file_name}',
                f'{self.dest_dir}/{self.file_name}'
            )


def safe(path, config):
    screpr = Screpr(path, config, mode='safe')
    screpr.load_cfg()
    screpr.cfg_to_dict()
    screpr.walk_through_folders()
    return 'done'
