weightRatioM = {"Flat Bench Press":1.00, "Barbell Squat":1.5, "Barbell Standing Shoulder Press":0.65, "Bent Over Barbell Row":1.0,
                 "Romanian Deadlift (RDL)":1.25, "Standing Barbell Bicep Curl":0.3, "Straight Bar Tricep Pushdown":0.3, "Machine Calf Raise":1.0}

weightRatioF = {"Flat Bench Press":0.75, "Barbell Squat":1.25, "Barbell Standing Shoulder Press":0.5, "Bent Over Barbell Row":0.6,
                 "Romanian Deadlift (RDL)":1.0, "Standing Barbell Bicep Curl":0.2, "Straight Bar Tricep Pushdown":0.2, "Machine Calf Raise":0.75}



bench = -1
squat = -1
shoulderPress = -1
barbellRow = -1
rdl = -1
barbellCurl = -1
tricepPushdown = -1
calfRaise = -1




gender = ""
units = -1
weight = -1

exercises = {"Flat Bench Press":bench,"Barbell Squat":squat,"Barbell Standing Shoulder Press":shoulderPress, "Bent Over Barbell Row":barbellRow,
             "Romanian Deadlift (RDL)":rdl, "Standing Barbell Bicep Curl":barbellCurl, "Straight Bar Tricep Pushdown":tricepPushdown, "Machine Calf Raise":calfRaise}

#Sample exercises for every muscle group
advice = {"Flat Bench Press":"Some exercises that may help growing this muscle include: Incline Dumbell Press, Pec Deck Fly, and the Chest Press Machine.",
          "Barbell Squat":"Some exercises that may help growing this muscle include: Hack Squat, Leg Extensions, and Leg Press.",
          "Barbell Standing Shoulder Press":"Some exercises that may help growing this muscle include: Dumbell Shoulder Press, Machine Rear Delt Flies, and Dumbell Lateral Raises.", 
          "Bent Over Barbell Row":"Some exercises that may help growing this muscle include: Assisted Pull-Ups, Cable Row Machine, and Lat Pulldowns.",
          "Romanian Deadlift (RDL)":"Some exercises that may help growing this muscle include: Hip Thrusts, Leg Curls, and Barbell Squats.", 
          "Standing Barbell Bicep Curl":"Some exercises that may help growing this muscle include: Unilateral Dumbell Bicep Curls, Preacher Curls, and Assisted Chin-Ups.", 
          "Straight Bar Tricep Pushdown":"Some exercises that may help growing this muscle include: Skullcrushers, Assisted Dips, and Overhead Rope Tricep Extensions.", 
          "Machine Calf Raise":"Some exercises that may help growing this muscle include: Standing Machine Calf Raises, Seated Calf Raises, and most leg exercises."}




#The bit that plays at the start, gets weight, units, gender.
def basicInfo():
    #reset all variables for this part
    gender = ""
    units = -1
    weight = -1



    #Get the units
    while (units != 1 and units != 2):
        units = int(input("What units would you like to use?\n1.Pounds (lbs)\n2.Kilograms (kg)\n"))
        if (units != 1 and units != 2):
            print("Invalid Response\n")

    if (units == 2):
        units = "kg"
    else:
        units = "lb"



    #Get Weight
    while (weight <= 0):
        weight = float(input(f"\nHow much do you weigh?\n(Enter in {units}).\n"))
        if (weight <=0):
            print("Invalid Response\n")
    


    while (gender != "M" and gender != "F" and gender != "O"):
        gender = input("\nFinally, what is your gender?\n(M/F/O)\n")
        if (gender != "M" and gender != "F" and gender != "O"):
            print("Invalid Response\n")
    

        
#Different output if gender is O, but uses the male statistics.
    if gender == "O":
        if (input(f"\nYou weigh {weight}{units}s, and are not a male or female.\nIs this correct? (Y/N)\n").lower() != "y"):
            print("Let's try again, then.")
            basicInfo()
        else:
            if (gender == "F"):
                gender = "female"
            else:
                gender = "male"
    else:
        if (gender == "F"):
            gender = "female"
        else:
            gender = "male"
        if (input(f"\nYou weigh {weight}{units}s, and are a {gender}.\nIs this correct? (Y/N)\n").lower() != "y"):
            print("\nLet's try again, then.\n")
            basicInfo()

    return [gender,units,weight]

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Does the equation that gets the score for every muscle group
def getStat(bodyWeight,exercise,weight):
    retVal = weight / bodyWeight

    if (gender == "male"):
        retVal /= weightRatioM[exercise]
    if (gender == "female"):
        retVal /= weightRatioF[exercise]
    return retVal








tempList = basicInfo()
gender = tempList[0]
units = tempList[1]
weight = tempList[2]

#Cycle through every exercise
for i in dict.keys(exercises):
    tempInput = float(input("What is your one rep max on " + i + "?\n(Type -1 to not consider this exercise).\n"))
    if (tempInput > 0):
        exercises[i] = getStat(weight,i,tempInput)

lowest = -1
highest = -1
#Get lowest and highest values
for i in dict.keys(exercises):
    if exercises[i] != -1:
        if (lowest == -1):
            lowest = i
        else:
            if exercises[i] <= exercises[lowest]:
                lowest = i
        if (highest == -1):
            highest = i
        else:
            exercises[i] >= exercises[highest]
            highest = i

print(f"\nThat's it! Time to calculate the results...\n\nYour weakest exercise is your {lowest.upper()}, with a score of {exercises[lowest]}\n{advice[lowest]}\n")
print(f"Your strongest exercise is your {highest.upper()}, with a score of {exercises[highest]}")





#blah blah blah
