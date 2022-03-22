is_male = True
is_tall = True
if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are neither male or tall")
#here if 1 or 2 statements are true it print first truth but if nothing is true it print the second truth
print("------------------------")
is_male = True
is_tall = True
if is_male and is_tall:
    print("You are a tall male")
else:
    print("You are either not male or not tall or not both")
#here the both statements have to be true to print first truth otherwise it print 2nd truth
print("------------------------")
is_male = True
is_tall = True
if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall :
    print("You are a not a male but are tall")
else:
    print("You are not a male or not tall")