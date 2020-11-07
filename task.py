# -*- coding: UTF-8 -*-
import xlrd
import re
# data_save_words_path =  "E:\\code\\save_words.txt"#所有汉字
# data_out = xlrd.open_workbook('E:\\code\\1.xls')
# # print(data_out.sheet_names())
# raw_word=[]
# table = data_out.sheet_by_name(data_out.sheet_names()[1])
# rowNum = table.nrows
# for i in range(0,rowNum):
#     temp = table.cell(i,1).value
#     # print(temp)
#     # print(len(temp))
#     for j in range(0,len(temp)):
#         if temp[j] not in raw_word:
#             raw_word.append(temp[j])
# print(raw_word)
# with open(data_save_words_path,'w+') as f:
#     f.write(str(raw_word).replace(' ','').replace('[','').replace(']','').replace("'",'').replace(',',''))
#     f.close()


print('烟台'.encode(encoding="utf-8"))
str2 = '烟台'.encode(encoding="utf-8")
print(str2.decode("utf-8"))


# print(type(str2))
# str1 = '\xe7\x83\x9f\xe5\x8f\xb0'
# print(str1.encode('utf-8'))
#  字库格式  :00400880110023FFCC000000020042004202420143FE42004200420002000000;"行",0
data_input_path = 'E:\\code\\fonts.TXT'
out_put_path ='E:\\code\\fonts\\low\\'
with open(data_input_path,'r') as input_f:
    while True:
        content = input_f.readline()
        if not content:
            break
        result = re.search(":(.*?);",content)
        if result is not None:
            ture_result = result.group(0).replace(":","").replace(";","")
            # print(result.group(0).replace(":","").replace(";",""))
            print(ture_result)
            chinese_word = re.search("\"(.*?)\"",content).group(0).replace(";","")
            print(chinese_word)
            # out_file_name = out_put_path + str(chinese_word.encode(encoding="utf-8")).replace('\\x','').replace('b\\','').replace('"','').replace('\'','').lstrip('b').upper()+'.txt'
            out_file_name = out_put_path + str(chinese_word.encode(encoding="utf-8")).replace('\\x','').replace('b\\','').replace('"','').replace('\'','').lstrip('b')+'.txt'
            print(out_file_name)
            with open(out_file_name,"w") as output_f:
                output_f.write(ture_result)
                output_f.close
    input_f.close()

