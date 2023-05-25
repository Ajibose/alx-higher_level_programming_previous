#!/usr/bin/python3
"""
    A script that ads its argument to a list

"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

arg_list = []
filename = "add_item.json"
for i in sys.argv:
    if i != sys.argv[0]:
        arg_list.append(i)
with open(filename, 'a', encoding="utf-8") as f:
    save_to_json_file(arg_list, filename)
    load_from_json_file(filename)
