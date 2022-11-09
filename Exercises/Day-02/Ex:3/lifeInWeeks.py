# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
timeLeftInYears = 90 - int(age)
timeLeftInDays = timeLeftInYears * 365
timeLeftInWeeks = timeLeftInYears * 52
timeLeftInMonths = timeLeftInYears * 12
print(f"You have {timeLeftInDays} days, {timeLeftInWeeks} weeks, and {timeLeftInMonths} months left.")
