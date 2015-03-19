import codecs
import json
import sqlite3

class Activite:
	"""docstring for Activite"""
	def __init__(self, EquipementId, ComInsee, ActCode):
		self.EquipementId = EquipementId
		self.ComInsee = ComInsee
		self.ActCode = ActCode

	def __repr__(self):
		return "{} - {} - {}".format(self.ComInsee, self.ActCode, self.EquipementId)

	def get_equipementId(self):
		return str(self.EquipementId)

	def get_actCode(self):
		return str(self.ActCode)

	def get_comInsee(self):
		return str(self.ComInsee)

	def set_equipementId(self, EquipementId):
		self.EquipementId = EquipementId

	def set_actCode(self, ActCode):
		self.ActCode = ActCode

	def set_comInsee(self, comInsee):
		self.ComInsee = ComInsee

	def SQLcreate(self):
		return "CREATE TABLE activite (EquipementId INTEGER, ComInsee INTEGER, ActCode INTEGER)"
	
	def SQLinsert(self):
		return "INSERT INTO activite VALUES ({}, {}, {})".format(self.EquipementId, self.ComInsee, self.ActCode)


def parse_json_activite(file):
	activite = []

	json_data = codecs.open(file, encoding="utf-8").read()
	data = json.loads(json_data)

	for it in data["data"]:
		if (it["EquipementId"] != None and it["ComInsee"] != None and it["ActCode"] != None):
			activite.append(Activite(it["EquipementId"], it["ComInsee"], it["ActCode"]))

	return activite


items = parse_json_activite("ressource/activite.json")
'''
for item in items:
	print(item)'''