# importing csv module
import csv
import os
# csv file name
script_dir = os.path.dirname(__file__)  # Script directory
full_path = os.path.join(script_dir, '../../input/question-3/main.csv')
rows = []
fields = []
# reading csv file
with open(full_path, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    fields = next(csvreader)
    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)

red_index = fields.index('Red Cards')
yellow_index = fields.index('Yellow Cards')


def sort_red(val):
    return val[red_index]


def sort_yellow(val):
    # print(val[2])
    return int (val[2])


data_1 = dict()

for index, row in enumerate(rows):
    if row[red_index] in data_1:
        data_1[row[red_index]].append([
            index,
            row[0],
            int(row[yellow_index]),
            int(row[red_index]),
        ])
    else:
        data_1[row[red_index]] = [[
            index,
            row[0],
            row[yellow_index],
            row[red_index],
        ]]
# rows.sort(key=sort_red, reverse=True)
data_00 = sorted(data_1.keys(), reverse=True)
data_0 = {}
for row in data_00:
    # data_0[row].sort(key=sort_yellow, reverse=True)
    
    data_1[row].sort(key=sort_yellow, reverse=True)
    print(data_1[row])
    print("-------------------")

    data_0[row] = data_1[row]

# print(data_0)
print("-------------------")

# for row in data_0:
#     data_0[row].sort(key=sort_yellow, reverse=True)

data = []
for row in data_0:
    for i in data_0[row]:
        data.append(i)
# print(data)

filename = os.path.join(script_dir, '../../output/answer-3/main.csv')

with open(filename, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the fields
    csvwriter.writerow(["",fields[0], fields[yellow_index], fields[red_index]])

    # writing the data rows
    csvwriter.writerows(data)
