class Activite():
	"""docstring for Activite"""
	def __init__(self, equipementId, equactivitePratique, equactivitePraticable, equactiviteSalleSpe, equNbequIdentique, actLib, actNivLib, comLib, comInsee):
		self.equipementId = equipementId
		self.equactivitePratique = equactivitePratique
		self.equactivitePraticable = equactivitePraticable
		self.equactiviteSalleSpe =  equactiviteSalleSpe
		self.equNbequIdentique = equNbequIdentique
		self.actCode = actCode
		self.actLib = actLib
		self.actNivLib = actNivLib

	def get_equipementId(self):
		return str(self.equipementId)
		
	def get_equactivitePratique(self):
		return str(self.equactivitePraticable)

	def get_equactivitePraticable(self):
		return str(self.equactivitePraticable)

	def get_equactiviteSalleSpe(self):
		return str(self.equactiviteSalleSpe)

	def get_equNbequIdentique(self):
		return str(self.equNbequIdentique)
		
	def get_actCode(self):
		return str(self.actCode)

	def get_actNivLib(self):
		return str(self.actNivLib)

	def get_comLib(self):
		return str(self.comLib)

	def get_comInsee(self):
		return str(self.comInsee)

	def set_equipementId(self, equipementId):
		self.equipementId = equipementId
		
	def set_equactivitePratique(self, equactivitePratique):
		self.equactivitePratique= equactivitePratique

	def set_equactivitePraticable(self, equactivitePraticable):
		self.equactivitePraticable = equactivitePraticable

	def set_equactiviteSalleSpe(self, equactiviteSalleSpe):
		self.equactiviteSalleSpe = equactiviteSalleSpe

	def set_equNbequIdentique(self, equNbequIdentique):
		self.equNbequIdentique = equNbequIdentique
		
	def set_actCode(self, actCode):
		self.actCode = actCode

	def set_actNivLib(self, actNivLib):
		self.actNivLib = actNivLib

	def set_comLib(self, comLib):
		self.comLib comLib

	def set_comInsee(self, comInsee):
		self.comInsee = comInsee
