
# %%

from sondakika_local import Local
import pandas as pd
from pathlib import Path
 
# %%    
 
# %% Verileri indir
def get_haber(dosyaadi:str="data.csv", isDistrict:bool=False) -> pd.DataFrame:

    data = []
    
    for il, ilçeler in Local.sehirler.items():
        print(f"{il} ili haberleri:")
        local = Local(il) 
        
        if isDistrict:
            for ilçe in ilçeler:
                print(f"{ilçe} ilçesi haberleri:")
                city = ilçe
                local = Local(city)
                newss = local.news(limit=10000)
                for key in newss:
                    newss[key]['city2'] = il.lower()
                data.extend(list(newss.values()))
        else:
            newss = local.news()
            data.extend(list(newss.values()))
            for key in newss:
                newss[key]['city2'] = il.lower()


    csvFile=Path(dosyaadi)
    df = pd.DataFrame(data)
    
    if csvFile.exists():
        df2=pd.read_csv(csvFile)
        df=pd.concat([df,df2],ignore_index=True)
        csvFile.unlink()
 
    df = df.drop_duplicates(subset=['title']) 
    df['tarih'] = pd.to_datetime(df['tarih'], errors='coerce')
    df.to_csv(csvFile)
    return df

csvFile=Path("haber_il.csv")
df=get_haber(csvFile.name)

 

 

 

# %% Veri Önişleme


dfil=pd.read_csv("haber_il.csv")
dfilce=pd.read_csv("haber_ilce.csv")



df = pd.concat([dfil,dfilce],ignore_index=True)
df = df.drop_duplicates(subset=['title']) 
df.drop("Unnamed: 0",axis=1,inplace=True)
df.dropna()

# %%

df['tarih'] = pd.to_datetime(df['tarih'], errors='coerce')
df['city2']=df['city2'].apply(lambda x:x.lower())

df[df["city"] != df["city2"] ].head()

# %%
