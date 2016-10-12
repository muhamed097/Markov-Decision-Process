# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 17:43:32 2016

@author: my computer
"""
import sys

dummy1 = sys.argv[1] #no need for number of states
dummy2 = sys.argv[2] #no need for number of actions
file = sys.argv[3]
discount = sys.argv[4]
discount = float(discount)


with open(file, "r") as inputs:
    data = inputs.read().split("\n")
    
#used for creation of dictionary so that you can end up with 
def name(i):
    '''Trivial eq. for creating state names to pair with reward values'''
    return "s" + str(i)

#Formatting
states = [data[x].split(" ") for x in range(len(data))]

#Formatting
if states[-1] ==  ['']:
    del states[-1]

#Store reward in dictionary with state name
rewards = {name(x + 1): states[x][1] for x in range(len(states))}

def create():
    '''Overall view of the MDP where the state values are replaced with
        their equivalent number values'''
    mdp = []
    #replacing states with values
    for x in range(len(states)):
        mdp.append([rewards.get(states[x][s],states[x][s]) 
                    for s in range(1,len(states[x]))])
        mdp[x].insert(0,"s" + str(x+1))
        #getting rid of parens for formatting
    for x in range(len(mdp)):
        for y in range(3,len(mdp[x]),3):
            l = list(mdp[x][y+1])
            del l[-1]
            l = ''.join(l)
            mdp[x][y+1] = l
    
    for x in range(len(mdp)):
        if mdp[x][-1] == '':
            del mdp[x][-1]   
    return mdp

mdp = create()

def act(row, mdp):
    '''Getting the probabilities of each action for each state'''
    y = 0
    count = 1
    actions = {}
    for x in range(2,len(mdp[row]) -3, 3):
        if mdp[row][x] == mdp[row][x+3]:
            y += float(mdp[row][x+1]) * float(mdp[row][x+2])             
        else:
            if mdp[row][x] == mdp[row][x-3]:
                y += float(mdp[row][x+1]) * float(mdp[row][x+2])
                actions["a" + mdp[row][x][-1]] = y
                y = 0
                count += 1
            else:
                actions["a" + mdp[row][x][-1]] = float(mdp[row][x+2]) * \
                                                 float(mdp[row][x+1])
                y = 0
                count += 1
    if mdp[row][-3] != mdp[row][-6]:
        actions["a" + mdp[row][-3][-1]] = float(mdp[row][-2]) * \
                                          float(mdp[row][-1])
    else:
        y += float(mdp[row][-1]) * float(mdp[row][-2])
        actions["a" + mdp[row][-3][-1]] = y
    return actions

def start(dic,reward):
    '''Used for getting start rewards and random actions'''
    return (reward, max(dic, key=dic.get))

def func(dic, discount, reward):
    '''Equation for calulating J Value'''
    j =  reward + (discount * max(dic.values()))
    j = round(j, 5)
    return (j, max(dic, key=dic.get))

l = []
for x in range(20):
    if x == 0:
        js = [start(act(0,mdp), int(mdp[x][1])) for x in range(len(mdp)) ]              
        print("After iteration 1: ",end="")
        for y in range(len(js)):
            print("(" + "s" + str(y+1) +" " + js[y][1] + " " 
                    + '{0:.4f}'.format(js[y][0]) + ")", end="")
        l.append(js)
        print()#formatting
    else:
        xs = [act(x,mdp) for x in range(len(mdp))] #updating actions
        ys = [func(xs[x], discount, int(mdp[x][1])) for x in range(len(mdp))] #new j values and max action
        l.append(ys)
        print("After iteration " + str(x + 1) +": ", end="")
        for y in range(len(l[0])):
            print("(" + "s" + str(y+1) +" " + l[x][y][1] + " " 
                    + '{0:.4f}'.format(l[x][y][0]) + ")", end="")
        zs = [i[0] for i in ys] #get just j value
        rewards = {name(x + 1): zs[x] for x in range(len(ys))} #j values now new rewards
        mdp = create() #updating in mdp
        print() #Formatting
        