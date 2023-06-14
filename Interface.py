# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 15:21:58 2019

@author: Frank, Alex y Susana 
"""
import Tkinter as tk
import serial
import struct
import time
import os
import binascii



# Configuracion de DOBOT
cmd_str_10 = [ 0 for i in range(10) ]
cmd_str_42 = [ '\x00' for i in range(42) ]

ser = serial.Serial(#serial connection
    port='COM16',
    baudrate=9600,
    parity=serial.PARITY_NONE,#serial.PARITY_ODD,
    stopbits=serial.STOPBITS_ONE,#serial.STOPBITS_TWO,
    bytesize=serial.EIGHTBITS#,#serial.SEVENBITS
    #timeout=None

)

ser.isOpen()

# Open Serial port will reset dobot, wait seconds
print "Wait 3 seconds..."
time.sleep(3) 

def dobot_cmd_send( cmd_str_10 ):
    global cmd_str_42
    cmd_str_42 = [ '\x00' for i in range(42) ]
    cmd_str_42[0]  = '\xA5'
    cmd_str_42[41] = '\x5A'
    for i in range(10):
        str4 = struct.pack( '<f', float(cmd_str_10[i]) )
        cmd_str_42[4*i+1] = str4[0]
        cmd_str_42[4*i+2] = str4[1]
        cmd_str_42[4*i+3] = str4[2]
        cmd_str_42[4*i+4] = str4[3]
    cmd_str = ''.join( cmd_str_42 )
    print binascii.b2a_hex( cmd_str )
    time.sleep(1)
    ser.write( cmd_str )

#state 3
def dobot_cmd_send_3( x = 265, y = 0, z = -30 ,r = 0,ig=0):
    global cmd_str_10
    cmd_str_10 = [ 0 for i in range(10) ]
    cmd_str_10[0] = 3
    cmd_str_10[2] = x
    cmd_str_10[3] = y
    cmd_str_10[4] = z
    cmd_str_10[5] = r
    cmd_str_10[6] = ig
    cmd_str_10[7] = 1 # MOVL
    dobot_cmd_send( cmd_str_10 )

def dobot_cmd_send_91():
    global cmd_str_10
    cmd_str_10 = [ 0 for i in range(10) ]
    cmd_str_10[0] = 9
    cmd_str_10[1] = 1
    cmd_str_10[2] = 200 #JointVel
    cmd_str_10[3] = 200 #JointAcc
    cmd_str_10[4] = 200 #ServoVel
    cmd_str_10[5] = 200 #ServoAcc
    cmd_str_10[6] = 800 #LinearVel
    cmd_str_10[7] = 1000 #LinearAcc
    dobot_cmd_send( cmd_str_10 )

def dobot_cmd_send_9():#configuracion de pump
    global cmd_str_10
    cmd_str_10 = [ 0 for i in range(10) ]
    cmd_str_10[0] = 9
    cmd_str_10[1] = 4
    cmd_str_10[2] = 0 #param1 0:suction;1:Gripper;2:laser
    dobot_cmd_send( cmd_str_10 )



def dobot_cmd_send_10( VelRat = 100, AccRat = 100 ):
    global cmd_str_10
    cmd_str_10 = [ 0 for i in range(10) ]
    cmd_str_10[0] = 10
    cmd_str_10[2] = VelRat
    cmd_str_10[3] = AccRat
    dobot_cmd_send( cmd_str_10 )
    
def mov_posicion_uno():
    time.sleep(1.5) 
    ser.close()
    ser.open()
    dobot_cmd_send_3( 190, 0, 0 ,0,0)
    time.sleep(0.5) 
    dobot_cmd_send_3( 190, -30, -70 , -45,0)
    time.sleep( 0.5 )
    dobot_cmd_send_3( 190, -30, -70 , -45,1)
    time.sleep( 0.5 )
    dobot_cmd_send_3( 190, -30, 0 , -45,1)
    time.sleep( 0.5 )
    dobot_cmd_send_3( 190, -30, 0 ,-45,1)
    time.sleep(0.5)    

def mov_posicion_dos():
    time.sleep(1.5) 
    ser.close()
    ser.open()
    dobot_cmd_send_3( 190, 0, 0 ,0,0)
    time.sleep(0.5) 
    dobot_cmd_send_3( 190, 0, -70 , -45,0)
    time.sleep( 0.5 )
    dobot_cmd_send_3( 190, 0, -70 , -45,1)
    time.sleep( 0.5 )
    dobot_cmd_send_3( 190, 0, 0 , -45,1)
    time.sleep( 0.5 )
    
def mov_posicion_tres():
    time.sleep(1.5) 
    ser.close()
    ser.open()
    dobot_cmd_send_3( 190, 0, 0 ,0,0)
    time.sleep(0.5) 
    dobot_cmd_send_3( 195, 35, -70 , -45,0)
    time.sleep( 0.5 )
    dobot_cmd_send_3( 195, 35, -70 , -45,1)
    time.sleep( 0.5 )
    dobot_cmd_send_3( 195, 35, 0 , -45,1)
    time.sleep( 0.5 )
    
def mov_posicion_cuatro():    
    dobot_cmd_send_3( 190, 0, 0 ,-45,1)
    time.sleep(0.5) 
    dobot_cmd_send_3( 0, -240, -70 , -45,1)
    time.sleep( 0.5 )
    dobot_cmd_send_3( 0, -240, -70 , -45,0)
    time.sleep( 0.5 )
    dobot_cmd_send_3( 190, 0, 0 ,-45,0)
    time.sleep(2) 
    ser.close()
    ser.open()
    
def mov_posicion_cinco():
    dobot_cmd_send_3( 190, 0, 0 ,-45,1)
    time.sleep(0.5) 
    dobot_cmd_send_3( 30, -240, -70 , -45,1)
    time.sleep( 0.5 )
    dobot_cmd_send_3( 30, -240, -70 , -45,0)
    time.sleep( 0.5 )
    dobot_cmd_send_3( 190, 0, 0 ,-45,0)
    time.sleep(0.5) 
    ser.close()
    
def mov_posicion_seis():
    dobot_cmd_send_3( 190, 0, 0 ,-45,1)
    time.sleep(0.5) 
    dobot_cmd_send_3( -35, -240, 0 , -45,1)
    time.sleep( 0.5 )
    dobot_cmd_send_3( -35, -240, -70 , -45,0)
    time.sleep( 0.5 )
    dobot_cmd_send_3( -35, -240, 0 , -45,0)
    time.sleep( 0.5 )
    dobot_cmd_send_3( 190, 0, 0 ,-45,0)
    time.sleep(0.5) 
    ser.close()
    
def mov_posicion_siete():
    dobot_cmd_send_3( 190, 0, 0 ,-45,1)
    time.sleep(0.5) 
    dobot_cmd_send_3( 0, -240, -40 , -45,1)
    time.sleep( 0.5 )
    dobot_cmd_send_3( 0, -240, -40 , -45,0)
    time.sleep( 0.5 )
    dobot_cmd_send_3( 0, -240, 0 , -45,0)
    time.sleep( 0.5 )
    dobot_cmd_send_3( 190, 0, 0 ,-45,0)
    time.sleep(2) 
    ser.close()
    ser.open()
    
def mov_posicion_ocho():  
    dobot_cmd_send_3( 190, 0, 0 ,-45,1)
    time.sleep(0.5) 
    dobot_cmd_send_3( 0, -240, -7 , -45,1)
    time.sleep( 0.5 )
    dobot_cmd_send_3( 0, -240, -7 , -45,0)
    time.sleep( 0.5 )
    dobot_cmd_send_3( 0, -240, 0 , -45,0)
    time.sleep( 0.5 )
    dobot_cmd_send_3( 190, 0, 0 ,-45,0)
    time.sleep(0.5) 
    ser.close()
    
def mov_posicion_bloque(pos = 0):
        
    if (pos == 1):
        mov_posicion_uno()
    elif(pos== 2):
        mov_posicion_dos()
    else:
        mov_posicion_tres()

def inicializar():
    print ("Dobot Test Begin")
    #b='hello'.encode('utf-8')
    time.sleep(1.8) 
    #ser.write(b)
    dobot_cmd_send_9() #config
    time.sleep(0.5)
    dobot_cmd_send_91() #config
    time.sleep(0.5)
    dobot_cmd_send_10() #config
    time.sleep(0.5) 

window = tk.Tk()
window.title("Robotic arm in PDI")

## Label
lbl = tk.Label(window, text="Hello",font=("Arial Bold", 50))
lbl.grid(column=0, row=0)

# Ancho y alto de ventana (Ancho x Alto)
window.geometry('600x300')

# Boton
global num_count1 
num_count1 = 0

global num_count2 
num_count2 = 0

global num_count3 
num_count3 = 0

global num_count4 
num_count4 = 0

global num_count5 
num_count5 = 0

global Estado
Estado = 0

global arreglo_color
archivo = open("colores.txt","r")
A = archivo.read()
arreglo_color = [2-int(A[0]),2-int(A[1]),2-int(A[2])]
print arreglo_color
archivo.close()

def clicked1():
    
    global num_count1 #Incrementando contador
    global num_count2
    global num_count3
    global num_count4
    global num_count5
    
    num_count1 += 1
    
    
    if(num_count1==1 and num_count1 != num_count2 and num_count1 != num_count3 and num_count1 !=num_count4 and num_count1 != num_count5):
        btn1.configure(bg="red")
    else:
        if(num_count1==1): 
            num_count1+= 1
    
    if(num_count1==2 and num_count1 != num_count2 and num_count1 != num_count3 and num_count1 !=num_count4 and num_count1 != num_count5):
        btn1.configure(bg="green")
    else:
        if(num_count1==2):
            num_count1+= 1
            
    if(num_count1==3 and num_count1 != num_count2 and num_count1 != num_count3 and num_count1 !=num_count4 and num_count1 != num_count5):
        btn1.configure(bg="blue")
    else:
        if(num_count1==3):
            num_count1+= 1
            
    if(num_count1>3):
        btn1.configure(bg="white")
        num_count1=0
        print("El valor de num_count1 es: ", num_count1);
    else:
        num_count1 = num_count1
    
    
def clicked2():
    
    global num_count2 #Incrementando contador
    global num_count1
    global num_count3
    global num_count4
    global num_count5
    num_count2 += 1
    
    if(num_count2==1 and num_count2 != num_count1 and num_count2 != num_count3 and num_count2 !=num_count4 and num_count2 != num_count5):
        btn2.configure(bg="red")
    else:
        if(num_count2==1): 
            num_count2+= 1
        
    if(num_count2==2 and num_count2 != num_count1 and num_count2 != num_count3 and num_count2 !=num_count4 and num_count2 != num_count5):
        btn2.configure(bg="green")
    else:
        if(num_count2==2): 
            num_count2+= 1
            
    if(num_count2==3 and num_count2 != num_count1 and num_count2 != num_count3 and num_count2 !=num_count4 and num_count2 != num_count5):
        btn2.configure(bg="blue")
    else:
        if(num_count2==3): 
            num_count2+= 1
    
    if(num_count2>3):
        btn2.configure(bg="white")
        num_count2=0
        print("El valor de num_count2 es: ", num_count2);
    else:
        num_count2 = num_count2

def clicked3():
    
    global num_count3 #Incrementando contador
    global num_count1
    global num_count2
    global num_count4
    global num_count5
    num_count3 += 1
    
    if(num_count3==1 and num_count3 != num_count1 and num_count3 != num_count2 and num_count3 !=num_count4 and num_count3 != num_count5):
        btn3.configure(bg="red")
    else:
        if(num_count3==1): 
            num_count3+= 1
            
    if(num_count3==2 and num_count3 != num_count1 and num_count3 != num_count2 and num_count3 !=num_count4 and num_count3 != num_count5):
        btn3.configure(bg="green")
    else:
        if(num_count3==2): 
            num_count3+= 1
    if(num_count3==3 and num_count3 != num_count1 and num_count3 != num_count2 and num_count3 !=num_count4 and num_count3 != num_count5):
        btn3.configure(bg="blue")
    else:
        if(num_count3==3): 
            num_count3+= 1
            
    if(num_count3>3):
        btn3.configure(bg="white")
        num_count3=0
        print("El valor de num_count3 es: ", num_count3);
    else:
        num_count3 = num_count3
        
        
def clicked4():
    
    global num_count4 #Incrementando contador
    global num_count1
    global num_count2
    global num_count3
    global num_count5
    num_count4 += 1
    
    if(num_count4==1 and num_count4 != num_count1 and num_count4 != num_count2 and num_count4 !=num_count3 and num_count4 != num_count5):
        btn4.configure(bg="red")
    else:
        if(num_count4==1): 
            num_count4+= 1
            
    if(num_count4==2 and num_count4 != num_count1 and num_count4 != num_count2 and num_count4 !=num_count3 and num_count4 != num_count5):
        btn4.configure(bg="green")
    else:
        if(num_count4==2): 
            num_count4+= 1
    if(num_count4==3 and num_count4 != num_count1 and num_count4 != num_count2 and num_count4 !=num_count3 and num_count4 != num_count5):
        btn4.configure(bg="blue")
    else:
        if(num_count4==3): 
            num_count4+= 1
            
    if(num_count4>3):
        btn4.configure(bg="white")
        num_count4=0
        print("El valor de num_count4 es: ", num_count4);
    else:
        num_count4 = num_count4

def clicked5():
    
    global num_count5 #Incrementando contador
    global num_count1
    global num_count2
    global num_count3
    global num_count4
    num_count5 += 1
    
    if(num_count5==1 and num_count5 != num_count1 and num_count5 != num_count2 and num_count5 !=num_count3 and num_count5 != num_count4):
        btn5.configure(bg="red")
    else:
        if(num_count5==1): 
            num_count5+= 1
    if(num_count5==2 and num_count5 != num_count1 and num_count5 != num_count2 and num_count5 !=num_count3 and num_count5 != num_count4):
        btn5.configure(bg="green")
    else:
        if(num_count5==2): 
            num_count5+= 1
            
    if(num_count5==3 and num_count5 != num_count1 and num_count5 != num_count2 and num_count5 !=num_count3 and num_count5 != num_count4):
        btn5.configure(bg="blue")
    else:
        if(num_count5==3): 
            num_count5+= 1
            
    if(num_count5>3):
        btn5.configure(bg="white")
        num_count5=0
        print("El valor de num_count5 es: ", num_count5);
    else:
        num_count5 = num_count5
        
def Estado_5():
    global num_count4
    global arreglo_color
    posicion = 0 
    if(num_count4!=0):
        posicion = arreglo_color[num_count4-1] + 1
        mov_posicion_bloque(posicion)
        mov_posicion_seis()
    ser.close()
    
def Estado_4():
    global num_count5
    global arreglo_color
    posicion = 0 
    if(num_count5!=0):
        posicion = arreglo_color[num_count5-1] + 1
        mov_posicion_bloque(posicion)
        mov_posicion_cinco()
    Estado_5()
        
def Estado_3():
    global num_count1
    global arreglo_color
    posicion = 0 
    if(num_count1!=0):
        posicion = arreglo_color[num_count1-1] + 1
        mov_posicion_bloque(posicion)
        mov_posicion_ocho()
    Estado_4()   
        
def Estado_2():
    global num_count2
    global arreglo_color
    posicion = 0 
    if(num_count2!=0):
        posicion = arreglo_color[num_count2-1] + 1
        mov_posicion_bloque(posicion)
        mov_posicion_siete()
    Estado_3()     
    
def Estado_1():
    global num_count3
    global arreglo_color
    posicion = 0 
    if(num_count3!=0):
        posicion = arreglo_color[num_count3-1] + 1
        mov_posicion_bloque(posicion)
        mov_posicion_cuatro()
    Estado_2()
        
def clickEnviar():
    Estado_1()
    
    
            
inicializar()

btn1 = tk.Button(window, text="      ",bg="white", fg="red",command=clicked1)
btn1.grid(column=2, row=1)

btn2 = tk.Button(window, text="      ",bg="white", fg="red",command=clicked2)
btn2.grid(column=2, row=2)

btn3 = tk.Button(window, text="      ",bg="white", fg="red",command=clicked3)
btn3.grid(column=2, row=3)

btn4 = tk.Button(window, text="      ",bg="white", fg="red",command=clicked4)
btn4.grid(column=3, row=3)

btn5 = tk.Button(window, text="      ",bg="white", fg="red",command=clicked5)
btn5.grid(column=1, row=3)

btnEnviar = tk.Button(window, text="Enviar",bg="white", fg="red",command=clickEnviar)
btnEnviar.grid(column=2, row=5)


#Cambiar el color del fondo
window.mainloop()
