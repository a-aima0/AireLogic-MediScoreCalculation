from datetime import datetime, timedelta

scoresList = []

def mediScore(airOrOxygen: int, consciousness: int, respirationRange: int, SpO2: int, temp: float, cbg: float, fasting: bool) -> int:
    print("")
    totalScore = 0
    
    # air or oxygen
    if (airOrOxygen == 2):
        totalScore+=2
        
    # consciousness
    if (consciousness != 0):
        totalScore += 3
        
    # respiration range
    if (respirationRange <= 8):
        totalScore += 3
    elif (9 <= respirationRange <= 11):
        totalScore += 1
    elif (21 <= respirationRange <= 24):
        totalScore += 2
    elif (respirationRange >= 25):
        totalScore += 3
    
    # SpO2
    if (airOrOxygen == 0):  # on air
        if (SpO2 <= 83):
            totalScore += 3
        elif (84 <= SpO2 <= 85):
            totalScore += 2
        elif (86 <= SpO2 <= 87):
            totalScore += 1
        elif (88 <= SpO2 <= 92 or SpO2 >= 93):
            totalScore += 0
    else:  # on oxygen
        if (SpO2 <= 83):
            totalScore += 3
        elif (84 <= SpO2 <= 85):
            totalScore += 2
        elif (86 <= SpO2 <= 87):
            totalScore += 1
        elif (88 <= SpO2 <= 92):
            totalScore += 0
        elif (93 <= SpO2 <= 94):
            totalScore += 1
        elif (95 <= SpO2 <= 96):
            totalScore += 2
        else:  # >= 97
            totalScore += 3
        
    # temperature
    temp = round(temp, 1)
    
    if (temp <= 35.0):
        totalScore += 3
    elif (35.1 <= temp <= 36.0):
        totalScore += 2
    elif (38.1 <= temp <= 39.0):
        totalScore += 1
    elif(temp >= 39.1):
        totalScore += 2
    
    # cbg and fasting
    cbg = round(cbg, 1)
    
    if fasting:
        if (cbg <= 3.4):
            totalScore += 3
        elif (3.5 <= cbg <= 3.9):
            totalScore += 2
        elif (4.0 <= cbg <= 5.4):
            totalScore += 0
        elif (5.5 <= cbg <= 5.9):
            totalScore += 2
        else: # >= 6.0
            totalScore += 3
    else:
        if (cbg <= 4.5):
            totalScore += 3
        elif (4.5 < cbg <= 5.8):
            totalScore += 2
        elif (5.9 <= cbg <= 7.8):
            totalScore += 0
        elif (7.9 <= cbg <= 8.9):
            totalScore += 2
        else: # >= 9.0
            totalScore += 3
        
    if scoresList:
        score, time = scoresList[-1]
        if datetime.now() - time <= timedelta(hours=24):
            increase = totalScore - score
            if increase > 2:
                print("ALERT: Medi score increased by " + str(increase) + " points.")
                print("Previous score: " + str(score) + ", new score: " + str(totalScore) + "")
    
            
    scoresList.append((totalScore, datetime.now()))
    return totalScore

# tests
print(mediScore(0,0,15,95,37.1, 3.4, True))
print(mediScore(2,0,17,95,37.1, 6, True))
print(mediScore(2,1,23,88,38.5, 5.6, False))
print(mediScore(2,2,25,93,40.4, 16, False))
print(mediScore(0,1,15,80,37.2, 3, False))

