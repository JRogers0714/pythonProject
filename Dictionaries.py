month_conversions = {                  # must always use these for dictionaries {}
    "Jan": "January",                   # "key": "Value" must have both
    "Feb": "February",                   # key value pairs
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

print(month_conversions["Nov"])

print(month_conversions.get("Luv"))

# creating a default value

print(month_conversions.get("Luv", "not a valid key"))

