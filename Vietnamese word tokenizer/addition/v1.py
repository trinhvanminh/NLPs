import time
import re

#redesign file VDic_uni.txt

# with open('VDic_uni.txt','r', encoding='utf-8') as f:
#     with open('VDic_v2.txt', 'w', encoding='utf-8') as f2:
#         for line in f:
#             f2.write(line.split('\t')[0] + '\n')
    

#get dictionary to quick search

# def getDict(ifile):
#     Dict = {}
#     #utf-8-sig   --> ignore the first character - the character mark as unicode file in notepad (u'\ufeff')
#     with open(ifile, 'r', encoding='utf-8-sig') as f:
#         for index, line in enumerate(f):
#             if Dict.get(line[0]):
#                 continue
#             else:
#                 Dict[line[0]] = index
#     return Dict




#support material: https://regex101.com/r/uEyTN8/12  and  https://regexr.com/desktop
        
s = "Text... Text. Text! Text? PGS.TS. Nguyen Van A. Text."
def sentence_tokenizer(str):
    # split = re.split('(?<=[.?!])\s+', str)
    split = re.split(r'(?<=(?:(?<!ThS(?=\.))(?<!TS(?=\.))(?<!PGS(?=\.))(?<!GS(?=\.))(?<!BS(?=\.)))[.?!])\s+', str)
    return split



# splits = sentence_tokenizer(s)


# for sen in splits:
#     vi_word = []

#     words = sen.split()
#     first_char = words[0]

#     #Dict #!!!!! first_char is UPPERCASE character ????
#     start_line = Dict[first_char]

#     #start to get data = readline(start_line --> to ?end) with VDic_v2.txt
    

    




