import matplotlib.pyplot as plt
import numpy as np

#valores fornecidos pelo fabricante
tensao_limiar = 1.0
beta = 0.002

#valores variaveis na analise
vdd = 5.0
rd = 1000

#incrementando o valor de vgs e descobrindo o valor de id e vds
vgs_inicio = 0.0
vgs_limite = 5.0
lista_vgs = []
lista_id = []
lista_vds = []
n = 0

while vgs_inicio < vgs_limite:
    print("------------------------------------------")

    #regiao de corte
    if(vgs_inicio < tensao_limiar):
        id = 0
        vds = vdd - (rd*id)
        lista_id = id
        lista_vds = vds
        print("id corte = ", id)
        print("vds corte = ", vds)

    #regiao de saturacao
    if(vds >= (vgs_inicio-tensao_limiar)):
        id = (beta/2)*(vgs_inicio-tensao_limiar)*(vgs_inicio-tensao_limiar)
        vds = vdd - (rd*id)
        lista_id = id
        lista_vds = vds
        print("id saturacao = ", id)
        print("vds saturacao = ", vds)

    #regiao ohmica / regiao de triodo
    if(vds < (vgs_inicio-tensao_limiar)):
        id = beta*(((vgs_inicio-tensao_limiar)*vds)-vds**2/2)
        vds = vdd - (rd*id)
        lista_id = id
        lista_vds = vds
        print("id triodo = ", id)
        print("vds triodo = ", vds)

    lista_vgs = vgs_inicio
    vgs_inicio += 0.15
    n = n + 1
    print("vgs = ", lista_vgs) #valores de vgs
    print("qtd de valores = ", n) #qtd de elementos na lista
    print("------------------------------------------")

#os graficos estao aparecendo vazios 

#grafico 1 - vgs x vds
fig, ax = plt.subplots()
ax.plot(lista_vgs,lista_vds)

ax.set(xlabel = 'VGS [V]', ylabel = 'VDS [V]', title= 'Gráfico de VGS x VDS')
ax.grid()
fig.savefig('vgsevds.jpg')
plt.show()

#grafico 2 - id x vgs
figu, bx = plt.subplots()
bx.plot(lista_id,lista_vgs)

bx.set(xlabel = 'ID [V]', ylabel = 'VGS [V]', title= 'Gráfico de ID x VGS')
bx.grid()
figu.savefig('idversusvgs.jpg')
plt.show()
