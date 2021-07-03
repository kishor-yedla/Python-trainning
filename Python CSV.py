
import csv
value = [('kishor, abhinav', 2), ('Rakesh', 3)]
with open('file1.csv','w') as out:
    csv_out = csv.writer(out)
    csv_out.writerow(['Name','Number'])
    for row in value:
	    csv_out.writerow(row)