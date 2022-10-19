import csv
from os import linesep

def read_csv(path):
    csv_data = []
    with open(path, "r+", encoding="UTF8", newline=None) as file:
        csv_data = list(csv.reader(file))
    return csv_data


tag_csv = "./tags/danbooru.csv"
tag_csv_zh = "./tags/danbooru-0-zh.csv"
tag_csv_new = "./tags/danbooru-zh.csv"


if __name__ == "__main__":

    csv_list = read_csv(tag_csv)
    csv_list_zh = read_csv(tag_csv_zh)
    print(len(csv_list))
    print(len(csv_list_zh))

    for i in range(len(csv_list_zh)):
        if len(csv_list_zh[i]) != 3:
            print("error {}".format(csv_list_zh[i]))
            continue
        for j in range(len(csv_list)):
            if csv_list[j][0] != "0" or len(csv_list[j]) == 3:
                continue
            if csv_list_zh[i][0] == csv_list[j][0]:
                csv_list[j].append(csv_list_zh[i][2])
                break


    with open(tag_csv_new, "w", encoding="UTF8", newline=None) as file:
        writer = csv.writer(file, lineterminator="\n")
        writer.writerows(csv_list)