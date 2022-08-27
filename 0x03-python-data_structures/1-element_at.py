#!/usr/bin/python3
def element_at(my_list, idx):
    for i in my_list:
        i = my_list[idx]
        if i < 0 or my_list.index(i) >= len(my_list):
            return None
        else:
            return i
