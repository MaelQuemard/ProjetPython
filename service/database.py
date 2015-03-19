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

	def insert(self, it):
		co = self.conn.cursor()
		for its in it:
			co.execute(its.SQLinsert())

	def selectAll(self, name):
		co = self.conn.cursor()
		res = "<h1>"+name+"</h1>"
		res = res + "<table border=1>"
		for row in co.execute("SELECT * FROM "+name):
			res = res + "<tr>"
			for el in row:
				res = res + "<td>"+str(el)+"</td>"
			res = res + "</tr>"
		res = res +"</table>"
		return res

	def close(self):
		self.conn.close()