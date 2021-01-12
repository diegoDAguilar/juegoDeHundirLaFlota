import numpy as np
from Constantes import *
from disparar import disparar


def maquina_apunta_dispara(ataca, defiende, d1):

    d2_acierta = True
    dn_acierta = True
    barco_vivo = True
    coord_dict = {'N': (0, -1),
                  'S': (0, 1),
                  'E': (1, 0),
                  'W': (-1, 0)}

    v_h_dict = {'V': ('N', 'S'), 'H': ('E', 'W')}
    v_h_elegido = None

    direcciones_posibles = list(coord_dict.keys())
    barco_localizado = False


    objetivos_pendientes = []
    direccion = direcciones_posibles.pop(np.random.randint(len(direcciones_posibles)))


    # Calcula las coordenadas adyacentes
    # ojo con los limites del tablero

    # Selecciona una direccion random entre N,S,E,W
    #print('direccion:', direccion)
    # Aqui se aniaden a objetivos_pendientes las coord a las que debe disparar
    # solo se aniaden si no hay un objetivo pendiente
    eligiendo = np.random.randint(1)
    while not barco_localizado:

        if not objetivos_pendientes:
            if eligiendo:
                [objetivos_pendientes.append((d1[0] + coord_dict[o][0], d1[1] + coord_dict[o][1])) for o in coord_dict.keys() if o in v_h_dict['V']]
                #print('Aniadido a pendientes V:', objetivos_pendientes)
                v_h_elegido = 'V'
            else:
                [objetivos_pendientes.append((d1[0] + coord_dict[o][0], d1[1] + coord_dict[o][1])) for o in coord_dict.keys() if o in v_h_dict['H']]
                #print('Aniadido a pendientes H:', objetivos_pendientes)
                v_h_elegido = 'H'
            # Comprueba que no se metiese ninguno que corresponda a fuera del tablero
            for o in objetivos_pendientes:
                if not (0 <= o[0] <= 9 and 0 <= o[1] <= 9):
                    objetivos_pendientes.remove(o)
            # para que escoja la otra direccion cuando no queden objetivos
            eligiendo = not eligiendo

        d2 = objetivos_pendientes.pop(np.random.randint(len(objetivos_pendientes)))
        # Se usa porque he cambiado el orden de columna fila a fila columna
        d2 = d2[::-1]
        #print('d2 es: ', d2)
        d2_acierta, _ = disparar(ataca, defiende, d2)
        # si acierta el segundo disparo Y NO ESTA MUERTO
        if d2_acierta:
            #print(f'Coordenada Vertical u Horizontal del barco localizada en {d2}.')
            barco_localizado = True
            #print('El barco esta en: ', v_h_elegido)
            dn = d2
            while barco_vivo:
                # mientras el barco siga a flote sigue insistiendo en esa direccion
                # Comprueba que la coordenada a disparar siga dentro del tablero
                if 0<=d2[0] + coord_dict[direccion][0]<=9 and 0<=d2[1] + coord_dict[direccion][1]<=9:
                    dn_acierta, _ = disparar(ataca, defiende, (d2[0] + coord_dict[direccion][0],
                                          d2[1] + coord_dict[direccion][1]))
                else:
                    # Con este codigo se prevee el error de salirse del tablero
                    dn_acierta, _ = disparar(ataca, defiende, (np.random.randint(TAM_TABLERO),
                                                               np.random.randint(TAM_TABLERO)))
                # si hunde el barco vacia la lista de disparos pendientes y termina
                if dn_acierta == D_VICTORIA:
                    return D_VICTORIA
                if dn_acierta != D_ACERTASTE:
                    # Si deja de acertar pero el barco sigue vivo es que esta en
                    # la otra direccion N <-> S, E <-> W, como ya se eliminaron
                    # las otras alternativas, solo queda una dir posible
                    #direccion = [o for o in v_h_dict[v_h_elegido] if o != direccion]
                    #objetivos_pendientes.append(dn + coord_dict[direccion])
                    #return (objetivos_pendientes, direccion)
                    #print('La maquina ha fallado')
                    return D_FALLASTE

        else:
            #print(f'Agua en la direccion {direccion}, en el punto {direccion} y {d2}.')
            return D_FALLASTE








