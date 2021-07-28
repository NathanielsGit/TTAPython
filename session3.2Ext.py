name = input("Please enter your name: ")
print ("Hi " + name + " welcome to the examination portal")
TargetGrade = int(input("Enter your target grade: "))
print ("Enter your score to find out your grade")

score = int(input("enter your score here: "))
def mark_grade(score):
    if score < 40:
        print("Sorry, you didn't achieve the pass mark on this occasion")
    elif score > 40 and score < 55:
        print("Congratulations, you scored a 3rd class honors")
    elif score > 55 and score < 70:
        print("Congratulations, you scored a 2.2 honors")
    elif score > 70 and score < 85:
        print("Congratulations, you scored a 2.1")
    elif score > 85 and score < 100:
        print("Congratulations, you scored a 2.1")

mark_grade(score)

if TargetGrade > score:
    print ("study harder")
else:
    print ("well done")