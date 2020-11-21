import re
import os.path





def ValidPhoneNumber(phone_numbers):
     valid_pn = []
     if not os.path.isfile('VNphone_numbers_format.txt'):
          print('File not exist')
     else:
          with open('VNphone_numbers_format.txt','r') as f:
               VNphone_numbers = f.read()
          for pn in phone_numbers:
               if pn[0] == '0' and (pn[1:3] in VNphone_numbers):
                    valid_pn.append(pn)
               elif pn[0] == '+' and (pn[3:5] in VNphone_numbers):
                    valid_pn.append(pn)
     return valid_pn
                    
                    

def extract_data(text):
     emails = re.findall('[\w\.-]+@[\w\.-]+\.\w{2,5}', text)
     phone_numbers = re.findall('(?:\+84|0)[3|8|9]\d{8}',text)
     #doan code tren se lay ve link rut gon vd: http://docs.python.org/3/library/re.html   --->  return: http://docs.python.org
     # urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', text)
     urls = re.findall('https?://[^\s]+', text)
     # e = re.findall('https?://\S+', text)
     return emails, phone_numbers, urls
    
 
def main():
     ifile = input('Input file *.txt: ')
     if not os.path.isfile(ifile):
          print('File not exist')
     else:
          emails,phone_numbers,urls = [],[],[]
          with open(ifile,'r') as f:
               text = f.read()
          emails, phone_numbers, urls = extract_data(text)
          if not emails and not phone_numbers and not urls:
               print('There is no email, link or phone number here')
          else:
               # print(emails, phone_numbers,urls,text)
               phone_numbers = ValidPhoneNumber(phone_numbers)
               list_tuple = list()
               for e in emails:
                    tp = list()
                    tp += text.find(e), len(e), 'email'
                    list_tuple.append(tuple(tp))
               for pn in phone_numbers:
                    tp = list()
                    tp += text.find(pn), len(pn), 'phone number'
                    list_tuple.append(tuple(tp))
               for url in urls:
                    tp = list()
                    tp += text.find(url), len(url), 'website'
                    list_tuple.append(tuple(tp))

               for i in list_tuple:
                    print(i)


if __name__ == "__main__":
     main()