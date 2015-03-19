import json
import codecs
import sqlite3

class Installation:
	"""docstring for installation"""
	def __init__(self, ComInsee, InsNumeroInstall):
		self.InsNumeroInstall = InsNumeroInstall
		self.ComInsee = ComInsee

	def __repr__(self):
		return "{} - {}".format(self.ComInsee, self.InsNumeroInstall)

	def get_ComInsee(self):
		return str(self.ComInsee)

	def get_InsNumeroInstall(self):
		return str(self.InsNumeroInstall)

	def set_comInsee(self, ComInsee):
		self.ComInsee = ComInsee

	def set_insNumeroInstall(self, InsNumeroInstall):
		self.InsNumeroInstall = InsNumeroInstall

	def SQLcreate(self):
		return "CREATE TABLE installation (ComInsee INTEGER, InsNumeroInstall INTEGER)"
	def SQLinsert(self):
		return "INSERT INTO installation VALUES ({}, {})".format(self.ComInsee, self.InsNumeroInstall)

def parse_json_installation(file):
	install = []

	json_data = codecs.open(file, encoding="utf-8").read()
	data = json.loads(json_data)

	for it in data["data"]:
		install.append(Installation(it["ComInsee"], it["InsNumeroInstall"]))

	return install

items = parse_json_installation("ressource/installation.json")
'''
for item in items:
	print(item)'''