voted = {}
voted['tom'] =True
def check_voted(name):
    if voted.get(name):
        print ("Get out you criminal scum")
    else:
        voted[name] = True
        print("You can voted")

check_voted("tom")
check_voted("tom")
check_voted("jarry")