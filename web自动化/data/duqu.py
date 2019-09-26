import xlrd
class duqu():
    def du(self):
        d=[]
        f = xlrd.open_workbook(r'e:\demo\web自动化\data\web自动化.xlsx')
        sheet = f.sheets()[0]
        a = sheet.nrows
        for i in range(a):
            b = sheet.row_values(i)
            d.append(b)
        return d
