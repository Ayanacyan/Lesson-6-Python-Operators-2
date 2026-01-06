character=input("Enter a character: ")

if ('A'<= character <= 'Z')or('a'<= character <= 'z'):
    print("This is an alphabet")

elif character.isdigit():
    print("This is a number, not an alphabet")

else:
    print("This is not an alphabet")                  