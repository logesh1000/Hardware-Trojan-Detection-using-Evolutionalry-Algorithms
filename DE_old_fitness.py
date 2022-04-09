import random
import numpy as np
from logic import logic
from transition_probability import trans_prob
from scoap import scoap
from score import calc_rank
import time

start_time = time.time()

psize = 10
ckt = 'c880'
node = '773'
loc = '1'
trj = '1'

golden_circuit_file = 'Patterns/verilog/' + ckt + '.v'
trojan_inserted_file =  'Patterns/verilog/' + ckt + '_trojan'+trj+'_location' + loc + '_node' + node + '.v'

print(trojan_inserted_file, '\n\n')
file = open(golden_circuit_file)
line = file.readlines()
file.close()
for i in range(len(line)):
    if line[i].startswith('// Ninputs'):
        line[i] = line[i].split(' ')
        n = int(line[i][2])
        break

theta = 0.0001  # threshold to find rare nodes
it = 10


def xor(a, b):
    return bin(int(a, 2) ^ int(b, 2)).replace('0b', '').zfill(n)


def mul(a, b):
    return bin(int(a, 2) & int(b, 2)).replace('0b', '').zfill(n)


def add(a, b):
    return bin(int(a, 2) | int(b, 2)).replace('0b', '').zfill(n)


def individual(length):
    res = ''
    a = [random.randint(0, 1) for x in range(length)]
    for i in a:
        res += str(i)
    return res


def population(count, length):
    return [individual(length) for x in range(count)]


def mutation(a, b, c, n):
    return (add(mul(xor(b, c), individual(n)), a))


def crossover(a, b, cp):
    trail = ''
    for i in range(len(a)):
        if random.random() < cp:
            trail += b[i]
        else:
            trail += a[i]
    return trail


def fitnessindi(y):
    x = bin(0).replace('0b', '').zfill(n)
    a, b, c = logic(trojan_inserted_file, x)
    e, f, g = logic(trojan_inserted_file, y)
    rare_node, trn_pr = trans_prob(trojan_inserted_file, theta)

    # print(rank)
    count = 0
    for i in range(len(g)):
        for j in range(len(rare_node)):
            if g[i][0] == rare_node[j]:
                if g[i][1] != c[i][1]:
                    count += 1
                    # print(rank[i][0],rank[i][1])
    fit_fun = count
    return fit_fun


def differential_algorithm(pop_len=n, crossp=0.7, popsize=psize, its=it):
    pop = population(popsize, pop_len)
    i = 0
    while i < its:
        for j in range(popsize):
            idxs = [idx for idx in range(popsize) if idx != j]
            idx1, idx2, idx3 = np.random.choice(idxs, 3, replace=False)
            a = pop[idx1]
            b = pop[idx2]
            c = pop[idx3]
            mut = mutation(a, b, c, pop_len)
            trail = crossover(pop[j], mut, crossp)
            if fitnessindi(trail) > fitnessindi(pop[j]):
                pop[j] = trail
        i += 1
    return pop


pop = differential_algorithm()
'''
-----------------------------------------------------------------
detection  part
-----------------------------------------------------------------
'''

flag = 0

for i in range(len(pop)):
    print('Pattern :', pop[i], '\nFitness ', fitnessindi(pop[i]))
    a_1, b_1, c_1 = logic(golden_circuit_file, pop[i])
    e_1, g_1, f_1 = logic(trojan_inserted_file, pop[i])
    count = 0
    for j in range(len(b_1)):
        if g_1[j] != b_1[j]:
            count += 1
    x = 0
    x = bin(x).replace('0b', '').zfill(n)
    a_2, b_2, c_2 = logic(golden_circuit_file, x)
    e_2, f_2, g_2 = logic(golden_circuit_file, pop[i])
    rare_node_2, trn_pr = trans_prob(golden_circuit_file, theta)
    # print(rare_node_2)
    count_1 = 0
    for j in range(len(g_2)):
        for k in range(len(rare_node_2)):
            if g_2[j][0] == rare_node_2[k]:
                if g_2[j][1] != c_2[j][1]:
                    count_1 += 1
    k_2, l_2, m_2 = logic(trojan_inserted_file, x)
    h_2, i_2, j_2 = logic(trojan_inserted_file, pop[i])
    rare_node_3, trn_pr = trans_prob(trojan_inserted_file, theta)
    # print(rare_node_3)
    count_2 = 0
    for j in range(len(j_2)):
        for k in range(len(rare_node_3)):
            if j_2[j][0] == rare_node_3[k]:
                if j_2[j][1] != m_2[j][1]:
                    count_2 += 1
    print('Trigger coverage for benchmark circuit:', count_1, '\nTrigger coverage for given circuit:', count_2)
    print('Number of output changed by trojan circuit represented as Trojan coverage:', count / len(b_1))
    print()
    if count > 0 and count_2 != count_1:
        flag = 1

print(rare_node_3)
if flag == 1:
    print('\nTrojan present in circuit')
else:
    print('\nTrojan is not present in circuit')
print("--- %s seconds ---" % (time.time() - start_time))