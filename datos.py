import pandas as pd
import json
import constantes as cts
from grafica import Grafica

class myDatos:
    def __init__(self):
        self.init_variables()

    def append_data(self,jsonData:json):
        dict_data = json.loads(json.dumps(jsonData))
        union_data = {}
        union_data.update(dict_data)
        union_data.update(self.updata_data)
        self.all_Data.append(union_data)
        

    def get_data(self):
        self.df_data = pd.DataFrame(self.all_Data)
        self.df_all_data = self.df_data.copy()
        self.df_data = self.df_data.tail(1)
        return self.df_data
    
    def actualizar_data(self,datos):
        self.updata_data = {cts.voltaje_real:datos[0],cts.current:datos[1],cts.watts:datos[2]}

    def save_csv(self):
        self.df_all_data.to_csv('sensores.csv', index=False)
        

    def wait_data(self,wait:bool = False): 
        self.wait = wait

    def is_waiting(self)-> bool:
        return self.wait
    
    def init_variables(self):
        self.updata_data =  {cts.voltaje_real:0,cts.current:0,cts.watts:0}
        self.all_Data = []
        self.df_data = None
        self.wait = False
        self.df_all_data = None