def trans_prob(circuit_file,theta):
    # tp for 2 input and gate
    def and2(pa,pb):
        return (1-(pa*pb))

    # tp for not gate
    def not1(pa):
        return (1-pa)

    # tp for 2 input nand gate
    def nand2(pa,pb):
        return (pa*pb)

    # tp for 3 input nand gate
    def nand3(pa,pb,pc):
        return (pa*pb*pc)

    # tp for 4 input nand gate
    def nand4(pa,pb,pc,pd):
        return (pa*pb*pc*pd)

    # tp for 5 input nand gate
    def nand5(pa,pb,pc,pd,pe):
        return (pa*pb*pc*pd*pe)

    # tp for 8 input nand gate
    def nand8(pa,pb,pc,pd,pe,pf,pg,ph):
        return (pa*pb*pc*pd*pe*pf*pg*ph)

    # tp for buffer gate
    def buf1(pa):
        return pa

    # tp for 2 input nor gate
    def nor2(pa,pb):
        return (1-((1-pa)*(1-pb)))

    # tp for 3 input nor gate
    def nor3(pa,pb,pc):
        return (1-((1-pa)*(1-pb)*(1-pc)))

    # tp for 4 input nor gate
    def nor4(pa,pb,pc,pd):
        return (1-((1-pa)*(1-pb)*(1-pc)*(1-pd)))

    # tp for 8 input nor8 gate
    def nor8(pa,pb,pc,pd,pe,pf,pg,ph):
        return (1-((1-pa)*(1-pb)*(1-pc)*(1-pd)*(1-pe)*(1-pf)*(1-pg)*(1-ph)))

    # tp for 2 input or gate
    def or2(pa,pb):
        return pa*pb

    # tp for 3 input or gate
    def or3(pa,pb,pc):
        return pa*pb*pc

    # tp for 2 input xor gate
    def xor2(pa,pb):
        return (1-((pa+pb)-(2*pa*pb)))

    # tp for 3 input and gate
    def and3(pa,pb,pc):
        return (1-pa*pb*pc)

    # tp for 4 input and gate
    def and4(pa,pb,pc,pd):
        return (1-pa*pb*pc*pd)

    # tp for 4 input or gate
    def or4(pa,pb,pc,pd):
        return (pa*pb*pc*pd)

    # tp for 5 input or gate
    def or5(pa,pb,pc,pd,pe):
        return (pa*pb*pc*pd*pe)

    # tp for 5 input and gate
    def and5(pa,pb,pc,pd,pe):
        return (1-pa*pb*pc*pd*pe)

    # tp for 8 input and gate
    def and8(pa,pb,pc,pd,pe,pf,pg,ph):
        return (1-pa*pb*pc*pd*pe*pf*pg*ph)

    # tp for 9 input and gate
    def and9(pa,pb,pc,pd,pe,pf,pg,ph,pi):
        return (1-pa*pb*pc*pd*pe*pf*pg*ph*pi)
       
       
    file=open(circuit_file)
    #os.system('cd hope & hope -D -N -F c17_with_fault c17_with.bench')
    lines = file.readlines()
    file.close()
    
    code=[]
    for line in lines:
        line = line.strip()
        if not len(line)==0:
            code.append(line)
    
    for i in range(len(code)):               #getting input from verilog file
        if code[i].startswith("input"):
            start=i
        if code[i].startswith("output"):
            end=i
    inp=[]
    for i in range(start,end):
        code[i]=code[i].strip("input; ")
        inp+=code[i].split(",")
    for i in inp:
        if len(i)==0:
            inp.remove(i)
    
    for i in range(len(inp)):         #assigning input as 0.5
        vars()[inp[i]]=0.5
    
    for i in range(len(code)):               #getting input from verilog file
        if code[i].startswith("output"):
            start_o=i
        if code[i].startswith("wire"):
            end_o=i
           
           
    out=[]
    for i in range(start_o,end_o):
        code[i]=code[i].strip("output; ")
        out+=code[i].split(",")
    for i in out:
        if len(i)==0:
            out.remove(i)
    
    for i in range(len(code)):               #getting input from verilog file
        if code[i].startswith("wire"):
            start_w=i
        if code[i].startswith("nand") or code[i].startswith("or") or code[i].startswith("xor") or code[i].startswith("and") or code[i].startswith("nor") or code[i].startswith("not") or code[i].startswith("buf"):
            end_w=i
            break
    wire=[]
    for i in range(start_w,end_w):
        code[i]=code[i].strip("wire; ")
        wire+=code[i].split(",")
    for i in wire:
        if len(i)==0:
            wire.remove(i)
    
    
    for line in code:               #calculating transition probabilty
        if line.startswith("nand") or line.startswith("or") or line.startswith("xor") or line.startswith("and") or line.startswith("nor") or line.startswith("not") or line.startswith("buf"):
            line=line.split(" ")
            for i in range(len(line)):
                line[i]=line[i].strip(",;()")
            if line[0]=="nand":
                i=len(line[3:])
                if i==2:
                    vars()[line[2]]=nand2(vars()[line[-i]],vars()[line[-i+1]])
                if i==3:
                    vars()[line[2]]=nand3(vars()[line[-i]],vars()[line[-i+1]],vars()[line[-i+2]])
                if i==4:
                    vars()[line[2]]=nand4(vars()[line[-i]],vars()[line[-i+1]],vars()[line[-i+2]],vars()[line[-i+3]])
                if i==5:
                    vars()[line[2]]=nand5(vars()[line[-i]],vars()[line[-i+1]],vars()[line[-i+2]],vars()[line[-i+3]],vars()[line[-i+4]])
                if i==8:
                    vars()[line[2]]=nand8(vars()[line[-i]],vars()[line[-i+1]],vars()[line[-i+2]],vars()[line[-i+3]],vars()[line[-i+4]],vars()[line[-i+5]],vars()[line[-i+6]],vars()[line[-i+7]])
            if line[0]=="xor":
                i=len(line[3:])
                if i==2:
                    vars()[line[2]]=xor2(vars()[line[-i]],vars()[line[-i+1]])
            if line[0]=="and":
                i=len(line[3:])
                if i==2:
                    vars()[line[2]]=and2(vars()[line[-i]],vars()[line[-i+1]])
                if i==3:
                    vars()[line[2]]=and3(vars()[line[-i]],vars()[line[-i+1]],vars()[line[-i+2]])
                if i==4:
                    vars()[line[2]]=and4(vars()[line[-i]],vars()[line[-i+1]],vars()[line[-i+2]],vars()[line[-i+3]])
                if i==5:
                    vars()[line[2]]=and5(vars()[line[-i]],vars()[line[-i+1]],vars()[line[-i+2]],vars()[line[-i+3]],vars()[line[-i+4]])
                if i==8:
                    vars()[line[2]]=and8(vars()[line[-i]],vars()[line[-i+1]],vars()[line[-i+2]],vars()[line[-i+3]],vars()[line[-i+4]],vars()[line[-i+5]],vars()[line[-i+6]],vars()[line[-i+7]])
                if i==9:
                    vars()[line[2]]=and9(vars()[line[-i]],vars()[line[-i+1]],vars()[line[-i+2]],vars()[line[-i+3]],vars()[line[-i+4]],vars()[line[-i+5]],vars()[line[-i+6]],vars()[line[-i+7]],vars()[line[-i+8]])
            if line[0]=="or":
                i=len(line[3:])
                if i==2:
                    vars()[line[2]]=or2(vars()[line[-i]],vars()[line[-i+1]])
                if i==3:
                    vars()[line[2]]=or3(vars()[line[-i]],vars()[line[-i+1]],vars()[line[-i+2]])
                if i==4:
                    vars()[line[2]]=or4(vars()[line[-i]],vars()[line[-i+1]],vars()[line[-i+2]],vars()[line[-i+3]])
                if i==5:
                    vars()[line[2]]=or5(vars()[line[-i]],vars()[line[-i+1]],vars()[line[-i+2]],vars()[line[-i+3]],vars()[line[-i+4]])
            if line[0]=="nor":
                i=len(line[3:])
                if i==2:
                    vars()[line[2]]=nor2(vars()[line[-i]],vars()[line[-i+1]])
                if i==3:
                    vars()[line[2]]=nor3(vars()[line[-i]],vars()[line[-i+1]],vars()[line[-i+2]])
                if i==4:
                    vars()[line[2]]=nor4(vars()[line[-i]],vars()[line[-i+1]],vars()[line[-i+2]],vars()[line[-i+3]])
                if i==8:
                    vars()[line[2]]=nor8(vars()[line[-i]],vars()[line[-i+1]],vars()[line[-i+2]],vars()[line[-i+3]],vars()[line[-i+4]],vars()[line[-i+5]],vars()[line[-i+6]],vars()[line[-i+7]])
            if line[0]=="not":
                vars()[line[2]]=not1(vars()[line[3]])
            if line[0]=="buf":
                vars()[line[2]]=buf1(vars()[line[3]])
    tp=[]
  #  for i in inp:
   #     tp.append([i, vars()[i], (1 - vars()[i]),vars()[i]*(1-vars()[i])])
    for i in wire:
        tp.append([i, vars()[i], (1-vars()[i]),vars()[i]*(1-vars()[i])])
#    for i in out:
 #       tp.append([i, vars()[i], (1 - vars()[i]),vars()[i]*(1-vars()[i])])
    rare_n=[]
    for i in wire:
        if vars()[i]*(1-vars()[i])<theta:
            rare_n.append(i)
        #print(i,vars()[i]*(1-vars()[i]))
    return rare_n, tp

#print(trans_prob('Patterns/verilog/c17_trojan2_location1_node16.v',0.3))
