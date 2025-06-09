import Function as fun
import Turtle as tur

while True:
        print("1.파일 읽어오기, 2.데이터 출력 및 저장하기, 3.그래프 그리기, 4.종료하기")
        react = input("번호를 입력해주세요.")
        if react == "1":
            print("파일을 읽어오겠습니다.")
            fun.Read_files()
            
        elif react == "2":
            print("등급과 개인평균을 계산하여 기존 학적 정보와 같이 저장 및 출력을 진행합니다.")
            fun.print_write_files()
        
        elif react == "3":
            print("터틀 그래픽을 이용하여 각 과목의 총 평균을 표현합니다.")
            tur.draw_dim()
            kor_avg, math_avg, eng_avg = fun.all_average()
            tur.draw_bar(-100, kor_avg, "국어", "red")
            tur.draw_bar(0, math_avg, "수학", "green")
            tur.draw_bar(100, eng_avg, "영어", "blue")
        
        elif react == "4":
            break
        else:
            print("잘못된 값을 입력하셨습니다. 1~4번 중에서 택해주십시오.")

print("프로그램이 종료되었습니다.")