from tkinter import *
from tkinter import ttk
from functools import partial

# Create functions
#----------------------------------------------------#
# Calculate Alice's Public Key

def calc_public_a(label_a_result,n1,n2,n3):  
	num1 = (n1.get())
	num2 = (n2.get())
	num3 = (n3.get())
	result = ((int(num2)**(int(num3))%int(num1)))
	label_a_result.config(text=" %d" % result)
	return
#----------------------------------------------------#
# Calculate Bob's Public Key

def calc_public_b(label_b_result,n1,n2,n3):
	num1 = (n1.get())
	num2 = (n2.get())
	num3 = (n3.get())
	result = ((int(num2)**(int(num3))%int(num1)))
	label_b_result.config(text=" %d" % result)
	return
#----------------------------------------------------#
# Calculate the Shared Secret on Alice's side

def ss_a(label_ss_a_result,n1,n2,n3,n4):
	num1 = (n1.get())
	num2 = (n2.get())
	num3 = (n3.get())
	num4 = (n4.get())
	result= ((((int(num1))**(int(num2)))%(int(num3)))**(int(num4)))%(int(num3))   
	label_ss_a_result.config(text=" %d" % result)
	return

#----------------------------------------------------#
# Calculate the Shared Secret on Bob's side

def ss_b(label_ss_b_result,n1,n2,n3,n4):
	num1 = (n1.get())
	num2 = (n2.get())
	num3 = (n3.get())
	num4 = (n4.get())
	result= ((((int(num1))**(int(num2)))%(int(num3)))**(int(num4)))%(int(num3))   
	label_ss_b_result.config(text=" %d" % result)
	return
#----------------------------------------------------#

# Define Window properties

root=Tk()
root.geometry("650x550")            # Opening window size LxB
root.title("COMP830: Diffie–Hellman (DH) Key Exchange demo") # Window title

#----------------------------------------------------#

# Declare all the entry variables

cn_prime_var=StringVar()
pr_root_var=StringVar()
private_a_var=StringVar()
private_b_var=StringVar()
public_a_var=StringVar()
public_b_var=StringVar()

#----------------------------------------------------#
# Labels 
# Common Prime and Primitive root
# packs not needed with grid

cn_prime=Label(root,text="Enter the common prime 'N'")
pr_root=Label(root,text="Enter the primitive root 'g'")

cn_prime.config(font="Calibri 12")
pr_root.config(font="Calibri 12")

cn_prime.grid(row=0,column=0,sticky=W)
pr_root.grid(row=1,column=0,sticky=W)

cn_prime_entry=ttk.Entry(root, width=20, textvariable=cn_prime_var)
pr_root_entry=ttk.Entry(root, width=20, textvariable=pr_root_var)

cn_prime_entry.grid(row=0,column=1)
pr_root_entry.grid(row=1,column=1)


#----------------------------------------------------#
# Labels 
# Private Keys

private_a=Label(root,text= "Enter Alice's private key 'private_a' (This is never shared !)")
private_b=Label(root,text= "Enter Bob's private key 'private_b' (This is never shared !)")

private_a.config(font="Calibri 12")
private_b.config(font="Calibri 12")

private_a.grid(row=2,column=0,sticky=W)
private_b.grid(row=3,column=0,sticky=W)

private_a_entry=ttk.Entry(root,width=20,textvariable=private_a_var)
private_b_entry=ttk.Entry(root,width=20,textvariable=private_b_var)

private_a_entry.grid(row=2,column=1)
private_b_entry.grid(row=3,column=1)

#----------------------------------------------------#
# Buttons
# Public Keys

label_a_result=Label(root)
label_a_result.grid(row=5,column=1)

calc_public_a = partial(calc_public_a,label_a_result,cn_prime_var,pr_root_var,private_a_var)
button_public_a=Button(root, text="Calculate Alice's public key",command=calc_public_a)
button_public_a.grid(row=4,sticky=W)

