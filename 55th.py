a = 1  #this right here is at the global scope

def confusion():
    a =5
    return a  #this right here is at the local scope


print(confusion())

print(a)


# Python scope rules

#1..............start with local
#2..............parent local
#3..............Global
#4...............predefined python functions 


#What are paramenters then;

#Global keyword


total = 0

def count():
    global total
    total += 1
    return total


count()
count()
print(count())