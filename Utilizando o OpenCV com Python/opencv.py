import cv2 #importando a biblioteca 
import numpy as np #Importando a imagem para um numpy array, que depois usaremos a função .imread do OpenCV, que possibilitará o retorno da imagem, o estado e os pixels para um numpy. 

img = cv2.imread('godot.png', cv2.IMREAD_COLOR) #a variável img (que será esse numpy) que retornará o retorno da função cv2.imread() que possuem dois parâmetros:

#godot.png é o nome do arquivo importado para fazer a leitura pelo OpenCV 

#podemos mudar o parâmetro da cor, ao invés de color, podemoremos colocar IMREAD_Grayscale ou até mesmo ser substituindo por 0, outra constante


cv2.namedWindow('Hello World') #para exibirmos a imagem precisamos criar uma janela, usamos o comando cv2, com a função namedWindow, e como o nome do 1°parâmetro, colocaremos o titulo que será 'Hello World' 
cv2.imshow('Hello World', img) #aqui sera exibida a imagem, inserida dentro da janela acima, aqui estará o 2° parâmetro da função cv2. A imagem que queremos exibir, estará no Array chamado img.
cv2.waitKey() #tempo para a janela fechar, estará como indefinido, para que ela fique constatemente aberta 