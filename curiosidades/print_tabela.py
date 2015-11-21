"""
Universidade Federal da Paraíba
Departamento de Ciências Exatas
Disciplina: Introdução à Programação
Professor: Rodrigo Rebouças de Almeida
           http://rodrigor.dcx.ufpb.br

Este programa imprime uma tabela de caracteres UNICODE.

Data: 17/05/2015
"""

arquivo = open('ascii.txt','w')
for i in range(3000):
    arquivo.write(" {}:{} \t".format(i,chr(i)))

arquivo.close()