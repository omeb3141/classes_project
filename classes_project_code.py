from enum import Enum

class MahaProfession(Enum):
    elint = "Elint"
    commint = "Commint"

class MahaStudent():
    def __init__(self, full_name, id, mail, recruit_date, profession):
        self.full_name = full_name
        self.id = id
        self.mail = mail
        self.recruit_date = recruit_date
        self.profession = profession


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