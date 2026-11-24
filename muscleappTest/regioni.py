"""
regioni.py  -  LE FORME DEL CORPO (coordinate dei poligoni sul Canvas)

Il Canvas e' una "tela" di LARGHEZZA x ALTEZZA pixel. (0,0) e' in alto a sinistra,
x cresce verso destra, y cresce verso il basso.

Ogni muscolo e' un poligono = lista di punti (x, y).
La chiave del dizionario (es. "pettorali") deve essere IDENTICA all'"id"
scritto in data/muscoli.json: e' il "ponte" tra grafica e dati.

QUANDO AVRETE UN'ILLUSTRAZIONE VERA: usate tools/trova_coordinate.py per
leggere le coordinate dei punti e sostituite i poligoni qui sotto.
"""

LARGHEZZA = 360
ALTEZZA = 620
CENTRO = LARGHEZZA // 2  # 180: asse di simmetria del corpo


def specchia(punti):
    """Restituisce lo stesso poligono riflesso rispetto all'asse centrale.
    Cosi' disegniamo solo meta' corpo e l'altra meta' viene gratis."""
    return [(2 * CENTRO - x, y) for (x, y) in punti]


def coppia(punti):
    """Un muscolo sinistro + il suo gemello destro."""
    return [punti, specchia(punti)]


# Parti decorative (non cliccabili): testa, collo, tronco, braccia, gambe
SILHOUETTE = [
    ("ovale", (150, 20, 210, 90)),
    ("poligono", [(168, 88), (192, 88), (196, 112), (164, 112)]),
    ("poligono", [(140, 110), (220, 110), (214, 200), (210, 310), (150, 310), (146, 200)]),
    ("poligono", [(94, 112), (144, 108), (128, 252), (112, 345), (80, 345), (92, 252)]),
    ("poligono", specchia([(94, 112), (144, 108), (128, 252), (112, 345), (80, 345), (92, 252)])),
    ("poligono", [(144, 306), (180, 306), (176, 470), (166, 600), (142, 600), (140, 470)]),
    ("poligono", specchia([(144, 306), (180, 306), (176, 470), (166, 600), (142, 600), (140, 470)])),
]

_SPALLE = [(142, 114), (116, 120), (98, 144), (102, 174), (126, 168), (136, 135)]
_BRACCIO_ALTO = [(96, 180), (122, 172), (122, 240), (100, 246)]
_AVAMBRACCIO = [(96, 252), (120, 246), (112, 335), (88, 340)]

REGIONI = {
    "fronte": {
        "spalle": coppia(_SPALLE),
        "pettorali": coppia([(144, 120), (179, 126), (179, 186), (146, 190), (128, 170), (136, 135)]),
        "bicipiti": coppia(_BRACCIO_ALTO),
        "avambracci": coppia(_AVAMBRACCIO),
        "addominali": coppia([(152, 194), (179, 194), (179, 305), (160, 305), (152, 250)]),
        "quadricipiti": coppia([(146, 312), (179, 312), (179, 452), (158, 456), (144, 400)]),
    },
    "retro": {
        "trapezio": coppia([(179, 110), (158, 114), (138, 126), (160, 160), (179, 205)]),
        "spalle": coppia(_SPALLE),
        "dorsali": coppia([(142, 172), (166, 176), (179, 212), (179, 290), (158, 286), (142, 228)]),
        "tricipiti": coppia(_BRACCIO_ALTO),
        "avambracci": coppia(_AVAMBRACCIO),
        "glutei": coppia([(148, 306), (179, 306), (179, 380), (150, 384), (144, 345)]),
        "femorali": coppia([(146, 388), (179, 388), (179, 470), (160, 474), (144, 440)]),
        "polpacci": coppia([(146, 486), (176, 486), (172, 555), (160, 560), (148, 545)]),
    },
}
