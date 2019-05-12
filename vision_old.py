# -*- coding: utf-8 -*-
#BIBLIOTECAS:
import cv2
import time
import numpy as np

#VARIÁVEIS:
temperatura = 29
radiacao = 27
rad = 0


cont_save = 0
l_cont_save = 0
n_cont_save = 0
nl_cont_save = 0
p_cont_save = 0
lp_cont_save = 0
np_cont_save = 0
nlp_cont_save = 0

alpha = 1
beta = 12

font = cv2.FONT_HERSHEY_SIMPLEX

start = time.time()

video = cv2.VideoCapture(0)

#FUNÇÕES:
def change_res(widht, eight):
    video.set(3, widht)
    video.set(4, eight)

def print_info(tela,rad_c):
    timer = time.time() - start
    rad_c = timer*(radiacao/36000)
    cv2.putText(tela, str(round(timer, 1)) + ' s', (0, 350), font, 1, (0, 255, 255), 2)
    cv2.putText(tela, str(temperatura) + ' C', (0, 390), font, 1, (0, 255, 255), 2)
    cv2.putText(tela, str(radiacao) + ' Sv/h  '+ str(round(rad_c,3))+' Sv', (0, 430), font, 1, (0, 255, 255), 2)
    cv2.putText(tela, str(time.ctime()), (0, 470), font, 1, (0, 255, 255), 2)
    cv2.putText(tela, 'alpha: ' + str(alpha) + '  beta: ' + str(beta), (0, 20), font, 0.6, (0, 255, 255), 2)

