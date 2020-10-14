import numpy as np


d1_acierta = True
dn_acierta = True
barco_vivo = True
d1 = np.array((3, 5))
coord_dict = {'N': np.array((0, -1)),
              'S': np.array((0, 1)),
              'E': np.array((1, 0)),
              'W': np.array((-1, 0))}

v_h_dict = {'V': ('N', 'S'), 'H': ('E', 'W')}
v_h_elegido = None
direcciones_posibles = list(coord_dict.keys())
direccion = None
barco_localizado = False
objetivos_pendientes = []

if d1_acierta:
    # Calcula las coordenadas adyacentes
    # ojo con los limites del tablero

    # Selecciona una direccion random entre N,S,E,W
    direccion = direcciones_posibles.pop(np.random.randint(len(direcciones_posibles)))
    while not barco_localizado:

        # Aqui se aniaden a objetivos_pendientes las coord a las que debe disparar
        # en funcion de si elige disparar Vertical o Horizontal
        # solo se aniaden si no hay un objetivo pendiente
        if not objetivos_pendientes:
            # v_h_dict contiene V con N,S y H con E,W
            if direccion in v_h_dict['V']:
                [objetivos_pendientes.append(d1 + coord_dict[o]) for o in coord_dict.keys() if o in v_h_dict['V']]
                v_h_elegido = 'V'
            else:
                [objetivos_pendientes.append(d1 + coord_dict[o]) for o in coord_dict.keys() if o in v_h_dict['H']]
                v_h_elegido = 'H'

        dn = objetivos_pendientes.pop(np.random.randint(len(objetivos_pendientes)))
        print(dn)
        #dn_acierta = diparar(dn)
        # si acierta el segundo disparo
        if dn_acierta:
            print(f'Coordenada Vertica u Horizontal del barco localizada en {dn}.')
            # Si elige V, elimina H y viceversa
            [direcciones_posibles.remove(i) for i in direcciones_posibles.copy() if i not in v_h_dict[v_h_elegido]]
            print('Disparando a esas coordenadas.')
            break
        else:
            print(f'Agua en la direccion {direccion}.')
            pass

    while barco_vivo:
        while dn_acierta:
            objetivos_pendientes.append(dn+coord_dict[direccion])
            dn = objetivos_pendientes.pop(np.random.randint(len(objetivos_pendientes)))
            #dn_acierta = disparar(dn)
            # si hunde el barco vacia la lista de disparos pendientes y termina
            if dn_acierta == 'barco_hundido':
                barco_vivo = False
                objetivos_pendientes.clear()
                break
        # Si deja de acertar pero el barco sigue vivo es que esta en
        # la otra direccion N <-> S, E <-> W, como ya se eliminaron
        # las otras alternativas, solo queda una dir posible
        direccion = direcciones_posibles.pop()





