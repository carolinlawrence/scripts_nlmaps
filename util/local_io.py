# -*- coding: utf-8 -*-
"""Holds read and write functions"""
import codecs

def read_lines_in_list(file_to_read):
    """ Iterates over the lines in a file and adds the line to a list

    :param file_to_read: the location of the file to be read
    :return: a list where each entry corresponds to a line in the file
    """
    list = []
    with codecs.open(file_to_read, 'r', encoding='utf8') as f:
        for line in f:
            list.append(line.rstrip('\n'))
    return list

def write_list_to_file(list, file_to_write):
    """ Iterates over the entries in a list and writes them to a file,
    one list entry corresponds to one line in the file

    :param list: the list to be written to a file
    :param file_to_write: the file to write to
    :return: 0 on success
    """
    with codecs.open(file_to_write, 'w', encoding='utf8') as f:
        for line in list:
            print >>f, line
    return 0