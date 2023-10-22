import pandas as pd 

df=pd.read_csv("truth.csv")

for r in df.TruthOrDare:
    a=input("start:")
    if a=='1':
        print(r)
        answer=input('input:')
        l=[]
        l.extend(answer)
        df2=pd.DataFrame(l,index=range(len(l)))
        print(l)