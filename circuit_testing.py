circuit_file = 'Patterns/vedic/4_bit_ripple_adder.v'
input_bit = '100110010'
 
#a,b,c = logic('Patterns/vedic/2x2.v','0000')
 
def and2(pa, pb):
    out = pa and pb
    if out == True:
        return 1
    return 0

def not1(pa):
    out = not (pa)
    if out == True:
        return 1
    return 0

def nand2(pa, pb):
    out = not (pa and pb)
    if out == True:
        return 1
    return 0

def nand3(pa, pb, pc):
    out = not (pa and pb and pc)
    if out == True:
        return 1
    return 0

def nand4(pa, pb, pc, pd):
    out = not (pa and pb and pc and pd)
    if out == True:
        return 1
    return 0

def nand5(pa, pb, pc, pd, pe):
    out = not (pa and pb and pc and pd and pe)
    if out == True:
        return 1
    return 0

def nand8(pa, pb, pc, pd, pe, pf, pg, ph):
    out = not (pa and pb and pc and pd and pe and pf and pg and ph)
    if out == True:
        return 1
    return 0

def buf1(pa):
    return pa

def nor2(pa, pb):
    out = not (pa or pb)
    if out == True:
        return 1
    return 0

def nor3(pa, pb, pc):
    out = not (pa or pb or pc)
    if out == True:
        return 1
    return 0

def nor4(pa, pb, pc, pd):
    out = not (pa or pb or pc or pd)
    if out == True:
        return 1
    return 0

def nor8(pa, pb, pc, pd, pe, pf, pg, ph):
    out = not (pa or pb or pc or pd or pe or pf or pg or ph)
    if out == True:
        return 1
    return 0

def or2(pa, pb):
    out = (pa or pb)
    if out == True:
        return 1
    return 0

def or3(pa, pb, pc):
    out = (pa or pb or pc)
    if out == True:
        return 1
    return 0

def xor2(pa, pb):
    out = ((pa or pb) and (not (pa) or not (pb)))
    if out == True:
        return 1
    return 0

def and3(pa, pb, pc):
    out = (pa and pb and pc)
    if out == True:
        return 1
    return 0

def and4(pa, pb, pc, pd):
    out = (pa and pb and pc and pd)
    if out == True:
        return 1
    return 0

def or4(pa, pb, pc, pd):
    out = (pa or pb or pc or pd)
    if out == True:
        return 1
    return 0

def or5(pa, pb, pc, pd, pe):
    out = (pa or pb or pc or pd or pe)
    if out == True:
        return 1
    return 0

def and5(pa, pb, pc, pd, pe):
    out = (pa and pb and pc and pd and pe)
    if out == True:
        return 1
    return 0

def and8(pa, pb, pc, pd, pe, pf, pg, ph):
    out = (pa and pb and pc and pd and pe and pf and pg and ph)
    if out == True:
        return 1
    return 0

def and9(pa, pb, pc, pd, pe, pf, pg, ph, pi):
    out = (pa and pb and pc and pd and pe and pf and pg and ph and pi)
    if out == True:
        return 1
    return 0

file = open(circuit_file)
# os.system('cd hope & hope -D -N -F c17_with_fault c17_with.bench')
lines = file.readlines()
file.close()

code = []
for line in lines:
    line = line.strip()
    if not len(line) == 0:
        code.append(line)

for i in range(len(code)):  # getting input from verilog file
    if code[i].startswith("input"):
        start = i
    if code[i].startswith("output"):
        end = i
inp = []
for i in range(start, end):
    code[i] = code[i].strip("input; ")
    inp += code[i].split(",")
for i in inp:
    if len(i) == 0:
        inp.remove(i)

for i in range(len(input_bit)):
    vars()[inp[i]] = int(input_bit[i])

for i in range(len(code)):  # getting input from verilog file
    if code[i].startswith("output"):
        start_o = i
    if code[i].startswith("wire"):
        end_o = i

out = []
for i in range(start_o, end_o):
    code[i] = code[i].strip("output; ")
    out += code[i].split(",")
for i in out:
    if len(i) == 0:
        out.remove(i)

for i in range(len(code)):  # getting input from verilog file
    if code[i].startswith("wire"):
        start_w = i
    if code[i].startswith("nand") or code[i].startswith("or") or code[i].startswith("xor") or code[i].startswith(
            "and") or code[i].startswith("nor") or code[i].startswith("not") or code[i].startswith("buf"):
        end_w = i
        break
wire = []
for i in range(start_w, end_w):
    code[i] = code[i].strip("wire; ")
    wire += code[i].split(",")
for i in wire:
    if len(i) == 0:
        wire.remove(i)

