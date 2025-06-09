
from dataclasses import dataclass

#dataclass를 이용한 구조체 Students(일종의 커스텀 자료형)이자 class Students(표현법 동일)
#https://ihp001.tistory.com/43

#dataclass 모듈 사용법
#https://www.daleseo.com/python-dataclasses/


#편리한 데이터 구분을 위해서
@dataclass
class Students:
    name : str
    dept : str #학과
    kor : int
    eng : int
    math : int
    avg : float
    deg : str #등급

students_list = []

def Read_files():
    with open('data.txt', 'r', encoding='utf-8') as files:
        for line in files:
            parts = line.strip().split() #\n, 공백을 기준으로 나누기
            if len(parts) >= 5:
                name = parts[0]
                dept = parts[1]  # 학과명이 2단어 이상일 수 있으므로
                kor = int(parts[2])
                eng = int(parts[3])
                math = int(parts[4])
                

                avg = round((kor + eng + math) / 3, 5) #소수점 5자리
                deg = personal_grade(avg)

                student = Students(name, dept, kor, eng, math, avg, deg) #
                students_list.append(student)
#파일 데이터 읽어오면서 띄어쓰기로 구분된 값을 저장

def print_write_files():
    with open('result.txt', 'w', encoding='utf-8') as files:
        for student in students_list:
            files.write(f"{student.name} {student.dept} {student.kor} {student.eng} {student.math} {student.avg} {student.deg}")
        files.write(f"\n\n\n {deg_count()}")
        for student in students_list:
            print(f"{student.name} {student.dept} {student.kor} {student.eng} {student.math} {student.avg} {student.deg}")
        print(f"\n\n\n {deg_count()}")
    #for 이름, 학과(dept), 각학점,(kor, eng, math) 개인 평균(avg), 등급(deg)
    #등급의 종류와 개수
#https://ybworld.tistory.com/20

def all_average():
    all_eng = 0; all_math = 0; all_kor = 0
    count=len(students_list) #명 수
    for student in students_list:
        all_kor += student.kor
        all_eng += student.eng
        all_math += student.math
    
    avg_math = 0; avg_eng = 0; avg_kor = 0
    avg_eng = all_eng / count; avg_kor = all_kor / count; avg_math = all_math / count
    return avg_eng, avg_kor, avg_math  

def personal_grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    else:
        return 'F'

def deg_count():
    grade_counter = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    
    for student in students_list:
        grade = student.deg
        grade_counter[grade] += 1

    deg_data = ""
    for grade in grade_counter:
        deg_data += f"{grade}: {grade_counter[grade]}명\n"
    return deg_data

            
        

