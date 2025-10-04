student_perfomance_dict = {}


while True:
    input_string = input()

    if input_string == "END":
        break

    name, subject, grade = input_string.split()

    student_perfomance_dict[name, subject] = grade

student_surname = input()
subjects = {}

for item in student_perfomance_dict.items():
    if item[0][0] == student_surname:
        subjects[item[0][1]] = item[1]

for subject in sorted(subjects.items()):
    print(f"{subject[0]} {subject[1]}")

