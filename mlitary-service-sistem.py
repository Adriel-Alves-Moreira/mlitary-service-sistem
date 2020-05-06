from datetime import date
import webbrowser
from time import sleep
current = date.today().year
birth = int(input("Year of birth: "))
age = current - birth
print("Who was born in {} is {} years old in {}". format(birth, age, current))
if age == 18:
    print("You are already 18 years old, and it's time to enlist in your country's armed forces")
    sleep(8)
    webbrowser.open("http://www.eb.mil.br/")
    exit()
elif age < 18:
    future = 18 - age
    rd = current + future
    print("You are not yet 18 years old, you must join the armed forces in {}".format(rd))
elif age > 18:
    past = age - 18
    rd = current - past
    print("You should have joined the military in {}".format(rd,))
