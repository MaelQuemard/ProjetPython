# -*- coding: utf-8 -*-

import modele.installation as ins
import modele.equipement as eq
import modele.activite as act
from progressbar import *
import service.database as db

inst = ins.parse_json_installation("ressource/installation.json")
equip = eq.parse_json_equipement("ressource/equipement.json")
acts = act.parse_json_activite("ressource/activite.json")

database = db.Database("db/test.db")
database.create("installation", inst[0])
pbar = ProgressBar(widgets=['Insert into installations to database: ', Percentage(), ' ', ETA()])
for elem in pbar(inst):
	database.insertOne(elem)

pbar = ProgressBar(widgets=['Insert into equipement to database: ', Percentage(), ' ', ETA()])
database.create("equipement", equip[0])
for elem in pbar(equip):
	database.insertOne(elem)

pbar = ProgressBar(widgets=['Insert into activite to database: ', Percentage(), ' ', ETA()])
database.create("activite", acts[0])
for elem in pbar(acts):
	database.insertOne(elem)

database.commit()

database.close()

database