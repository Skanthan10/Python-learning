# Write your code here :-)
# Write your code here :-)
#  Grocery List for A Store call Tamil Store
# we will assign numbers for each item for user input
# get input for Quantity and Item
# the source file is pricelist.txt, the content will be opened as 'read' mode

#read = file.readlines ()    # Phython will read the source file, line by line and temporalily stores in 'file.readline()
# this will print line by line what was found in the source file
#print (read [0], read [1],read [2],read [3],read [4],read [5],read [6],read [7],read [8],read [9],read [10],read [11],'\n')
#print (read[0]) #this will print the first line from source file. we can change the value inside square bracket for the line we need

# datetime object containing current date and time
from datetime import datetime
current = datetime.now()

dt_string = current.strftime("%d/%m/%Y %H:%M:%S")               # dd/mm/YY H:M:S

dt= current.strftime("%d%m%Y-%H%M%S")

print(dt_string,"\n")

input_file = open ("pr_list.txt", 'r')
all_items = input_file.readlines ()
price_list = {}

for item in all_items :
    print (item)
    item_name = item.split (',')[0].strip()
    item_price = item.split (',')[1].strip()
    price_list[item_name] = item_price
input_file.close()

grand_total_list = []
all_line_items = []

cart = True
while cart :
        print ("\n")
        item = input ("Enter Item name :" )
        if item == "q" :
            cart = False
        else :
            quantity =int (input ("Enter Quantity :"))
            item_price = int(price_list[item])
            grand_total_list.append(item_price)

            line_item = ("    " + item.upper() + " : " + str(price_list[item]) +" @ " +str(quantity) +" = $ " + str(float(item_price)))
            #print(line_item)
            all_line_items.append(line_item)

#print(all_line_items)
f = open ("grand_total_bill" + dt + ".txt", "w")
name = '''

        Welcome Tamil Store
        2010 Ellesmere RD
        Scarborough
        (416)123-4567'''
print (name,"\n")
f.write (name+"\n")
for item in all_line_items :
    print (item)
    f.write (item+"\n")

print ("\n","           Total = " + str(sum(grand_total_list)))
f.write ("\n"+"Total = " + str(sum(grand_total_list)))

#f=open ("grand_total_list", "r")
#print (f.read())

print("*** Thank You for Shopping ***")
f.write ("*** Thank You for Shopping ***"+"\n")
print ("     *** Come Again ***","\n","\n")
f.write ("     *** Come Again ***",+"\n",+"\n")
f.close()

#  Reading a content from text file
#  Need to save the source file as "txt" file in the Phython folder
# use open file command to open the file content
#











