user = input("enter your user name please in capital letters")
print("HELLO"+" "+user+" "+"\nThese are the lottery results of today's lottery " )
print()
#part 1 - יצירת 5 מספרים אקראיים הנקראים הכדורים הלבנים
import random

whiteball_numbers=[]
a = random.randint(1, 20)
while len(whiteball_numbers) < 5:
    a = random.randint(1, 20)
    if a not in whiteball_numbers:
        whiteball_numbers.append(a)

#part2 - יצירת מספר אחד חזק נקרא פאוורבל
powerball_number = 0
for i in range(1):
    b=random.randint(1,10)
    powerball_number = b

whiteball_numbers.append(powerball_number)
print("Your whitball numbers :\n",whiteball_numbers)
print()

#יצירת 5 מספרים אקראיים שהם יהיו המספרים הזוכים
winning_numbers_of_today = []
# c=random.randint(1,20)
while len(winning_numbers_of_today) < 5:
    c = random.randint(1, 20)
    if c not in winning_numbers_of_today:
        winning_numbers_of_today.append(c)


#יצירת מספר אחד חזק נקרא והוא יהיה המספר הזוכה של היום
# winning_powerball_number=0
for i in range(1):
    d=random.randint(1,10)
    winning_numbers_of_today.append(d)
print("The winning numbers of today are : \n", winning_numbers_of_today)
print()

#פונקציה שמשווה בין 2 הרשימות בודקת אם יש התאמה ומביאה תעריף זכייה
def compar_score():
    count=0
    for i in(whiteball_numbers):
        for j in(winning_numbers_of_today):
            if i==j :
                count+=1
    print("Matches number :", count)
    print()
    if count == 5 and winning_numbers_of_today[5] == whiteball_numbers[5]:
        print("JACKPOT!!\n YOU WON 324,000,000$")
    elif count == 5 and winning_numbers_of_today[5]!= whiteball_numbers[5]:
        print("YOU WON 1,000,000$\n *** no powerball number ***")

    elif count == 4 and winning_numbers_of_today[5] == whiteball_numbers[5]:
        print("YOU WON 10,000$")
    elif count == 4 and winning_numbers_of_today[5] != whiteball_numbers[5]:
        print("YOU WON 100$\n *** no powerball number ***")

    elif count == 3 and winning_numbers_of_today[5]== whiteball_numbers[5]:
        print("YOU WON 100$")
    elif count == 3 and winning_numbers_of_today[5]!= whiteball_numbers[5]:
        print("YOU WON 7$\n *** no powerball number ***")

    elif count == 2 and winning_numbers_of_today[5] == whiteball_numbers[5]:
        print("YOU WON 7$")
    elif count == 2 and winning_numbers_of_today[5] != whiteball_numbers[5]:
        print("TRY AGAIN !!!!\n *** no powerball number ***")

    elif count == 1 and winning_numbers_of_today[5] == whiteball_numbers[5]:
        print("YOU WON 4$")
    elif count == 1 and winning_numbers_of_today[5] != whiteball_numbers[5]:
        print("TRY AGAIN !!!\n! *** no powerball number ***")

    elif count == 0 and winning_numbers_of_today[5] == whiteball_numbers[5]:
        print("YOU WON 4$")


    elif count == 0 and winning_numbers_of_today[5] != whiteball_numbers[5]:
        print("TRY AGAIN !!!!")

#קריאה לפונקצית הניקוד והתחלת ההגרלה
compar_score()

























