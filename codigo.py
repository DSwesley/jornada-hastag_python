# Passo a passo do projeto

# 1 -  entrar no sistema da empresa
#      - https://dlp.hashtagtreinamentos.com/python/intensivao/login
# install pip3 pyautogui (biblioteca)
# importe as bibliotecas (pyautogui, time)

import pyautogui
import time

# comandos pyautogui
# clicar -> pyautogui.click
# escrever -> pyautogui.write
# apertar uma tecla -> pyautogui.press
# atalho -> pyautogui.hotkeyhttps?//dlp.hashtagtreinamentos.com/python/intensivao/login
# scroll -> pyautogui.scroll (numero) (numero positivo sobe o scroll 1000) (numero negativo desce o scrool -100)

pyautogui.PAUSE= 0.2
link= "dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(0.6)


# 2  - fazer login
pyautogui.click(x=580, y=465)
pyautogui.write("aaaaaaaa@aaa.com")
pyautogui.press("tab")
pyautogui.write("#%#$DGFD#%$#$#Dddfd")
pyautogui.click(x=702, y=630)
time.sleep(0.6)

# 3  - importar a base de dados
#importar biblioteca para leitura de dados (pandas)
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)


for linha in tabela.index:
    # 4  - cadastrar um produto
    pyautogui.click(x=469, y=351)
    #codigo
    pyautogui.write(str(tabela.loc[linha,"codigo"]))
    pyautogui.press("tab")
    #marca
    pyautogui.write(str(tabela.loc[linha,"marca"]))
    pyautogui.press("tab")
    #tipo
    pyautogui.write(str(tabela.loc[linha,"tipo"]))
    pyautogui.press("tab")
    #categoria
    pyautogui.write(str(tabela.loc[linha,"categoria"]) ) 
    pyautogui.press("tab")
    #preco
    pyautogui.write(str(tabela.loc[linha,"preco_unitario"]))
    pyautogui.press("tab")
    #custo
    pyautogui.write(str(tabela.loc[linha,"custo"]))
    pyautogui.press("tab")
    #obs
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")
    
    #enviar  
    pyautogui.press("enter")
    pyautogui.scroll(5000)
    time.sleep(0.2)

# 5  - repetir isso ate acabar o produto

