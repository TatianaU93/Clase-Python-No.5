from  indicadores import  Indicadores

class Nomina(Indicadores):

    def __init__(self):
        self.__salarioBasico = 0
        self.__diasLiquidados = 0
        self.__auxulio_Transporte = 106454
        self.__smlv = self.salariominimo()

    def setSalario(self, salarioBasico):
        if str(type(salarioBasico)) == "<class 'float'>" or str(type(salarioBasico)) == "<class 'int'>":
            if self.__smlv <= salarioBasico:
                self.__salarioBasico = salarioBasico
            else:
                print ("El salario basico no puede ser inferior al SLMV vigente")    
        else:
            print ("Error")

    def getSalario(self):
        return self.__salarioBasico

    def setDiasLiquidados(self, diasLiquidados:int):
        self.__diasLiquidados = diasLiquidados

    def getDiasLiquidados(self):
        return self.__diasLiquidados

    def salarioDevengado(self):
        try:
            return (self.__salarioBasico/30) * self.__diasLiquidados
        except:
            print("Error en alguna de las variables")

    def auxilioTransporte(self):
        if self.__salarioBasico > (self.__smlv * 2):
            return 0
        else:
            return (self.__auxulio_Transporte/30 * self.__diasLiquidados)

    def totalDevengado(self):
        return self.salarioDevengado() + self.auxilioTransporte()

    def __str__(self):
        return str("Salario Basico: {} \n"
                    "Dias liquidados: {} \n"
                    "Salario devengado: {} \n"
                    "Auxilio de transporte: {} \n"
                    "Total Devengado: {} \n").format(
                        self.__salarioBasico,
                        self.__diasLiquidados,
                        self.salarioDevengado(),
                        self.auxilioTransporte(),
                        self.totalDevengado())
