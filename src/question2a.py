import csv
import sys

def max_func(files_list, order_index, index):
    cur_order = files_list[index][1][order_index]
    cur_max = files_list[index][0][cur_order]
    for i in range(len(files_list)):
        if cur_order not in files_list[i][0]:
            files_list[i][0][cur_order] = files_list[i][0][files_list[i][1][len(files_list[i][1]) - 1]]
        if cur_max < files_list[i][0][cur_order]:
            cur_max = files_list[i][0][cur_order]
    return cur_max


def is_seen(files_list, cur_file, index, seen_list):
    for i in range(len(seen_list)):
        if i != cur_file and files_list[cur_file][1][index] not in seen_list[i]:
            return False
    return True


def load_data(file_arr):
    all_files_list = []
    for file_name in file_arr:
        f = open(file_name, 'r')
        data = csv.reader(f)
        ranks = {}
        order = []
        for line in data:
            ranks[line[0]] = float(line[1])
            order.append(line[0])
        all_files_list.append((ranks, order))
        f.close()
    return all_files_list


def fagin(files_list, k):
    seen_all = 0
    seen_per_file = [{} for f in files_list]
    ranks_aggr = {}
    index = 0
    stop = False
    while not stop:
        for i in range(len(files_list)):
            cur_order = files_list[i][1][index]
            ranks_aggr[cur_order] = max_func(files_list, index, i)
            seen_per_file[i][cur_order] = 1
            if is_seen(files_list, i, index, seen_per_file):
                seen_all += 1
            if seen_all == k:
                stop = True
                break
        index += 1
    return sorted(ranks_aggr.items(), key=lambda x: x[1], reverse=True)[0:k]


if len(sys.argv) > 1:
    files_data_list = load_data(sys.argv[1:])
    print(fagin(files_data_list, 3))
