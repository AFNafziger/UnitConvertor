"""
Created on Wed Feb  3 10:57:44 2021

@author: Atticus Nafziger

Create a program/programs that will take a measurement from the user, a number 
from the user, and a visual representation from the user and display it. 
"""


Measurements = ["Length","Height","Weight","Amount","Time","Temperature","Calories","Volume"]
#Length Dict
LUnits = {"inches":1/39.3701,"yards":1/1.09361,"feet":1/3.28084,"miles":1/0.000621371,"meters":1/1,"centimeters":1/100,"kilometers":1/1000, "football fields":91.44,"hands":0.1016,"cars":4.5,"buses":14,"pencils":0.15,"bricks":0.225,"cats":0.46,"titanics":269}
#Height Dict
HUnits = {"inches":1/39.3701,"yards":1/1.09361,"feet":1/3.28084,"miles":1/0.000621371,"meters":1/1,"centimeters":1/100,"kilometers":1/1000,"adult men":1.77,"empire state buildings":443,"pencils":0.15,"eiffel towers":324}
#Weight Dict
WUnits = {"grams":1,"kilograms":1000,"metric tonnes":1000000,"pounds":453.59, "US tons":907185,"elephants":6350000,"people":56000,"paperclips":1,"bricks":2270,"blue whales":181437000,"cans of soda":384,"smart phones":200}
#Time Dict
TUnits = {"seconds":1/3600, "minutes":1/60,"hours":1,"days":24, "weeks":168, "decades":87600,"human lifespans": 692040,"lengths of pregnancies": 6570,"lunch breaks": 1/2,"blinks of the eye": 0.4/3600}
#Temperature Dict
TmUnits = {"celcius":1, "fahrenheit":1,"kelvin":1}
TmVisuals = {"boiling water":212 ,"room temperature":77,"freezing":32}
#Calorie Dict
CUnits = {"kilocalories":1,"calories":1/1000,"hamburgers":354,"poptarts":200,"cans of coke":140, "apples":95}
#Volume Dict
VUnits = {"liters":1,"gallons":1/0.264172,"ounces":1/33.814,"mililiters":1/1000, "cans of soda":0.354882, "bathtubs":158.987}



#Instructions
for i in range (10):
    print()
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Description: The user will select a measurement they want to convert units in. \nThe user will then select their initial unit and the amount of said units, and \nfinally, the unit they want to convert to. ")
print()
print("Example: User selects the height function by typing in \"height\", selects their\nunit by typing \"feet\", types \"20\" for their amount, and types \"people\" as the \nconvertion. The program then responds with 3.5859 people")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
for i in range (3):
    print()
def lengthFunc():
    print()
    print(*LUnits, sep =", ")
    userUnit = input("Select your unit of measurement: ") 
    userUnit = userUnit.lower()
    print(userUnit)
    userNum = input("Enter your number of "+userUnit+": ")
    print()
    print(*LUnits, sep = ", ")
    visual = input("What would you like to view the units as? ")
    visual = visual.lower()
        #print(LUnits[userUnit])
    x = (float(userNum) * LUnits[userUnit])/LUnits[visual]
    print ("That is " +str(round(x,4))+ " "+ visual)

def heightFunc():
    print()
    print(*HUnits, sep =", ")
    userUnit = input("Select your unit of measurement: ") 
    userUnit = userUnit.lower()
    print(userUnit)
    userNum = input("Enter your number of "+userUnit+": ")
    print()
    print(*HUnits, sep = ", ")
    visual = input("What would you like to view the units as? ")
    visual = visual.lower()
    x = (float(userNum) * HUnits[userUnit])/HUnits[visual]
    print ("That is " +str(round(x,4))+ " "+ visual)

def weightFunc():
    print()
    print(*WUnits, sep =", ")
    userUnit = input("Select your unit of measurement: ") 
    userUnit = userUnit.lower()
    print(userUnit)
    userNum = input("Enter your number of "+userUnit+": ")
    print()
    print(*WUnits, sep = ", ")
    visual = input("What would you like to view the units as? ")
    visual = visual.lower()
    x = (float(userNum) * WUnits[userUnit])/WUnits[visual]
    print ("That is " +str(round(x,4))+ " "+ visual)

def amountFunc():
    print()
    amount = int(input("Enter a number amount: "))
    print()
    visual = input("Enter a letter or symbol you would like to use as the visual: ")
    VList = []
    for i in range(amount):
        VList.append(visual)
    print(*VList, sep = " ")

def timeFunc():
    print()
    print(*TUnits, sep =", ")
    userUnit = input("Select your measurement of time: ") 
    userUnit = userUnit.lower()
    print(userUnit)
    userNum = input("Enter your number of "+userUnit+": ")
    print()
    print(*TUnits, sep = ", ")
    visual = input("What would you like to view the units as? ")
    visual = visual.lower()
    x = (float(userNum) * TUnits[userUnit])/TUnits[visual]
    print ("That is " +str(round(x,4))+ " "+ visual)

def tempFunc():
    print()
    print(*TmUnits, sep =", ")
    userUnit = input("Select your units of temperature: ") 
    userUnit = userUnit.lower()
    print(userUnit)
    userNum = input("Enter your temperature in "+userUnit+": ")
    print()
    
    if userUnit == "celcius":
        userNum = float((float(userNum) *9/5)+32)
    if userUnit == "kelvin":
        userNum = float((float(userNum) - 273.15) * 9/5 + 32)
        #print(userNum)
    print(*TmVisuals, sep = ", ")
    visual = input("What would you like to view the units as? ")
    visual = visual.lower()
    x = (float(userNum) * TmUnits[userUnit])/TmVisuals[visual]
    print ("That is " +str(round(x,4))+ " times the temperature of "+ visual)

def calorieFunc():
    print()
    print(*CUnits, sep =", ")
    userUnit = input("Select your unit of measurement: ") 
    userUnit = userUnit.lower()
    print(userUnit)
    userNum = input("Enter your number of "+userUnit+": ")
    print()
    print(*CUnits, sep = ", ")
    visual = input("What would you like to view the units as? ")
    visual = visual.lower()
    x = (float(userNum) * CUnits[userUnit])/CUnits[visual]
    print ("That is " +str(round(x,4))+ " "+ visual)
    
def volumeFunc():
    print()
    print(*VUnits, sep =", ")
    userUnit = input("Select your unit of measurement: ") 
    userUnit = userUnit.lower()
    print(userUnit)
    userNum = input("Enter your number of "+userUnit+": ")
    print()
    print(*VUnits, sep = ", ")
    visual = input("What would you like to view the units as? ")
    visual = visual.lower()
        #print(LUnits[userUnit])
    x = (float(userNum) * VUnits[userUnit])/VUnits[visual]
    print ("That is " +str(round(x,4))+ " "+ visual)

#User selects the function they want
def doit():      
    print(*Measurements, sep = ", " )
    userMes = input("Please select a measurement: ")
    userMes = userMes.lower()
    print(userMes)

#Call on the needed function
    if userMes == "length":
        lengthFunc()
    if userMes == "height":
        heightFunc()
    if userMes == "weight":
        weightFunc()
    if userMes == "amount":
        amountFunc()
    if userMes == "time":
        timeFunc()
    if userMes == "temperature":
        tempFunc()
    if userMes == "calories":
        calorieFunc()
    if userMes =="volume":
        volumeFunc()
useit = "yes"
while useit == "yes":
    doit()
    for i in range(3):
        print()
    useitA = input("Run again? Type \'yes\':  ")
    useit = useitA.lower()
    print()
    print()
    if useit != "yes":
        print("Thank you for using Unit Converter")
