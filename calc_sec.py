import os
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import time
import random
import numpy as np
from logic import logic
from transition_probability import trans_prob
from scoap import scoap
from score import calc_rank



file = []
sec=[]
for i in os.listdir('L:/final_year_project/Patterns/verilog'):
    file.append(i)
    start_time = time.time()
    golden_circuit_file = 'L:/final_year_project/Patterns/verilog/'+i
    trojan_inserted_file = 'L:/final_year_project/Patterns/verilog/'+i
    
    files = open(golden_circuit_file)
    line = files.readlines()
    files.close()
    for i in range(len(line)):
        if line[i].startswith('// Ninputs'):
            line[i] = line[i].split(' ')
            n = int(line[i][2])
            break
    theta = 0.3  # threshold to find rare nodes
    it = 1 
    psize=10


    def individual(length, min, max):
        return [random.randint(min, max) for x in range(length)]


    def population(count, length, min, max):
        return [individual(length, min, max) for x in range(count)]


    def fitness(pop):
        x = 0
        x = bin(x).replace('0b', '').zfill(n)
        fit_fun = []
        for i in range(len(pop)):
            y = ''
            for j in range(len(pop[i])):
                y += str(pop[i][j])
            a, b, c = logic(trojan_inserted_file, x)
            e, f, g = logic(trojan_inserted_file, y)
            rare_node, trn_pr = trans_prob(trojan_inserted_file, theta)
            scp = scoap(trojan_inserted_file)
            rank = []
            for i in range(len(scp)):
                rank.append([scp[i][0], calc_rank(scp[i], trn_pr[i], g[i])])
            count = 0
            for i in range(len(g)):
                for j in range(len(rare_node)):
                    if g[i][0] == rare_node[j]:
                        if g[i][1] != c[i][1]:
                            count += rank[i][1]
            fit_fun.append(count)
        return max(fit_fun)


    def fitnessindi(individual):
        x = bin(0).replace('0b', '').zfill(n)
        y = ''
        for i in range(len(individual)):
            y += str(individual[i])
        a, b, c = logic(trojan_inserted_file, x)
        e, f, g = logic(trojan_inserted_file, y)
        scp = scoap(trojan_inserted_file)
        rare_node, trn_pr = trans_prob(trojan_inserted_file, theta)
        rank = []
        for i in range(len(scp)):
            rank.append([scp[i][0], calc_rank(scp[i], trn_pr[i], g[i])])
        # print(rank)
        count = 0
        for i in range(len(g)):
            for j in range(len(rare_node)):
                if g[i][0] == rare_node[j]:
                    if g[i][1] != c[i][1]:
                        count += rank[i][1]
                        # print(rank[i][0],rank[i][1])
        fit_fun = count
        return fit_fun


    def evolve(pop, retain=1, random_select=0.05, mutate=0.01):
        # fit = fitness(pop)
        retain_length = int(len(pop) * retain)
        parents = pop[:retain_length]
        graded = [(fitnessindi(x), x) for x in parents]
        graded = [x[1] for x in sorted(graded, reverse=True)]
        for individual in pop[retain_length:]:
            if random_select > random.random():
                parents.append(individual)
        for individual in parents:
            if mutate > random.random():
                pos_to_mutate = random.randint(0, len(individual) - 1)
                individual[pos_to_mutate] = random.randint(min(individual), max(individual))

        desired_length = len(pop)
        # print(graded)
        # print(graded[1])
        children = []
        count = 0
        while len(children) < desired_length:
            male = graded[count]
            count = count + 1
            if count == len(graded):
                count = 0
            female = graded[count]
            count = count + 1
            if count == len(graded):
                count = 0
            half = int(len(male) / 2)
            child1 = male[:half] + female[half:]
            child2 = female[:half] + male[half:]
            children.append(child1)
            children.append(child2)

        if (fitness(children) > fitness(parents)):
            return children
        else:
            return parents


    p = population(psize, n, 0, 1)

    fitness_history = [fitness(p)]
    # print(fitness(p))
    maxi = fitness(p)
    c = evolve(p)
    for i in range(it):
        c = evolve(c)
        presnt = fitness(c)
        if (maxi < presnt):
            maxi = presnt
        fitness_history.append(presnt)
    sec.append(time.time()-start_time)

print(sec)

   
df = pd.DataFrame({'time': sec[:]})
writer = ExcelWriter('L:/final_year_project/time.xlsx')
df.to_excel(writer, 'Sheet1', index=False)
writer.save()
