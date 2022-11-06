# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
capName1=name1.upper()
capName2=name2.upper()
combinedNames=capName1+capName2
T=combinedNames.count('T')
R=combinedNames.count('R')
U=combinedNames.count('U')
E=combinedNames.count('E')
L=combinedNames.count('L')
O=combinedNames.count('O')
V=combinedNames.count('V')
E=combinedNames.count('E')
totalTrue = T+R+U+E
totalLove = L+O+V+E
totalScore = str(totalTrue)+str(totalLove)
if int(totalScore) < 10 or int(totalScore) > 90:
    print(f"Your score is {totalScore}, you go together like coke and mentos.")
elif int(totalScore) > 40 and int(totalScore) < 50:
    print(f"Your score is {totalScore}, you are alright together.")     
else:
    print(f"Your score is {totalScore}")
