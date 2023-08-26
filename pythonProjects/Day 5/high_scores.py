
students_scores = input("Input list of students scores: ").split()
print(type(students_scores))
for n in range(0,len(students_scores)):
    students_scores[n] = int(students_scores[n])



highest_score = 0
for score in students_scores:
    if score > highest_score:
        highest_score = score

print(highest_score)