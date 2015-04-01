import json
import codecs
import sqlite3

class Installation:
	"""docstring for installation"""
	def __init__(self, ComInsee, InsNumeroInstall, InsNoVoie, InsLibelleVoie, InsCodePostal, ComLib, Latitude, Longitude):
		self.InsNumeroInstall = InsNumeroInstall
		self.ComInsee = ComInsee
		self.InsNoVoie = InsNoVoie
		self.InsLibelleVoie = InsLibelleVoie
		self.InsCodePostal = InsCodePostal
		self.ComLib = ComLib
		self.Latitude = Latitude
		self.Longitude = Longitude

	def __repr__(self):
		return "{} - {} - {} - {} - {} - {} - {} - {}".format(self.ComInsee, self.InsNumeroInstall, self.InsNoVoie, self.InsLibelleVoie, self.InsCodePostal, self.ComLib, self.Latitude, self.Longitude)

	def get_ComInsee(self):
		return str(self.ComInsee)

	def get_InsNumeroInstall(self):
		return str(self.InsNumeroInstall)

	def get_InsNoVoie(self):
		return str(self.InsNoVoie)

	def get_InsLibelleVoie(self):
		return str(self.InsLibelleVoie)

	def get_InsCodePostal(self):
		return str(self.InsCodePostal)

	def get_ComLib(self):
		return str(self.ComLib)

	def get_Latitude(self):
		return str(self.Latitude)

	def get_Longitude():
		return str(self.Longitude)

	def SQLcreate(self):
		return "CREATE TABLE installation (ComInsee INTEGER, InsNumeroInstall INTEGER, InsNoVoie VARCHAR, InsLibelleVoie VARCHAR, InsCodePostal INTEGER, ComLib VARCHAR, Latitude REAL, Longitude REAL)"
	
	def SQLinsert(self):
		return "INSERT INTO installation VALUES({}, {}, '{}', '{}' , {}, '{}', {} , {})".format(self.ComInsee, self.InsNumeroInstall, self.InsNoVoie.replace("'", '"'), self.InsLibelleVoie.replace("'",'"') , self.InsCodePostal, self.ComLib.replace("'",'"'), self.Latitude , self.Longitude)

def parse_json_installation(file):
	install = []

	json_data = codecs.open(file, encoding="utf-8").read()
	data = json.loads(json_data)

	for it in data["data"]:
		if (it["InsNoVoie"] != None and it["InsLibelleVoie"]):
			install.append(Installation(it["ComInsee"], it["InsNumeroInstall"], it["InsNoVoie"], it["InsLibelleVoie"], it["InsCodePostal"], it["ComLib"], it["Latitude"], it["Longitude"]))

	return install

items = parse_json_installation("ressource/installation.json")
'''
for item in items:
	print(item)'''