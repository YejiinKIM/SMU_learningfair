print("--- 아르바이트 급여 계산 프로그램 ---")
print("--- 2021년 최저시급은 8720원입니다 ---")
print("")

mywage = 0
totalwage = 0 
basic = int(input("시급을 입력하세요: "))
print("")

print("[시급]")
print("*** 주간근무 :", basic, "원 ***")
print("*** 야간근무 : 주간 시급 * 1.5 ***")
print("")


while True:
    select = input("주간근무 or 야간근무를 입력하세요 - - - >")
    worktime = int(input("근무 시간을 입력해 주세요 - - - >"))
    insurance = input("공제할 항목 소득세 or 4대보험 고르세요: ")
    print("")

    if worktime >= 15:
        plus = int(input("주휴수당이 발생하였습니다. 하루 일급을 입력해주세요: "))
        print("")

        if select == '주간근무' and insurance == '소득세':
            mywage = basic*worktime+plus
            totalwage = mywage-mywage*0.033

        elif select == '주간근무' and insurance == '4대보험':
            mywage = (basic*worktime+plus)
            totalwage = mywage-mywage*0.0913

        elif select == '야간근무' and insurance == '소득세':
            mywage = basic*worktime*1.5+plus
            totalwage = mywage-mywage*0.033

        else:#추가
            mywage = basic*worktime*1.5+plus
            totalwage = mywage-mywage*0.0913

        print(worktime, "시간 동안",select,"에 일을 한 급여는 ",mywage, "입니다.")
        print("보험료를 공제한 급여는 ",totalwage, "입니다.")
        
    else:
        if select == '주간근무' and insurance == '소득세':
            mywage = basic*worktime
            totalwage = mywage-mywage*0.033

        elif select == '주간근무' and insurance == '4대보험':
            mywage = (basic*worktime)
            totalwage = mywage-mywage*0.0913

        elif select == '야간근무' and insurance == '소득세':
            mywage = basic*worktime*1.5
            totalwage = mywage-mywage*0.033

        else:#추가
            mywage = basic*worktime*1.5
            totalwage = mywage-mywage*0.0913

        print(worktime, "시간 동안",select,"에 일을 한 급여는 ",mywage, "입니다.")
        print("보험료를 공제한 급여는 ",totalwage, "입니다.")

    print("")
    print("끝!")
    break   
