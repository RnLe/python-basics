import time, locale
name = input("Please enter your name: ")
print("Hello, %s!" %name)

# Date and time in local language settings
locale.setlocale(locale.LC_ALL, "")     # Uses the locally used language for time formatting
time = time.strftime("Todays is %A, the %d. %B.")
print(time)