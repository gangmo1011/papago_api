print(__name__)

def test_func():
    print('test function입니다')

if __name__ == '__main__' :
   print(__name__)
    print('test.py를 직접 실행한 경우')

else : 
    print(__name__)
    print('testy.py가 import되어 실행된 경우')