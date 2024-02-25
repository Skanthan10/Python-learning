# Write your code here :-)

from datetime import datetime
today = datetime.today()
print(today,"\n")


# datetime object containing current date and time
from datetime import datetime
current = datetime.now()
print("now =", current)

# dd/mm/YY H:M:S
dt_string = current.strftime("** %d/%m/%Y ** %H:%M:%S **")
print("date and time =",dt_string,"\n")






















from datetime import date
today = date.today()
# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")
print("d1 =", d1,"\n")

# Textual month, day and year	
d2 = today.strftime("%B %d, %Y")
print("d2 =", d2,"\n")

# mm/dd/y
d3 = today.strftime("%m/%d/%y")
print("d3 =", d3,"\n")

# Month abbreviation, day and year	
d4 = today.strftime("%b-%d-%Y")
print("d4 =", d4,"\n")
