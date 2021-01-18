def Maquina_Turing(estado=None,  # estados de la maquina de turing
                   blanco=None,  # simbolo blanco de el alfabeto de la cinta
                   reglas=[],  # reglas de transicion
                   cinta=[],
                   final=None,  # estado valido y/o final
                   posicion=0):  # posicion siguiente de la maquina

    st = estado
    # seguridad prevenir errores
    if not cinta: cinta = [blanco]
    if posicion < 0: posicion += len(cinta)
    if posicion >= len(cinta) or posicion < 0: raise Error("Error se ha inicializo mal la posicion")

    reglas = dict(((s0, v0), (v1, dr, s1)) for (s0, v0, v1, dr, s1) in reglas)
    """
Estado	 Símbolo leído	  Símbolo escrito	    Mov. 	  Estado sig.
p(s0)	      1(v0)	          x(v1)            R(dr)	     p(s1)
"""
    while True:
        print(st, '\t', end=" ")
        for i, v in enumerate(cinta):
            if i == posicion:
                print("[%s]" % (v,), end=" ")
            else:
                print(v, end=" ")
        print()

        if st == final: break
        if (st, cinta[posicion]) not in reglas: break

        (v1, dr, s1) = reglas[(st, cinta[posicion])]
        cinta[posicion] = v1  # rescribe el simbolo de la cinta

        # movimeinto del cabezal
        if dr == 'left':
            if posicion > 0:
                posicion -= 1
            else:
                cinta.insert(0, blanco)
        if dr == 'right':
            posicion += 1
            if posicion >= len(cinta): cinta.append(blanco)
        st = s1


print("Maquina de turin que calcula el número consecutivo de un número dado en binario.")
Maquina_Turing(estado='q0',  # estado inicial de la maquina de turing
               blanco='b',  # simbolo blanco de el alfabeto dela cinta
               cinta=list("111"),  # inserta los elementos en la cinta
               final='q2',  # estado valido y/o final
               reglas=map(tuple,  # reglas de transicion
                          [
                              "q0 b b right q0".split(),
                              "q0 1 1 right q0".split(),
                              "q0 b b left q1".split(),
                              "q1 1 b left q1".split(),
                              "q1 b 1 right q2".split(),
                              "q1 b 1 left q2".split(),
                              "q1 b 1 right q2".split(),
                          ]
                          )
               )
print("Integrantes: "
      "\n-Henry Froylan Chuc Tec"
      "\n-Gelmon Hernandez Martinez")