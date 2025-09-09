import cv2
import numpy
import matplotlib.pyplot as plt


def plotGrafico(imagem, x):

    pixel = 256*[0] #Define eixo x
    for i in range(256):
        pixel[i]=i

    plt.xlabel('pixel')  #nome eixo x
    plt.ylabel('quantidade') #nome eixo y
    plt.title('histograma da imagem ' + x ) #Titulo do plot

    histograma = numpy.zeros(256, dtype=int)        #Cria o histograma da imagem
    for i in  range(imagem.shape[0]):
        for j in range (imagem.shape[1]):
            histograma[imagem[i,j]] += 1

    plt.bar(pixel,histograma ,color ='blue')
    plt.show()

def transformarCinza(imagem):
    canalGray = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8)
    for i in  range(imagem.shape[0]):
        for j in range (imagem.shape[1]):
            canalGray[i,j] = int(imagem[i, j].sum() // 3)
    
    return canalGray

def alterarTom(imagem,contraste,brilho):
    novaImagem = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8)
    for i in  range(imagem.shape[0]):
        for j in range (imagem.shape[1]):
            y = int(imagem[i][j])
            x  = (contraste * y) + brilho
            if x >255:
                novaImagem[i][j] = 255
            else:
                novaImagem[i][j] = x
    return novaImagem

def negativoImagem(imagem):
    novaImagem = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8)
    for i in  range(imagem.shape[0]):
        for j in range (imagem.shape[1]):
            novaImagem[i][j] = 255 - imagem[i][j]

    return novaImagem

def curvaImagem(imagem):
    novaImagem = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8)
    for i in  range(imagem.shape[0]):
        for j in range (imagem.shape[1]):
            y = (imagem[i][j])
            x = (-255*((1/256)*y)**2)
            novaImagem[i][j] = x
    return novaImagem


def main():

    imagem = cv2.imread("C:\\Users\\aluno\\Desktop\\processamento-de-imagem-main\\Aula-3\\tigre.jpg")


    canalGray = transformarCinza(imagem)
    plotGrafico(canalGray, "cinza")

    # novaImagem = alterarTom(canalGray,2,0)
    # cv2.imshow("nova Imagem", novaImagem)

    cv2.imshow("Canal gray", canalGray)
    # plotGrafico(novaImagem, "contraste 2x")
    # negativo = negativoImagem(canalGray)
    # cv2.imshow("negativo", negativo)
    # plotGrafico(negativo,"negativo")

    curva = curvaImagem(canalGray)
    plotGrafico(curva,"curva")
    cv2.imshow("curva",curva)
    cv2.waitKey(0)

if __name__ == "__main__":
    main()
