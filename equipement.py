class equipement():
	"""docstring for Equipement"""
	def __init__(self, comInsee, comLib, insNumeroInstall, insNom, equipementId, equNom, equNomBatiment):
		self.comInsee = comInsee
		self.comLib = comLib
		self.insNumeroInstall = insNumeroInstall
		self.insNom = insNom
		self.equipementId = equipementId
		self.equNom = equNom
		self.equNomBatiment = equNomBatiment

	def get_comInsee(self):
		return str(self.comInsee)

	def get_comLib(self):
		return str(self.comLib)

	def get_insNumeroInstall(self):
		return str(self.insNumeroInstall)

	def get_insNom(self):
		return str(self.insNom)

	def get_equipementId(self):
		return str(self.equipementId)

	def get_equNom(self):
		return str(self.equNom)

	def get_equNomBatiment(self):
		return str(self.equNomBatiment)

	def set_comInsee(self, comInsee):
		self.comInsee = comInsee

	def set_comLib(self, comLib):
		self.comLib =comLib

	def set_insNumeroInstall(self, insNumeroInstall):
		self.insNumeroInstall = insNumeroInstall

	def set_insNom(self, insNom):
		self.insNom = insNom

	def set_equipementId(self, equipementId):
		self.equipementId = equipementId

	def set_equNom(self, equNom):
		self.equNom = equNom

	def set_equNomBatiment(self, equNomBatiment):
		self.equNomBatiment = equNomBatiment
