# -*- coding: utf-8 -*-

import sqlite3

class Database:
	"""Class Database"""
	def __init__(self, pathdb):
		self.conn = sqlite3.connect(pathdb)
		self.pathdb = pathdb

	'''Function to create table associate at the name and item'''
	def create(self, name, item):
		co = self.conn.cursor()
		co.execute("DROP TABLE IF EXISTS "+name)
		co.execute(item.SQLcreate())
		self.conn.commit()

	'''Function to insert the element one by one at the table associate at the name'''
	def insertOne(self, name):
		co = self.conn.cursor()
		co.execute(name.SQLinsert())

	'''Function to select all the database'''
	def selectAll(self, name):
		co = self.conn.cursor()
		return co.execute("SELECT * FROM " + name)

	'''Function to commit the database'''
	def commit(self):
		self.conn.commit()

	'''Function to close the connection of database'''
	def close(self):
		self.conn.close()

	'''Function to execute request for had the places with the name of city and activity'''
	def requestActivityCity(self, commune, activite):
		co = self.conn.cursor()
		return co.execute("SELECT DISTINCT a.ActLib, i.ComLib, e.EquNom, i.Latitude, i.Longitude FROM installation i, equipement e, activite a WHERE i.InsNumeroInstall=e.InsNumeroInstall and e.EquipementId = a.EquipementId and i.ComLib = \"" + commune + "\" and a.ActLib= \""+activite + "\"")

	'''Function to execute request for had the name of activity with name of city'''
	def requestActivity(self, commune):
		co = self.conn.cursor()
		return co.execute("SELECT DISTINCT a.ActLib FROM installation i, equipement e, activite a WHERE i.InsNumeroInstall=e.InsNumeroInstall and e.EquipementId = a.EquipementId and i.ComLib = \"" + commune +"\"")

	'''Function to execute request for had the name of city with the name of activity'''
	def requestCity(self):
		co = self.conn.cursor()
		return co.execute("SELECT DISTINCT i.ComLib FROM installation i")