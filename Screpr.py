import json
import jsonschema


class Screpr:
    def __init__(self, work_dir_path, cfg_path, *args, **kwargs):
        self.work_dir_path = work_dir_path
        self.cfg_path = cfg_path

        self.mode = kwargs.get('mode') or 'move'
        self.log = kwargs.get('log') or False
        self.clean = kwargs.get('clean') or False

        self.user_cfg = self.load_cfg()
        self.screpr_cfg = self.user_cfg_to_dict()

    def load_cfg(self):
        with open(self.cfg_path, 'r') as read_file:
            config = json.load(read_file)
            validation_fail = self.json_validation(config)
            if validation_fail:
                raise Exception

            return config

    def user_cfg_to_dict(self):
        screpr_cfg = {}
        for path, user_regexs in self.user_cfg.items():
            for regex in user_regexs:
                screpr_cfg[regex] = path

        return screpr_cfg

    def json_validation(self, config):
        validator = {
            "patternProperties": {
                ".+": {"type": "array"}
            }
        }
        return jsonschema.validate(config, validator)
