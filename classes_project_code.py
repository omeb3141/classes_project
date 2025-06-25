from enum import Enum

class MahaProfession(Enum):
    elint = "Elint"
    commint = "Commint"

class MahaStudent():
    total_students_number = 0
    def __init__(self, full_name, id, mail, recruit_date, profession):
        self.full_name = full_name
        self.id = id
        self.mail = mail
        self.recruit_date = recruit_date
        self.profession = profession
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

def checking_correct_condition(string_id):
    sum1 = 0
    for i in range(0, len(string_id)-1):
        if i%2 == 1:
            num_to_add = 2*int(string_id[i])
            if num_to_add >= 10:
                sum1 += num_to_add // 10 + num_to_add % 10
            else:
                sum1 += num_to_add
        else:
            sum1 += int(string_id[i])
    return min(10-(sum1%10), (sum1%10)) == int(string_id[-1])

def checking_correct_mail():


