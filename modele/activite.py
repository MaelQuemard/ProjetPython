import codecs
import json
import sqlite3

class Activite:
	"""Class Activite"""
	def __init__(self, EquipementId, ComInsee, ActCode, ActLib):
		self.EquipementId = EquipementId
		self.ComInsee = ComInsee
		self.ActCode = ActCode
		self.ActLib = ActLib

	'''Equivalent of toString'''
	def __repr__(self):
		return "{} - {} - {} - {}".format(self.ComInsee, self.ActCode, self.EquipementId, self.ActLib)

	def get_equipementId(self):
		return str(self.EquipementId)

	def get_actCode(self):
		return str(self.ActCode)

	def get_comInsee(self):
		return str(self.ComInsee)

	def get_actLib(self):
		return str(self.ActLib)

	'''For create the table associate at activite'''
	def SQLcreate(self):
		return "CREATE TABLE activite (EquipementId INTEGER, ComInsee INTEGER, ActCode INTEGER, ActLib VARCHAR)"
	
	'''For insert on the table activite'''
	def SQLinsert(self):
		return "INSERT INTO activite VALUES ({}, {}, {}, '{}')".format(self.EquipementId, self.ComInsee, self.ActCode, self.ActLib.replace("'", '"'))

'''For parse the JSON of activite'''
def parse_json_activite(file):
	activite = []

	json_data = codecs.open(file, encoding="utf-8").read()
	data = json.loads(json_data)

	for it in data["data"]:
		if (it["EquipementId"] != None and it["ComInsee"] != None and it["ActCode"] != None and it["ActLib"] != None):
			activite.append(Activite(it["EquipementId"], it["ComInsee"], it["ActCode"], it["ActLib"]))

	return activite


items = parse_json_activite("ressource/activite.json")
'''
for item in items:
	print(item)'''