import numpy
import matplotlib.pyplot as plt
import collections
def ELECTION(S):
    iterator=0
    slot=""
    while(slot!="SINGLE"):
        iterator+=1
        n=S
        pi_vector=[]
        values_iterator=0
        
        for i in range(n):
            z=numpy.random.choice([0,1],p=[1-1/n,1/n])  #przypadek 
            pi_vector.append(z)  #
                       

        for el in pi_vector:
            if el == 1:
                values_iterator += 1
        
        if values_iterator == 1:
            slot="SINGLE"
        elif values_iterator > 1:
            slot="COLLISION"
        else:
            slot="NULL"
    return(iterator)
def returnning_function(num_of_trys):
    values_i=[]
    dict_counter_i=collections.OrderedDict({})
    for el in range(num_of_trys):
        f=ELECTION(100)
        values_i.append(f)
        if str(f) not in dict_counter_i.keys():
            dict_counter_i[str(f)]=1
        else:
            dict_counter_i[str(f)]+=1
    print(dict_counter_i)
    x=sorted([int(i) for i in dict_counter_i.keys()])
    y=[dict_counter_i[str(g)] for g in x]
    avr=(sum([el*el_2 for el,el_2 in zip(x,y)] )/num_of_trys)
    var=(1/(num_of_trys-1))*sum([pow((el-avr),2) for el in x])
    print("wartość średnia:",avr)
    print("wartość oczekiwana",var)
    plt.bar(x, y, color='b')
    plt.xlabel('liczba slotów')
    plt.ylabel('Ilosc przypadków')
    plt.show()
print(returnning_function(100))

