
kidsnumber = 1
sumAges = 0
aNumber = int(input("תכניס את גילו של תלמיד מספר " + str(kidsnumber) + ": "))

CanEnterParty = 0
CantEnterParty = 0

while not (aNumber==-1) :
    kidsnumber += 1
    if aNumber > 15 or aNumber < 12:
        print("אתה לא יכול להיכנס למסיבה")
        CantEnterParty += 1

    else:
        print("אתה יכול להיכנס למסיבה")
        CanEnterParty += 1
        sumAges += aNumber

    aNumber = int(input("תכניס את גילו של תלמיד מספר " + str(kidsnumber) + ": "))

print("אתה לא יכול להיכנס למסיבה.")
CantEnterParty += 1

print("נכנסו " + str(CanEnterParty) + " תלמידים ולא הורשו להיכנס " + str(CantEnterParty) + " תלמידים")

if CanEnterParty == 0:
    print("ממוצע גיל האנשים שהורשו להכנס : 0 אף תלמיד לא נכנס למסיבה")
else:
    average = sumAges / CanEnterParty
    twoDigitsAverage = int(average * 100) / 100
    print("ממוצע גיל הנכנסים : " + str(twoDigitsAverage))