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

	def insert(self, items):
		co = self.conn.cursor()
		for item in items:
			co.execute(item.SQLinsert())

	def insertOne(self, name):
		co = self.conn.cursor()
		co.execute(name.SQLinsert())

	def selectAll(self, name):
		co = self.conn.cursor()
		res = "<h1>"+ name +"</h1>"
		res = res + "<table border=1>"
		for row in co.execute("SELECT * FROM " + name):
			print(row)
			res = res + "<tr>"
			for element in row:
				res = res + "<td>"+str(element)+"</td>"
			res = res + "</tr>"
		res = res + "</table>"
		return res

	def commit(self):
		self.conn.commit()

	def close(self):
		self.conn.close()