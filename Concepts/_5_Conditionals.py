#if
age=20
if age>=18:
    print("Eligible to vote")

is_logged_in=True

if is_logged_in:
    print("Welcome User")

#if else
age=16
if age>=18:
    print("Eligible")
else:
    print("Not Eligible")

#if elif else
marks=75

if marks>=90:
    print("Grade A")
elif marks>=75:
    print("Grade B")
else:
    print("Grade C")

#Nested if
age=20
citizen=True

if age>=18:
    if citizen:
        print("Eligible to vote")

#Ternary operator
age=20
result="Eligible" if age>=18 else "Not Eligible"
print(result)

#Match Case
day = 2

match day:
    case 1:
        print("Monday")

    case 2:
        print("Tuesday")

    case _:
        print("Invalid Day")
