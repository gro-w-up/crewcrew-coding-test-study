import re

def solution(files):
    answer = []
    file_list = [re.split('([0-9]+)', file) for file in files]

    # sorted 정렬 기준 사용하기
    file_list = sorted(file_list, key=lambda x: (x[0].lower(), int(x[1])))

    return [''.join(file) for file in file_list]