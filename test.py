f_user = open("user.txt")
user = f_user.readlines()

f_supplier = open("supplier.txt")
supplier = f_supplier.readlines()

for item in range(len(supplier)):
    print(item)
    line = item.split(",")
    city = line[0]
    supplier = line[1]
    # rate = line[2]

