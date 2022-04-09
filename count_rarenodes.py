import os
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from transition_probability import trans_prob
import numpy as np


for i in os.listdir('L:/final_year_project/Patterns/verilog'):
    
    a,b=trans_prob('L:/final_year_project/Patterns/verilog/'+i,0.001)

    b = np.array(b)
    b = b.transpose()
   
    df = pd.DataFrame({'Nodes': b[0][:],
                       'tp_0': b[1][:],
                       'tp_1': b[2][:]})
    writer = ExcelWriter('L:/final_year_project/Patterns/tp/0.001/'+i.replace('.v','')+'.xlsx')
    df.to_excel(writer, 'Sheet1', index=False)
    writer.save()
