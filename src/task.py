# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa
#       #https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import time 

# pyautogui.click -> clicar com 0 mouse
# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.hotkey -> atalho (combinação de teclas)


pyautogui.PAUSE = 1
# abrir o chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
# entrar no link 
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")
# esperar o site carregar
time.sleep(10)

#########################################################

# Passo 2: Fazer o login
pyautogui.click(x=467, y=397)
pyautogui.write("famaszila.couto@gmail.com")


pyautogui.press("tab") # passa para o campo de senha
pyautogui.write("senha")

pyautogui.press("tab") # passa para o botão de login
pyautogui.press("enter")

time.sleep(4)
# Passo 3: Importar a base de dados de produtos
# pip install pandas numpy openpyxl
import pandas

tabela =  pandas.read_csv("produtos.csv")
print(tabela)

# Passo 4: Cadastrar 1 produto
# Passo 5: Repetir o cadastro para todos os produtos    
# pip install pyautogui


