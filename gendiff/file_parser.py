import json
import yaml


def json_parse(filename):
    data = json.load(open(filename))
    return data


def yaml_parse(filename):
    with open(filename, "r") as file:
        res = yaml.load(file.read(), Loader=yaml.Loader)
    return res
