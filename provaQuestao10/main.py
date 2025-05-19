'''Requisitos:

A classe pessoa é abstrata
O método marcarPresenca da classe pessoa é abstrato
O atributo cpf é fracamente privado
O atributo matrícula é fortemente privado
Construa um método assessor e um método modificador para o atributo matrícula
Construa um arquivo main para testar a construção de um aluno'''

from Aluno import Aluno

aluno1 = Aluno(25, "Joe Madureira", "05678965203", 63241188)

strinAluno1 = str(aluno1)

print(f"Informações do aluno:\n{strinAluno1}")

aluno1.setMatricula(12345678)

strinAluno1 = str(aluno1)

print(f"Informações do aluno:\n{strinAluno1}")

