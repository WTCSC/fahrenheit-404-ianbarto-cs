starting_temp = input("What temperature are you starting with: Kelvin(K) Fahrenheit(F) Celsius(C)")
starting_value = float(input("What is the value of your current temperature?"))
converting_temp = input("What are you converting your temperature to: Kelvin(K) Fahrenheit(F) Celsius(C)")

if starting_temp.lower() == ("f"):
    if converting_temp.lower() == ("k"):
        Answer = (starting_value - 32) * 5/9 + 273.15
        print (f" {starting_value}°F is {Answer}°K")
    elif converting_temp.lower() == ("c"):
        Answer = (starting_value - 32) * 5/9
        print (f" {starting_value}°F is {Answer}°C")
elif starting_temp.lower() == ("k"):
    if converting_temp.lower() == ("f"):
        Answer = (starting_value - 273.15) * 9/5 + 32
        print (f" {starting_value}°K is {Answer}°F")
    elif converting_temp.lower() == ("c"):
        Answer = (starting_value - 273.15)
        print (f" {starting_value}°K is {Answer}°C")
elif starting_temp.lower() == ("c"):
    if converting_temp.lower() == ("f"):
        Answer = (starting_value * 9/5) + 32
        print (f" {starting_value}°C is {Answer}°F")
    elif converting_temp.lower() == ("k"):
        Answer = (starting_value + 273.15)
        print (f" {starting_value}°C is {Answer}°K")

        


        





