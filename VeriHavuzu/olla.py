# %%
from sondakika_local import Local
import pandas as pd
from pathlib import Path
import json
from tqdm import tqdm

tqdm.pandas()
# %%


dfil=pd.read_csv("haber_il.csv")
dfilce=pd.read_csv("haber_ilce.csv")

df = pd.concat([dfil,dfilce],ignore_index=True)
df = df.drop_duplicates(subset=['title']) 
df.drop("Unnamed: 0",axis=1,inplace=True)
df['tarih'] = pd.to_datetime(df['tarih'], errors='coerce')
df['city2']=df['city2'].apply(lambda x:x.lower())

df.dropna()
 



# %%
from ollama import Client
from ollama  import GenerateResponse

client = Client(
  host='http://192.168.200.38:11434',
  headers={'x-some-header': 'some-value'}
)

def Suc_Turu(metin:str):
    
    prompt = """

    gruplar:    
    Kişilere Karşı İşlenen Suçlar
    Mala Karşı İşlenen Suçlar
    Ekonomik Suçlar
    Siber Suçlar
    Düzen ve Kamu Güvenliğine Karşı İşlenen Suçlar
    Narkotik Suçları
    Organize Örgüt Suçları
    Hiçbiri

    sana vereceğim haber metni için yukardaki gruplardan birini seç ve 
    Cevabı sadece suç_türü özelliği içeren json formatında ver. haber içeriği bir suç içermiyorsa Hiçbiri grubunu seç
 

    Haber Metni :
    {}


    """.format(metin)


    
    response: GenerateResponse = client.generate(model='llama3.1:70b', prompt=prompt,format="json",keep_alive="40h")
 
    # print(metin) 
    # print(response["response"]) 
    return response["response"]

def Suc_Iceriklimi(metin:str):
    
    prompt = """
 

    sana vereceğim haber metni suç içerikli ise {{'suc' = 1}} , değil ise {{'suc' = 0}} şeklinde json formatında dönüş yap
     

    Haber Metni :
    {}


    """.format(metin)


    
    response: GenerateResponse = client.generate(model='llama3.1:70b', prompt=prompt,format="json",keep_alive="40h")
 
    # print(metin) 
    # print(response["response"]) 
    return response["response"]
# %%

# df=df.head(15000)
df_grouped = df.groupby('city')
df_sample =df_grouped.apply(lambda x: x.sample(n=min(len(x), 8)))
 
df_sample['suc_turu_title'] = df_sample.progress_apply(lambda x: Suc_Turu(x['title']) , axis=1)
# df_sample.to_csv("haberler_tur1.csv")
df_sample['suc_turu_content'] = df_sample.progress_apply(lambda x: Suc_Turu(x['content']) , axis=1)
df_sample=df_sample.reset_index(drop=True)
df_sample.to_csv("haberler_tur.csv")

# %%

df_sample=pd.read_csv("haberler_tur.csv")

 
# df_sample=df_sample.reset_index(drop=True)
# df_sample['suc_turu_content1'] = df_sample['suc_turu_content'].apply(lambda x: json.loads(x).get('suç_türü'))
# df_sample['suc_turu_title1'] = df_sample['suc_turu_title'].apply(lambda x: json.loads(x).get('suç_türü'))
# df_sample.drop(columns=['suc_turu_content','suc_turu_title','Unnamed: 0'], inplace=True)

df_sample['suc_turu'] = df_sample.apply(lambda x: 'Hiçbiri' if x['suc_turu_title1'] == 'Hiçbiri' else x['suc_turu_content1'],axis=1)
 
df_sample['SucIcerikliMi'] = df_sample['suc_turu'].apply(lambda x: 0 if x == 'Hiçbiri' else 1)
df_sample = df_sample[df_sample['suc_turu_content1'] == df_sample['suc_turu_title1']]
# df_sample = df_sample[df_sample['suc_turu_content1'] != 'Hiçbiri']
# df_sample = df_sample[df_sample['suc_turu_title1'] != 'Hiçbiri']


df_sample = df_sample.sort_values(by=['SucIcerikliMi', 'suc_turu'])

df_sample.drop(columns=['suc_turu_content1','suc_turu_title1','Unnamed: 0'], inplace=True)
df_sample.reset_index(drop=True)
df_sample.to_csv('haberler_cleaned.csv')
df_sample.to_excel('haberler_cleaned.xlsx')


 

# %%
 
# %%
df_sample['suc_turu_title1'] = df_sample['suc_turu_title'].apply(lambda x: json.loads(x).get('suç_türü'))
# %%


df_grouped2 = df_sample.groupby('suc_turu')
df_sample2 =df_grouped2.apply(lambda x: x.sample(n=min(len(x), 1)))
df_sample2.to_excel()
# %%
