#gerador de senhas seguras

import random

letra_maiuscula = chr(random.randint(65,90))
letra_minuscula = chr(random.randint(97,122))
char_especial = chr(random.randint(33,64))
lista_numeros = []

# letra_maiuscula = str(chr(random.randint(65,90)))
# letra_minuscula = str(chr(random.randint(97,122)))
# char_especial = str(chr(random.randint(33,64)))

# ****************************
for i in range(5):
    numeros = random.randrange(0,9)
    lista_numeros.append(numeros)
# ****************************


random.shuffle(lista_numeros)
lista_numeros = str(lista_numeros) [1:-1]
lista_numeros = lista_numeros.replace(',', '')

print('GERADOR DE SENHAS')
lista_nova = print('Sua nova senha é: ',letra_maiuscula,letra_minuscula,lista_numeros,char_especial)
# lista_nova = print('Sua nova senha é: ',letra_maiuscula.rstrip(),letra_minuscula.rstrip(),lista_numeros.rstrip(),char_especial.rstrip())

# a 97
# b 98
# c 99
# d 100
# e 101
# f 102
# g 103
# h 104
# i 105
# j 106
# k 107
# l 108
# m 109
# n 110
# # o 111
# # p 112
# # q 113
# # r 114
# # s 115
# # t 116
# # u 117
# # v 118
# # w 119
# # x 120
# # y 121
# # z 122
# A 65
# B 66
# C 67
# D 68
# E 69
# F 70
# G 71
# H 72
# I 73
# J 74
# K 75
# L 76
# M 77
# N 78
# O 79
# P 80
# Q 81
# R 82
# S 83
# T 84
# U 85
# V 86
# W 87
# X 88
# Y 89
# Z 90
# ! 33
# " 34
# # 35
# $ 36
# % 37
# & 38
# ' 39
# ( 40
# ) 41
# * 42
# + 43
# , 44
# - 45
# . 46
# / 47
# : 58
# ; 59
# < 60
# = 61
# > 62
# ? 63
# @ 64

    

