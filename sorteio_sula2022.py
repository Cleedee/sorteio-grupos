from base import Time

pote1 = [
    Time('Santos', 'santos.png', 'BRA', ranking=8),
    Time('São Paulo', 'saopaulo.png', 'BRA', ranking=13),
    Time('Internacional', 'interrs.png', 'BRA', ranking=17),
    Time('Independiente', 'indepc.png', 'ARG', ranking=10),
    Time('Racing', 'racingc.png', 'ARG', ranking=19),
    Time('Lanús', 'lanusc.png', 'ARG', ranking=24),
    Time('LDU', 'ldu.png', 'EQU'),  # se si classificar
    Time('Junior Barranquilla', 'junior.png', 'COL')  # se si classificar
]

pote2 = [
    Time('Defensa y Justicia', 'defensayjusticia.png', 'ARG', ranking=36)
]

pote3 = [
    Time('Atlético-GO', 'atlego.png', 'BRA', ranking=100),
    Time('Ceará', 'ceara.png', 'BRA', ranking=107),
    Time('Banfield', 'banfield.png', 'ARG', ranking=113),
    Time('Unión', 'union_santa_fe.png', 'ARG', ranking=142),
]

pote4 = [
    Time('Cuiabá', 'cuiaba_mt.png', 'BRA', ranking=253),
]

desclassificados = []

preclassificados = [
    Time('Jorge Wilstermann', '', 'BOL', True, ranking=39),
    Time('Guabirá', '', 'BOL', True, ranking=140),
    Time('Royal Pari', '', 'BOL', True, ranking=150),
    Time('Oriente Petrolero', '', 'BOL', True, ranking=84),
    Time('Unión Española', '', 'CHI', True, ranking=68),
    Time('Deportes Antofagasta', '', 'CHI', True, ranking=197),
    Time('Ñublense', '', 'CHI', True),
    Time('Unión La Calera', '', 'CHI', True, ranking=91),
]
