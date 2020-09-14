from jsonschema import validate
import json

with open('screpr_config.json', 'r') as read_file:
    config_dict = json.load(read_file)

alpha = {"/home/rtdge/Pictures/": [
        "jpg", "jpeg", "png"
    ]}
print(alpha)

beta = {
    "type": "object",
    "patternProperties": {
        ".+": {"type": "array"}
    }
}

validate(alpha, beta)