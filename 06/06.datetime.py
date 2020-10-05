import datetime

def get_datetime():
    #현재시간 구하기
    now = datetime.datetime.now()
    print("현재시간:", now)

    #생성자를 활용한 현재시간 구하기
    dt = datetime.datetime(2020, 10, 5)   #최소한 연월일은 지정해줘야 한다.
    print(dt)

    #속성
    print(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second, dt.microsecond)
    print(dt, "는 무슨 요일?", dt.weekday())    #월요일이 0

    #날짜 객체의 반환
    print(now.date(), type(now.date()))

    #시간 객체의 반환
    print(now.time(), type(now.time()))

if __name__ == "__main__":
    get_datetime()



#timedelta: 두 datetime은 대소를 비교 可, 차이도 구할 수 있다.
def timedelta_ex():
    now = datetime.datetime.now()
    past = datetime.datetime(1990, 5, 11)

    print(now > past)

    diff = now - past
    print(diff, type(diff))

#datetime과 timedelta을 합산하면 새로운 날짜를 얻을 수 있다.
#오늘로부터 100일 후 구하기:
    future = now + datetime.timedelta(days=100)
    print("오늘로부터 100일 후: ", future)

if __name__ == "__main__":
    timedelta_ex()


#datetime의 포맷팅:
def format_date():
    #datetime -> str: strftime
    #str -> datetime: strptime

    #1
    now = datetime.datetime.now()

    print("strftime: ", now.strftime("%Y-%m-%d %H:%M:%S"))

    #2
    s = '1990-05-11 14:00'
    dt = datetime.datetime.strptime(s,
                                    "%Y-%m-%d %H:%M")
    print("strptime: ", dt, type(dt))

if __name__ == "__main__":
    format_date()




