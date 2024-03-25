student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

score_set = 0
for score in student_scores:
  if score_set < score:
    score_set = score
print(f"The heighest score in the class is: {score_set}")