# take a input percentage of a student and print the grade according to mark
"""
 80 to 100  very good
60 to 79 good
41 to 59 average
<=40 fail
"""

Per=int(input("Enter Percentage"))
if Per>=80:
    print("Very good")
elif Per>= 60:
    print("good")
elif Per>=41:
    print("Average")
else:
    print("fail")