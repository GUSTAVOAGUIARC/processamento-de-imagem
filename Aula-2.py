import cv2
import numpy
import matplotlib.pyplot as plt

def separarCamada(imagem):
    #Cria uma matriz do tamanho da imagem contendo somente 0
    canalBlue = canalBlue = numpy.zeros((imagem.shape[0], imagem.shape[1], imagem.shape[2]), dtype=numpy.uint8)     
    canalGreen = canalBlue = numpy.zeros((imagem.shape[0], imagem.shape[1], imagem.shape[2]), dtype=numpy.uint8)
    canalRed = canalBlue = numpy.zeros((imagem.shape[0], imagem.shape[1], imagem.shape[2]), dtype=numpy.uint8)

    canalBlue[:,:,0] = imagem[:,:,0]    #copia o canal azul para a nova matriz
    canalGreen[:,:,1] = imagem[:,:,1]
    canalRed[:,:,2] = imagem[:,:,2]

    return canalBlue , canalGreen, canalRed


def plotGrafico(imagem, cor):

    pixel = 256*[0] #Define eixo x
    for i in range(256):
        pixel[i]=i

    plt.xlabel('pixel')  #nome eixo x
    plt.ylabel('quantidade') #nome eixo y
    plt.title('histograma da imagem') #Titulo do plot

    histograma = numpy.zeros(256, dtype=int)        #Cria o histograma da imagem
    for i in  range(imagem.shape[0]):
        for j in range (imagem.shape[1]):
            histograma[imagem[i,j]] += 1

    plt.bar(pixel,histograma ,color = cor)
    plt.show()


def main():

    imagem = cv2.imread("tigre.jpg")

    canalBlue, canalGreen, canalRed = separarCamada(imagem)
    plotGrafico(canalBlue, 'blue')
    plotGrafico(canalGreen, 'green')
    plotGrafico(canalRed, 'red')

    cv2.imshow("Canal red", canalRed)
    cv2.waitKey(0)

if __name__ =='__main__':
    main()
