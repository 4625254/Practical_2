n = int(input("Enter the number of students: "))

student = []
score = []
i = 0

for i in range(n):
    student.append(str(input("Student Name: ")))
    score.append(float(input("Score: ")))

index = score.index(max(score))
print("Student with the highest score is",student[index],"who scored",score[index])

student.remove(student[index])
score.remove(score[index])

index = score.index(max(score))

print("Student with the highest score is",student[index],"who scored",score[index])
