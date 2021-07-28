name = input("Please enter your name here")
print("Hi" + name + ", thanks for choosing the Boom box music app, here you'll find the latest music and features")
print("Choose which package you would like to go for")
options = input("Enter S for standard, A for avid, C for creative")

def std_ft():
    print("Access to D-Cypher, our very own in app feature that shows yoy the lyrics to any song")
    print("Awesome music at your finger tips")

def avd_ft():
    print("Ad free listening")
    print("Playlist recommendation")
    print("Access to listening parties(be the first to hear when artists release new music")

def crtv_ft():
    print("Exclusive features and industry updates")
    print("Access to podcasts")
    print("Connect with other creatives through Boom Chat"

if options == "s":
    print("You chose the Standard package, here are the features")
    std_ft()
elif options == "a":
    print("You chose the avid listener package, here are the features")
    std_ft()
    avd_ft()
elif options == "c":
    print("You chose the creatives package, here are the features")
    std_ft()
    avd_ft()
    crtv_ft()
