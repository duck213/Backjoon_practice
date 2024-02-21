grade = int(input())
if 90 <= grade <= 100:
    grade = 'A'
elif 80 <= grade < 90:
    grade = 'B'
elif 70 <= grade < 80:
    grade = 'C'
elif 60 <= grade < 70:
    grade = 'D'
else:
    grade = 'F'
print(grade)
