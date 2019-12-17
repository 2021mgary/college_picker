# Must use a model.py page with at least 1 function that takes input and returns something
def college(x):
    if x in range(0,7):
        college = "city college of new york"
    elif x in range(7,11):
        college = "fordham university"
    elif x in range(11,15):
        college = "UCLA"
    elif x in range(15,19):
        college = "amherst college"
    elif x in range(19,24):
        college = "barnard college"
    elif x in range(24,26):
        college = "morehouse college"
    elif x in range(25,27):
        college = "stanford university"
    elif x in range(27,28):
        college = "MIT"
    else:
        college = "no college"
    return college

print(college(7))
print(college(26))
