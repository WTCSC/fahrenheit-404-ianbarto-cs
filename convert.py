starting_temp = input("What temperature are you starting with: Kelvin(K) Fahrenheit(F) Celsius(C)")
starting_value = input("What is the value of your current temperature?")
converting_temp = input("What are you converting your temperature to: Kelvin(K) Fahrenheit(F) Celsius(C)")

if starting_temp == ("f") or starting_temp == ("F"):
    if converting_temp == ("k") or converting_temp == ("K"):
        Answer = (int(starting_value) - 32) * 5/9 + 273.15
        print (f" {starting_value} is {Answer} in Kelvin")
    elif converting_temp == ("c") or converting_temp == ("C"):
        Answer = (int(starting_value)-32) * 5/9
        print (f" {starting_value} is {Answer} in Celsius")
elif starting_temp == ("K") or starting_temp == ("k"):
    if converting_temp == ("f") or converting_temp ("F"):
        Answer = (int(starting_value) - 273.15) * 9/5 + 32
        print (f" {starting_value} is {Answer} in Fahrenheit")
    elif converting_temp == ("c") or converting_temp == ("C"):
        Answer = (int(starting_value) - 273.15)
        print (f" {starting_value} is {Answer} in Celsius")
elif starting_temp == ("c") or starting_temp == ("C"):
    if converting_temp == ("f") or converting_temp ("F"):
        Answer = (int(starting_value) * 9/5) + 32
        print (f" {starting_value} is {Answer} in Fahrenheit")
    elif converting_temp == ("k") or converting_temp == ("K"):
        Answer = (int(starting_value)+ 273.15)
        print (f" {starting_value} is {Answer} in Kelvin")
        





