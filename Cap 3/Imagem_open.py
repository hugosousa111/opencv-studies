import cv2

imagem = cv2.imread("imagem.jpg") #carrega a imagem
cv2.imshow("Imagem", imagem) #exibe
cv2.waitKey(0)
cv2.destroyAllWindows()
