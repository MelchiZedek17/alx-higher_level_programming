#!/usr/bin/python3
def search_replace(my_list, search, replace):
    clone_list = my_list.copy()
    for i in range(len(clone_list)):
        if clone_list[i] == search:
            clone_list[i] = replace
    return clone_list
