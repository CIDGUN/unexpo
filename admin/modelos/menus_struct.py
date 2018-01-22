# -*- coding: utf-8 -*-
try:
 from ztec.zdb import DB
except:
 from zdb import DB
db=DB()
db.load=True
db('Menus').campo('Nombre',db.str,False,True,False,False,0,-1,None,None)
db('Menus').campo('Contenido',db.list,False,True,False,False,0,-1,None,None)
db('Menus').campo('args',db.dict,False,True,False,False,0,-1,None,None)
db('Menus').campo('Fecha',db.str,False,True,False,False,0,-1,None,'%d/%m/%Y %H:%M:%S')
db('Menus').campo('Status',db.list,False,True,False,False,0,-1,None,None)
db('Menus-categoria').campo('Nombre',db.str,False,True,False,False,0,-1,None,None)
db('Menus-categoria').campo('Contenido',db.list,False,True,False,False,0,-1,None,None)
db('Menus-categoria').campo('Fecha',db.str,False,True,False,False,0,-1,None,'%d/%m/%Y %H:%M:%S')
db('Menus-categoria').insertar('Menu principal', [], '12/7/2017 10:27:11')
#el metodo es el name del 
#el indicie no importa tanto ya que los nombres de las pagina y entradas deben ser unicos
db('Menus').insertar('Menu principal', [[{'url': 'index',"value":["modelo","tabla",0],'name': 'index', 
  'children': [{'url': 'entrada', 'name': 'Entrada', 'children': [],"value":["modelo","tabla",0]}, 
    {'url': ["modelo","tabla","controlador","metodo"], 'name': 'Categoria', 'children': []}
    ]}, 
  {'url': 'Categoria', 'name': 'Categoria', 'children': [],"value":["modelo","tabla",0]}, 
  {'url': 'entrada', 'name': 'Entrada', 'children': [],"value":["modelo","tabla",0]}
  ],
  {"nivel-superior":False,"menu-principal":True,"menu-pie":False,"menu-barra-superior":False,"menu-mi-cuenta":False,},
  ], 
  {'Menu': 0}, 
  '12/7/2017 10:27:11', 
  ['Publicado'])

db.load=False

