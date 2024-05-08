from datetime import datetime
import pandas as pd
import sys

from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
import requirements as rqr

from openpyxl import load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows


class Image:

    def __init__(self, dt, user, layer):
        self._dt = dt
        self._user = user
        self._layer = layer

    def get_dt(self):
        return self._dt
    
    def get_phenomena_presence(self):
        return self._phenomena_presence
    
    def get_convection(self):
        return self._convection
    
    def get_dust(self):
        return self._dust
    
    def get_fog(self):
        return self._fog
    
    def get_fire_forest(self):
        return self._fire_forest
    
    def get_cold_drop(self):
        return self._cold_drop
    
    def get_user(self):
        return self._user
    
    def get_layer(self):
        return self._layer
    


    def set_dt(self,value):
        self._dt = value

    def set_phenomena_presence(self,value):
        self._phenomena_presence = value

    def set_convection(self,value):
        self._convection = value

    def set_dust(self,value):
        self._dust = value

    def set_fog(self,value):
        self._fog = value
    
    def set_fire_forest(self,value):
        self._fire_forest = value
    
    def set_cold_drop(self,value):
        self._cold_drop = value

    def verify_existence(self):
        df = pd.read_excel(rqr.path_to_excel, sheet_name="phenomena_infos", header=0)
        for irow in range(len(df)):
            if df.iloc[irow,0] == self.get_dt() and df.iloc[irow,1] == self.get_user() and df.iloc[irow,3] == self.get_layer() :
                return True
        return False

    def add(self):
        workbook = load_workbook(rqr.path_to_excel)
        sheet = workbook["phenomena_infos"]

        nouvelle_ligne = [self.get_dt(), self.get_user(), datetime.now().isoformat(), self.get_layer(), self.get_phenomena_presence()]+self.get_convection().infos_list()+self.get_dust().infos_list()+self.get_fog().infos_list()+self.get_fire_forest().infos_list()+self.get_cold_drop().infos_list()
        new_df = pd.DataFrame([nouvelle_ligne], columns=["Datetime", "User", "DatetimeAdded", "Layer", "Phenomena_presence", 
                                                        "Convection_phenomena","Convection_NW","Convection_NE","Convection_SE","Convection_SW",
                                                        "Dust_phenomena","Dust_NW","Dust_NE","Dust_SE","Dust_SW",
                                                        "Fog_phenomena","Fog_NW","Fog_NE","Fog_SE","Fog_SW",
                                                        "Fire_Forest_phenomena","Fire_Forest_NW","Fire_Forest_NE","Fire_Forest_SE","Fire_Forest_SW",
                                                        "Fire_Forest_phenomena","Fire_Forest_NW","Fire_Forest_NE","Fire_Forest_SE","Fire_Forest_SW"])
        for row in dataframe_to_rows(new_df, index=False, header=False):
            sheet.append(row)

        workbook.save(rqr.path_to_excel)
