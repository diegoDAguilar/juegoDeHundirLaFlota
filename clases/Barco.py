class Barco:

    def __init__(self, coordenadas):


        #Diccionario de coordenadas
        self.coordenadas = dict(zip(coordenadas, [True for _ in coordenadas]))

    def estoy_vivo(self):
        for c in self.coordenadas.values():
            if c:
                return True
        else:
            return False

    def golpear_barco(self, coordenada_impacto):
        f = coordenada_impacto[0]
        c = coordenada_impacto[1]
        # Si tiene esa coordenada la marca a False
        if self.coordenadas.get((c, f)):
            self.coordenadas[c, f] = False

        #print('Barco golpeado')

    def get_coordenadas(self):
        return self.coordenadas.keys()
