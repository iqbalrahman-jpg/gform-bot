import random
import time
import data

# ===================================================================================================
# 5
kategori = [45, 0, 13]

index = 0
times = 58

soal = [10,7,2,6,3,3]

nim: list[int] = [
    232017086,
    232018083,
    232018152,
    232018221,
    232018226,
    232019004,
    232019078,
    232019106,
    232019110,
    232019173,
    232019205,
    232020006,
    232020020,
    232020025,
    232020031,
    232020032,
    232020050,
    232020065,
    232020090,
    232020091,
    232020105,
    232020136,
    232020142,
    232020147,
    232020164,
    232020165,
    232020173,
    232020179,
    232020184,
    232020191,
    232020193,
    232020200,
    232020205,
    232021003,
    232021005,
    232021008,
    232021012,
    232021014,
    232021018,
    232021021,
    232021031,
    232021044,
    232021046,
    232021056,
    232021060,
    232021067,
    232021073,
    232021085,
    232021088,
    232021090,
    232021097,
    232021104,
    232021111,
    232021135,
    232021139,
    232021143,
    232021147,
    232021151,
]

nama: list[str] = [
    "VANIA AURELLIA NOVERINAE",
    "FERDERIKA CETRIN DENGO",
    "INGGRIT CORIANTJI EKA PUTRI LUMAKEKI",
    "DIANA",
    "TESANIA VICTOR TAKIN ALLO",
    "ADEVITO",
    "FRANSISKA",
    "RESKY",
    "STEFANUS BUBURAYAI",
    "RICKY",
    "ADE",
    "KALFARINA",
    "EVELIN SORAYA",
    "VIOLETA LIKUMAHUA",
    "SAMUEL DELHA BINTANG JUNIAS",
    "BRYANT MARTIN ANDRE SILITONGA",
    "DENNIS ARMUNANTO",
    "MARIA MARCELLA AYU RETNO",
    "CHRISTIAN",
    "EDUARDUS DANANG SETYA ADI",
    "YESAYA BRIAN SYAHPUTRA",
    "SISKA CANDRA WIDYASARI",
    "ALVIN",
    "MAVERICK SHARON MAHULETTE",
    "DIAN",
    "JENDI MARALE",
    "JEYZIKA",
    "JERIKHO ABRIANTO PAPA",
    "DANIEL",
    "DANY",
    "RAFLY",
    "RATNA SARI SILITONGA",
    "HAPPY",
    "JOSHUA",
    "JONATHAN ARYO PRATAMA",
    "ESTEFANIA",
    "STEVANNI",
    "SELLA",
    "CHRISTOPHER",
    "AYUMI",
    "AGITIARA BERLIANA RANJANI",
    "LAURENSIUS JULIAN TRISNA NUGRAHA",
    "ANANG",
    "MARIO ELFANDI",
    "ANTONIO KENNY",
    "ERLENA",
    "MAULINA",
    "NATHANIEL LYAPUTERA",
    "CHRISTALIA",
    "DONNA OCTAVIANITA",
    "NUKE",
    "JENNY",
    "SILVY",
    "EVANGEL",
    "MARIA",
    "GRACIELLA",
    "ALVINA",
    "JENNY OCTAVIA CHRISTI H. OJAI",
]

kelamin: list[int] = [
    1,0,1,1,1,0,1,0,0,0,1,1,1,1,0,0,0,1,0,0,0,1,0,0,1,1,1,0,0,0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,0,1,1,0,1,1,1,1,1,1,1,1,1,1,
]
