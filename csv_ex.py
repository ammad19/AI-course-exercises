#writing
import csv
with open("competitions.csv","a",newline="") as f:
    data_handler = csv.writer(f, delimiter=",")
    #data_handler.writerow(["Year","Event","Winner"])
    data_handler.writerow(["1985","Best-Kept Lawn","None"])
    data_handler.writerow(["1989","Gobstones","W National"])

#reading
import csv
with open("competitions.csv") as f:
    contents = csv.reader(f)
#    for content in contents:
#        print(content)
    potter_competitions = []
    for each_line in contents:
        potter_competitions+=each_line
    print(potter_competitions)
