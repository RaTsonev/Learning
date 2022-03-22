#"Jan"....... is the key and "January"...... is the value
monthConversions={
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
    }
print(monthConversions["Jan"])
#first way to output the month
print("------------------------")
print(monthConversions.get("Dec"))
#second way to output the month
print("------------------------")
print(monthConversions.get("Luv", "Not a valid key"))
