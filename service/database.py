# -*- coding: utf-8 -*-

import sqlite3

class Database:
	def __init__(self, pathdb):
		self.conn = sqlite3.connect(pathdb)
		self.pathdb = pathdb

	def create(self, name, item):
		co = self.conn.cursor()
		co.execute("DROP TABLE IF EXISTS "+name)
		co.execute(item.SQLcreate())
		self.conn.commit()

	def insertOne(self, name):
		co = self.conn.cursor()
		co.execute(name.SQLinsert())

	def selectAll(self, name):
		co = self.conn.cursor()
		res = "<h1>"+ name +"</h1>"
		res = res + "<table border=1>"
		return co.execute("SELECT * FROM " + name)
		#	res = res + "<tr>"
		#	for element in row:
		#		res = res + "<td>"+str(element)+"</td>"
		#	res = res + "</tr>"
		#res = res + "</table>"
		#return res

	def commit(self):
		self.conn.commit()

	def close(self):
		self.conn.close()

	def requestActivityCity(self, commune, activite):
		co = self.conn.cursor()
		return co.execute("SELECT DISTINCT a.ActLib, i.ComLib, e.EquNom, i.Latitude, i.Longitude FROM installation i, equipement e, activite a WHERE i.InsNumeroInstall=e.InsNumeroInstall and e.EquipementId = a.EquipementId and i.ComLib = \"" + commune + "\" and a.ActLib= \""+activite + "\"")

	def requestCity(self, commune):
		co = self.conn.cursor()
		return co.execute("SELECT DISTINCT a.ActLib FROM installation i, equipement e, activite a WHERE i.InsNumeroInstall=e.InsNumeroInstall and e.EquipementId = a.EquipementId and i.ComLib = \"" + commune +"\"")