import json

format_data = '{:^0}\t{:^12}\t{:^8}\t{:^8}\t{:^10}'


def save(info):
    file = open("students.txt", "w", encoding='utf-8')
    for i in info:
        file.write(json.dumps(i, ensure_ascii=False))
        file.write('\n')
    file.close()
    input('戻る')


def read(info):
    file = open("students.txt", "r", encoding='utf-8')
    format_title = '{:^0}\t{:^12}\t{:^8}\t{:^8}\t{:^10}'
    print(format_title.format('ID', '名前', '年齢', '性別', '成績'))
    while True:
        ss = file.readline()
        if ss == '':
            break
        s = json.loads(ss,strict=False)
        print(format_data.format(s.get('id'), s.get('name'), s.get('age'), s.get('sex'), s.get('score')))
        info += [s]
    file.close()
    input('戻る')
    return info
