from abc import ABC, abstractmethod

class Pessoa (ABC):
    def __init__(self, id, nome, cpf):
        self.id = id
        self.nome = nome 
        self._cpf = cpf

    
    def getInformacoes(self):
        infos = f'''
            ID: {self.id}.
            Aluno: {self.nome}.
            CPF: {self._cpf}
        '''
        return infos
    
    @abstractmethod
    def marcarPresenca(self):
        pass

    def matricular(self):
        pass