label_public_a=Label(root, text="Alice's public key: public_a = (g^private_a) mod N")
label_public_a.config(font="Calibri 12")
label_public_a.grid(row=5,column=0,sticky=W)

label_b_result=Label(root)
label_b_result.grid(row=7,column=1)

calc_public_b=partial(calc_public_b,label_b_result,cn_prime_var,pr_root_var,private_b_var)
button_public_b=Button(root, text="Calculate Bob's public key",command=calc_public_b)
button_public_b.grid(row=6,sticky=W)

label_public_b=Label(root, text="Bob's public key: public_b = (g^private_b) mod N")
label_public_b.config(font="Calibri 12")
label_public_b.grid(row=7,column=0,sticky=W)

label_descp=Label(root, text="The public keys are now exchanged.")
label_descp.config(font="Calibri 12")
label_descp.grid(row=8,column=0,sticky=W)

#----------------------------------------------------#

#Line Break for better readability


label_line=Label(root, text="------------------------------------------------------------------")
label_line.config(font="Calibri 12")
label_line.grid(row=9,column=0)#,sticky=W)

#----------------------------------------------------#

#Shared Secret Calculation on Alice's side

#Labels


label_ss_a1=Label(root,text="Alice receives Bob's public key: public_b ")
label_ss_a2=Label(root,text="Alice calculates the shared secret as: ss_a = (public_b^private_a)mod N")
label_ss_a3=Label(root,text="Shared Secret calculated by Alice")

label_ss_a1.config(font="Calibri 12")
label_ss_a1.grid(row=10,column=0,sticky=W)

label_ss_a2.config(font="Calibri 12")
label_ss_a2.grid(row=11,column=0,sticky=W)

label_ss_a3.config(font="Calibri 12")
label_ss_a3.grid(row=13,column=0,sticky=W)


#Buttons and Calculation command


label_ss_a_result=Label(root)
label_ss_a_result.grid(row=13,column=1)


ss_a = partial(ss_a,label_ss_a_result,pr_root_var,private_b_var,cn_prime_var,private_a_var)
#ideally should have used the output of calc_public_b as an input variable to ss_a
button_ss_a=Button(root, text="Calculate Shared Secret Alice",command=ss_a)
button_ss_a.grid(row=12,sticky=W)


#----------------------------------------------------#

#Line Break for better readability



label_line=Label(root, text="------------------------------------------------------------------")
label_line.config(font="Calibri 12")
label_line.grid(row=19,column=0)#,sticky=W)

#----------------------------------------------------#

#Shared Secret Calculation on Bob's side

#Labels

label_ss_b1=Label(root,text="Bob receives Alice's public key: public_a ")
label_ss_b2=Label(root,text="Bob calculates the shared secret as: ss_b = (public_a^private_b)mod N")
label_ss_b3=Label(root,text="Shared Secret calculated by Bob")

label_ss_b1.config(font="Calibri 12")
label_ss_b1.grid(row=20,column=0,sticky=W)

label_ss_b2.config(font="Calibri 12")
label_ss_b2.grid(row=21,column=0,sticky=W)

label_ss_b3.config(font="Calibri 12")
label_ss_b3.grid(row=25,column=0,sticky=W)


#Buttons and Calculation command

label_ss_b_result=Label(root)
label_ss_b_result.grid(row=25,column=1)


ss_b = partial(ss_b,label_ss_b_result,pr_root_var,private_a_var,cn_prime_var,private_b_var) 
#ideally should have used the output of calc_public_a as an input variable to ss_b
button_ss_b=Button(root, text="Calculate Shared Secret Bob",command=ss_b)
button_ss_b.grid(row=24,sticky=W)

#----------------------------------------------------#

#Line Break for better readability



label_line=Label(root, text="------------------------------------------------------------------")
label_line.config(font="Calibri 12")
label_line.grid(row=26,column=0)#,sticky=W)

#----------------------------------------------------#


root.mainloop()

