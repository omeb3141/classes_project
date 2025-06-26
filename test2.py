from classes_project_code import MahaElintStudent, MahaStudent

def test_fail_id():
    m1 = MahaStudent("Omer Bahir", 54, "omerbahir10@gmail.com", "2025-03-19", "Elint")
def test_fail_update_mail():
    m1 = MahaStudent("Omer Bahir", 543700421, "omerbahir10@gmail.com", "2025-03-19", "Elint")
    m1.Mail = "omerbahir10@gmail.c.om"

def test_fail_recruit_date():
    m1 = MahaStudent("Omer Bahir", 543700421, "omerbahir10@gmail.com", "2025-08-19", "Elint")

def test_fail_profession():
    m1 = MahaStudent("Omer Bahir", 543700421, "omerbahir10@gmail.com", "2025-08-19", "Erint")

def test_fail_full_name():
    m1 = MahaStudent("Omer B ahir", 543700421, "omerbahir10@gmail.com", "2025-08-19", "Elint")

def test_fail_mail():
    m1 = MahaStudent("Omer Bahir", 543700421, "omer@bahir10@gmail.com", "2025-08-19", "Elint")