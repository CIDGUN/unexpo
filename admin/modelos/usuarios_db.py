# -*- coding: utf-8 -*-
try:
 from ztec.zdb import DB
except:
 from zdb import DB
db=DB()
db.load=True
db('Usuarios').campo('Nombre',db.str,False,True,False,False,0,-1,None,None)
db('Usuarios').campo('Contenido',db.list,False,True,False,False,0,-1,None,None)
db('Usuarios').campo('args',db.dict,False,True,False,False,0,-1,None,None)
db('Usuarios').campo('Fecha',db.str,False,True,False,False,0,-1,None,'%d/%m/%Y %H:%M:%S')
db('Usuarios').campo('Status',db.list,False,True,False,False,0,-1,None,None)
db('Opciones').campo('Nombre',db.str,False,True,False,False,0,-1,None,None)
db('Opciones').campo('Valores',db.list,False,True,False,False,0,-1,None,None)
db('Usuarios').insertar('Administrador', [[{'name': 'usuario', 'value': 'Administrador', 'Usuario': 'text'}, {'Email': 'text', 'value': 'marquis@occoasolutions.com', 'name': 'email'}, {'Password': 'text', 'name': 'password', 'value': 'marquis@2017'}, {'opcion': 1, 'opciones': 'archivos', 'Avatar': 'select', 'value': 0, 'name': 'avatar'}, {'Token': 'hidden', 'name': 'token', 'value': 'e!S|W91P'}, {'Muere': 'hidden', 'name': 'muere', 'value': '29/7/2017 10:54:9'}, {'Login': 'hidden', 'name': 'login', 'value': True}, {'opcion': 0, 'value': 0, 'name': 'tipo', 'opciones': 'usuarios', 'Permisologia': 'select'}]], {'Usuario': 0}, '12/7/2017 10:27:11', [])
db('Usuarios').insertar('Programador', [[{'name': 'usuario', 'value': 'Programador', 'Usuario': 'text'}, {'Email': 'text', 'value': 'jzerpa.occoa@gmail.com', 'name': 'email'}, {'Password': 'text', 'name': 'password', 'value': 'occoasolutions'}, {'opcion': 1, 'Avatar': 'select', 'value': 0, 'name': 'avatar'}, {'Token': 'hidden', 'name': 'token', 'value': 'EK)y]Q0x'}, {'Muere': 'hidden', 'name': 'muere', 'value': '1/10/2017 17:14:39'}, {'Login': 'hidden', 'name': 'login', 'value': True}]], {'Usuario': 1}, '29/7/2017 10:38:36', [])
db('Usuarios').insertar('yorby', [[{'name': 'usuario', 'value': 'yorby', 'Usuario': 'text'}, {'Email': 'text', 'value': 'yorby@gmail.com', 'name': 'email'}, {'Password': 'text', 'name': 'password', 'value': '12345'}, {'opcion': 1, 'opciones': 'archivos', 'Avatar': 'select', 'value': 0, 'name': 'avatar'}, {'Token': 'hidden', 'name': 'token', 'value': 'n8sDz(]@'}, {'Muere': 'hidden', 'name': 'muere', 'value': '15/8/2017 13:34:43'}, {'Login': 'hidden', 'name': 'login', 'value': False}, {'opcion': 0, 'value': 0, 'name': 'tipo', 'opciones': 'usuarios', 'Permisologia': 'select'}]], {'Usuario': 2}, '15/8/2017 12:34:43', [])
db('Opciones').insertar('Permisos', ['Root', 'Usuario'])
db.load=False
