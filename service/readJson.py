#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Allows to read a JSON file
"""

import json
#from modele import installation
#from modele import equipement
#from modele import activite

from pprint import pprint

class readJson:

	def __init__(self, pathfile):
		self.pathfile = pathfile
		
	def read(self):
		with open('../ressource/'+self.pathfile) as data_file:
			data = json.load(data_file)

		i = 0

		while i < 10 :
			i += 1
			print(data["data"][i]["ActLib"])
			print(data["data"][i]["ActCode"])
			print(data["data"][i]["EquipementId"])
