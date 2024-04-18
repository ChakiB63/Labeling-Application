class Phenomena:
    
    def __init__(self, presence, list): # list de bool pour chaque orientation [nw,ne,se,sw]
        self._presence = presence
        self._nw = list[0]
        self._ne = list[1]
        self._se = list[2]
        self._sw = list[3]

    # Getters

    def get_presence(self):
        return self._presence
    
    def get_nw(self):
        return self._nw

    def get_ne(self):
        return self._ne

    def get_se(self):
        return self._se

    def get_sw(self):
        return self._sw

    # Setters
    def set_presence(self, value):
        self._presence = value

    def set_nw(self, value):
        self._nw = value

    def set_ne(self, value):
        self._ne = value

    def set__se(self, value):
        self._se = value

    def set_sw(self, value):
        self._sw = value

    def infos_list(self):
        return [self.get_presence(), self.get_nw(), self.get_ne(), self.get_se(), self.get_sw()]