for line in code:  # calculating transition probabilty
    if line.startswith("nand") or line.startswith("or") or line.startswith("xor") or line.startswith(
            "and") or line.startswith("nor") or line.startswith("not") or line.startswith("buf"):
        line = line.split(" ")
        for i in range(len(line)):
            line[i] = line[i].strip(",;()")
        if line[0] == "nand":
            i = len(line[3:])
            if i == 2:
                vars()[line[2]] = nand2(vars()[line[-i]], vars()[line[-i + 1]])
            if i == 3:
                vars()[line[2]] = nand3(vars()[line[-i]], vars()[line[-i + 1]], vars()[line[-i + 2]])
            if i == 4:
                vars()[line[2]] = nand4(vars()[line[-i]], vars()[line[-i + 1]], vars()[line[-i + 2]],
                                        vars()[line[-i + 3]])
            if i == 5:
                vars()[line[2]] = nand5(vars()[line[-i]], vars()[line[-i + 1]], vars()[line[-i + 2]],
                                        vars()[line[-i + 3]], vars()[line[-i + 4]])
            if i == 8:
                vars()[line[2]] = nand8(vars()[line[-i]], vars()[line[-i + 1]], vars()[line[-i + 2]],
                                        vars()[line[-i + 3]], vars()[line[-i + 4]], vars()[line[-i + 5]],
                                        vars()[line[-i + 6]], vars()[line[-i + 7]])
        elif line[0] == "xor":
            i = len(line[3:])
            if i == 2:
                vars()[line[2]] = xor2(vars()[line[-i]], vars()[line[-i + 1]])
        elif line[0] == "and":
            i = len(line[3:])
            if i == 2:
                vars()[line[2]] = and2(vars()[line[-i]], vars()[line[-i + 1]])
            if i == 3:
                vars()[line[2]] = and3(vars()[line[-i]], vars()[line[-i + 1]], vars()[line[-i + 2]])
            if i == 4:
                vars()[line[2]] = and4(vars()[line[-i]], vars()[line[-i + 1]], vars()[line[-i + 2]],
                                       vars()[line[-i + 3]])
            if i == 5:
                vars()[line[2]] = and5(vars()[line[-i]], vars()[line[-i + 1]], vars()[line[-i + 2]],
                                       vars()[line[-i + 3]], vars()[line[-i + 4]])
            if i == 8:
                vars()[line[2]] = and8(vars()[line[-i]], vars()[line[-i + 1]], vars()[line[-i + 2]],
                                       vars()[line[-i + 3]], vars()[line[-i + 4]], vars()[line[-i + 5]],
                                       vars()[line[-i + 6]], vars()[line[-i + 7]])
            if i == 9:
                vars()[line[2]] = and9(vars()[line[-i]], vars()[line[-i + 1]], vars()[line[-i + 2]],
                                       vars()[line[-i + 3]], vars()[line[-i + 4]], vars()[line[-i + 5]],
                                       vars()[line[-i + 6]], vars()[line[-i + 7]], vars()[line[-i + 8]])
        elif line[0] == "or":
            i = len(line[3:])
            if i == 2:
                vars()[line[2]] = or2(vars()[line[-i]], vars()[line[-i + 1]])
            if i == 3:
                vars()[line[2]] = or3(vars()[line[-i]], vars()[line[-i + 1]], vars()[line[-i + 2]])
            if i == 4:
                vars()[line[2]] = or4(vars()[line[-i]], vars()[line[-i + 1]], vars()[line[-i + 2]],
                                      vars()[line[-i + 3]])
            if i == 5:
                vars()[line[2]] = or5(vars()[line[-i]], vars()[line[-i + 1]], vars()[line[-i + 2]],
                                      vars()[line[-i + 3]], vars()[line[-i + 4]])
        elif line[0] == "nor":
            i = len(line[3:])
            if i == 2:
                vars()[line[2]] = nor2(vars()[line[-i]], vars()[line[-i + 1]])
            if i == 3:
                vars()[line[2]] = nor3(vars()[line[-i]], vars()[line[-i + 1]], vars()[line[-i + 2]])
            if i == 4:
                vars()[line[2]] = nor4(vars()[line[-i]], vars()[line[-i + 1]], vars()[line[-i + 2]],
                                       vars()[line[-i + 3]])
            if i == 8:
                vars()[line[2]] = nor8(vars()[line[-i]], vars()[line[-i + 1]], vars()[line[-i + 2]],
                                       vars()[line[-i + 3]], vars()[line[-i + 4]], vars()[line[-i + 5]],
                                       vars()[line[-i + 6]], vars()[line[-i + 7]])
        elif line[0] == "not":
            vars()[line[2]] = not1(vars()[line[3]])
        elif line[0] == "buf":
            vars()[line[2]] = buf1(vars()[line[3]])
inp_logic = []
out_logic = []
wire_logic = []
for i in inp:
    inp_logic.append([i, vars()[i]])
for i in wire:
    wire_logic.append([i, vars()[i]])
for i in out:
    out_logic.append([i, vars()[i]])

print('in',inp_logic)
print('out',out_logic)