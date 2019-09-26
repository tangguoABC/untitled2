import xlrd


class Duqu():
   def dqexcel(self):
      a = []
      f = xlrd.open_workbook(r'D:\Users\Administrator\PycharmProjects\untitled2\com.qk.butterfly\data\ds_data.xls')
      sheet = f.sheets()[0]
      content = sheet.nrows
      for i in range(content):
         b = sheet.row_values(i)
         a.append(b)
      print(a)
      return a

d=Duqu()
d.dqexcel()