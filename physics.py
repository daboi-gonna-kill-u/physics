# importiong math for rqare root etc
import math

def calculate():
    
    #checking if user wants to continue
    opt = int(input("Equations of Motion Calculator \n Choose an option: \n 1. Calculate missing value(s) \n 2. Quit \n Enter your choice (1/2):"))
    
   
   #exit:
    if opt == 2:
        print('Exiting')
        
    

    #continuing function:
    elif opt == 1:
        global u,v,t,s,a
        u = float(input("Enter initial velocity (m/s): "))
        v = float(input("Enter final velocity (m/s): "))
        t = float(input("Enter time taken (s): "))
        s = float(input("Enter distance (m): "))
        a = float(input("Acceleration (a): "))

        

#falisafe for checking for insufficient values:
        values = [u,v,t,s,a]
        sum = 0
        
        for value in range(len(values)):
             if values[value] != '':
                  sum  = sum +1

        if sum < 3:
             print('Insufficient values')
             exit(1)
    


        #time formule:
        if t == '' and v == '':
            t = (2*s)/( u + math.sqrt((2*a*s) + (u**2))) # dont ask how i got it ..... somethin by doing variations of s= ut + 1/2at^2
            print(t)
        if t == '' and v != '' and u != '' and a != '':
            t = (v-u)/a
            print(t)

        #acceleration formule:
        if a == '' and t == '':
            a = ((v*v)-(u*u))/(2*s) 
            print(f"a = {a} ")
        if t != '' and a == '' and s == '':
            a = ((v-u)/t)
            print(f"a = {a}")

        #distance formule:
        if s == '' and t != '' and u != '' and a != '':
            s = (u*t)+(0.5*a*t*t) 
            print(f"s = {s}")
        if t == '' and s == '' and a != '' and v != '' and u != '' :
            s = ((v*v)-(u*u)/(2*a))
            print(f"s = {s}")

        #final velocity
        if v == '' and a != '' and t != '':
            v = a*t
            print(f"v = {v}")
        if t == '' and v == '' and a != '' and s != '' and u != '':
            v = math.sqrt((u*u)+(2*a*s))
            print(f"v= {v}")
            
        #initial velocity
        if u == '' and a != '' and t != '':
            u = v - (a*t)
            print(f"u = {u}")
        if t == '' and u == '' and a != '' and s != '' and v != '':
            u =math.sqrt((v*v)-(2*a*s))
            print(f"u = {u}")
        print("u, v , t ,s , a =", u , v,t,s,  a)


calculate()