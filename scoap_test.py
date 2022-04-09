def scoap_values(filename):
    def not1cc(cc0,cc1):
        out0=cc1+1
        out1=cc0+1
        return [out0,out1,0]
    def buf1cc(cc0,cc1):
        out0=cc0+1
        out1=cc1+1
        return [out0,out1,0]
    def and2cc(acc0,acc1,bcc0,bcc1):
        out0=min(acc0,bcc0)+1
        out1=acc1+bcc1+1
        return [out0,out1,0]
    def and3cc(acc0,acc1,bcc0,bcc1,ccc0,ccc1):
        out0=min(acc0,bcc0,ccc0)+1
        out1=acc1+bcc1+ccc1+1
        return [out0,out1,0]
    def and4cc(acc0,acc1,bcc0,bcc1,ccc0,ccc1,dcc0,dcc1):
        out0=min(acc0,bcc0,ccc0,dcc0)+1
        out1=acc1+bcc1+ccc1+dcc1+1
        return [out0,out1,0]
    def and5cc(acc0,acc1,bcc0,bcc1,ccc0,ccc1,dcc0,dcc1,ecc0,ecc1):
        out0=min(acc0,bcc0,ccc0,dcc0,ecc0)+1
        out1=acc1+bcc1+ccc1+dcc1+ecc1+1
        return [out0,out1,0]
    def and8cc(acc0,acc1,bcc0,bcc1,ccc0,ccc1,dcc0,dcc1,ecc0,ecc1,fcc0,fcc1,gcc0,gcc1,hcc0,hcc1):
        out0=min(acc0,bcc0,ccc0,dcc0,ecc0,fcc0,gcc0,hcc0)+1
        out1=acc1+bcc1+ccc1+dcc1+ecc1+fcc1+gcc1+hcc1+1
        return [out0,out1,0]
    def and9cc(acc0,acc1,bcc0,bcc1,ccc0,ccc1,dcc0,dcc1,ecc0,ecc1,fcc0,fcc1,gcc0,gcc1,hcc0,hcc1,icc0,icc1):
        out0=min(acc0,bcc0,ccc0,dcc0,ecc0,fcc0,gcc0,hcc0,icc0)+1
        out1=acc1+bcc1+ccc1+dcc1+ecc1+fcc1+gcc1+hcc1+icc1+1
        return [out0,out1,0]
    def nand2cc(acc0,acc1,bcc0,bcc1):
        out0=acc1+bcc1+1
        out1=min(acc0,bcc0)+1
        return [out0,out1,0]
    def nand3cc(acc0,acc1,bcc0,bcc1,ccc0,ccc1):
        out0=acc1+bcc1+ccc1+1
        out1=min(acc0,bcc0,ccc0)+1
        return [out0,out1,0]
    def nand4cc(acc0,acc1,bcc0,bcc1,ccc0,ccc1,dcc0,dcc1):
        out0=acc1+bcc1+ccc1+dcc1+1
        out1=min(acc0,bcc0,ccc0,dcc0)+1
        return [out0,out1,0]
    def nand5cc(acc0,acc1,bcc0,bcc1,ccc0,ccc1,dcc0,dcc1,ecc0,ecc1):
        out0=acc1+bcc1+ccc1+dcc1+ecc1+1
        out1=min(acc0,bcc0,ccc0,dcc0,ecc0)+1
        return [out0,out1,0]
    def nand8cc(acc0,acc1,bcc0,bcc1,ccc0,ccc1,dcc0,dcc1,ecc0,ecc1,fcc0,fcc1,gcc0,gcc1,hcc0,hcc1):
        out0=acc1+bcc1+ccc1+dcc1+ecc1+fcc1+gcc1+hcc1+1
        out1=min(acc0,bcc0,ccc0,dcc0,ecc0,fcc0,gcc0,hcc0)+1
        return [out0,out1,0]
    def nor2cc(acc0,acc1,bcc0,bcc1):
        out0=min(acc1,bcc1)+1
        out1=acc0+bcc0+1
        return [out0,out1,0]
    def nor3cc(acc0,acc1,bcc0,bcc1,ccc0,ccc1):
        out0=min(acc1,bcc1,ccc1)+1
        out1=acc0+bcc0+ccc0+1
        return [out0,out1,0]
    def nor4cc(acc0,acc1,bcc0,bcc1,ccc0,ccc1,dcc0,dcc1):
        out0=min(acc1,bcc1,ccc1,dcc1)+1
        out1=acc0+bcc0+ccc0+dcc0+1
        return [out0,out1,0]
    def nor8cc(acc0,acc1,bcc0,bcc1,ccc0,ccc1,dcc0,dcc1,ecc0,ecc1,fcc0,fcc1,gcc0,gcc1,hcc0,hcc1):
        out0=min(acc1,bcc1,ccc1,dcc1,ecc1,fcc1,gcc1,hcc1)+1
        out1=acc0+bcc0+ccc0+dcc0+ecc0+fcc0+gcc0+hcc0+1
        return [out0,out1,0]
    def or2cc(acc0,acc1,bcc0,bcc1):
        out0=acc0+bcc0+1
        out1=min(acc1,bcc1)+1
        return [out0,out1,0]
    def or3cc(acc0,acc1,bcc0,bcc1,ccc0,ccc1):
        out0=acc0+bcc0+ccc0+1
        out1=min(acc1,bcc1,ccc1)+1
        return [out0,out1,0]
    def or4cc(acc0,acc1,bcc0,bcc1,ccc0,ccc1,dcc0,dcc1):
        out0=acc0+bcc0+ccc0+dcc0+1
        out1=min(acc1,bcc1,ccc1,dcc1)+1
        return [out0,out1,0]
    def or5cc(acc0,acc1,bcc0,bcc1,ccc0,ccc1,dcc0,dcc1,ecc0,ecc1):
        out0=acc0+bcc0+ccc0+dcc0++ecc0+1
        out1=min(acc1,bcc1,ccc1,dcc1,ecc1)+1
        return [out0,out1,0]
    def xor2cc(acc0,acc1,bcc0,bcc1):
        out0=min(acc0+bcc0,acc1+bcc1)+1
        out1=min(acc1+bcc0,acc0+bcc1)+1
        return [out0,out1,0]



    #controlability
    def not1co(zco):
        return zco+1
    def buf1co(zco):
        return zco
    def and2co(zco,acc1,bcc1):
        a=zco+bcc1+1
        b=zco+acc1+1
        return a,b
    def and3co(zco,acc1,bcc1,ccc1):
        a=zco+bcc1+ccc1+1
        b=zco+acc1+ccc1+1
        c=zco+acc1+bcc1+1
        return a,b,c
    def and4co(zco,acc1,bcc1,ccc1,dcc1):
        a=zco+bcc1+ccc1+dcc1+1
        b=zco+acc1+ccc1+dcc1+1
        c=zco+acc1+bcc1+dcc1+1
        d=zco+acc1+bcc1+ccc1+1
        return a,b,c,d
    def and5co(zco,acc1,bcc1,ccc1,dcc1,ecc1):
        a=zco+bcc1+ccc1+dcc1+ecc1+1
        b=zco+acc1+ccc1+dcc1+ecc1+1
        c=zco+acc1+bcc1+dcc1+ecc1+1
        d=zco+acc1+bcc1+ccc1+ecc1+1
        e=zco+acc1+bcc1+ccc1+dcc1+1
        return a,b,c,d,e
    def and8co(zco,acc1,bcc1,ccc1,dcc1,ecc1,fcc1,gcc1,hcc1):
        a=zco+bcc1+ccc1+dcc1+ecc1+fcc1+gcc1+hcc1+1
        b=zco+acc1+ccc1+dcc1+ecc1+fcc1+gcc1+hcc1+1
        c=zco+acc1+bcc1+dcc1+ecc1+fcc1+gcc1+hcc1+1
        d=zco+acc1+bcc1+ccc1+ecc1+fcc1+gcc1+hcc1+1
        e=zco+acc1+bcc1+ccc1+dcc1+fcc1+gcc1+hcc1+1
        f=zco+acc1+bcc1+ccc1+dcc1+ecc1+gcc1+hcc1+1
        g=zco+acc1+bcc1+ccc1+dcc1+ecc1+fcc1+hcc1+1
        h=zco+acc1+bcc1+ccc1+dcc1+ecc1+fcc1+gcc1+1
        return a,b,c,d,e,f,g,h
    def and9co (zco,acc1,bcc1,ccc1,dcc1,ecc1,fcc1,gcc1,hcc1,icc1):
        a=zco+bcc1+ccc1+dcc1+ecc1+fcc1+gcc1+hcc1+icc1+1
        b=zco+acc1+ccc1+dcc1+ecc1+fcc1+gcc1+hcc1+icc1+1
        c=zco+acc1+bcc1+dcc1+ecc1+fcc1+gcc1+hcc1+icc1+1
        d=zco+acc1+bcc1+ccc1+ecc1+fcc1+gcc1+hcc1+icc1+1
        e=zco+acc1+bcc1+ccc1+dcc1+fcc1+gcc1+hcc1+icc1+1
        f=zco+acc1+bcc1+ccc1+dcc1+ecc1+gcc1+hcc1+icc1+1
        g=zco+acc1+bcc1+ccc1+dcc1+ecc1+fcc1+hcc1+icc1+1
        h=zco+acc1+bcc1+ccc1+dcc1+ecc1+fcc1+gcc1+icc1+1
        i=zco+acc1+bcc1+ccc1+dcc1+ecc1+fcc1+gcc1+hcc1+1
        return a,b,c,d,e,f,g,h,i
    def or2co(zco,acc0,bcc0):
        a=zco+bcc0+1
        b=zco+acc0+1
        return a,b
    def or3co(zco,acc0,bcc0,ccc0):
        a=zco+bcc0+ccc0+1
        b=zco+acc0+ccc0+1
        c=zco+acc0+bcc0+1
        return a,b,c
    def or4co(zco,acc0,bcc0,ccc0,dcc0):
        a=zco+bcc0+ccc0+dcc0+1
        b=zco+acc0+ccc0+dcc0+1
        c=zco+acc0+bcc0+dcc0+1
        d=zco+acc0+bcc0+ccc0+1
        return a,b,c,d
    def or5co(zco,acc0,bcc0,ccc0,dcc0,ecc0):
        a=zco+bcc0+ccc0+dcc0+ecc0+1
        b=zco+acc0+ccc0+dcc0+ecc0+1
        c=zco+acc0+bcc0+dcc0+ecc0+1
        d=zco+acc0+bcc0+ccc0+ecc0+1
        e=zco+acc0+bcc0+ccc0+dcc0+1
        return a,b,c,d,e
    def or8co(zco,acc0,bcc0,ccc0,dcc0,ecc0,fcc0,gcc0,hcc0):
        a=zco+bcc0+ccc0+dcc0+ecc0+fcc0+gcc0+hcc0+1
        b=zco+acc0+ccc0+dcc0+ecc0+fcc0+gcc0+hcc0+1
        c=zco+acc0+bcc0+dcc0+ecc0+fcc0+gcc0+hcc0+1
        d=zco+acc0+bcc0+ccc0+ecc0+fcc0+gcc0+hcc0+1
        e=zco+acc0+bcc0+ccc0+dcc0+fcc0+gcc0+hcc0+1
        f=zco+acc0+bcc0+ccc0+dcc0+ecc0+gcc0+hcc0+1
        g=zco+acc0+bcc0+ccc0+dcc0+ecc0+fcc0+hcc0+1
        h=zco+acc0+bcc0+ccc0+dcc0+ecc0+fcc0+gcc0+1
        return a,b,c,d,e,f,g,h
    def xor2co(zco,acc0,acc1,bcc0,bcc1):
        a=zco+min(bcc0,bcc1)+1
        b=zco+min(acc0,acc1)+1
        return a,b
    file=open(filename)
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
        vars()[inp[i]]=[1,1,0]

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
    const=[]
    for line in code:               #calculating transition probabilty
        if line.startswith("nand") or line.startswith("or") or line.startswith("xor") or line.startswith("and") or line.startswith("nor") or line.startswith("not") or line.startswith("buf"):
            line=line.split(" ")
            for i in range(len(line)):
                line[i]=line[i].strip(",;()")
            const.append(line)
            if line[0]=="nand" or line[0]=="NAND":
                i=len(line[3:])
                if i==2:
                    vars()[line[2]]=nand2cc(vars()[line[-i]][0],vars()[line[-i]][1],vars()[line[-i+1]][0],vars()[line[-i+1]][1])
                if i==3:
                    vars()[line[2]]=nand3cc(vars()[line[-i]][0],vars()[line[-i]][1],vars()[line[-i+1]][0],vars()[line[-i+1]][1],vars()[line[-i+2]][0],vars()[line[-i+2]][1])
                if i==4:
                    vars()[line[2]]=nand4cc(vars()[line[-i]][0],vars()[line[-i]][1],vars()[line[-i+1]][0],vars()[line[-i+1]][1],vars()[line[-i+2]][0],vars()[line[-i+2]][1],vars()[line[-i+3]][0],vars()[line[-i+3]][1])
                if i==5:
                    vars()[line[2]]=nand5cc(vars()[line[-i]][0],vars()[line[-i]][1],vars()[line[-i+1]][0],vars()[line[-i+1]][1],vars()[line[-i+2]][0],vars()[line[-i+2]][1],vars()[line[-i+3]][0],vars()[line[-i+3]][1],vars()[line[-i+4]][0],vars()[line[-i+4]][1])
                if i==8:
                    vars()[line[2]]=nand8cc(vars()[line[-i]][0],vars()[line[-i]][1],vars()[line[-i+1]][0],vars()[line[-i+1]][1],vars()[line[-i+2]][0],vars()[line[-i+2]][1],vars()[line[-i+3]][0],vars()[line[-i+3]][1],vars()[line[-i+4]][0],vars()[line[-i+4]][1],vars()[line[-i+5]][0],vars()[line[-i+5]][1],vars()[line[-i+6]][0],vars()[line[-i+6]][1],vars()[line[-i+7]][0],vars()[line[-i+7]][1])
            if line[0]=="xor" or line[0]=="XOR":
                i=len(line[3:])
                if i==2:
                    vars()[line[2]]=xor2cc(vars()[line[-i]][0],vars()[line[-i]][1],vars()[line[-i+1]][0],vars()[line[-i+1]][1])
            if line[0]=="and" or line[0]=="AND":
                i=len(line[3:])
                if i==2:
                    vars()[line[2]]=and2cc(vars()[line[-i]][0],vars()[line[-i]][1],vars()[line[-i+1]][0],vars()[line[-i+1]][1])
                if i==3:
                    vars()[line[2]]=and3cc(vars()[line[-i]][0],vars()[line[-i]][1],vars()[line[-i+1]][0],vars()[line[-i+1]][1],vars()[line[-i+2]][0],vars()[line[-i+2]][1])
                if i==4:
                    vars()[line[2]]=and4cc(vars()[line[-i]][0],vars()[line[-i]][1],vars()[line[-i+1]][0],vars()[line[-i+1]][1],vars()[line[-i+2]][0],vars()[line[-i+2]][1],vars()[line[-i+3]][0],vars()[line[-i+3]][1])
                if i==5:
                    vars()[line[2]]=and5cc(vars()[line[-i]][0],vars()[line[-i]][1],vars()[line[-i+1]][0],vars()[line[-i+1]][1],vars()[line[-i+2]][0],vars()[line[-i+2]][1],vars()[line[-i+3]][0],vars()[line[-i+3]][1],vars()[line[-i+4]][0],vars()[line[-i+4]][1])
                if i==8:
                    vars()[line[2]]=and8cc(vars()[line[-i]][0],vars()[line[-i]][1],vars()[line[-i+1]][0],vars()[line[-i+1]][1],vars()[line[-i+2]][0],vars()[line[-i+2]][1],vars()[line[-i+3]][0],vars()[line[-i+3]][1],vars()[line[-i+4]][0],vars()[line[-i+4]][1],vars()[line[-i+5]][0],vars()[line[-i+5]][1],vars()[line[-i+6]][0],vars()[line[-i+6]][1],vars()[line[-i+7]][0],vars()[line[-i+7]][1])
                if i==9:
                    vars()[line[2]]=and9cc(vars()[line[-i]][0],vars()[line[-i]][1],vars()[line[-i+1]][0],vars()[line[-i+1]][1],vars()[line[-i+2]][0],vars()[line[-i+2]][1],vars()[line[-i+3]][0],vars()[line[-i+3]][1],vars()[line[-i+4]][0],vars()[line[-i+4]][1],vars()[line[-i+5]][0],vars()[line[-i+5]][1],vars()[line[-i+6]][0],vars()[line[-i+6]][1],vars()[line[-i+7]][0],vars()[line[-i+7]][1],vars()[line[-i+8]][0],vars()[line[-i+8]][1])
            if line[0]=="or" or line[0]=="OR":
                i=len(line[3:])
                if i==2:
                    vars()[line[2]]=or2cc(vars()[line[-i]][0],vars()[line[-i]][1],vars()[line[-i+1]][0],vars()[line[-i+1]][1])
                if i==3:
                    vars()[line[2]]=or3cc(vars()[line[-i]][0],vars()[line[-i]][1],vars()[line[-i+1]][0],vars()[line[-i+1]][1],vars()[line[-i+2]][0],vars()[line[-i+2]][1])
                if i==4:
                    vars()[line[2]]=or4cc(vars()[line[-i]][0],vars()[line[-i]][1],vars()[line[-i+1]][0],vars()[line[-i+1]][1],vars()[line[-i+2]][0],vars()[line[-i+2]][1],vars()[line[-i+3]][0],vars()[line[-i+3]][1])
                if i==5:
                    vars()[line[2]]=or5cc(vars()[line[-i]][0],vars()[line[-i]][1],vars()[line[-i+1]][0],vars()[line[-i+1]][1],vars()[line[-i+2]][0],vars()[line[-i+2]][1],vars()[line[-i+3]][0],vars()[line[-i+3]][1],vars()[line[-i+4]][0],vars()[line[-i+4]][1])
            if line[0]=="nor" or line[0]=="NOR":
                i=len(line[3:])
                if i==2:
                    vars()[line[2]]=nor2cc(vars()[line[-i]][0],vars()[line[-i]][1],vars()[line[-i+1]][0],vars()[line[-i+1]][1])
                if i==3:
                    vars()[line[2]]=nor3cc(vars()[line[-i]][0],vars()[line[-i]][1],vars()[line[-i+1]][0],vars()[line[-i+1]][1],vars()[line[-i+2]][0],vars()[line[-i+2]][1])
                if i==4:
                    vars()[line[2]]=nor4cc(vars()[line[-i]][0],vars()[line[-i]][1],vars()[line[-i+1]][0],vars()[line[-i+1]][1],vars()[line[-i+2]][0],vars()[line[-i+2]][1],vars()[line[-i+3]][0],vars()[line[-i+3]][1])
                if i==8:
                    vars()[line[2]]=nor8cc(vars()[line[-i]][0],vars()[line[-i]][1],vars()[line[-i+1]][0],vars()[line[-i+1]][1],vars()[line[-i+2]][0],vars()[line[-i+2]][1],vars()[line[-i+3]][0],vars()[line[-i+3]][1],vars()[line[-i+4]][0],vars()[line[-i+4]][1],vars()[line[-i+5]][0],vars()[line[-i+5]][1],vars()[line[-i+6]][0],vars()[line[-i+6]][1],vars()[line[-i+7]][0],vars()[line[-i+7]][1])
            if line[0]=="not" or line[0]=="NOT":
                vars()[line[2]]=not1cc(vars()[line[3]][0],vars()[line[3]][1])
            if line[0]=="buf" or line[0]=="BUFF":
                vars()[line[2]]=buf1cc(vars()[line[3]][0],vars()[line[3]][1])


    for i in range(len(const)-1,-1,-1):
        if const[i][0]=="not" or const[i][0]=="NOT":
            vars()[const[i][2]][2]=not1co(vars()[const[i][2]][2])
        if const[i][0]=="buf" or const[i][0]=="BUFF":
            vars()[const[i][2]][2]=buf1co(vars()[const[i][2]][2])

        if const[i][0]=='and' or const[i][0]=='AND':
            x=len(const[i][3:])
            if x==2:
                a,b=and2co(vars()[const[i][2]][2],vars()[const[i][-x]][1],vars()[const[i][-x+1]][1])
                vars()[const[i][-x]][2]=a
                vars()[const[i][-x+1]][2]=b
            if x==3:
                a,b,c=and3co(vars()[const[i][2]][2],vars()[const[i][-x]][1],vars()[const[i][-x+1]][1],vars()[const[i][-x+2]][1])
                vars()[const[i][-x]][2]=a
                vars()[const[i][-x+1]][2]=b
                vars()[const[i][-x+2]][2]=c
            if x==4:
                a,b,c,d=and4co(vars()[const[i][2]][2],vars()[const[i][-x]][1],vars()[const[i][-x+1]][1],vars()[const[i][-x+2]][1],vars()[const[i][-x+3]][1])
                vars()[const[i][-x]][2]=a
                vars()[const[i][-x+1]][2]=b
                vars()[const[i][-x+2]][2]=c
                vars()[const[i][-x+3]][2]=d

            if x==5:
                a,b,c,d,e=and5co(vars()[const[i][2]][2],vars()[const[i][-x]][1],vars()[const[i][-x+1]][1],vars()[const[i][-x+2]][1],vars()[const[i][-x+3]][1],vars()[const[i][-x+4]][1])
                vars()[const[i][-x]][2]=a
                vars()[const[i][-x+1]][2]=b
                vars()[const[i][-x+2]][2]=c
                vars()[const[i][-x+3]][2]=d
                vars()[const[i][-x+4]][2]=e
            if x==8:
                a,b,c,d,e,f,g,h=and8co(vars()[const[i][2]][2],vars()[const[i][-x]][1],vars()[const[i][-x+1]][1],vars()[const[i][-x+2]][1],vars()[const[i][-x+3]][1],vars()[const[i][-x+4]][1],vars()[const[i][-x+5]][1],vars()[const[i][-x+6]][1],vars()[const[i][-x+7]][1])
                vars()[const[i][-x]][2]=a
                vars()[const[i][-x+1]][2]=b
                vars()[const[i][-x+2]][2]=c
                vars()[const[i][-x+3]][2]=d
                vars()[const[i][-x+4]][2]=e
                vars()[const[i][-x+5]][2]=f
                vars()[const[i][-x+6]][2]=g
                vars()[const[i][-x+7]][2]=h

            if x==9:
                a,b,c,d,e,f,g,h,ic = and9co(vars()[const[i][2]][2],vars()[const[i][-x]][1],vars()[const[i][-x+1]][1],vars()[const[i][-x+2]][1],vars()[const[i][-x+3]][1],vars()[const[i][-x+4]][1],vars()[const[i][-x+5]][1],vars()[const[i][-x+6]][1],vars()[const[i][-x+7]][1],vars()[const[i][-x+8]][1])
                vars()[const[i][-x]][2]=a
                vars()[const[i][-x+1]][2]=b
                vars()[const[i][-x+2]][2]=c
                vars()[const[i][-x+3]][2]=d
                vars()[const[i][-x+4]][2]=e
                vars()[const[i][-x+5]][2]=f
                vars()[const[i][-x+6]][2]=g
                vars()[const[i][-x+7]][2]=h
                vars()[const[i][-x+8]][2]=ic

        if const[i][0]=='nand' or const[i][0]=='NAND':
            x=len(const[i][3:])
            if x==2:
                a,b=and2co(vars()[const[i][2]][2],vars()[const[i][-x]][1],vars()[const[i][-x+1]][1])
                vars()[const[i][-x]][2]=a
                vars()[const[i][-x+1]][2]=b
            if x==3:
                a,b,c=and3co(vars()[const[i][2]][2],vars()[const[i][-x]][1],vars()[const[i][-x+1]][1],vars()[const[i][-x+2]][1])
                vars()[const[i][-x]][2]=a
                vars()[const[i][-x+1]][2]=b
                vars()[const[i][-x+2]][2]=c
            if x==4:
                a,b,c,d=and4co(vars()[const[i][2]][2],vars()[const[i][-x]][1],vars()[const[i][-x+1]][1],vars()[const[i][-x+2]][1],vars()[const[i][-x+3]][1])
                vars()[const[i][-x]][2]=a
                vars()[const[i][-x+1]][2]=b
                vars()[const[i][-x+2]][2]=c
                vars()[const[i][-x+3]][2]=d
            if x==5:
                a,b,c,d,e=and5co(vars()[const[i][2]][2],vars()[const[i][-x]][1],vars()[const[i][-x+1]][1],vars()[const[i][-x+2]][1],vars()[const[i][-x+3]][1],vars()[const[i][-x+4]][1])
                vars()[const[i][-x]][2]=a
                vars()[const[i][-x+1]][2]=b
                vars()[const[i][-x+2]][2]=c
                vars()[const[i][-x+3]][2]=d
                vars()[const[i][-x+4]][2]=e
            if x==8:
                a,b,c,d,e,f,g,h=and8co(vars()[const[i][2]][2],vars()[const[i][-x]][1],vars()[const[i][-x+1]][1],vars()[const[i][-x+2]][1],vars()[const[i][-x+3]][1],vars()[const[i][-x+4]][1],vars()[const[i][-x+5]][1],vars()[const[i][-x+6]][1],vars()[const[i][-x+7]][1])
                vars()[const[i][-x]][2]=a
                vars()[const[i][-x+1]][2]=b
                vars()[const[i][-x+2]][2]=c
                vars()[const[i][-x+3]][2]=d
                vars()[const[i][-x+4]][2]=e
                vars()[const[i][-x+5]][2]=f
                vars()[const[i][-x+6]][2]=g
                vars()[const[i][-x+7]][2]=h

        if const[i][0]=='or' or const[i][0]=='OR':
            x=len(const[i][3:])
            if x==2:
                a,b=or2co(vars()[const[i][2]][2],vars()[const[i][-x]][0],vars()[const[i][-x+1]][0])
                vars()[const[i][-x]][2]=a
                vars()[const[i][-x+1]][2]=b
            if x==3:
                a,b,c=or3co(vars()[const[i][2]][2],vars()[const[i][-x]][0],vars()[const[i][-x+1]][0],vars()[const[i][-x+2]][0])
                vars()[const[i][-x]][2]=a
                vars()[const[i][-x+1]][2]=b
                vars()[const[i][-x+2]][2]=c
            if x==4:
                a,b,c,d=or4co(vars()[const[i][2]][2],vars()[const[i][-x]][0],vars()[const[i][-x+1]][0],vars()[const[i][-x+2]][0],vars()[const[i][-x+3]][0])
                vars()[const[i][-x]][2]=a
                vars()[const[i][-x+1]][2]=b
                vars()[const[i][-x+2]][2]=c
                vars()[const[i][-x+3]][2]=d
            if x==5:
                a,b,c,d,e=or5co(vars()[const[i][2]][2],vars()[const[i][-x]][0],vars()[const[i][-x+1]][0],vars()[const[i][-x+2]][0],vars()[const[i][-x+3]][0],vars()[const[i][-x+4]][0])
                vars()[const[i][-x]][2]=a
                vars()[const[i][-x+1]][2]=b
                vars()[const[i][-x+2]][2]=c
                vars()[const[i][-x+3]][2]=d
                vars()[const[i][-x+4]][2]=e
        if const[i][0]=='nor' or const[i][0]=='NOR':
            x=len(const[i][3:])
            if x==2:
                a,b=or2co(vars()[const[i][2]][2],vars()[const[i][-x]][0],vars()[const[i][-x+1]][0])
                vars()[const[i][-x]][2]=a
                vars()[const[i][-x+1]][2]=b
            if x==3:
                a,b,c=or3co(vars()[const[i][2]][2],vars()[const[i][-x]][0],vars()[const[i][-x+1]][0],vars()[const[i][-x+2]][0])
                vars()[const[i][-x]][2]=a
                vars()[const[i][-x+1]][2]=b
                vars()[const[i][-x+2]][2]=c
            if x==4:
                a,b,c,d=or4co(vars()[const[i][2]][2],vars()[const[i][-x]][0],vars()[const[i][-x+1]][0],vars()[const[i][-x+2]][0],vars()[const[i][-x+3]][0])
                vars()[const[i][-x]][2]=a
                vars()[const[i][-x+1]][2]=b
                vars()[const[i][-x+2]][2]=c
                vars()[const[i][-x+3]][2]=d
            if x==8:
                a,b,c,d,e,f,g,h=or8co(vars()[const[i][2]][2],vars()[const[i][-x]][0],vars()[const[i][-x+1]][0],vars()[const[i][-x+2]][0],vars()[const[i][-x+3]][0],vars()[const[i][-x+4]][0],vars()[const[i][-x+5]][0],vars()[const[i][-x+6]][0],vars()[const[i][-x+7]][0])
                vars()[const[i][-x]][2]=a
                vars()[const[i][-x+1]][2]=b
                vars()[const[i][-x+2]][2]=c
                vars()[const[i][-x+3]][2]=d
                vars()[const[i][-x+4]][2]=e
                vars()[const[i][-x+5]][2]=f
                vars()[const[i][-x+6]][2]=g
                vars()[const[i][-x+7]][2]=h
        if const[i][0]=='xor' or const[i][0]=='XOR':
            x=len(const[i][3:])
            if x==2:
                a,b=xor2co(vars()[const[i][2]][2],vars()[const[i][-x]][0],vars()[const[i][-x]][1],vars()[const[i][-x+1]][0],vars()[const[i][-x+1]][1])
                vars()[const[i][-x]][2]=a
                vars()[const[i][-x+1]][2]=b

    scoap=[]
    for i in inp:
        scoap.append([i,vars()[i][0],vars()[i][1],vars()[i][2]])
    for i in wire:
        scoap.append([i,vars()[i][0],vars()[i][1],vars()[i][2]])
    for i in out:
        scoap.append([i,vars()[i][0],vars()[i][1],vars()[i][2]])
    return scoap

import os
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np

files = []
for i in os.listdir('Patterns/verilog/'):
    print(i)
    scoap = np.array(scoap_values('Patterns/verilog/'+i))
    scoap = scoap.transpose()
    df = pd.DataFrame({'Nodes': scoap[0][:],
                       'CC0': scoap[1][:],
                       'CC1': scoap[2][:],
                       'CO' : scoap[3][:]})
    writer = ExcelWriter('Patterns/verilog/'+i.replace('.v','')+'.xlsx')
    df.to_excel(writer, 'Sheet1', index=False)
    writer.save()