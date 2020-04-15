#special structure in python, which allows us to store information in key value pairs
#convert a 3-digit month name to full name

month_conversions = {
    "Jan" : "January","Apr": "April", "Jul": "July"}
#all of the keys will need to be unique

print(month_conversions["Apr"])#accessing specific key and will give associated values
print(month_conversions.get("Jan"))#another way to do same
