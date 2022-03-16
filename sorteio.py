import random

from base import Time, LETRAS_8_GRUPOS, sorteio_pote





pote1 = [
    Time("Palmeiras", "palmeiras.png", "BRA"),
    Time("River Plate", "riverc.png", "ARG"),
    Time("Boca Jrs", "bocc.png", "ARG"),
    Time("Flamengo", "fla.png", "BRA"),
    Time("Nacional", "naciouru.png", "URU"),
    Time("Peñarol", "penarol.png", "URU"),
    Time("Athlético", "atlpr.png", "BRA"),
    Time("Atlético-MG", "atletico.png", "BRA")
]

pote2 = [
    Time("Cerro Porteño", "cerropor.png", "PAR"),
    Time("Libertad", "libertad.png", "PAR"),
    Time("Ind. Del Valle", "indep_j_teran.jpg", "EQU"),
    Time("Univ. Católica", "unicatolica.png", "CHI"),
    Time("Emelec", "emelec.png", "EQU"),
    Time("Corinthians", "corinthians.png", "BRA"),
    Time("Colo-Colo", "colocolo.png", "CHI"),
    Time("Velez Sarsfield", "velez.png", "ARG")
]

pote3 = [
    Time("Sporting Cristal", "cristal.jpg", "PER"),
    Time("RB Bragantino", "bragantino.png", "BRA"),
    Time("Tachira", "tachira.png", "VEN"),
    Time("Alianza Lima", "alianza.jpg", "PER"),
    Time("Tolima", "dtolima_col.png", "COL"),
    Time("Colon", "colon.png", "ARG"),
    Time("Caracas", "caracas.png", "VEN"),
    Time("Dep. Cali", "dep_cali.png", "COL")
]

pote4 = [
    Time("Always Ready", "always_ready_bol.png", "BOL"),
    Time("Talleres", "talleres.png", "ARG"),
    Time("Ind. Petrolero", "indeppetrobol.png", "BOL"),
    Time("Fortaleza", "fortaleza.png", "BRA")
]

grupo1 = [
    # Time("Millonarios", "millo.png", "COL", True),
    # desclassificado pelo Fluminense
    Time("Fluminense", "fluminense.png", "BRA", True),
    # Time("Atlético Nacional", "medelin.png", "COL", True),
    # desclassificado pelo Olimpia
    # Time("Universidade César Vallejo", "cesarvallejo.png", "PER", True),
    # desclassificado pelo Olimpia
    Time("Olímpia", "olimpia.png", "PAR", True)
]

grupo2 = [
    # Time("Audax Italiano", "audax.gif", "CHI", True),
    # desclassificado pelo Estudiantes
    Time("Estudiantes", "estudic.png", "ARG", True),
    Time("Everton", "everton_ch.gif", "CHI", True),
    # Time("Monagas", "monagas_ven.png", "VEN", True)
    # desclassificado pelo Everton
]

grupo3 = [
    # Time("Deportivo Lara", "dep_lara_ven.gif", "VEN", True),
    # desclassificado pelo Bolivar
    # Time("Bolivar", "bolivar.png", "BOL", True),
    # desclassificado pelo Universid Católica
    Time("Universid Católica", "un_catolica_ecu.png", "EQU", True),
    # Time("Plaza Colonia", "plazacolonia.png", "URU", True),
    # desclassificado pelo The Strongest
    Time("The Strongest", "strongest.png", "BOL", True)
]

grupo4 = [
    Time("América Mineiro", "ammg.gif", "BRA", True),
    # Time("Guarani", "guarani_par.png", "URU", True),
    # desclassificado pelo América
    # Time("City Torque", "torque_uru.png", "URU", True), Perdeu para o Barcelona nos pênaltis
    # Time("Universitário", "universitaria_peru.png", "PER", True),
    # desclassificado pelo Barcelona
    # Time("Barcelona SC", "barcelonaeq.png", "EQU", True)
]


