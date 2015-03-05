#!/Python34 python
# -*- coding: utf-8 -*-

import modele.installation as ins
#import modele.equipement as eq
import modele.activite as act

import service.database as db

inst = ins.parse_json_installation("c:/Users/Mael/Documents/Github/ProjetPython/ressource/installation.json")

acts = act.parse_json_activite("c:/Users/Mael/Documents/Github/ProjetPython/ressource/activite.json")

database = db.Database("c:/Users/Mael/Documents/Github/ProjetPython/db/test.db")
database.create("installation", inst[0])
database.insert(inst)
database.selectAll("installation")

database = db.Database("c:/Users/Mael/Documents/Github/ProjetPython/db/test.db")
database.create("activite", acts[0])
database.insert(acts)
database.selectAll("activite")
