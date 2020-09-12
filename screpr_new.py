import os
import json

with open('screpr_config.json', 'r') as read_file:
    config_dict = json.load(read_file)

key_list = []
for key in config_dict.keys():
    key_list.append(key)

for path, _, files in os.walk(os.getcwd()):
    for file_name in files:
        file_format = file_name.split('.')[-1]
        current_file_path = f'{path}/{file_name}'
        for key in key_list:
            if file_format in config_dict[key]:
                destination = f'{key}/{file_name}'
                os.rename(current_file_path, destination)
