
# importing csv module
import csv
import os
# csv file name
script_dir = os.path.dirname(__file__)  # Script directory
full_path = os.path.join(script_dir, '../../input/question-1/main.csv')

# initializing the titles and rows list
rows = []

# reading csv file
with open(full_path, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)


year = []
Population = []
Violent = []
Property = []
Murder = []
Forcible_Rape = []
Robbery = []
Aggravated_assault = []
Burglary = []
Larceny_Theft = []
Vehicle_Theft = []
vil_count = 0
prop_count = 0
mur_count = 0
f_count = 0
rob_count = 0
ag_count = 0
bur_count = 0
lar_count = 0
veh_count = 0
field_data = ['', 'Population', 'Violent', 'Property', 'Murder',
              'Forcible_Rape', "Robbery", "Aggravated_assault",
              "Burglary", "Larceny_Theft", "Vehicle_Theft"]
data = []
counter = 0
for index, row in enumerate(rows):
    # print(row[2])
    year_no = int(row[0])

    vil_count += int(row[3])
    prop_count += int(row[4])
    mur_count += int(row[5])
    f_count += int(row[6])
    rob_count += int(row[7])
    ag_count += int(row[8])
    bur_count += int(row[9])
    lar_count += int(row[10])
    veh_count += int(row[11])
    counter += 1
    if (year_no % 10 == 0):
        year.append(year_no)
        vil_count = int(row[3])
        prop_count = int(row[4])
        mur_count = int(row[5])
        f_count = int(row[6])
        rob_count = int(row[7])
        ag_count = int(row[8])
        bur_count = int(row[9])
        lar_count = int(row[10])
        veh_count = int(row[11])
        counter = 1
    if (year_no % 10 == 9 or index == len(rows)-1):
        Population.append(int(row[1]))
        Violent.append(vil_count)
        Property .append(prop_count)
        Murder .append(mur_count)
        Forcible_Rape .append(f_count)
        Robbery .append(rob_count)
        Aggravated_assault .append(ag_count)
        Burglary .append(bur_count)
        Larceny_Theft .append(lar_count)
        Vehicle_Theft .append(veh_count)


for index, yr in enumerate(year):
    data.append(
        [yr,
         Population[index],
         Violent[index],
         Property[index],
         Murder[index],
         Forcible_Rape[index],
         Robbery[index],
         Aggravated_assault[index],
         Burglary[index],
         Larceny_Theft[index],
         Vehicle_Theft[index],
         ]
    )

# filename = "main.csv"
filename = os.path.join(script_dir, '../../output/answer-1/main.csv')

# writing to csv file
with open(filename, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the fields
    csvwriter.writerow(field_data)

    # writing the data rows
    csvwriter.writerows(data)
