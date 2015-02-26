#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

class Database:
	def __init__(self, pathdb, name):
		self.conn = sqlite3.connect(path)
		self.pathdb = pathdb
		self.name = name

	def create(self, it):
		co = self.conn.cursor()
		co.execute("DROP TABLE IF EXISTS "+self.name)
		co.execute(it.SQLcreate())
