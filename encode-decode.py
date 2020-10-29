#importing modules

from tkinter import *
import base64

#initialize window
root = Tk()
root.geometry('1080x720')
root.resizable(10,10)

#title of the window
root.title("Message Encoder & Decoder")



#label

Label(root, text ='ENCODE DECODE', font = 'arial 20 bold').pack()
Label(root, text ='Mini Project For RNSIT', font = 'arial 20 bold').pack(side =BOTTOM)


#define variables

Text = StringVar()
private_key = StringVar()
mode = StringVar()
Result = StringVar()


#######define function#####

#function to encode

def Encode(key,message):
    enc=[]
    for i in range(len(message)):
        print(i,"loop var \n")
        key_c = key[i % len(key)]
        print(key_c,"key new val \n")
        print(ord(message[i]),"converted message index\n")
        print(ord(key_c),"converted key index\n")
        print(chr((ord(message[i]) + ord(key_c)) % 256),"character generated\n")
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
        l=base64.urlsafe_b64encode("".join(enc).encode()).decode()
        print(l,"encoded\n")
    return l

#function to decode

def Decode(key,message):
    dec=[]
    print(message,"message\n")
    message = base64.urlsafe_b64decode(message).decode()
    print(message,"message decoded")
    for i in range(len(message)):
        print("\n",i,"lop var\n")
        key_c = key[i % len(key)]
        print(key_c,"converted key index\n")
        print(ord(message[i]),"converted message\n")
        print(ord(key_c),"converted key\n")
        print(chr((256 + ord(message[i])- ord(key_c)) % 256),"character generated\n")
        dec.append(chr((256 + ord(message[i])- ord(key_c)) % 256))
        
    return "".join(dec)

#function to set mode
def Mode():
    if(mode.get() == 'e'):
        Result.set(Encode(private_key.get(), Text.get()))
    elif(mode.get() == 'd'):
        Result.set(Decode(private_key.get(), Text.get()))
    else:
        Result.set('Invalid Mode')



#Function to exit window
        
def Exit():
    root.destroy()


#Function to reset
def Reset():
    Text.set("")
    private_key.set("")
    mode.set("")
    Result.set("")


#################### Label and Button #############

#Message
Label(root, font= 'arial 24 bold', text='MESSAGE').place(x= 160,y=60)
Entry(root, font = 'arial 20', textvariable = Text, bg = 'ghost white').place(x=490, y = 60)

#key
Label(root, font = 'arial 24 bold', text ='KEY').place(x=160, y = 120)
Entry(root, font = 'arial 20', textvariable = private_key , bg ='ghost white').place(x=490, y = 120)


#mode
Label(root, font = 'arial 18 bold', text ='MODE(e-encode, d-decode)').place(x=160, y = 180)
Entry(root, font = 'arial 20', textvariable = mode , bg= 'ghost white').place(x=490, y = 180)



#result
Entry(root, font = 'arial 20 bold', textvariable = Result, bg ='ghost white').place(x=490, y = 240)

######result button
Button(root, font = 'arial 20 bold', text = 'RESULT'  ,padx =2,bg ='LightBlue' ,command = Mode).place(x=160, y = 240)


#reset button
Button(root, font = 'arial 20 bold' ,text ='RESET' ,width =6, command = Reset,bg = 'LightYellow', padx=2).place(x=240, y = 400)

#exit button
Button(root, font = 'arial 20 bold',text= 'EXIT' , width = 6, command = Exit,bg = 'OrangeRed', padx=2, pady=2).place(x=360, y = 400)
root.mainloop()
