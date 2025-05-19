from Pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, id, nome, cpf, matricula):
        super().__init__(id, nome, cpf)
        self.__matricula = matricula

    def marcarPresenca(self):
        return super().marcarPresenca()
    
    def setMatricula(self, novaMatricula):
        self.__matricula = novaMatricula

    def __str__(self):
        alunosInfos = super().getInformacoes()
        return f"{alunosInfos}Matrícula: {self.__matricula}."

    def matricular(self):
        pass