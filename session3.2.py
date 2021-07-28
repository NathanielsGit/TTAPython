name = input("Please enter your name: ")
print ("Hi " + name + " welcome to the examination portal")
print ("Enter your score to find out your grade")

score = int(input("enter your score here: "))

def mark_grade (score):
    if score < 40:
        print ("Sorry, you didn't achieve the pass mark on this occasion")
    elif score > 40 and score <55:
        Print ("Congratulations, you scored a 3rd class honors")
    elif score > 55 and score <70:
        Print("Congratulations, you scored a 2.2 honors")
    elif score > 70 and score <85:
        Print("Congratulations, you scored a 2.1")
    elif score > 85 and score <100:
        Print("Congratulations, you scored a 2.1")
print mark_grade(score)
