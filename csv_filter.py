import csv

ref_dict = dict()
new_file = 'Vijay-ICLR 2019.csv'
fields_list = list()
with open(new_file,"r") as f:
    csv_reader = csv.reader(f)
    for line in csv_reader:
        for x in line:
            fields_list.append(x)
            ref_dict[x] = ""
        break

with open(new_file,"r") as f1:
    csv_reader1 = csv.reader(f1)
    i = 0
    for line in csv_reader1:
        if i == 0:
            i = i + 1
        else:
            # print(line)
            j=0
            for key in ref_dict.keys():
                ref_dict[key] = line[j]
                j = j + 1
            break
print(ref_dict)
l = len(ref_dict['Ratings'].split(","))
new_csv = "vijay_iclr.csv"
with open(new_csv,"w+") as f2:
    csv_wrt = csv.writer(f2)
    csv_wrt.writerow(fields_list)

f2.close()

with open(new_csv,"a+") as m:
    csv_wtr_m = csv.writer(m)
    # len_ratings = len(ref_dict['Ratings'].split(","))
    x_list = list()
    for key in ref_dict:
        # print(key)
        # print(ref_dict[key])
        x_list.append(ref_dict[key])

        # csv_wtr_m.writerow(x_list)
# print()
    len_ratings = len(x_list[3].split(","))
    
    # print(x_list)
    rate_list = x_list[3].split(",")
    conf_list = x_list[5].split(",")
    #
    for y in range(len(rate_list)):
        x_list[3] = rate_list[y]
        x_list[5] = conf_list[y]
        csv_wtr_m.writerow(x_list)







