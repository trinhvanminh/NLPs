import re

def sentence_tokenizer(str):
    # split = re.split('(?<=[.?!])\s+', str)
    split = re.split(r'(?<=(?:(?<!ThS(?=\.))(?<!TS(?=\.))(?<!PGS(?=\.))(?<!GS(?=\.))(?<!BS(?=\.)))[.?!])\s+', str)
    return split

def modify_sen_list(sen_list_raw):
    sen_ = []
    for sen in sen_list_raw:
        # print(type(sen), sen) --> all str
        sen = sen.replace(sen[0],sen[0].lower())
        sen_.append(re.sub(r'((?<!ThS(?=\.))(?<!TS(?=\.))(?<!PGS(?=\.))(?<!GS(?=\.))(?<!BS(?=\.))[.!?])',r' \1',sen, 1))
    return sen_

def word_case_list(words):
    l = len(words)
    word_case = []
    for idx in range(l):
        word_case_child = []
        for i in range(1, min(4, l - idx)):
            t = ''
            for j in range(i):
                t += words[j + idx] + ' '
            t += words[i + idx]
            word_case_child.append(t)
        word_case.append(word_case_child)

    return word_case

def is_in_Dict(w, Dict_file):
    while True:
        line = Dict_file.readline()
        if not line:
            return False
        if w == line[:-1]:
            return True

def vi_word_tokenizer(Dict_fname, word_case_list):
    wcl = word_case_list
    with open(Dict_fname,'r',encoding='utf-8-sig') as f:
        vi_word_list = ['bé', 'Hoa', 'được', 'dịp', 'nô', 'đùa', 'thoả', 'thích', '...']
        for wc in wcl:
            t = ''
            for w in wc:
                f.seek(0)
                if is_in_Dict(w, f):
                    t = w
            if t != '':
                vi_word_list.append(t.replace(' ','_'))
    return vi_word_list
                    

if __name__ == "__main__":
    # str = input('Nhập Str: ')
    # str = "Ngày chủ nhật bố mẹ vắng nhà... Bé Hoa được dịp nô đùa thoả thích. Text nè! Text nè? PGS.TS. Nguyen Van A. Text."
    str = "Bé Hoa được dịp nô đùa thoả thích."
    sen_list_raw = sentence_tokenizer(str)
    sen_list = modify_sen_list(sen_list_raw)
    for sen in sen_list:
        words = sen.split()
        wcl = word_case_list(words)
        print(vi_word_tokenizer('VDic_v2.txt',wcl))


