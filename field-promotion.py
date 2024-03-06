import random
# A program that grants officers field promotions

# Accepting data on officer
name = input ("Enter your name please: ")
rank = input ("Enter Rank in abriviated form (lt. capt. lt.col.) ")
parent_unit = input ("Enter your parent unit: ")
current_unit = input ("Enter unit of current posting: " )
posin_current_unit = input ("What position do you hold in your current unit: ")
new_rank=""
# Promotion
if rank=="lt." or rank=="Lt.":
    new_rank = "Capt."
elif rank=="capt."or rank== "Capt.":
    new_rank = "Maj."
elif rank=="maj."or rank=="Maj.":
    new_rank = "Lt. Col."
elif rank=="lt. Col." or rank== "Lt. Col.":
    new_rank = "Col"
else:
    print ("invalid format of rank enetered")

# printing and Promotion
print ("Good Evening, "+ rank+ " "+ name)
print ("Your data \n"+rank +" "+name+"\n Parent Unit: "+parent_unit+"\n Current unit: "+ current_unit + "\n Current Designation: "+ posin_current_unit)
print ("Congratulations, on account of being in an operational field area you have been made acting "+ new_rank)
