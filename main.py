import csv
import pandas as pd
#Step 4
df = pd.read_csv('Sample_Data_Age.csv')
df = df.sort_values(by='Name')
df.to_csv('Alpha.csv', index=False)
#Step 1
with open('Sample_Data_Age.csv') as csv_file:
   csv_reader = csv.reader(csv_file, delimiter=',')
   counter_1 = 0
   counter_2 = 0
   counter_3 = 0
   counter_4 = 0
   for row in csv_reader:
        age = int(row[1])
        #step 2
        if age > 64:
            print(row)
            #Step 3
            with open('Age_over_64.csv', 'a', newline='') as csv_file:
                csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                csv_writer.writerows([row])
        #Step 5
        if age > 55:
            counter_1 += 1
            print(counter_1)
        elif age > 36:
            counter_2 +=1
            print(counter_2)
        elif age >25:
            counter_3 +=1
            print(counter_3)
        elif age > 18:
            counter_4 += 1
            print(counter_4)