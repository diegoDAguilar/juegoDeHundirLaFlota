class Barco:

    def __init__(self, coordenadas):


        #Diccionario de coordenadas
        self.coordenadas = dict(zip([x for x in coordenadas], [True for x in coordenadas]))

    def estoy_vivo(self):
        for c in self.coordenadas.values():
            if c:
                #print('Estoy vivo')
                return True

        else:
            #print('Barco hundido')
            return False

    def golpear_barco(self, impacto):
        c = impacto[0]
        f = impacto[1]
        # Si tiene esa coordenada la marca a False
        if self.coordenadas.get((c, f)):
            self.coordenadas[c, f] = False

        #print('Barco golpeado')

    def get_coordenadas(self):
        return self.coordenadas.keys()
