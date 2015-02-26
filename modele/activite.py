import codecs
import json
import sqlite3

class Activite:
	"""docstring for Activite"""
	def __init__(self, equipementId, comInsee, actCode):
		self.equipementId = equipementId
		self.comInsee = comInsee
		self.actCode = actCode

	def __repr__(self):
		return "{} - {} - {}".format(self.comInsee, self.actCode, self.equipementId)

	def get_equipementId(self):
		return str(self.equipementId)

	def get_actCode(self):
		return str(self.actCode)

	def get_comInsee(self):
		return str(self.comInsee)

	def set_equipementId(self, equipementId):
		self.equipementId = equipementId

	def set_actCode(self, actCode):
		self.actCode = ac

	def set_comInsee(self, comInsee):
		self.comInsee = comInsee

def parse_json_activite(file):
	activite = []

	json_data = codecs.open(file, encoding="utf-8").read()
	data = json.loads(json_data)

	for it in data["data"]:
		activite.append(Activite(it["EquipementId"], it["ComInsee"], it["ActCode"]))

	return activite

items = parse_json_activite("../ressource/activite.json")

for item in items:
	print(item)
