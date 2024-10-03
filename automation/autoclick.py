import pyautogui
import time

# Tempo de espera para se preparar
time.sleep(5)

# Posição onde o clique será feito (x, y)
posicao = (500, 300)  # Exemplo de coordenada na tela

# Função para clicar
def clicar_repetidamente(intervalo, repeticoes):
    for i in range(repeticoes):
        pyautogui.click(posicao)  # Clique na posição especificada
        time.sleep(intervalo)  # Intervalo entre cliques

# Parâmetros: intervalo entre cliques e o número de cliques
clicar_repetidamente(intervalo=1, repeticoes=10)
