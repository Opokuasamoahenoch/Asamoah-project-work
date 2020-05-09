#INPUT
"""entering of farenheight value"""
farenheight_value = int(input("please enter your farenheight teparature value  "))
#PROCESSING
"""this deals with the conversion of farenheight to celsius"""
celcius_value = (farenheight_value -32) *(5/9)
#OUTPUT
"""the final celcius number"""
print(celcius_value)
celcius_number = round(celcius_value, 2)
print(celcius_number)