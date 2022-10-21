
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


# 연락처 목록 파일에서 불러내서 / 가공 후 표시
def print_all_contacts():

    # 파일매니저에서 목록을 받아오자.
    content_list = FileManager.read_content_in_file()
    # print(content_list)

    # ,로만 이어진 str 들을 => 가공해서 출력
    for content  in  content_list:
        # 가공 1. 줄바꿈 제거
        # str의 replace (치환) 기능 활용ㄴ 
        content =  content.replace('\n', '')
        # print(content)

        # 가공 2. 조경진(35세) : 010-5112-3237 형태.
        # ,로 구별된 데이터들을 각각 추출.
        # 조경진,010,1988 를 => ,를 기준으로 분리 => 목록으로.
        # split 기능 활용

        info_list = content.split(',')
        # print(info_list)

        name = info_list[0]
        phone_num = info_list[1]
        birth_year = int(info_list[2])
        age = 2022 - birth_year + 1

        print(f'{name}({age}세) : {phone_num}')




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

        # 파일매니저에서, 저장된 연락처 불러오기 => 화면에 출력
        # 별도 함수에서 실행

        print_all_contacts()

    else:
        print('잘못된 입력입니다.')