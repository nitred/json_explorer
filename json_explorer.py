"""File containing the implementation of json explorer."""
from __future__ import unicode_literals

import json


def __explore_list(depth, json_list):
    """Explore json list.

    Args:
        depth (int): The current depth of exploration of the json object. It is
            used to determine the level of indentation of the text.
        json_list (list): A list object which is a sub object of the original
            json object.

    Returns:
        None: The function just prints output to console.
    """
    this_tabs = "".join(['\t'] * depth)
    sub_tabs = "".join(['\t'] * (depth + 1))
    print("{}LIST".format(this_tabs))

    if len(json_list) > 0:
        for item in json_list[:1]:
            if isinstance(item, dict):
                __explore_dict(depth + 1, item)
            elif isinstance(item, list):
                __explore_list(depth + 1, item)
            else:
                print("{}VALUE: {}".format(sub_tabs, item))
                print("{}TYPE : {}".format(sub_tabs, type(item)))
                print("{}.".format(sub_tabs))
                print("{}.".format(sub_tabs))
                print("{}.".format(sub_tabs))
    else:
        print("{}EMPTY LIST".format(sub_tabs))
        print("{}".format(sub_tabs))


def __explore_dict(depth, json_dict):
    """Explore json dict.

    Args:
        depth (int): The current depth of exploration of the json object. It is
            used to determine the level of indentation of the text.
        json_dict (dict): A dict object which is a sub object of the original
            json object.

    Returns:
        None: The function just prints output to console.
    """
    this_tabs = "".join(['\t'] * depth)
    sub_tabs = "".join(['\t'] * (depth + 1))
    val_tabs = "".join(['\t'] * (depth + 2))
    print("{}DICT".format(this_tabs))

    if len(json_dict) > 0:
        for key in json_dict:
            print("{}{}".format(sub_tabs, key))
            if isinstance(json_dict[key], dict):
                __explore_dict(depth + 1, json_dict[key])
            elif isinstance(json_dict[key], list):
                __explore_list(depth + 1, json_dict[key])
            else:
                print("{}VALUE: {}".format(val_tabs, json_dict[key]))
                print("{}TYPE : {}".format(val_tabs, type(json_dict[key])))
    else:
        print("{}EMPTY".format(sub_tabs))
        print("{}".format(sub_tabs))


def explore_object(json_obj):
    """Explore json object.

    Args:
        json_obj (object): A json object to be explored.

    Returns:
        None: The function just prints output to console.
    """
    print("HEAD")
    if isinstance(json_obj, dict):
        __explore_dict(0, json_obj)
    elif isinstance(json_obj, list):
        __explore_list(0, json_obj)
    else:
        print("{}VALUE: {}".format("\t", json_obj))
        print("{}TYPE : {}".format("\t", type(json_obj)))


def explore_string(json_str):
    """Explore json string.

    Args:
        json_str (str): The json string to be explored.

    Returns:
        None: The function just prints output to console.
    """
    json_obj = json.loads(json_str)
    explore_object(json_obj)


def explore_file(filepath):
    """Explore json file.

    Args:
        filepath (str): The full path of the json file to be explored.

    Returns:
        None: The function just prints output to console.
    """
    with open(filepath, 'r') as f:
        json_obj = json.loads(f.read())

    explore_object(json_obj)