#MAIN FRAME COM PRINT:
while True:
    conectado, frame = video.read()
    frame = cv2.addWeighted(frame, alpha, np.zeros(frame.shape, frame.dtype), 0, beta)
    print_info(frame,rad)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('s'):
        cont_save = cont_save + 1
        cv2.imwrite('pic_pict' + str(cont_save) + '.jpg', frame)

    if cv2.waitKey(1) == ord('r'):
        alpha = 1
        beta = 12
        denoising = 10

    if cv2.waitKey(1) == ord('7'):
        alpha = alpha + 1

    if cv2.waitKey(1) == ord('8'):
        alpha = alpha - 1

    if cv2.waitKey(1) == ord('4'):
        beta = beta + 1

    if cv2.waitKey(1) == ord('5'):
        beta = beta - 1

    #MAIN FRAME SEM PRINT
    if cv2.waitKey(1) == ord('l'):
        while True:
            conectado, frame = video.read()
            frame = cv2.addWeighted(frame, alpha, np.zeros(frame.shape, frame.dtype), 0, beta)
            cv2.imshow('frame', frame)

            if cv2.waitKey(1) == ord('s'):
                l_cont_save = l_cont_save + 1
                cv2.imwrite('l_pic_pict' + str(l_cont_save) + '.jpg', frame)

            if cv2.waitKey(1) == ord('r'):
                alpha = 1
                beta = 12
                denoising = 10

            if cv2.waitKey(1) == ord('7'):
                alpha = alpha + 1

            if cv2.waitKey(1) == ord('8'):
                alpha = alpha - 1

            if cv2.waitKey(1) == ord('4'):
                beta = beta + 1

            if cv2.waitKey(1) == ord('5'):
                beta = beta - 1

            #MAIN FRAME SEM PRINT COM DENOISING
            if cv2.waitKey(1) == ord('n'):
                denoising = 10
                while True:
                    conectado, frame = video.read()
                    frame = cv2.fastNlMeansDenoisingColored(frame, None, denoising, 10, 3, 9)
                    frame = cv2.addWeighted(frame, alpha, np.zeros(frame.shape, frame.dtype), 0, beta)

                    cv2.imshow('frame', frame)

                    if cv2.waitKey(1) == ord('s'):
                        nl_cont_save = nl_cont_save + 1
                        cv2.imwrite('nl_pic_pict' + str(nl_cont_save) + '.jpg', frame)

                    if cv2.waitKey(1) == ord('r'):
                        alpha = 1
                        beta = 12
                        denoising = 10

                    if cv2.waitKey(1) == ord('7'):
                        alpha = alpha + 1

                    if cv2.waitKey(1) == ord('8'):
                        alpha = alpha - 1

                    if cv2.waitKey(1) == ord('4'):
                        beta = beta + 1

                    if cv2.waitKey(1) == ord('5'):
                        beta = beta - 1

                    if cv2.waitKey(1) == ord('+'):
                        denoising = denoising + 1

                    if cv2.waitKey(1) == ord('-'):
                        denoising = denoising - 1

                    if cv2.waitKey(1) == ord('q'):
                        break

            if cv2.waitKey(1) == ord('q'):
                break

    #MAIN FRAME COM PRINT E DENOISING
    if cv2.waitKey(1) == ord('n'):
        denoising = 10
        while True:
            timer = time.time() - start
            conectado, frame = video.read()
            frame = cv2.fastNlMeansDenoisingColored(frame,None, denoising,10,3,9)
            frame = cv2.addWeighted(frame, alpha, np.zeros(frame.shape, frame.dtype), 0, beta)
            print_info(frame, rad)
            cv2.putText(frame, 'Denoising: ' + str(denoising), (0, 40), font, 0.6, (0, 255, 255), 2)

            cv2.imshow('frame', frame)

            if cv2.waitKey(1) == ord('s'):
                n_cont_save = n_cont_save + 1
                cv2.imwrite('n_pic_pict' + str(n_cont_save) + '.jpg', frame)

            if cv2.waitKey(1) == ord('r'):
                alpha = 1
                beta = 12
                denoising = 10

            if cv2.waitKey(1) == ord('7'):
                alpha = alpha + 1

            if cv2.waitKey(1) == ord('8'):
                alpha = alpha - 1

            if cv2.waitKey(1) == ord('4'):
                beta = beta + 1

            if cv2.waitKey(1) == ord('5'):
                beta = beta - 1

            if cv2.waitKey(1) == ord('+'):
                denoising = denoising + 1

            if cv2.waitKey(1) == ord('-'):
                denoising = denoising - 1

            if cv2.waitKey(1) == ord('q'):
                break

    #MAIN FRAME PRETO E BRANCO COM PRINT
    if cv2.waitKey(1) == ord('p'):
        while True:
            timer = time.time() - start
            conectado, frame = video.read()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame = cv2.addWeighted(frame, alpha, np.zeros(frame.shape, frame.dtype), 0, beta)
            print_info(frame)
            cv2.imshow('frame', frame)

            if cv2.waitKey(1) == ord('s'):
                p_cont_save = p_cont_save + 1
                cv2.imwrite('p_pic_pict' + str(p_cont_save) + '.jpg', frame)

            if cv2.waitKey(1) == ord('r'):
                alpha = 1
                beta = 12
                denoising = 10

            if cv2.waitKey(1) == ord('7'):
                alpha = alpha + 1

            if cv2.waitKey(1) == ord('8'):
                alpha = alpha - 1

            if cv2.waitKey(1) == ord('4'):
                beta = beta + 1

            if cv2.waitKey(1) == ord('5'):
                beta = beta - 1

            # MAIN FRAME PRETO E BRANCO SEM PRINT
            if cv2.waitKey(1) == ord('l'):
                while True:
                    conectado, frame = video.read()
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    frame = cv2.addWeighted(frame, alpha, np.zeros(frame.shape, frame.dtype), 0, beta)
                    cv2.imshow('frame', frame)

                    if cv2.waitKey(1) == ord('s'):
                        lp_cont_save = lp_cont_save + 1
                        cv2.imwrite('lp_pic_pict' + str(lp_cont_save) + '.jpg', frame)

                    if cv2.waitKey(1) == ord('r'):
                        alpha = 1
                        beta = 12
                        denoising = 10

                    if cv2.waitKey(1) == ord('7'):
                        alpha = alpha + 1

                    if cv2.waitKey(1) == ord('8'):
                        alpha = alpha - 1

                    if cv2.waitKey(1) == ord('4'):
                        beta = beta + 1

                    if cv2.waitKey(1) == ord('5'):
                        beta = beta - 1

                    # MAIN FRAME PRETO E BRANCO SEM PRINT COM DENOISING
                    if cv2.waitKey(1) == ord('n'):
                        denoising = 10
                        while True:
                            conectado, frame = video.read()
                            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                            frame = cv2.fastNlMeansDenoising(frame, None, denoising, 3, 9)
                            frame = cv2.addWeighted(frame, alpha, np.zeros(frame.shape, frame.dtype), 0, beta)

                            cv2.imshow('frame', frame)

                            if cv2.waitKey(1) == ord('s'):
                                nlp_cont_save = nlp_cont_save + 1
                                cv2.imwrite('nlp_pic_pict' + str(nlp_cont_save) + '.jpg', frame)

                            if cv2.waitKey(1) == ord('r'):
                                alpha = 1
                                beta = 12
                                denoising = 10

                            if cv2.waitKey(1) == ord('7'):
                                alpha = alpha + 1

                            if cv2.waitKey(1) == ord('8'):
                                alpha = alpha - 1

                            if cv2.waitKey(1) == ord('4'):
                                beta = beta + 1

                            if cv2.waitKey(1) == ord('5'):
                                beta = beta - 1

                            if cv2.waitKey(1) == ord('+'):
                                denoising = denoising + 1

                            if cv2.waitKey(1) == ord('-'):
                                denoising = denoising - 1

                            if cv2.waitKey(1) == ord('q'):
                                break

                    if cv2.waitKey(1) == ord('q'):
                        break

            # MAIN FRAME PRETO E BRANCO COM PRINT E DENOISING
            if cv2.waitKey(1) == ord('n'):
                denoising = 10
                while True:
                    timer = time.time() - start
                    conectado, frame = video.read()
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    frame = cv2.fastNlMeansDenoising(frame, None, denoising, 3, 9)
                    frame = cv2.addWeighted(frame, alpha, np.zeros(frame.shape, frame.dtype), 0, beta)
                    print_info(frame)
                    cv2.putText(frame, 'Denoising: ' + str(denoising), (0, 40), font, 0.6, (0, 255, 255), 2)

                    cv2.imshow('frame', frame)

                    if cv2.waitKey(1) == ord('s'):
                        np_cont_save = np_cont_save + 1
                        cv2.imwrite('np_pic_pict' + str(np_cont_save) + '.jpg', frame)

                    if cv2.waitKey(1) == ord('r'):
                        alpha = 1
                        beta = 12
                        denoising = 10

                    if cv2.waitKey(1) == ord('7'):
                        alpha = alpha + 1

                    if cv2.waitKey(1) == ord('8'):
                        alpha = alpha - 1

                    if cv2.waitKey(1) == ord('4'):
                        beta = beta + 1

                    if cv2.waitKey(1) == ord('5'):
                        beta = beta - 1

                    if cv2.waitKey(1) == ord('+'):
                        denoising = denoising + 1

                    if cv2.waitKey(1) == ord('-'):
                        denoising = denoising - 1

                    if cv2.waitKey(1) == ord('q'):
                        break

            if cv2.waitKey(1) == ord('q'):
                break

    if cv2.waitKey(1) == ord('q'):
        break

#LIBERAÇÃO DE MEMORIA E FINALIZAÇÃO DO PROGRAMA:
video.release()
cv2.destroyAllWindows()
