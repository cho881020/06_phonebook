# 파일 입출력을 전담하는 클래스

class FileManager:

    # 전화번호부 파일명 => 클래스 변수
    file_name = 'phone_book.csv'

    # str이 들어오면 => 파일에 추가 기록.
    # 어느 객체인지? 관계 없다 => 단순 기능 수행
    # classmethod로 설정해, 클래스 변수도 활용.

    @classmethod
    def write_content_to_file(cls, content):

        with open(cls.file_name, 'a', encoding='UTF-8') as file:
            # pass # 지정된 파일명으로 내용 이어붙이기 모드 진입.
            # 단순히 입력 내용을 붙이기만 하겠다. + 줄바꿈
            file.write(f'{content}\n')


    # read_content_in_file 클래스 메쏘드
    # 한줄씩 읽어내서, list로 담아서 리턴
    # [ '조경진,010-5112-3237,1988', '김친구,010-5555-6666,1992' ]

    @classmethod
    def read_content_in_file(cls):
        # 파일을 읽기모드 열자.
        # 파일명 : 클래스 변수 활용
        with open(cls.file_name, 'r', encoding='UTF-8') as file:
            
            # list를 만들고 읽은 줄을 추가
            # read_lines = []
            
            # # 읽을 내용이 없을때까지 무한
            # while True:
                
            #     line = file.readline()
            #     if line == '':
            #         break

            #     read_lines.append(  line  )

            # 읽은 줄들을 모아서 list로.
            read_lines = file.readlines()

            return read_lines
