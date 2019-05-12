#!/usr/bin/env python

# Bibliotecas necessarias
import rospy
import cv2
import sys
import time
import numpy as np
from std_msgs.msg import String
from std_msgs.msg import Int32
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError


# Variaveis globais
start = time.time()
temp = 26
rad = 37


# Funcao responsavel por salvar as img da camera
def save_img(tela, id = time.time()):
    if cv2.waitKey(1) == ord('s'):
        cv2.imwrite('pic_ROSBOT1' + str(id) + '.jpg', tela)
        print ('imagem salva')


# Funcao do print das informacoes na tela
def print_info(tela, temperatura, radiacao):
    # Font usada 
    font = cv2.FONT_HERSHEY_SIMPLEX

    # Marcacao do tempo de execucao do programa
    timer = int(time.time() - start)

    # Print das informacoes na tela
    cv2.putText(tela, str(timer) + 's', (10, 20), font, 0.5, (0, 255, 255), 1)
    cv2.putText(tela, str(temperatura) + 'C', (60, 20), font, 0.5, (0, 255, 255), 1)
    cv2.putText(tela, str(radiacao) + 'Sv/h', (110, 20), font, 0.5, (0, 255, 255), 1)
    cv2.putText(tela, str(time.ctime()), (10, 230), font, 0.5, (0, 255, 255), 1)


# Funcao q ira executar sistema de visao
def callback(data):
    # Criacao do objeto de convercao
    bridge = CvBridge()

    # Converter a imagem ros para imagem cv2
    cv2_frame = bridge.imgmsg_to_cv2(data, "bgr8")

    # Escrever as informacoes na imagem
    print_info(cv2_frame, temp, rad)

    # Exibir a imagem em uma janela
    cv2.imshow('ROSBOT1 Vision', cv2_frame)    

    # Funcao para salvar imagem
    save_img(cv2_frame)

    cv2.waitKey(1)


def listener():
    # Inicio do node camera_sub
    rospy.init_node('vision_sub', anonymous=True)

    # Inscricao no topico e definicao da callback como funcao a ser executada
    rospy.Subscriber("vision_topic", Image, callback)

    # Mantem o python funcionando apos o encerramendo do node
    rospy.spin()


# Funcao main
if __name__ == '__main__':
    listener()


