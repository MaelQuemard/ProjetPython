import json
import codecs
import sqlite3

class Installation:
	"""docstring for installation"""
	def __init__(self, comInsee, insNumeroInstall):
		self.insNumeroInstall = insNumeroInstall
		self.comInsee = comInsee

	def __repr__(self):
		return "{} - {}".format(self.comInsee, self.insNumeroInstall)

	def get_comInsee(self):
		return str(self.comInsee)

	def get_insNumeroInstall(self):
		return str(self.insNumeroInstall)

	def set_comInsee(self, comInsee):
		self.comInsee = comInsee

	def set_insNumeroInstall(self, insNumeroInstall):
		self.insNumeroInstall = insNumeroInstall

	def SQLcreate(self):
		return "CREATE TABLE installation (comInsee INTEGER, insNumeroInstall INTEGER)"
	def SQLinsert(self):
		return "INSERT INTO installation VALUES ({}, {})".format(self.comInsee, self.insNumeroInstall)

def parse_json_installation(file):
	install = []

	json_data = codecs.open(file, encoding="utf-8").read()
	data = json.loads(json_data)

	for it in data["data"]:
		install.append(Installation(it["ComInsee"], it["InsNumeroInstall"]))

	return install

items = parse_json_installation("ressource/installation.json")

for item in items:
	print(item)