import openpyxl
class excelManager:
    def __init__(self, name):
        self.wb= openpyxl.Workbook()
        self.sheet=self.wb.active
        self.name = name

    def celdas(self,val,col,num):
        self.sheet = self.wb.active
        self.sheet[f"{col}{num+1}"]=val

    def obtener_atributo2(self):
        return self.atributo2

    def guardar(self):
        self.wb.save('registro.xlsx')