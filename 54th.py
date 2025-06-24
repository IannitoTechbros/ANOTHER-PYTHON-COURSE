#let's talk about scopes - what varibales do I have access to 

#we have global variables and local variables

#we also have function scopes

if True:
    x = 10


def look_for_x():
    print(x)


look_for_x()


