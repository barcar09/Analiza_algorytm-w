import numpy
import collections
import math
import matplotlib.pyplot as plt

def ELECTION(num_of_trys, S, value_n,known_n):
    iterator = 0
    slot= ""                                          # counters and iterators
    values_i = []
    dict_counter_i = collections.OrderedDict({})
    # dict_counter_m=collections.OrderedDict({})
    for el in range(num_of_trys):
        while(slot != "SINGLE"):                      # since slot!= single ( leader not found)
            iterator += 1
            pi_vector = 0           
            values_iterator = 0
            if known_n == "KNOW_N":    # If we known numer of devices N
                n = S
                for el in range(1, n+1):
                    z = numpy.random.choice([0, 1],p=[1-1 / n,1 / n])  # create propability vector
                    pi_vector += z
            elif known_n == "NOT_KNOW_N":  # if we dont know numer of devices N
                n = math.ceil(math.log(S, 2))
                glf = value_n
                # Propability vector changing depend's on witch round we get trough.             
                round = (iterator % n) + 1                                             
                for elg in range(1, glf + 1):
                    z = numpy.random.choice([0, 1],p=[1 - 1 / 2 ** round,1 / 2 ** round])  # vector of propability for unknown number of devices
                    pi_vector += z
                
            
        
            if pi_vector == 1:
                slot="SINGLE"
            elif pi_vector > 1:                   # Choose type of slot
                slot="COLLISION"
            else:
                slot="NULL"

        f=iterator      # return how many slot we have since we choose leader
        if str(f) not in dict_counter_i.keys():
            dict_counter_i[str(f)] = 1
        else:                                   # Dict of how many many slots we have from number of trys we declare
            dict_counter_i[str(f)] += 1
        f = 0
        iterator = 0        # resets counters 
        slot = ""
    
    x=sorted([int(i) for i in dict_counter_i.keys()])
    

    # prepering and plot our data 
    y=[dict_counter_i[str(g)] for g in x]
    hoose_lider_in1=0
    for el in range(1,n+1):
        try:
            hoose_lider_in1+=dict_counter_i[str(el)]   
        except KeyError:
            pass
    avr=(sum([el*el_2 for el,el_2 in zip(x,y)] )/num_of_trys)
    var=(1/(num_of_trys-1))*sum([pow((el-avr),2) for el in x])
    print("wartość średnia:",avr)
    print("wartość oczekiwana",var)
    #print("wybranych w 1 slocie",y[0])
    #print("sigma",choose_lider_in1/num_of_trys)
    #plt.bar(x, y, color='b')
    #plt.xlabel('liczba slotów')
    #plt.ylabel('Ilosc przypadków')
    #plt.show()
    return(hoose_lider_in1)




def sigma_returner(): # Return average of return in frist round in n = 2/500/100
    esa = [2, 500, 1000]
    counter = 0
    for el in esa:
        counter+=ELECTION(100, 1000, el, "NOT_KNOW_N")
    return counter / 300

print(sigma_returner())