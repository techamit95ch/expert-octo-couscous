# importing csv module
import csv
import os
# csv file name
script_dir = os.path.dirname(__file__)  # Script directory
full_path = os.path.join(script_dir, '../../input/question-2/main.csv')

rows = []

# reading csv file
with open(full_path, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
    # extracting field names through first row
    fields = next(csvreader)
    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)

field_data = ['', 'min', 'max']
data = dict()

for index, row in enumerate(rows):
    if row[3] in data:
        if(data[row[3]]["min"] > row[1]):
            data[row[3]]["min"] = row[1]
        if(data[row[3]]["max"] < row[1]):
            data[row[3]]["max"] = row[1]
    else:
        data[row[3]] = {
            "min": row[1],
            "max": row[1]
        }
    # print
data_2 = []
for i in sorted(data.keys(), reverse=True):
    data_2.append([i, data[i]["min"], data[i]["max"]])


filename = os.path.join(script_dir, '../../output/answer-2/main.csv')

# writing to csv file
with open(filename, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the fields
    csvwriter.writerow(field_data)
    csvwriter.writerow(['occupation'])

    # writing the data rows
    csvwriter.writerows(data_2)

# print(data_2)
