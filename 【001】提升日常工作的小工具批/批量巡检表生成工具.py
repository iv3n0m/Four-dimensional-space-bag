import xlwings as wx

'''
date:2019-10-1
author:DASHU

'''


name = 'XXXXXXXXX巡检表'

#app = wx.App(visible=True,add_book=False)

wb = wx.Book(name + '(2018.12.17-2018.12.21).xlsx')
print (wb.name, wb.fullname)
print (wb.app)
print (wb.sheets)
wb.activate()

sht = wb.sheets[0]
print (sht)

date = []
with open("1.txt",'r') as f:
    for i in f.readlines():
        i = i.strip('\n')
        sht.range('D2').value = ('巡检日期:' + i)
        wb.save(name + '('+ i + ')' + '.xlsx')



wb.close()
