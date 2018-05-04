# -*- coding: utf-8 -*-
"""Given a file of hypotheses and a file with the gold sequences, the sequence level accuracy is output"""

from __future__ import print_function
import argparse
import codecs


def parse_arguments():
    """Parses the command line arguments.

    :return parsed_arguments: a dictionary containing the command line arguments
    """
    parser = argparse.ArgumentParser(description='A neural network based semantic parser for NLmaps')
    parser.add_argument('--input', '-i', required=True,
                        help='Location of the input file'),
    parser.add_argument('--gold', '-g', required=True,
                        help='Location of the gold file')
    parsed_arguments = parser.parse_args()
    return parsed_arguments


def write_list_to_file(list, file_to_write):
    """ Iterates over the entries in a list and writes them to a file,
    one list entry corresponds to one line in the file

    :param list: the list to be written to a file
    :param file_to_write: the file to write to
    :return: 0 on success
    """
    with codecs.open(file_to_write, 'w', encoding='utf8') as f:
        for line in list:
            print(line, file=f)
    return 0


def read_lines_in_list(file_to_read):
    """ Iterates over the lines in a file and adds the line to a list

    :param file_to_read: the location of the file to be read
    :return: a list where each entry corresponds to a line in the file
    """
    list = []
    with open(file_to_read, 'r') as f:
        for line in f:
            list.append(line.rstrip('\n'))
    return list


def evaluate(hypos, golds):
    """ Calculates the sequence level accuracy given a list of hypotheses
    and a gold list with the true sequences.

    :param hypos: a list of hypotheses
    :param golds: a list of true sequences
    :return:
    """
    sigf = []
    tp = 0
    empty = 0
    fp = 0
    total = len(golds)
    for (hyp, gold) in zip(hypos, golds):
        if hyp == gold:
            tp += 1
            sigf.append("1 1 1")
        elif hyp == "empty" or hyp == "" or "Warning::Issue in line" in hyp:
            empty += 1
            sigf.append("0 0 1")
        else:
            fp += 1
            sigf.append("0 1 1")
    recall = 0
    precision = 0
    f1 = 0
    if total != 0:
        recall = 1.0 * tp / total
    if (tp+fp)!=0:
        precision = 1.0 * tp / (tp+fp)
    if (precision+recall)!=0:
        f1 = 2.0 * precision * recall / (precision + recall)
    eval = "r: %s p: %s f: %s" % (round(recall*100, 2), round(precision*100, 2), round(f1*100, 2))
    eval_print = "%s" % round(f1*100, 8)
    print(eval_print)
    return eval, sigf


if __name__ == '__main__':
    parsed_arguments = parse_arguments()
    hypos_input = read_lines_in_list(parsed_arguments.input)
    golds_input = read_lines_in_list(parsed_arguments.gold)
    eval_result, sigf_result = evaluate(hypos_input, golds_input)
    write_list_to_file([eval_result], "%s.eval" % parsed_arguments.input)
    write_list_to_file(sigf_result, "%s.sigf" % parsed_arguments.input)