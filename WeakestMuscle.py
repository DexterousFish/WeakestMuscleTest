#Info for running program
weightRatioM = {"Flat Bench Press":1.00, "Barbell Squat":1.5, "Barbell Standing Shoulder Press":0.65, "Bent Over Barbell Row":1.0,
                 "Romanian Deadlift (RDL)":1.25, "Standing Barbell Bicep Curl":0.35, "Straight Bar Tricep Pushdown":0.3, "Machine Calf Raise":0.9}
weightRatioF = {"Flat Bench Press":0.75, "Barbell Squat":1.25, "Barbell Standing Shoulder Press":0.5, "Bent Over Barbell Row":0.6,
                 "Romanian Deadlift (RDL)":1.0, "Standing Barbell Bicep Curl":0.25, "Straight Bar Tricep Pushdown":0.2, "Machine Calf Raise":0.7}
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


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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
    
    #Gender
    while (gender != "m" and gender != "f" and gender != "o"):
        gender = input("\nFinally, what is your gender?\n(M/F/O)\n")
        gender.lower()
        if (gender != "m" and gender != "f" and gender != "o"):
            print("Invalid Response\n")
     

#Different output if gender is O, but uses the male statistics.
    if gender == "o":
        if (input(f"\nYou weigh {weight}{units}s, and are not a male or female.\nIs this correct? (Y/N)\n").lower() != "y"):
            print("Let's try again, then.")
            basicInfo()
        else:
            if (gender == "f"):
                gender = "female"
            else:
                gender = "male"
    else:
        if (gender == "f"):
            gender = "female"
        else:
            gender = "male"
        if (input(f"\nYou weigh {weight}{units}s, and are a {gender}.\nIs this correct? (Y/N)\n").lower() != "y"):
            print("\nLet's try again, then.\n")
            basicInfo()

    return [gender,units,weight]


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Does the equation that gets the score for every muscle group
def getStat(bodyWeight,exercise,weight,gender):
    retVal = weight / bodyWeight

    if (gender == "male"):
        retVal /= weightRatioM[exercise]
    if (gender == "female"):
        retVal /= weightRatioF[exercise]
    return retVal


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def muscleTest():
    #reset all data
    exercises = {"Flat Bench Press":bench,"Barbell Squat":squat,"Barbell Standing Shoulder Press":shoulderPress, "Bent Over Barbell Row":barbellRow,
             "Romanian Deadlift (RDL)":rdl, "Standing Barbell Bicep Curl":barbellCurl, "Straight Bar Tricep Pushdown":tricepPushdown, "Machine Calf Raise":calfRaise}

    tempList = basicInfo()
    gender = tempList[0]
    units = tempList[1]
    weight = tempList[2]

    #Cycle through every exercise
    for i in dict.keys(exercises):
        tempInput = float(input("What is your one rep max on " + i + "?\n(Type -1 to not consider this exercise).\n"))
        if (tempInput > 0):
            exercises[i] = round(getStat(weight,i,tempInput,gender),3)

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
                if exercises[i] >= exercises[highest]:
                    highest = i
    
    if (lowest == -1 or highest == -1):
        print("\nYou can't just ignore everything!\n")
    else:

        print(f"\nThat's it! Time to calculate the results...\n\nYour weakest exercise is your {lowest.upper()}, with a score of {round(exercises[lowest],3)}\n{advice[lowest]}\n")
        print(f"Your strongest exercise is your {highest.upper()}, with a score of {round(exercises[highest],3)}\n")

        tempInput = ""
        while tempInput.lower() != "y" and tempInput.lower() != "n":
            tempInput = input("Would you like to view the scores of all of your exercises? (Y/N)")
        if tempInput == "y":
            for i in dict.keys(exercises):
                print(f"{i} = {exercises[i]}")
        print("")


#----------------------------------------------------------------------------------------------------------------------------------------------------------------


def bmiTest():
    infoRight = False
    while infoRight == False:
        units = -1
        weight = -1
        unitsH = -1
        height = -1

        #Get the units for weight
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

        if (units == 2):
            unitsH = "cm"
        else:
            unitsH = "in"

    
        #Get height
        while (height <= 0):
            height = float(input(f"\nHow tall are you?\n(Enter in {unitsH}).\n"))
            if (height <=0):
                print("Invalid Response\n")

    
        if (input(f"\nYou weigh {weight}{units}s, and are a {height}{unitsH} tall.\nIs this correct? (Y/N)\n").lower() != "y"):
                print("\nLet's try again, then.\n")
        else:
            infoRight = True
    
    if units == "kg":
        bmi = weight / (height**2)
    else:
        bmi = 703 * weight / (height**2)
    

    print(f"\nYou have a BMI of {bmi}!")

    if bmi <= 18.5:
        print(f"You are in the Underweight category (BMI of 0-18.5).")
    elif bmi > 18.5 and bmi <= 25:
        print("You are in the Healthy Weight category (BMI of 18.5-25). This is a very healthy range! Way to go!")
    elif bmi > 25 and bmi <= 30:
        print("You are in the Overweight category (BMI of 25-30).")
    else:
        print("You are in the Obese category (BMI of 30+).")
    print("\nNOTE: a BMI test is a very flawed way of deciding what kind of condition your health is in. If you have a genuine health problem, consult a doctor!")

    tempInput = ""
    while tempInput.lower() != "y":
        tempInput = input("\nDo you understand this? (Y/N)")
    


#------------------------------------------------------------------------------------------------------------------------------------------------------------------


def infoCredits():
    print("")
    print("""This software is a quick and easy way to discover where your muscle weaknesses may lie.
Simply run the software, and follow the instructions to find this out!
          
The recieved score on each exercise at the end of the program is given by the equation below:
(MaximumWeightMoved / BodyWeight) / (AdvancedBodyWeightRatio)
          
This "ratio" is essentially the amount of weight an advanced lifter is on average able to move compared to their body mass.
          
(To put it simply, if you have a score of over 1, you are considered an "advanced lifter" in that movement).
          
          
CREDITS:
    Sources used:
        ExRx.net
        strengthlevel.com
        NSCA.com
          
    Created by Mitchell Damuth
          
THIS PROGRAM SHOULD NOT BE USED AS A LEGITIMATE MEDICAL CONSULTANT! CONSULT A DOCTOR IF YOU HAVE ANY GENUINE QUESTIONS OR FEARS ABOUT YOUR HEALTH!
            """)
    input("Press Enter to continue")


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

tempInput = 0
while tempInput != 4:
    tempInput = 0
    print("Welcome to the Weakest Muscle Test!\n")
    print("Please make a selection\n(1) Run Weakest Muscle Test\n(2) Run BMI Test\n(3) Additional Info / Credits\n(4) Exit Program")

    tempInput = int(input())
    if tempInput == 1:
        print("")
        muscleTest()
    if tempInput == 2:
         print("")
         bmiTest()
    if tempInput == 3:
        print("")
        infoCredits()
    if tempInput == 4:
        tempInput = 4
