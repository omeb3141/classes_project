from enum import Enum
from datetime import date
from datetime import datetime


class MahaProfession(Enum):
    elint = "Elint"
    commint = "Commint"


class MahaStudent():
    total_students_number = 0

    def __init__(self, full_name, id, mail, recruit_date, profession):
        MahaStudent.total_students_number += 1
        if MahaStudent.checking_correct_full_name(full_name):
            self.full_name = full_name
        else:
            raise ValueError('illegal name')
        if MahaStudent.checking_correct_id(id):
            self.id = id
        else:
            raise ValueError('illegal id')
        if MahaStudent.checking_correct_mail(mail):
            self.mail = mail
        else:
            raise ValueError('illegal mail')
        if MahaStudent.checking_correct_date(recruit_date):
            self.recruit_date = recruit_date
        else:
            raise ValueError("illegal recruit date")
        if MahaStudent.checking_correct_profession(profession):
            self.profession = MahaProfession(profession)
        else:
            raise ValueError("illegal profession")


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
        counter_space_to_space_distance = 10
        for a in range(0, len(full_name)):
            if full_name[a] == " ":
                if counter_space_to_space_distance < 2:
                    return False
                counter_space_to_space_distance = 0
                nums_of_space += 1
            elif MahaStudent.is_char_english(full_name[a]):
                counter_space_to_space_distance += 1
            else:
                return False
        if nums_of_space > 0:
            return True
        return False

    @staticmethod
    def checking_correct_mail(mail):
        if mail.count("@") == 1 and mail.count('.') == 1:
            if mail.index("@") < mail.index(".") != len(mail) - 1 and mail.index("@") != 0:
                return True
        return False

    @staticmethod
    def checking_correct_condition_for_id(string_id):
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
        return MahaStudent.checking_correct_condition_for_id(id_string)

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

    @staticmethod
    def checking_correct_profession(profession):
        if profession in MahaProfession._value2member_map_:
            return True
        else:
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

    @Mail.setter
    def Mail(self, value):
        if MahaStudent.checking_correct_mail(value):
            self.mail = value
        else:
            print("illegal mail")

    @property
    def Recruit_Date(self):
        return self.recruit_date

    @property
    def Profession(self):
        return self.profession

    def get_pazam(self):
        return date.today() - datetime.strptime(self.recruit_date, '%Y-%m-%d').date()


class MahaElintStudent(MahaStudent):
    def __init__(self, full_name, id, mail, recruit_date):
        super().__init__(full_name, id, mail, recruit_date, "Elint")
        self.list_of_samples = []

    def add_sample(self, sample):
        if type(sample) == str:
            self.list_of_samples.append(sample)
        else:
            print("Only strings")

    @property
    def List_Of_Samples(self):
        return self.list_of_samples

