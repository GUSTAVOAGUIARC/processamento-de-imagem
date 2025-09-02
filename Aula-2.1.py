import cv2
import numpy
import matplotlib.pyplot as plt


def transformarCinza(imagem):
    canalGray = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8)
    for i in  range(imagem.shape[0]):
        for j in range (imagem.shape[1]):
            canalGray[i,j] = int(imagem[i, j].sum() // 3)
    
    return canalGray

def plotGrafico(imagem):

    pixel = 256*[0] #Define eixo x
    for i in range(256):
        pixel[i]=i

    plt.xlabel('pixel')  #nome eixo x
    plt.ylabel('quantidade') #nome eixo y
    plt.title('histograma da imagem em tons de Cinza') #Titulo do plot

    histograma = numpy.zeros(256, dtype=int)        #Cria o histograma da imagem
    for i in  range(imagem.shape[0]):
        for j in range (imagem.shape[1]):
            histograma[imagem[i,j]] += 1

    plt.bar(pixel,histograma ,color ='blue')
    plt.show()

def corteHistograma(imagem, x, teste):
    corte = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8)
    if teste == 'menor':
        for i in  range(imagem.shape[0]):
            for j in range (imagem.shape[1]):
                if imagem[i,j] <= x:
                    corte[i,j] = (imagem[i, j])
                else:
                    corte[i,j] = 255
    if teste == 'maior':
        for i in  range(imagem.shape[0]):
            for j in range (imagem.shape[1]):
                if imagem[i,j] >= x:
                    corte[i,j] = (imagem[i, j])
                else:
                    corte[i,j] = 0
    
   
    return corte
        

    

def main():

    imagem = cv2.imread("ArrozFeijao.jpg")
    imagem2 = cv2.imread("tigre.jpg")
    canalGray = transformarCinza(imagem)
    plotGrafico(canalGray)
 
    # cv2.imshow("Canal gray", canalGray)
    corteArroz = corteHistograma(canalGray,120, 'menor')        #  mostrar as cores menores que 120
    corte = corteHistograma(canalGray,120,'maior')
    cv2.imshow("ARROZ",corte)
    cv2.imshow("feijão",corteArroz)
    cv2.waitKey(0)

if __name__ =='__main__':
    main()