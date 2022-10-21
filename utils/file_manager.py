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