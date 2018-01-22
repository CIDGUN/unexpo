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
db('Menus').insertar('Menu principal', [[{'url': 'entrada', 'name': 'mi nueva nueva', 'children': []}, {'url': 'http://localhost/PTC/unexpo/admin/index', 'name': 'index', 'children': [{'url': 'http://localhost/PTC/unexpo/Inicio/Administrativos', 'name': 'Administrativos', 'children': []}, {'url': 'index', 'name': 'index', 'children': [{'url': 'index', 'name': 'index', 'children': []}, {'url': 'index', 'name': 'index', 'children': []}, {'url': ['paginas', '', 1, 'Inicio', 'Administrativos'], 'name': 'Administrativos', 'children': []}]}]}, {'url': 'http://localhost/PTC/unexpo/Inicio/Administrativos/carreras', 'name': 'Administrativos/carreras', 'children': []}, {'url': 'Categoria', 'name': 'Categoria', 'children': [{'url': 'entrada', 'name': 'Entrada', 'children': []}]}, {'url': 'Categoria', 'name': 'Categoria', 'children': []}], {'menu-barra-superior': False, 'nivel-superior': False, 'menu-pie': False, 'menu-principal': True, 'menu-mi-cuenta': True}], {'Menu': 0}, '19/11/2017 18:58:41', [{'name': 'control', 'value': ''}, {'name': 'modelo', 'value': 'paginas'}, {'name': 'indice', 'value': 0}])
db('Menus').insertar('mi nuevo', [[{'url': 'http://localhost/PTC/unexpo//index', 'name': 'index', 'children': []}, {'url': 'http://localhost/PTC/unexpo//Administrativos/carreras', 'name': 'Administrativos/carreras', 'children': []}], {'menu-barra-superior': False, 'nivel-superior': False, 'menu-pie': False, 'menu-principal': False, 'menu-mi-cuenta': False}], {'Menu': 1}, '19/11/2017 18:58:41', ['Publicada'])
db('Menus').insertar('Mi menu', [[{'url': 'http://localhost/PTC/unexpo/index', 'name': 'nombre de la etiqueta', 'children': []}, {'url': 'http://localhost/PTC/unexpo/Administrativos', 'name': 'Administrativos', 'children': []}], {'menu-barra-superior': False, 'nivel-superior': False, 'menu-pie': False, 'menu-principal': True, 'menu-mi-cuenta': True}], {'Menu': 2}, '19/11/2017 18:58:41', ['Publicada'])
db.load=False
