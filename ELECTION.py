import numpy
import matplotlib.pyplot as plt
import collections
import math
def ELECTION(num_of_trys,S,known_n):
    iterator=0
    slot=""                                          # counters and iterators
    values_i=[]
    dict_counter_i=collections.OrderedDict({})
    for el in range(num_of_trys):
        while(slot!="SINGLE"):                      # since slot!= single ( leader not found)
            iterator+=1
            pi_vector=[]            
            values_iterator = 0
            if known_n=="KNOW_N":    # If we known numer of devices N
                n = S
                for el in range(n):
                    z = numpy.random.choice([0,1],p=[1-1/n,1/n])  # create propability vector
                    pi_vector.append(z)
            elif known_n == "NOT_KNOW_N":  # if we dont know numer of devices N
                n = math.ceil(math.log(S,2))
                
                for elg in range(1,n+1):
                    z = numpy.random.choice([0,1],p=[1-1/2**elg,1/2**elg])    # vector of propability for unknown number of devices
                    pi_vector.append(z)
                
            for el in pi_vector:
                if el == 1:
                    values_iterator += 1
        
            if values_iterator == 1:
                slot="SINGLE"
            elif values_iterator > 1:                   # Choose type of slot
                slot="COLLISION"
            else:
                slot="NULL"

        f=iterator      # return how many slot we have since we choose leader
        if str(f) not in dict_counter_i.keys():
            dict_counter_i[str(f)]=1
        else:                                   # Dict of how many many slots we have from number of trys we declare
            dict_counter_i[str(f)]+=1
        f = 0
        iterator = 0        # resets counters 
        slot=""
    
    x=sorted([int(i) for i in dict_counter_i.keys()])   # prepering and plot our data 
    y=[dict_counter_i[str(g)] for g in x]
    choose_lider_in1=y[0]
    avr=(sum([el*el_2 for el,el_2 in zip(x,y)] )/num_of_trys)
    var=(1/(num_of_trys-1))*sum([pow((el-avr),2) for el in x])
    print("wartość średnia:",avr)
    print("wartość oczekiwana",var)
    print("wybranych w 1 slocie",y[0])
    print("sigma",choose_lider_in1/num_of_trys)
    plt.bar(x, y, color='b')
    plt.xlabel('liczba slotów')
    plt.ylabel('Ilosc przypadków')
    plt.show()

#ELECTION(100,100,"DETERMINISTIC")
ELECTION(100,100,"NOT_KNOW_N")