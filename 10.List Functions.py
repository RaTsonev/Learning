lucky_numbers = [4, 8, 15, 16, 23, 42]
friends=["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]
friends.extend(lucky_numbers)
# it means that "friends" list is extended with "lucky_numbers" list
friends.append("Creed")
# it means that "friends" list is appended with new word "Creed" in the end of the list
friends.insert(1, "Kelly")
# it means that we will insert a name to a specific place with place=index[1] and "Kelly" added name
friends.remove("Jim")
# it means that we remove the name "Jim" from the list
friends.clear()
# it means that the list is empty because the list is cleared
friends.pop()
# its means that we remove the last element from the list
print(friends)
print(friends.index("Kevin"))
# it shows us which is the index of the chosen word-"Kevin" from the list
print(friends.count("Jim"))
# it counts the numbers of times which the word "Jim" is mentioned
friends.sort()
print(friends)
# the words are "alfabetical ordered" in the list
lucky_numbers.sort()
print(lucky_numbers)
#the numbers are numbered
lucky_numbers.reverse()
print(lucky_numbers)
#its reverse the orded of numbers in the list
lucky_numbers.reverse()
print(lucky_numbers)
friends2 = friends.copy()
print(friends2)
#it copy the list of "friends" and paste it on "friends2"