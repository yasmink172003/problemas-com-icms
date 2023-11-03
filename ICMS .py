#!/usr/bin/env python
# coding: utf-8

# In[2]:


#variáveis iniciais
din_total = 1000
preco_compra = 0
trib_pago = 0
total_gasto = 0

#dados das camisetas
tipos_camisa = ['preta', 'branca', 'vermelha']
camisa_preco = {
    'preta':40,
    'branca':20,
    'vermelha':50,
}
camisa_qtd = {
    #quantidades compradas, e não do estoque.
    'preta':5,
    'branca':7,
    'vermelha': 3,
}

#função do icms
def icms(x):
    if x >=40:
        return x*0.065
    else:
        return x*0.025

#calculei o icms de cada tipo de camiseta

camisa_icms = {}

for i in camisa_preco:
    camisa_icms[i] = (icms(camisa_preco[i]))

# o total de tributo pago é o icms unitário multiplicado pela quantidade:
for i in camisa_preco:
    trib_pago += camisa_icms [i] * camisa_qtd[i]

# o preço da compra é o preço unitário multiplicado pela quantidade:
for i in camisa_preco:
    preco_compra += (camisa_preco[i]*camisa_qtd[i])

#aqui eu incremento as rolling sums importantes
din_total -= preco_compra + trib_pago
total_gasto += preco_compra + trib_pago

#resultados da compra total e do dinheiro pago em icms

print ('Tudo custou', total_gasto, 'Você tinha 1000, gastou', preco_compra, 'em camisas. Além disso,', trib_pago, 'foi pago em ICMS. Você agora tem', din_total, end = ' ')

#função do pis/cofins
def pis_cofins(x):
    return x * 0.15

#resultado do pis cofins
print ('Por causa dessa compra, a loja deverá pagar', pis_cofins(preco_compra), 'em PIS/Cofins pelo faturamento gerado, excluindo o ICMS da \nBase de Cálculo.', end = "\n")
print ('Antes do RE 574.706/PR, o ICMS seria parte da base de cálculo. Nesse modelo, o valor devido seria',pis_cofins(total_gasto))


# In[ ]: