from datetime import datetime
from excelManager import excelManager


def hora():
    return datetime.now().strftime('%H:%M:%S')

def restar_horas(hora2, hora1):
    # Convertir las horas de cadena a objetos datetime
    formato_hora = '%H:%M:%S'
    tiempo1 = datetime.strptime(hora1, formato_hora)
    tiempo2 = datetime.strptime(hora2, formato_hora)

    # Restar las horas
    resultado = tiempo1 - tiempo2

    # Formatear el resultado como una cadena en formato HH:MM:SS
    resultado_formateado = str(resultado)

    # Devolver el resultado formateado
    return resultado_formateado



class userManager:
    def __init__(self):
        self.excel = excelManager("registrousuarios.xlsx")
        self.users=[]
        self.horas=[]

    def pickin(self, name):
        if name in self.users:
            return 
        else:
            self.users.append(name)
            index = self.users.index(name)
            self.excel.celdas(name,"A",index)
            time=hora()
            self.excel.celdas(time,"B",index)
            self.horas.append(time)

    
    def pickout(self,name):
        index = self.users.index(name)
        time =hora()
        self.excel.celdas(time,"C",index)
        total= restar_horas(self.horas[index],time)
        self.excel.celdas(total,"D",index)
        self.users[index]=0
    
    def save(self):
        self.excel.guardar()
    


    def check(self,name):
        if name  in self.users:
            return True
        else:
            return False

        

    def syso(self):
        print(self.users)


