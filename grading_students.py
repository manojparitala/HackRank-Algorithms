'''
a passing grade is any grade 40 points or higher on a 100 point scale. Sam is a professor at the university and likes to round each student’s grade according to the following rules:

If the difference between the grade and the next higher multiple of 5 is less than 3, round to the next higher multiple of 5
If the grade is less than 38, don’t bother as it’s still a failing grade
Automate the rounding process then round a list of grades and print the results.
'''
def solve(grades):
    k = []
    for i in grades:
        if i < 38:
            k.append(i)
        else:
            j = i / 5
            j = round(j)
            diff = (j * 5) - i
            if diff < 3 and diff > 0:
                k.append(j * 5)
            else:
                k.append(i)
    return k


n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
    grades_t = int(input().strip())
    grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))
