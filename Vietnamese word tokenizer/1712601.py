import re
import os

def sentence_tokenizer(str):
    # split = re.split('(?<=[.?!])\s+', str)
    split = re.split(r'(?<=(?:(?<!ThS(?=\.))(?<!TS(?=\.))(?<!PGS(?=\.))(?<!GS(?=\.))(?<!BS(?=\.)))[.?!])\s+', str)
    return split

def modify_sen_list(sen_list_raw):
    sen_ = []
    for sen in sen_list_raw:
        # print(type(sen), sen) --> all str
        sen = sen.replace(sen[0],sen[0].lower(), 1)
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

def vi_word(Dict_fname, word_case_list):
    wcl = word_case_list
    vi_word_list = []
    with open(Dict_fname,'r',encoding='utf-8-sig') as f:
        for wc in wcl:
            t = ''
            for w in wc:
                f.seek(0)
                if is_in_Dict(w, f):
                    t = w
                else:
                    break
            if t != '':
                vi_word_list.append(t)
    return vi_word_list

def complete_sen(sen , vi_word_list):
    for vw in vi_word_list:
        sen = sen.replace(vw, vw.replace(' ','_'))
    return sen

def vi_word_tokenizer(str):
    sen_list_raw = sentence_tokenizer(str)
    sen_list = modify_sen_list(sen_list_raw)
    vi_sen = []
    for sen in sen_list:
        words = sen.split()
        wcl = word_case_list(words)
        vi_word_list = vi_word('VDic_v2.txt',wcl)
        comp_s = complete_sen(sen, vi_word_list)
        comp_s = comp_s.replace(comp_s[0],comp_s[0].upper(), 1)
        vi_sen.append(comp_s)
    return vi_sen

if __name__ == "__main__":
    str = input('Input: ')
    # str = "Ngày chủ nhật bố mẹ vắng nhà... Bé Hoa được dịp nô đùa thoả thích. Text! Text? PGS.TS. Nguyen Van A. Text."
    vwt = vi_word_tokenizer(str)
    for val in vwt:
        print(val)
    os.system("PAUSE")

    

