format_title = '{:^0}\t{:^12}\t{:^8}\t{:^8}\t{:^10}'
format_data = '{:^0}\t{:^12}\t{:^8}\t{:^8}\t{:^10}'


def add(info):
    while True:
        flag = False
        Id = int(input('学生のID:'))
        name = input('学生の名前:')
        age = int(input('学生の年齢:'))
        sex = input('学生の性別:')
        score = int(input('学生の成績:'))
        for i in info:
            if Id == i['id']:
                flag = True
                break
        if flag:
            input('このIDの学生情報の既に存在します。')
            break
        info += [{'id': Id, 'name': name, 'age': age, 'sex': sex, 'score': score}]
        q = input('追加は成功しました。Enterを押して進んでください。(ｑを入力しEnterを押して終了します。):')
        if q == 'q':
            break
    return info


def show(info):
    if len(info) == 0:
        input("暫く学生情報はございません。任意のキーを押して戻ってください。")
        return

    print(format_title.format('编号', '姓名', '年龄', '性别', '成绩'))

    for i in info:
        print(format_data.format(i.get('id'), i.get('name'), i.get('age'), i.get('sex'), i.get('score')))
    input('任意のキーを押してメインメニューに戻ってください')


def delete(info):
    flag = 0
    count = 0
    print("学生情報を削除")
    Id = int(input('対象の学生番号を入力(０を入力で戻る)：'))
    if Id == 0:
        return
    for i in info:
        if i['id'] == Id:
            del info[count]
            flag = 1
            input('削除は成功しました，任意のキーを押して戻ってください。')
        count += 1
    if flag == 0:
        print(Id, 'という名前の学生を見つかりませんでした。任意のキーを押して戻ってください。', end='')
        input()


def update(info):
    flag = 0
    print("学生情報を訂正")
    Id = int(input('対象の学生番号を入力(０を入力で戻る)：'))
    if Id == 0:
        return
    for i in info:
        if i['id'] == Id:
            flag = 1
            name = input('学生の名前:')
            age = int(input('学生の年齢:'))
            sex = input('性別:')
            score = input('学生の成績:')
            i['name'] = name
            i['age'] = age
            i['sex'] = sex
            i['score'] = score
            input('訂正は成功しました。任意のキーを押して進んでください。')
    if flag == 0:
        print( Id, 'という名前の学生情報を見つかりませんでした。任意のキーを押して戻ってください。', end='')
        input()


def sort(info):
    x = sorted(info, key=lambda info: info['score'])
    print('成績順位')
    print(format_title.format('ID', '名前', '年齢', '性別', '成績'))
    for i in x:
        print(format_data.format(i.get('id'), i.get('name'), i.get('age'), i.get('sex'), i.get('score')))
    input('メインメニューに戻る')

