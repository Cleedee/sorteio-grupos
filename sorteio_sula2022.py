from base import Time
import base

pote1 = [
]

pote2 = [
]

pote3 = [
]

pote4 = [
]

classificados = [
    Time('Santos', 'santos.png', 'BRA', ranking=8),
    Time('Independiente', 'indepc.png', 'ARG', ranking=10),
    Time('São Paulo', 'saopaulo.png', 'BRA', ranking=13),
    Time('Internacional', 'interrs.png', 'BRA', ranking=17),
    Time('Racing', 'racingc.png', 'ARG', ranking=19),
    Time('Lanús', 'lanusc.png', 'ARG', ranking=24),
    Time('Defensa y Justicia', 'defensayjusticia.png', 'ARG', ranking=36),
    Time('Atlético-GO', 'atlego.png', 'BRA', ranking=100),
    Time('Ceará', 'ceara.png', 'BRA', ranking=107),
    Time('Banfield', 'banfield.png', 'ARG', ranking=113),
    Time('Unión', 'union_santa_fe.png', 'ARG', ranking=142),
    Time('Cuiabá', 'cuiaba_mt.png', 'BRA', ranking=253),
]

desclassificados = [
    Time('Sol de América', 'soldeamerica_par.png', 'PAR', True, ranking=110),
    Time('Estudiantes de Mérida', '', 'VEN', True, ranking=88),
    Time('Royal Pari', 'royal_pari_bol.png', 'BOL', True, ranking=150),
    Time('Cienciano', 'cienciano.png', 'PER', True, ranking=119),
    Time('Ñublense', 'nublense_chi.png', 'CHI', True),
    Time('Liverpool', '', 'URU', True, ranking=157),
    Time('Mushuc Runa', 'musgucruna_ecu.jpg', 'EQU', True, ranking=233),
    Time('Sport Boys', 'sportboys.png', 'PER', True, ranking=138),
]

preclassificados = [
    Time('Jorge Wilstermann', 'wlstermann.png', 'BOL', True, ranking=39),
    Time('Guabirá', 'guabira_bol.png', 'BOL', True, ranking=140),
    Time('Oriente Petrolero', 'oriente.png', 'BOL', ranking=84),
    Time('Unión Española', 'unionesp.gif', 'CHI', True, ranking=68),
    Time('Deportes Antofagasta', 'antofagasta.png', 'CHI', True, ranking=197),
    Time('Unión La Calera', 'union_la_calera_chi.png', 'CHI', ranking=91),
    Time('La Equidad', 'laequidad_col.png', 'COL', True, ranking=79),
    Time('Independiente Medellín', 'indep_medellin.png', 'COL', True, ranking=55),
    Time('América de Cali', 'am_cali.png', 'COL', True, ranking=37),
    Time('Delfín', 'delfin_eq.jpg', 'EQU', True, ranking=70),
    Time('9 de Octubre', '9oct_ecu.png', 'EQU', True, ranking=191),
    Time('Nacional', 'nacional_par.png', 'PAR', True, ranking=6),
    Time('Guaireña', 'guairena_par.png', 'PAR', True, ranking=223),
    Time('General Caballero', 'general_jlm_par.png', 'PAR', ranking=999),   
    Time('Ayacucho', 'intideayacucho.png', 'PER', ranking=190),   
    Time('Melgar', 'melgar.png', 'PER', ranking=66),
    Time('Montevideo Wanderers', '', 'URU', True, ranking=73),
    Time('Cerro Largo', '', 'URU', True, ranking=153),
    Time('River Plate', 'river_uru.png', 'URU', ranking=95),
    Time('Metropolitanos', '', 'VEN', ranking=131), 
    Time('Hermanos Colmenare', '', 'VEN', True, ranking=999), 
    Time('Deportivo La Guaira', '', 'VEN', True, ranking=89),
    Time('LDU', 'ldu.png', 'EQU', ranking=20),
    Time('Junior Barranquilla', 'junior.png', 'COL', ranking=25)      
]

def traga_potes():
    classificaveis = preclassificados.copy()
    fase_de_grupo = classificados + preclassificados[0:16]
    fase_de_grupo.sort(key=base.pegar_ranking)
    perdedores = [
        base.Time("Perdedor do G1", "preliberta.jpg", "XXX", ranking=999),
        base.Time("Everton", "everton_ch.gif", "CHI"),
        base.Time("Perdedor do G3", "preliberta.jpg", "XXX", ranking=999),
        base.Time("Barcelona SC", "barcelonaeq.png", "EQU")
    ]
    pote1 = fase_de_grupo[0:8]
    pote2 = fase_de_grupo[8:16]
    pote3 = fase_de_grupo[16:24]
    pote4 = perdedores + fase_de_grupo[24:]    
    return (pote1, pote2, pote3, pote4)