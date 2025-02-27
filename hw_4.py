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


class Teacher(GeeksPeople):

    def __init__(self, name, email, phone_number, teacher_id, group_where_teach):
        GeeksPeople.__init__(self, name, email, phone_number)
        self.teacher_id = teacher_id
        self.group_where_teach = group_where_teach


class Admin(GeeksPeople):
    def __init__(self, name, email, phone_number):
        GeeksPeople.__init__(self, name, email, phone_number)


p1 = GeeksPeople("Vlad", "vladboulderchannel@gmail.com", "0505666038")
