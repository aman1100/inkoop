import csv
filename="hotels.csv"
Alldata=[]
data_row=[]
with open(filename, 'r') as csvfile:
    csvreader=csv.reader(csvfile)
    for row in csvreader:
        data_row.append(row)
states=[]
max_Tamilnadu=-1
min_Tamilnadu=10000000
max_Maharashtra=-1
min_Maharashtra=1000000
max_Karnataka=-1
min_Karnataka=100000
for row in data_row:
    if row[2]=="Tamilnadu":
        if int(row[3]) >max_Tamilnadu:
            max_Tamilnadu=int(row[3])
        if int(row[3]) <min_Tamilnadu:
            min_Tamilnadu=int(row[3])
#print(max_Tamilnadu)
for row in data_row:
    if row[2]=="Maharashtra":
        if int(row[3]) >max_Maharashtra:
            max_Maharashtra=int(row[3])
        if int(row[3]) <min_Maharashtra:
            min_Maharashtra=int(row[3])
#print(max_Maharashtra)
for row in data_row:
    if row[2]=="Karnataka":
        if int(row[3]) >max_Karnataka:
            max_Karnataka=int(row[3])
        if int(row[3]) <min_Karnataka:
            min_Karnataka=int(row[3])
# print(max_Karnataka)
# print(min_Karnataka,min_Maharashtra,min_Tamilnadu)
state=input("Enter state: ")
choice=input("Cost or Rating: (cost/rating) ")
Operation=input("Operation: (cheapest,average,highest) ")
if choice=="cost" and Operation=="highest":
    for row in data_row:
        if(row[2]==state and int(row[3])==max_Karnataka):
            print("Hotel with highest price in",state,"is",row[1],"with price",max_Karnataka)

elif choice == "cost" and Operation=="cheapest":
    for row in data_row:
        if(row[2]==state and int(row[3])==min_Karnataka):
            print("Hotel with lowest price in",state,"is",row[1],"with price",min_Karnataka)

elif choice == "cost" and Operation=="average":
    for row in data_row:
        if(row[2]==state and int(row[3])>min_Karnataka and int(row[3])<max_Karnataka):
            print("Hotel with average price in",state,"is",row[1],"with price",int(row[3]))

elif choice == "rating" and Operation=="cheapest":
    for row in data_row:
        if(row[2]==state and float(row[4])<3.0):
            print("Hotel with cheapest rating in",state,"is",row[1],"with rating",float(row[4]))

elif choice == "rating" and Operation=="average":
    for row in data_row:
        if(row[2]==state and float(row[4])>3.0 and float(row[4])<8.0):
            print("Hotel with average rating in",state,"is",row[1],"with rating",float(row[4]))

else:
    for row in data_row:
        if(row[2]==state and float(row[4])>9.0):
            print("Hotel with cheapest rating in",state,"is",row[1],"with rating",float(row[4]))