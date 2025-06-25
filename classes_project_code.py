from enum import Enum
from datetime import date
from datetime import datetime

class MahaProfession(Enum):
    elint = "Elint"
    commint = "Commint"


class MahaStudent():
    total_students_number = 0

    def __init__(self, full_name, id, mail, recruit_date, profession):
        if MahaStudent.checking_correct_full_name(full_name):
            self.full_name = full_name
        else:
            print("illegal name")
            self.full_name = "No"
        if MahaStudent.checking_correct_id(id):
            self.id = id
        else:
            print("illegal id")
            self.id = 0
        if MahaStudent.checking_correct_mail(mail):
            self.mail = mail
        else:
            print("illegal mail")
            self.mail = "No"
        if MahaStudent.checking_correct_date(recruit_date):
            self.recruit_date = recruit_date
        else:
            print("illegal recruit date")

        self.profession = MahaProfession(profession)
        MahaStudent.total_students_number += 1

    @classmethod
    def total_students(cls):
        return MahaStudent.total_students_number

    @classmethod
    def delete_student(cls):
        MahaStudent.total_students_number -= 1

    @staticmethod
    def is_char_english(char_eng):
        if 'a' <= char_eng <= 'z':
            return True
        if 'A' <= char_eng <= 'Z':
            return True
        return False

    @staticmethod
    def checking_correct_full_name(full_name):
        if len(full_name) == 0:
            return False
        nums_of_space = 0
        counter_space = 10
        for a in range(0, len(full_name)):
            if full_name[a] == " ":
                print(a, counter_space)
                if counter_space < 2:
                    return False
                counter_space = 0
                nums_of_space += 1
            elif MahaStudent.is_char_english(full_name[a]):
                counter_space += 1
            else:
                return False
        if nums_of_space > 0:
            return True
        return False

    @staticmethod
    def checking_correct_mail(mail):
        if mail.count("@") == 1 and mail.count('.') == 1:
            if mail.index("@") < mail.index("."):
                return True
        return False

    @staticmethod
    def checking_correct_condition(string_id):
        sum1 = 0
        for i in range(0, len(string_id) - 1):
            if i % 2 == 1:
                num_to_add = 2 * int(string_id[i])
                if num_to_add >= 10:
                    sum1 += num_to_add // 10 + num_to_add % 10
                else:
                    sum1 += num_to_add
            else:
                sum1 += int(string_id[i])
        return min(10 - (sum1 % 10), (sum1 % 10)) == int(string_id[-1])

    @staticmethod
    def checking_correct_id(id):
        id_string = str(id)
        if len(id_string) > 9:
            return False
        id_string = "0" * (9 - len(id_string)) + id_string
        return MahaStudent.checking_correct_condition(id_string)

    @staticmethod
    def date_is_legal(date_str):
        try:
            datetime.strptime(date_str, '%Y-%m-%d').date()
            return True
        except:
            return False

    @staticmethod
    def checking_correct_date(date_str):
        if MahaStudent.date_is_legal(date_str):
            if datetime.strptime(date_str, '%Y-%m-%d').date() <= date.today():
                return True
        return False

    @property
    def Full_Name(self):
        return self.full_name

    @property
    def Id(self):
        return self.id

    @property
    def Mail(self):
        return self.mail

    @property
    def Recruit_Date(self):
        return self.recruit_date

    @property
    def Profession(self):
        return self.profession


print(date.today())
d1 = date(1, 2, 3)
print(date.today() - d1)


def string_is_all_digits(string_sus):
    return all(a.isdigit() for a in string_sus)


def is_date_correct(date_given):
    date_list = date_given.split('.')
    if len(date_given) != 3:
        return False
    for st in date_list:
        if not string_is_all_digits(st):
            return False
    if not 0 < int(date_list[1]) < 13:
        return False
    if not 0 < int(date_list[1]) < 13:
        return 0






print(datetime.strptime("2025-06-25", '%Y-%m-%d').date() <= date.today())