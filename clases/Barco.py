import logging


class Barco:

    def __init__(self, coordenadas):


        #Diccionario de coordenadas
        self.coordenadas = dict(zip(map(tuple, coordenadas), [True for _ in coordenadas]))
        logging.basicConfig(level=logging.INFO)
        #logging.info('Objeto Barco creado')

    def estoy_vivo(self):
        for c in self.coordenadas.values():
            if c:
                return True
        else:
            return False

    def golpear_barco(self, coordenada_impacto):
        # Si tiene esa coordenada la marca a False
        if self.coordenadas.get(coordenada_impacto):
            self.coordenadas[coordenada_impacto] = False

        #print('Barco golpeado')

    def get_coordenadas(self):
        return self.coordenadas.keys()
