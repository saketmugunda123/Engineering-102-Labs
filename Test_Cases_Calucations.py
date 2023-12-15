

import random

#Variable to store point total
age = 0
chol = 0
smoker = False
treated = False
hdl = 0
sbp = 0
sex = False #False represents Female, True represents Male

#Function to give output according to different inputs (EX. cholestrol, age, SBP, etc)
def tenYearRisk(sex, age, chol, smoker, hdl, sbp, treated):
    points = 0
    yearRisk = ""
    #If per input to add to point total(nest inside if for male or female)
    if (sex == True):
        #Add points for age
        if (age < 35):
            points += -9
        elif (age < 40):
            points += -4
        elif (age < 45):
            points += 0
        elif (age < 50):
            points += 3
        elif (age < 55):
            points += 6
        elif (age < 60):
            points += 8
        elif (age < 65):
            points += 10
        elif (age < 70):
            points += 11
        elif (age < 75):
            points += 12
        else:
            points += 13
        #print(f'points after age: {points}')
        #Add points for cholestrol
        if (chol < 160):
            points += 0
        elif (chol < 200):
            if (age < 40):
                points += 4
            elif (age < 50):
                points += 3
            elif (age < 60):
                points += 2
            elif (age < 70):
                points += 1
            else:
                points += 0
        elif (chol < 240):
            if (age < 40):
                points += 7
            elif (age < 50):
                points += 5
            elif (age < 60):
                points += 3
            elif (age < 70):
                points += 1
            else:
                points += 0
        elif (chol < 280):
            if (age < 40):
                points += 9
            elif (age < 50):
                points += 6
            elif (age < 60):
                points += 4
            elif (age < 70):
                points += 2
            else:
                points += 1
        elif (chol >= 280):
            if (age < 40):
                points += 11
            elif (age < 50):
                points += 8
            elif (age < 60):
                points += 5
            elif (age < 70):
                points += 3
            else:
                points += 1
        #print(f'points after cholestrol: {points}')
        #Add points for smoking
        if (smoker == True):
            if (age < 40):
                points += 8
            elif (age < 50):
                points += 5
            elif (age < 60):
                points += 3
            elif (points < 70):
                points += 1
            elif (points < 80):
                points += 1
        #print(f'points after smoking: {points}')
        #Add points for HDL
        if (hdl < 40):
            points += 2
        elif (hdl < 50):
            points += 1
        elif (hdl < 60):
            points += 0
        else:
            points += -1
        #print(f'points after hdl: {points}')
        #Add points for SBP
        if (treated == False):
            if (sbp < 130):
                points += 0
            elif (sbp < 160):
                points += 1
            else:
                points += 2
        else:
            if (sbp < 120):
                points += 0
            elif (sbp < 130):
                points += 1
            elif (sbp < 160):
                points += 2
            else:
                points += 3
        #print(f'points after Sbp: {points}')
        #Convert points into 10 year risk
        if (points < 0):
            yearRisk = "<1"
        elif (points <= 4):
            yearRisk = "1"
        elif (points <= 6):
            yearRisk = "2"
        elif (points == 7):
            yearRisk = "3"
        elif (points == 8):
            yearRisk = "4"
        elif (points == 9):
            yearRisk = "5"
        elif (points == 10):
            yearRisk = "6"
        elif (points == 11):
            yearRisk = "8"
        elif (points == 12):
            yearRisk = "10"
        elif (points == 13):
            yearRisk = "12"
        elif (points == 14):
            yearRisk = "16"
        elif (points == 15):
            yearRisk = "20"
        elif (points == 16):
            yearRisk = "25"
        else:
            yearRisk = ">30"
        #print(yearRisk)
    else:
        #Add points for age
        if (age < 35):
            points += -7
        elif (age < 40):
            points += -3
        elif (age < 45):
            points += 0
        elif (age < 50):
            points += 3
        elif (age < 55):
            points += 6
        elif (age < 60):
            points += 8
        elif (age < 65):
            points += 10
        elif (age < 70):
            points += 12
        elif (age < 75):
            points += 14
        else:
            points += 16
        #print(f'points after age {points}')
        #Add points for cholestrol
        if (chol < 160):
            points += 0
        elif (chol < 200):
            if (age < 40):
                points += 4
            elif (age < 50):
                points += 3
            elif (age < 60):
                points += 2
            elif (age < 70):
                points += 1
            else:
                points += 1
        elif (chol < 240):
            if (age < 40):
                points += 8
            elif (age < 50):
                points += 6
            elif (age < 60):
                points += 4
            elif (age < 70):
                points += 2
            else:
                points += 1
        elif (chol < 280):
            if (age < 40):
                points += 11
            elif (age < 50):
                points += 8
            elif (age < 60):
                points += 5
            elif (age < 70):
                points += 3
            else:
                points += 2
        elif (chol >= 280):
            if (age < 40):
                points += 13
            elif (age < 50):
                points += 10
            elif (age < 60):
                points += 7
            elif (age < 70):
                points += 4
            else:
                points += 2   
        #print(f'points after cholestrol {points}')
        #Add points for smoker
        if (smoker == True):
            if (age < 40):
                points += 9
            elif (age < 50):
                points += 7
            elif (age < 60):
                points += 4
            elif (age < 70):
                points += 2
            elif (age < 80):
                points += 1
        #print(f'points after smoking {points}')
        #Add points for HDL
        if (hdl < 40):
            points += 2
        elif (hdl < 50):
            points += 1
        elif (hdl < 60):
            points += 0
        else:
            points += -1
        #print(f'points after HDL {points}')
        #Add points for SBP
        if (treated == False):
            if (sbp < 120):
                points += 0
            elif (sbp < 130):
                points += 1
            elif (sbp < 140):
                points += 2
            elif (sbp < 160):
                points += 3
            else:
                points += 4
        else:
            if (sbp < 120):
                points += 0
            elif (sbp < 130):
                points += 3
            elif (sbp < 140):
                points += 4
            elif (sbp < 160):
                points += 5
            else:
                points += 6
        #Convert points into Year Risk
        if (points < 9):
            yearRisk = "<1"
        elif (points <= 12):
            yearRisk = "1"
        elif (points <= 14):
            yearRisk = "2"
        elif (points == 15):
            yearRisk = "3"
        elif (points == 16):
            yearRisk = "4"
        elif (points == 17):
            yearRisk = "5"
        elif (points == 18):
            yearRisk = "6"
        elif (points == 19):
            yearRisk = "8"
        elif (points == 20):
            yearRisk = "11"
        elif (points == 21):
            yearRisk = "14"
        elif (points == 22):
            yearRisk = "17"
        elif (points == 23):
            yearRisk = "22"
        elif (points == 24):
            yearRisk = "27"
        else:
            yearRisk = ">30"
    gender = ""
    if (sex == True):
        gender = "M"
    else:
        gender = "F"
    smo = ""
    if (smoker == True):
        smo = "Y"
    else:
        smo = "N"
    med = ""
    if (treated == True):
        med = "Y"
    else:
        med = "N"
    print(f'sex:{gender} age:{age} cho:{chol} smo:{smo} hdl:{hdl} sbp:{sbp} med:{med} out:{yearRisk}')

#Create loop that randomly generates 1000 test cases
for i in range(250):
    randomNumber= random.randint(0, 1)
    if randomNumber == 0:
        gender = False
    else:
        gender = True
        
    randomNumber= random.randint(0, 1)
    if randomNumber == 0:
        smo = False
    else:
        smo = True  
    
    randomNumber= random.randint(0, 1)
    if randomNumber == 0:
        med = False
    else:
        med = True 
        
#Call Function
tenYearRisk (True,40,300,True,65,150,True)

