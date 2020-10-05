#pickle모듈: 객체를 직렬화, 역직렬화

import pickle

#직렬화 예제
def test_pickle_dump():
    with open("thieves.bin", "wb") as f:    #파일모드는 반드시 binary여야 함
        try:
            pickle.dump({"name": "홍길동", "age": 25}, f)
        except Exception as e:
            print(e, type(e))
            print("데이터를 덤프하지 못했습니다.")
        else:
            print("데이터를 덤프했습니다. ")

#if __name__ == "__main__":
#    test_pickle_dump()

##############################################################################

#역직렬화 예제
def test_pickle_load():
    with open("thieves.bin", "rb") as f:
        try:
            thief = pickle.load(f)
        except Exception as e:
            print(e, type(e))
            print("데이터를 로드하지 못했습니다.")
        else:
            print("데이터를 로드했습니다. ")
            print(thief)

# if __name__ == "__main__":
#     test_pickle_load()

#한 파일에 여러 객체를 직렬화: dump 중복수행
def test_pickle_multi_dump():
    t1 = {"name": "홍길동", "age": 25}
    t2 = {"name": "장길산", "age": 40}
    t3 = {"name": "임꺽정", "age": 35}

    with open("thieves.bin", "wb") as f:
        try:
            pickle.dump(t1, f)
            pickle.dump(t2, f)
            pickle.dump(t3, f)
        except Exception as e:
            print(e, type(e))
            print("데이터를 덤프하지 못했습니다.")
        else:
            print("데이터를 덤프했습니다. ")

# if __name__ == "__main__":
#    test_pickle_multi_dump()


#thieves.bin에서 사전을 역직렬화하여 리스트에 담아보기
def test_pickle_multi_load():
    thieves = []
    with open("thieves.bin", "rb") as f:
        """
        print(pickle.load(f))
        print(pickle.load(f))
        print(pickle.load(f))
        print(pickle.load(f)) #EOF에러 (End Of File)
        print(pickle.load(f))
        """
        while True:
            try:
                thief = pickle.load(f)
                thieves.append(thief)
            except EOFError as e:   #더이상 읽을 pickle이 없다!
                break
            else:
                print(thief)

if __name__ == "__main__":
   test_pickle_multi_load()
