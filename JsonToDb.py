# -*- coding: utf-8 -*-

import modele.installation as ins
import modele.equipement as eq
import modele.activite as act

import service.database as db

inst = ins.parse_json_installation("ressource/installation.json")
equip = eq.parse_json_equipement("ressource/equipement.json")
acts = act.parse_json_activite("ressource/activite.json")

print("installation : \n")
database = db.Database("db/test.db")
database.create("installation", inst[0])
database.insert(inst)
database.selectAll("installation")

print("\n equipement : \n")
database = db.Database("db/test.db")
database.create("equipement", equip[0])
database.insert(equip)
database.selectAll("equipement")

print("\n activite : \n")
database = db.Database("db/test.db")
database.create("activite", acts[0])
database.insert(acts)
database.selectAll("activite")
