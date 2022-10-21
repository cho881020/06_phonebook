
# 전화번호부 예시 문제

# 파일 내용 처리 클래스 불러오기
from utils import FileManager


# 이름 / 연락처 / 출생년도를 입력받고, 저장할 문구로 변환해주는 함수
def get_contact_info():
    name = input('이름 입력 : ')
    phone_num = input('전화번호 입력 : ')
    birth_year = int(input('출생년도 4자리로 기입 : '))

    # 3개의 데이터를 => 1줄로 묶어서 => (f''이 자동) 줄바꿈 붙여서 csv로 저장
    save_content = f'{name},{phone_num},{birth_year}'
    # 만들어진 문구를 결과로 리턴
    return save_content


# 사용자가 0을 넣을때 까지 반복
# 무한히 입력 받다가, 0을 넣으면 종료

while True:
    print('===== 전화번호부 =====')
    print('1. 전화번호 등록')
    print('2. 저장된 전화번호 목록 조회')
    print('0. 프로그램 종료')
    print('=====================')
    input_num = int( input('메뉴 선택 : ') )

    if input_num == 0:
        print('프로그램을 종료합니다.')
        break
    elif input_num == 1:
        print('전화번호 추가를 선택했습니다.')

        # 임시 Test : FileManager로 내용 저장 가능?
        # 사용할 메쏘드 : 클래스 메쏘드

        # FileManager.write_content_to_file('테스트문구')

        # 입력사항 2가지. 1: 이름 / 2: 폰번 => 키보드 입력
        # 별도 함수에서 작업.

        # 입력받아 가공한 문구를 => 파일에 저장
        FileManager.write_content_to_file( get_contact_info() )  


    elif input_num == 2:
        print('목록 조회를 선택했습니다.')
    else:
        print('잘못된 입력입니다.')