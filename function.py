# function with output

from fnmatch import fnmatch


def format_name(f_name,l_name):
    a_format = f_name.title()
    b_format = l_name.title()
    return a_format + b_format

print(format_name("adam","Pamungkas"))