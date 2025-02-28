class GeeksPeople:
    def __init__(self, name, email, phone_number):
        self.name = name
        self.email = email
        self.phone_number = phone_number

    def __str__(self):
        return f"Имя:{self.name}\nEmail почта:{self.email}\nНомер телефона:{self.phone_number}"


class Student(GeeksPeople):
    def __init__(self, name, email, phone_number, student_id, group_where_study):
        GeeksPeople.__init__(self, name, email, phone_number)
        self.student_id = student_id
        self.group_where_study = group_where_study

    def study(self):
        print(f"Студент: {self.name}\nУчится в группе под названием: {self.group_where_study}")


class Teacher(GeeksPeople):
    def __init__(self, name, email, phone_number, teacher_id, group_where_teach):
        GeeksPeople.__init__(self, name, email, phone_number)
        self.teacher_id = teacher_id
        self.group_where_teach = group_where_teach

    def teach(self):
        print(f"Преподователь: {self.name}\nПерподаёт в группе под названием: {self.group_where_teach}")


class Admin(GeeksPeople):
    def __init__(self, name, email, phone_number, admin_id):
        GeeksPeople.__init__(self, name, email, phone_number)
        self.admin_id = admin_id

    def create_group(self, name_group):
        print(f"Новая группа создана : {name_group}")

class Mentor(Student, Teacher):
    def __init__(
        self,
        name,
        email,
        phone_number,
        student_id,
        group_where_study,
        teacher_id,
        group_where_teach,
    ):
        Student.__init__(self, name, email, phone_number, student_id, group_where_study)
        Teacher.__init__(self, name, email, phone_number, teacher_id, group_where_teach)


# p1 = GeeksPeople("Vlad", "vladboulderchannel@gmail.com", "0505666038")
st1 = Student("Владислав", "vladboulder@gmail.com", "+79775782690", 1, "25-1B")
tch1 = Teacher("Владислав", "vlad@gmail.com", "0226606163", 2,"25-1B")
admin1 = Admin("Vladislav", "vladboulderchannel@gmail.com", "0505666038", 3)
ment1 = Mentor("Vladislav", "vladboulderchannel@gmail.com", "0505666038", 4, "25-1B", 5, "27-1B")

print(st1)
st1.study()
print("--------------------------------")

print(tch1)
tch1.teach()
print("--------------------------------")


print(admin1)
admin1.create_group("25-2B")
print("--------------------------------")

print(ment1)
ment1.study()
ment1.teach()
print("--------------------------------")
