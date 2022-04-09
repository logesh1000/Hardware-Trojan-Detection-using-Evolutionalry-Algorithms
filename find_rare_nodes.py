from transition_probability import trans_prob
circuit_file = 'Patterns/verilog/c7552.v'
theta = 0.1
r_n,tp=trans_prob(circuit_file,theta)

for i in range(len(r_n)):
    print(r_n[i],end=',')