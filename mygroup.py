groupmates = [
    {
        "name": "Иван",
        "surname": "Александров",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Александр",
        "surname": "Иванов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 3, 4]
    },
    {
        "name": "Кирилл",
        "surname": "Дроздов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [3, 4, 3]
    },
    {
        "name": "Виталий",
        "surname": "Нагирный",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 4, 5]
    },
    {
        "name": "Александра",
        "surname": "Васильева",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [5, 5, 4]
    }
]


def avg_score(students, avg):
    print(u"Имя".ljust(15), u"Фамилия".ljust(12), u"Экзамены".ljust(30), u"Оценки".ljust(10), u"Средний балл".ljust(20))
    result = []
    for student in students:
        stud = sum(student["marks"])/len(student["marks"])
        if stud >= avg:
            student["avg"] = stud
            result.append(student)

    for student in result:
        print(student["name"].ljust(15), student["surname"].ljust(12), str(student["exams"]).ljust(30),
              str(student["marks"]).ljust(10), round(student["avg"], 2))


def print_students(students):
    print(u"Имя".ljust(15), u"Фамилия".ljust(12), u"Экзамены".ljust(30), u"Оценки".ljust(20))
    for student in students:
        print(student["name"].ljust(15), student["surname"].ljust(12), str(student["exams"]).ljust(30),
              str(student["marks"]).ljust(20))


print_students(groupmates)

avg_s = float(input())

avg_score(groupmates, avg_s)
