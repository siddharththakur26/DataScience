'''
Input Format:
2
Harsh 25 26.5 28
Anurag 26 28 30
Harsh
'''
n = int(raw_input())
student_marks = {}
for _ in range(n):
    line = raw_input().split()
    name, scores = line[0], line[1:]
    scores = map(float, scores)
    student_marks[name] = scores
query_name = raw_input()
#print student_marks

for i in student_marks:
    if i == query_name:
        value = (sum(student_marks[i]))/len(student_marks[i])
        print("{0:.2f}".format(round(value,2)))
        break