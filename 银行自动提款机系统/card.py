class Card(object):
	def __init__(self, cardID, cardPasswd, cardMoney):
		self.cardID = cardID
		self.cardPasswd = cardPasswd
		self.cardMoney = cardMoney
		self.cardLock = False