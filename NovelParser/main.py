import csv
import os


def clean_s(s: str):
    # cleanup the sentence

    remove_sentence = [
        'bk笔趣阁手机端',
        '请收藏本站：https://www.ddxss.cc。顶点小说手机版：https://m.ddxss.cc',
        '『点此报错』『加入书签』'
    ]
    if s in remove_sentence:
        s = ''

    remove_prefix = [
        '看更多诱惑小说请关注微信npxswz各种乡村都市诱惑'
    ]
    for prefix in remove_prefix:
        if s.startswith(prefix):
            s = s[len(prefix):]

    remove_suffix = [
        '笔趣阁手机端'
    ]
    for suffix in remove_suffix:
        if s.endswith(suffix):
            s = s[:-len(suffix)]

    return s


def cleanup(raw: str):
    sentences = [s.strip() for s in raw.split('\n')]

    s_list = []
    for s in sentences:
        new_s = clean_s(s)
        # skip empty strings
        if new_s == '':
            continue
        s_list.append(new_s)

    return '\n\n'.join(s_list)


def preprocess(src: str):
    chapters = []
    with open(src, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        # skip column names
        next(reader)

        for row in reader:
            chapter_title = row[2]
            chapter_no = int(row[3].split('/')[-1].split('.')[0])
            # chapter 735-743 missing (inclusive)
            if chapter_no > 734:
                chapter_no += 9
            chapter_text = cleanup(row[4])
            chapters.append([chapter_no, chapter_title, chapter_text])

    return chapters


def to_md(title: str, author: str, notice: str, c_list):
    txt = '% {}\n% {}\n\n{}\n\n'.format(title, author, notice)

    for c in c_list:
        c_title = c[1]
        c_text = c[2]
        txt += '# {}\n\n'.format(c_title) + c_text + '\n\n'

    # remove the last '\n'
    return txt[:-1]


if __name__ == '__main__':
    path = 'data'
    filename = 'book'
    filepath = os.path.join(path, filename + '.csv')

    chapters = preprocess(src=filepath)

    # chapter 735-743 are missing (inclusive), read from extra source
    # Update: actually not missing, but a numbering mistake made by the author, so extra.csv is left empty
    # the following block of code does not have any effect when the csv file is empty
    extra_name = 'extra'
    extra_path = os.path.join(path, extra_name + '.csv')
    chapter_no = 735
    with open(extra_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            # csv row data: title,content
            chapter_title = row[0]
            chapter_text = cleanup(row[1])
            chapters.append([chapter_no, chapter_title, chapter_text])
            chapter_no += 1

    chapters.sort()
    print('Total chapters ({} expected):'.format(834 - 9), len(chapters))

    title = '法神重生'
    author = '我吃大老虎'
    notice = '注：本文第七百三四章后面跟着的是第七百四四章，经过检查发现剧情上并没有缺失，应该是原作者标注章节时的谬误。'
    md_txt = to_md(title, author, notice, chapters)

    output_name = filename + '.md'

    with open(output_name, 'w', encoding='utf-8') as f:
        f.write(md_txt)
