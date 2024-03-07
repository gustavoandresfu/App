# MIT License
# 
# Copyright (c) 2024 Gustavo Futo
# 
# Se concede permiso, de forma gratuita, a cualquier persona que obtenga una copia
# de este software y de los archivos de documentación asociados (el "Software"), para
# tratar el Software sin restricciones, incluyendo sin limitación los derechos
# de uso, copia, modificación, fusión, publicación, distribución, sublicencia
# y/o venta de copias del Software, y para permitir a las personas a las que se les
# proporcione el Software a hacer lo mismo, sujeto a las siguientes condiciones:
# 
# El aviso de copyright anterior y este aviso de permisos se incluirán en
# todas las copias o partes sustanciales del Software.
# 
# EL SOFTWARE SE PROPORCIONA "TAL CUAL", SIN GARANTÍA DE NINGÚN TIPO, EXPRESA O
# IMPLÍCITA, INCLUYENDO PERO NO LIMITADO A LAS GARANTÍAS DE COMERCIABILIDAD,
# APTITUD PARA UN PROPÓSITO PARTICULAR Y NO INFRACCIÓN. EN NINGÚN CASO LOS
# TITULARES DEL COPYRIGHT O LOS AUTORES SERÁN RESPONSABLES DE NINGÚN RECLAMO,
# DAÑO U OTRA RESPONSABILIDAD, YA SEA EN UNA ACCIÓN DE CONTRATO, AGRAVIO O CUALQUIER
# OTRA FORMA, DERIVADA DE, FUERA DE O EN CONEXIÓN CON EL SOFTWARE O EL USO U
# OTRAS NEGOCIACIONES EN EL SOFTWARE.

import tkinter as tk
from tkinter import messagebox
import cv2
from PIL import Image, ImageTk
import mediapipe as mp
import time
import pygame
import threading
from controladores.leccion_controlador import Leccion_controlador
from controladores.progreso_controlador import Progreso_controlador

