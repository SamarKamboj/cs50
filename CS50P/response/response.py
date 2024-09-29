from validator_collection import checkers

if checkers.is_email(input("Email: ")):
    print("Valid")
else:
    print("Invalid")