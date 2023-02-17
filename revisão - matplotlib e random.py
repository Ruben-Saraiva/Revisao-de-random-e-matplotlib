#!/usr/bin/env python
# coding: utf-8

# In[50]:


#importando as bibliotecas
import matplotlib
import matplotlib.pyplot as plt
import random as r
pessoas = []

# crianção de valores aleatórios
for p in range(1, 24):
    p = r.randrange(0, 60) 
    pessoas.append(p)
for p_2 in range(1, 19):
    p_2 = r.randrange(60, 130) 
    pessoas.append(p_2)
for p_3 in range(1, 26):
    p_3 = r.randrange(130, 200) 
    pessoas.append(p_3) 
for p_3 in range(1, 14):
    p_3 = r.randrange(200, 300) 
    pessoas.append(p_3)
for p_4 in range(1, 15):
    p_4 = r.randrange(300, 321) 
    pessoas.append(p_4)

# referência de anos
ano = [i for i in range(1929, 2022)]
rx = ano
ry = []

# elaboração simples de uma linha exponencial
for y in range(93):
    r = y**1.28
    ry.append(r)

# plotagem
plt.plot(ano, pessoas, color='red', label='Indivíduos')
plt.plot(rx, ry, color='black',label='Linha de Referência')
plt.title('Prática de Exercícios Físicos em Casa')
plt.xlabel('Anos')
plt.ylabel('Milhão')
plt.legend()
plt.show()


# In[ ]:





# In[ ]:




