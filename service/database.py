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
		res += "<table>"
		co.execute("SELECT COLUMN_NAME FROM ""INFORMATION_SCHEMA.COLUMNS"" WHERE TABLE_NAME = " + name)
		for row in co.execute("SELECT * FROM " + name):
			res += "<tr>"
			for el in row:
				res += "<td>"+str(el)+"</td>"
			res += "</tr>"
		res += "</table>"
		return res

	def close(self):
		self.conn.close()