class Clase_vista:

    def __init__(self,obj_clase, usuario):

        #interfaz grafica
        root = tk.Toplevel()
        self.nota_en_proceso = False
        self.root = root
        self.root.title("CLASE "+ obj_clase.nombre)
        self.root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))  
        self.root.resizable(True, True)
        self.root.state("zoomed")
        self.root.iconbitmap("recursos/musicar.ico")
        self.root.columnconfigure(0, weight=1)  
        self.root.columnconfigure(1, weight=5)  
        self.root.rowconfigure(0, weight=1)
        frame1 = tk.Frame(self.root, bg="#EAEAEA")
        frame1.grid(row=0, column=0, sticky="nsew")
        frame2 = tk.Frame(self.root, bg="#EAEAEA")
        frame2.grid(row=0, column=1, sticky="nsew")
        frame1.rowconfigure(0, weight=1)
        frame1.rowconfigure(1, weight=1)
        frame1.rowconfigure(2, weight=1)
        subframe3 = tk.Frame(frame1, bg="#DADADA")
        subframe3.grid(row=2, column=0, sticky="nsew")
        clase_num = obj_clase.orden
        self.btn_leccion1 = tk.Button(subframe3, text="Lección 1",command=lambda: self.mostrar_leccion1(frame1,frame2, clase_num,1))
        self.btn_leccion1.pack(padx=5, pady=5)
        self.btn_leccion2 = tk.Button(subframe3, text="Lección 2",command=lambda: self.mostrar_leccion2(frame1,frame2,clase_num,2))
        self.btn_leccion2.pack(padx=5, pady=5)
        self.btn_leccion3 = tk.Button(subframe3, text="Lección 3", command=lambda: self.mostrar_leccion3(usuario,frame1,frame2,clase_num,3))
        self.btn_leccion3.pack(padx=5, pady=5)
        self.mostrar_leccion1(frame1, frame2,clase_num,1)
        #bandera para detener las ejecuciones
        self.flag = False 
        root.protocol("WM_DELETE_WINDOW", lambda: self.cerrar()) #toma el cierre de la ventana x
        self.root.mainloop()
       



    def mostrar_leccion1(self, frame1, frame2,clase_num,leccion_num):
        
        try:
            leccion_plantilla = Leccion_controlador()
            #nos traemos los datos de la leccion
            leccion = leccion_plantilla.buscar_leccion(clase_num,leccion_num)
        except Exception as e:
            messagebox.showerror("Error", f"Hubo un problema: {e}")   

        subframe1 = tk.Frame(frame1, bg="#DADADA")
        subframe1.grid(row=0, column=0, sticky="nsew")
        label1 = tk.Label(subframe1, text=leccion.mensaje.texto,  wraplength=100, anchor="w")
        label1.pack(padx=5, pady=5)
        subframe2 = tk.Frame(frame1, bg="#DADADA")
        subframe2.grid(row=1, column=0, sticky="nsew")
        label2 = tk.Label(subframe2, text="TOCA LAS NOTAS CON EL DEDO INDICE DERECHO Y ESCUCHA CON ATENCIÓN",  
                          wraplength=100, anchor="w")
        label2.pack(padx=5, pady=5)

        cap = cv2.VideoCapture(0)  #camara captura
        pygame.init()
        pygame.mixer.init() 

        label_img = tk.Label(frame2)
        label_img.grid(row=0, column=0,columnspan=2)

        if cap.isOpened():
            mp_hands = mp.solutions.hands
            hands = mp_hands.Hands()


            def tocar_nota(nota_origen,duracion):
                color_marca = '(0,0,255)'
                color_original = nota_origen.color
                nota_origen.color = color_marca
                global nota_en_proceso
                if self.nota_en_proceso:
                     return 
                sound = pygame.mixer.Sound("recursos/notas/"+str(nota_origen.origen))

                def play_and_wait():
                    self.nota_en_proceso = True
                    sound.play()
                    pygame.time.wait(duracion)
                    sound.play(loops=-1)
                    sound.stop()
                    nota_origen.color = color_original
                    self.nota_en_proceso = False
                thread = threading.Thread(target=play_and_wait)
                thread.start()

            #cargamos la imagen de la camara 
            def mostrar_frame():
                _, frame = cap.read()
                frame = cv2.flip(frame, 1)
                try:
                    frame = cv2.resize(frame, (frame2.winfo_width(), frame2.winfo_height()))
                    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    resultado = hands.process(cv2image)
                    if resultado.multi_hand_landmarks:
                        for hand_landmarks in resultado.multi_hand_landmarks:
                           x_index = int(hand_landmarks.landmark[8].x * frame.shape[1])
                           y_index = int(hand_landmarks.landmark[8].y * frame.shape[0])

                           for nota_info in leccion.plantilla_detalle:
                                x_circulo = nota_info.posicion_x
                                y_circulo = nota_info.posicion_y
                                color_string = nota_info.color.strip('()') 
                                color_values = [int(x) for x in color_string.split(',')] 
                                color_tuple = tuple(color_values)
                                circulo_color = color_tuple
                                distancia_al_circulo = ((x_index - x_circulo)**2 + (y_index - y_circulo)**2)**0.5
                                if distancia_al_circulo < 20:
                                    duracion = 1000 
                                    tocar_nota(nota_info, duracion)

                    for nota_info in leccion.plantilla_detalle:
                        x_circulo = nota_info.posicion_x
                        y_circulo = nota_info.posicion_y
                        nota = nota_info.nota
                        color_string = nota_info.color.strip('()') 
                        color_values = [int(x) for x in color_string.split(',')]  
                        color_tuple = tuple(color_values)
                        circulo_color = color_tuple
                        cv2.circle(frame, (x_circulo, y_circulo), 20, circulo_color, -1)
                        cv2.putText(frame, str(nota), (x_circulo - 10, y_circulo + 35), cv2.FONT_HERSHEY_SIMPLEX, 0.5, circulo_color, 2)
                    img = Image.fromarray(frame)
                    imgtk = ImageTk.PhotoImage(image=img)
                    label_img.imgtk = imgtk
                    label_img.configure(image=imgtk)
                    label_img.after(10, mostrar_frame) #se refresca la imagen cada 10 ms
                except Exception as e:
                    pass    
          
            mostrar_frame() 
            
        else:
            messagebox.showinfo("Message", "Error al abrir la cámara")  

    def mostrar_leccion2(self,frame1, frame2, clase_num,leccion_num):
 
        try:
            leccion_plantilla = Leccion_controlador()
            #nos traemos los datos de la leccion
            leccion = leccion_plantilla.buscar_leccion(clase_num,leccion_num)
        except Exception as e:
            messagebox.showerror("Error", f"Hubo un problema: {e}")  

        self.control_btn(False)
        label_img = tk.Label(frame2)
        label_img.grid(row=0, column=0,columnspan=2)

        subframe1 = tk.Frame(frame1, bg="#DADADA")
        subframe1.grid(row=0, column=0, sticky="nsew")
        label1 = tk.Label(subframe1, text=leccion.mensaje.texto,  wraplength=100, anchor="w")
        label1.pack(padx=5, pady=5)
        subframe2 = tk.Frame(frame1, bg="#DADADA")
        subframe2.grid(row=1, column=0, sticky="nsew")
        label2 = tk.Label(subframe2, text="ESCUCHA CON ATENCIÓN Y LUEGO INTENTA REPETIR LA MELODÍA",  
                          wraplength=100, anchor="w")
        label2.pack(padx=5, pady=5)
       
        cap = cv2.VideoCapture(0) #capturamos la camara            
        

        pygame.init()
        pygame.mixer.init() 

        if cap.isOpened():
            mp_hands = mp.solutions.hands
            hands = mp_hands.Hands()

            def tocar_nota(nota_origen,duracion):
                color_marca = '(0,0,255)'
                color_original = nota_origen.color
                nota_origen.color = color_marca

                global nota_en_proceso

                if self.nota_en_proceso:
                     return 
                
                sound = pygame.mixer.Sound("recursos/notas/"+str(nota_origen.origen))

                def play_and_wait():
                    self.nota_en_proceso = True
                    sound.play()
                    pygame.time.wait(duracion)
                    sound.stop()
                    nota_origen.color = color_original
                    self.nota_en_proceso = False
                thread = threading.Thread(target=play_and_wait)
                thread.start()

            def tocar_secuencia(sec_nota,sec_duracion):
                sound = pygame.mixer.Sound("recursos/notas/"+str(sec_nota))
                def play_and_wait():
                    sound.play()
                    pygame.time.wait(sec_duracion)
                    sound.stop()
                play_and_wait()

            def reproducir_secuencia():
                    for secuencia in leccion.secuencia_detalle:
                        if not self.flag:  
                            tocar_secuencia(str(secuencia.nota.origen), int(secuencia.tiempo.valor * 1000))  
                    self.control_btn(True)             
            
            #cargamos la imagen de la camara 
            def mostrar_frame():
                _, frame = cap.read()
                frame = cv2.flip(frame, 1)
                try:
                    frame = cv2.resize(frame, (frame2.winfo_width(), frame2.winfo_height()))
                    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    resultado = hands.process(cv2image)
                    if resultado.multi_hand_landmarks:
                        for hand_landmarks in resultado.multi_hand_landmarks:
                           x_index = int(hand_landmarks.landmark[8].x * frame.shape[1])
                           y_index = int(hand_landmarks.landmark[8].y * frame.shape[0])

                           for nota_info in leccion.plantilla_detalle:
                                x_circulo = nota_info.posicion_x
                                y_circulo = nota_info.posicion_y
                                color_string = nota_info.color.strip('()')  # Eliminar los paréntesis
                                color_values = [int(x) for x in color_string.split(',')]  # Dividir y convertir a enteros
                                color_tuple = tuple(color_values)
                                circulo_color = color_tuple
                                distancia_al_circulo = ((x_index - x_circulo)**2 + (y_index - y_circulo)**2)**0.5
                                if distancia_al_circulo < 20:
                                    duracion = 1000  
                                    tocar_nota(nota_info, duracion)
                    for nota_info in leccion.plantilla_detalle:
                        x_circulo = nota_info.posicion_x
                        y_circulo = nota_info.posicion_y
                        color_string = nota_info.color.strip('()') 
                        color_values = [int(x) for x in color_string.split(',')]  
                        color_tuple = tuple(color_values)
                        circulo_color = color_tuple
                        cv2.circle(frame, (x_circulo, y_circulo), 20, circulo_color, -1)
                        cv2.putText(frame, str(nota_info.nota), (x_circulo - 10, y_circulo + 35), cv2.FONT_HERSHEY_SIMPLEX, 0.5, circulo_color, 2)

                    img = Image.fromarray(frame)
                    imgtk = ImageTk.PhotoImage(image=img)
                    label_img.imgtk = imgtk
                    label_img.configure(image=imgtk)
                    if not self.flag:
                     label_img.after(10, mostrar_frame) #refrescamos cada 10ms                 
                                    
                except Exception as e:
                    pass




            thread = threading.Thread(target=mostrar_frame)
            thread.start()    
            thread1 = threading.Thread(target=reproducir_secuencia)
            thread1.start()

        else:
            messagebox.showinfo("Message", "Error al abrir la cámara")              
     
    def mostrar_leccion3(self,usuario, frame1,frame2,clase_num,leccion_num):

        try:
            leccion_plantilla = Leccion_controlador()
            #nos traemos los datos de la leccion
            leccion = leccion_plantilla.buscar_leccion(clase_num,leccion_num)
            #iniciamos el progreso
            progreso = Progreso_controlador()
            

        except Exception as e:
            messagebox.showerror("Error", f"Hubo un problema: {e}")  




        self.control_btn(False)

        secuencia = [] #esta es la secuencia en ejecucion

        for secuencias in leccion.secuencia_detalle:
            nota = secuencias.nota.nombre_latino
            duracion = secuencias.tiempo.valor * 1000
            t_sec = (nota,duracion)
            secuencia.append(t_sec)
    

        subframe1 = tk.Frame(frame1, bg="#DADADA")
        subframe1.grid(row=0, column=0, sticky="nsew")
        label1 = tk.Label(subframe1, text=leccion.mensaje.texto,  wraplength=100, anchor="w")
        label1.pack(padx=5, pady=5)

        subframe2 = tk.Frame(frame1, bg="#DADADA")
        subframe2.grid(row=1, column=0, sticky="nsew")
        label2 = tk.Label(subframe2, text="ESCUCHA CON ATENCIÓN Y LUEGO INTENTA REPETIR LA MELODÍA",  
                          wraplength=100, anchor="w")
        label2.pack(padx=5, pady=5)

        cap = cv2.VideoCapture(0) #captura de camara
        
        label_img = tk.Label(frame2)
        label_img.grid(row=0, column=0,columnspan=2)


        pygame.init()
        pygame.mixer.init() 

        if cap.isOpened():
            mp_hands = mp.solutions.hands
            hands = mp_hands.Hands()


            def tocar_nota(nota_origen):

                color_marca = '(0,0,255)'
                color_original = nota_origen.color
                nota_origen.color = color_marca
                global nota_en_proceso

                if self.nota_en_proceso:
                     return 
                
                sound = pygame.mixer.Sound("recursos/notas/"+str(nota_origen.origen))

                def play_and_wait():
                    self.nota_en_proceso = True
                    sound.play(loops=-1)
                    pygame.time.wait(1000)
                    sound.stop()
                    self.nota_en_proceso = False
                    nota_origen.color = color_original
                    if secuencia: 
                        if nota_origen.nota == secuencia[0][0]:
                                  secuencia.pop(0)  
                        else:
                            messagebox.showinfo("Mensaje", " Intentalo de nuevo")
                            secuencia.clear() 
                            for secuencias in leccion.secuencia_detalle:
                                nota = secuencias.nota.nombre_latino
                                duracion = secuencias.tiempo.valor * 1000
                                t_sec = (nota,duracion)
                                secuencia.append(t_sec)

                    if not secuencia:
                        progreso.guardar(usuario,clase_num,leccion_num)
                        messagebox.showinfo("Mensaje", "Excelente has logrado completar con éxito la clase")
                        
                thread2 = threading.Thread(target=play_and_wait)
                thread2.start()

            def tocar_secuencia(sec_nota,sec_duracion):
                sound = pygame.mixer.Sound("recursos/notas/"+str(sec_nota))
                def play_and_wait():
                    sound.play()
                    pygame.time.wait(sec_duracion)
                    sound.stop()
                play_and_wait()
            

            def reproducir_secuencia():
                for secuencia in leccion.secuencia_detalle:
                    if not self.flag:  
                        tocar_secuencia(str(secuencia.nota.origen), int(secuencia.tiempo.valor * 1000))  
                self.control_btn(True)

            #cargamos la imagen de la camara 
            def mostrar_frame():
                _, frame = cap.read()
                frame = cv2.flip(frame, 1)

                try:
                    frame = cv2.resize(frame, (frame2.winfo_width(), frame2.winfo_height()))
                    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    resultado = hands.process(cv2image)
                                    
                    if resultado.multi_hand_landmarks:
                        for hand_landmarks in resultado.multi_hand_landmarks:
                           x_index = int(hand_landmarks.landmark[8].x * frame.shape[1])
                           y_index = int(hand_landmarks.landmark[8].y * frame.shape[0])

                           for nota_info in leccion.plantilla_detalle:
                                x_circulo = nota_info.posicion_x
                                y_circulo = nota_info.posicion_y
                                color_string = nota_info.color.strip('()')  
                                color_values = [int(x) for x in color_string.split(',')] 
                                color_tuple = tuple(color_values)
                                circulo_color = color_tuple
                                distancia_al_circulo = ((x_index - x_circulo)**2 + (y_index - y_circulo)**2)**0.5
                                if distancia_al_circulo < 20:
                                    tocar_nota(nota_info)


                    for nota_info in leccion.plantilla_detalle:
                        x_circulo = nota_info.posicion_x
                        y_circulo = nota_info.posicion_y
                        color_string = nota_info.color.strip('()') 
                        color_values = [int(x) for x in color_string.split(',')]  
                        color_tuple = tuple(color_values)
                        circulo_color = color_tuple
                        cv2.circle(frame, (x_circulo, y_circulo), 20, circulo_color, -1)
                        cv2.putText(frame, str(nota_info.nota), (x_circulo - 10, y_circulo + 35), cv2.FONT_HERSHEY_SIMPLEX, 0.5, circulo_color, 2)

                    img = Image.fromarray(frame)
                    imgtk = ImageTk.PhotoImage(image=img)
                    label_img.imgtk = imgtk
                    label_img.configure(image=imgtk)
                    if not self.flag:
                         label_img.after(10, mostrar_frame) #se refresca cada 10ms
                    

                except Exception as e:
                    pass    



            thread = threading.Thread(target=mostrar_frame)
            thread.start()    
            thread1 = threading.Thread(target=reproducir_secuencia)
            thread1.start()


        else:
            messagebox.showinfo("Message", "Error al abrir la cámara")              

    def cerrar(self):
        self.flag = True
        self.root.destroy()

    def control_btn(self, activa):
        if activa:
            self.btn_leccion1.config(state=tk.NORMAL)
            self.btn_leccion2.config(state=tk.NORMAL)
            self.btn_leccion3.config(state=tk.NORMAL)  
        else:
            self.btn_leccion1.config(state=tk.DISABLED)
            self.btn_leccion2.config(state=tk.DISABLED)
            self.btn_leccion3.config(state=tk.DISABLED) 


 




