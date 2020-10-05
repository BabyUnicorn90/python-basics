def handling_exception():
    lst = []

    try:
        print("예외 가능 코드 블록")

        if len(lst) > 3:   #방어코드
            lst[3] = 1
        #result = 4 / 0
        if "String".isdigit():
            int("String")
    except IndexError as e:    #구체적 예외
        print(e, type(e))
    except ZeroDivisionError as e:
        print(e, type(e))
    except ValueError as e:
        print(e, type(e))
    except Exception as e:      #구체적 예외로 처리되지 않은 모든 예외
        print(e, type(e))
    else:   #예외가 없을 때 수행될 코드
        print("예외 없이 코드를 수행하였습니다.")
    finally:   #예외유무 상관없이 항상 마지막에 수행 ---주로 자원정리할 때 사용
        print("예외 처리 종료")

    #예외처리순서 중요:
    #예외가 있다면: try - except - finally
    #예외가 없다면: try - else - finally

    print("End of Code")

if __name__ == "__main__":
    handling_exception()



##################################################################################################


#호출하는 함수:
def caller():
    try:
        result = callee(4, 0)
    except ZeroDivisionError as e:
        print(e, type(e))
    else:
        print(result)


#호출되는 함수:    --------내부에서 완벽하게 예외처리 및 복구가 힘들다면 호출한 함수로 예외처리를 위임(raise 예외객체)
def callee(a, b):
    if b == 0:
        raise ZeroDivisionError("0으로 나눌 수 없어요")
    return str.format("{ } / { } = { }".format(a, b, a/b))


if __name__ == "__main__":
    caller()
    callee()