db=DB()
#============================================
#TABLA de opciones
db("Opciones").campo("Nombre",db.str)
db("Opciones").campo("Valores",db.list)
db("Opciones").insertar("Becas",["Empresarial","Política","Preparaduria","Trabajo"])
#=============================================
db("Plantillas").campo("Nombre",db.str)
db("Plantillas").campo("Contenido",db.list)
db("Plantillas").campo("args",db.dict)
db("Plantillas").campo("Fecha",db.str)
db("Plantillas").campo("Status",db.list)
#============================================
db("Galerias").campo("Nombre",db.str)
db("Galerias").campo("Contenido",db.list)
db("Galerias").campo("args",db.dict)
db("Galerias").campo("Fecha",db.str)
db("Galerias").campo("Status",db.list)
#--------------------------------------------
db("Plantillas").insertar("Galerias",[
	[{"Nombre":"titulo","name":"titulo","value":""}],
	[
	{"Imagen 1":"img-admin","value":0,"opcion":0,"opciones":"archivos","name":"imagen"},
	]
	],
	{"Plantilla":0},
	zu.DateTime(),
	[]
	)
#--------------------------------------------
db("Plantillas").insertar("",[
	#Requisitos
	[{"Nombre":"titulo","name":"titulo","value":""},
	 {"Requisitos":"list","name":"requisitos","value":["Constancia de inscripción","Constancia de estudio","Record Académico","Cuenta Bancaria"]},
	 {"Pago":"number","name":"pago","value":250000},
	],
	],
	{"Beca":0},
	zu.DateTime(),
	[])
#--------------------------------------------
db("Galerias").insertar("APARTMENT AMENITIES",[
	[{"Nombre":"titulo","name":"titulo","value":"APARTMENT AMENITIES"}],
	[
	{"Imagen 1":"img-admin","value":0,"opcion":0,"opciones":"archivos","name":"imagen"},
	{"Imagen 2":"img-admin","value":0,"opcion":0,"opciones":"archivos","name":"imagen"},
	{"Imagen 3":"img-admin","value":0,"opcion":0,"opciones":"archivos","name":"imagen"},
	{"Imagen 4":"img-admin","value":0,"opcion":0,"opciones":"archivos","name":"imagen"},
	{"Imagen 5":"img-admin","value":0,"opcion":0,"opciones":"archivos","name":"imagen"},
	{"Imagen 6":"img-admin","value":0,"opcion":0,"opciones":"archivos","name":"imagen"},
	],
	],
	{"Galeria":0},
	zu.DateTime(),
	[]
	)
db("Becas").campo("Nombre",db.str)
db("Becas").campo("Contenido",db.list)
db("Becas").campo("args",db.dict)
db("Becas").campo("Fecha",db.str)
db("Becas").campo("Status",db.list)
db("Becas").insertar("Empresarial",[
	#Requisitos
	[{"Nombre":"titulo","name":"titulo","value":"Empresarial"},
	 {"Requisitos":"list","name":"requisitos","value":["Constancia de inscripción","Constancia de estudio","Record Académico","Cuenta Bancaria"]},
	 {"Pago":"number","name":"pago","value":250000},
	],
	],
	{"Beca":0},
	zu.DateTime(),
	[])
