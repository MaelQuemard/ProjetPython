import codecs
import json
import sqlite3

class Equipement:
	"""docstring for Equipement"""
	def __init__(self, comInsee, insNumeroInstall, equipementId):
		self.comInsee = comInsee
		self.insNumeroInstall = insNumeroInstall
		self.equipementId = equipementId

	def __repr__(self):
		return "{} - {} - {}".format(self.comInsee, self.insNumeroInstall, self.equipementId)

	def get_comInsee(self):
		return str(self.comInsee)

	def get_insNumeroInstall(self):
		return str(self.insNumeroInstall)

	def get_equipementId(self):
		return str(self.equipementId)

	def set_comInsee(self, comInsee):
		self.comInsee = comInsee

	def set_insNumeroInstall(self, insNumeroInstall):
		self.insNumeroInstall = insNumeroInstall

	def set_equipementId(self, equipementId):
		self.equipementId = equipementId

	def SQLcreate(self):
		return "CREATE TABLE IF NOT EXISTS equipement (equipementId INTEGER, comInsee INTEGER, insNumeroInstall INTEGER)"
	
	def SQLinsert(self):
		return "INSERT INTO equipement VALUES ({}, {}, {})".format(self.equipementId, self.comInsee, self.insNumeroInstall)


def parse_json_equipement(file):
	equip = []

	json_data = codecs.open(file, encoding="utf-8").read()
	data = json.loads(json_data)

	for it in data["data"]:
		equip.append(Equipement(it["ComInsee"], it["InsNumeroInstall"], it["EquipementId"]))

	return equip

items = parse_json_equipement("c:/Users/Mael/Documents/Github/ProjetPython/ressource/equipement.json")

for item in items:
	print(item)