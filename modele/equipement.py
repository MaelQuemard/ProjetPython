import codecs
import json
import sqlite3

class Equipement:
	"""docstring for Equipement"""
	def __init__(self, comInsee, insNumeroInstall, equipementId, EquNom):
		self.comInsee = comInsee
		self.insNumeroInstall = insNumeroInstall
		self.equipementId = equipementId
		self.EquNom = EquNom

	def __repr__(self):
		return "{} - {} - {} - {}".format(self.comInsee, self.insNumeroInstall, self.equipementId, self.EquNom)

	def get_comInsee(self):
		return str(self.comInsee)

	def get_insNumeroInstall(self):
		return str(self.insNumeroInstall)

	def get_equipementId(self):
		return str(self.equipementId)

	def SQLcreate(self):
		return "CREATE TABLE equipement (equipementId integer, comInsee integer, insNumeroInstall integer, EquNom VARCHAR)"
	
	def SQLinsert(self):
		return "INSERT INTO equipement VALUES ({}, {}, {}, '{}')".format(self.equipementId, self.comInsee, self.insNumeroInstall, self.EquNom.replace("'", '"'))


def parse_json_equipement(file):
	equip = []

	json_data = codecs.open(file, encoding="utf-8").read()
	data = json.loads(json_data)

	for it in data["data"]:
		equip.append(Equipement(it["ComInsee"], it["InsNumeroInstall"], it["EquipementId"], it["EquNom"]))

	return equip

items = parse_json_equipement("ressource/equipement.json")
'''
for item in items:
	print(item)'''