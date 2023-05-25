#!/usr/bin/python3
"""
    A script that ads its argument to a list

"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    arg_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    arg_list = []

for i in sys.argv:
    if i != sys.argv[0]:
        arg_list.append(i)

save_to_json_file(arg_list, "add_item.json")
