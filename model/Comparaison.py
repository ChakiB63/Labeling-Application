from datetime import datetime
import pandas as pd
import os
import random
import streamlit as st
import requirements as rqr
from openpyxl import load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows

def generate_random_pic(layer):
    str_file = random.choice(os.listdir(rqr.path_to_archieve+"/msg_fes_rgb_"+layer))
    return str_file

def regularize_str(_arg):
    _arg=':'.join(_arg.split('_'))
    return _arg

def file_to_datetime(filename):
    str_dt = filename[:-5][-19:] # to eleminate the extension and the Z added at the end of the name files.
    dt =regularize_str(str_dt)
    return dt

def verify_existence(layer, datetime1, datetime2, user):
    layer_df = pd.read_excel(rqr.path_to_excel, sheet_name=layer, header=0)
    for irow in range(len(layer_df)):
        if layer_df.iloc[irow,4] == user :
            if (layer_df.iloc[irow,0] == datetime1 and layer_df.iloc[irow,1] == datetime2) or (layer_df.iloc[irow,0] == datetime2 and layer_df.iloc[irow,1] == datetime1):
                return True
    return False

class Comparaison:

    def __init__(self, layer, user):
        nb_images= rqr.days_of_archieve * 96
        max_possible_combinations = len(st.secrets["passwords"]) * nb_images**4
        count = 0
        while True :
            if count >  max_possible_combinations:
                self._fin_archive = True
                break
            
            img1 = generate_random_pic(layer)
            img2 =  generate_random_pic(layer)

            dt1 = file_to_datetime(img1)
            dt2 = file_to_datetime(img2)
            if not verify_existence(layer, dt1, dt2, user) and dt1!=dt2:
                self._fin_archive = False
                self._layer = layer
                self._dt1 = dt1
                self._dt2 = dt2
                self._img1 = rqr.path_to_archieve+"/msg_fes_rgb_"+layer+"/"+img1
                self._img2 = rqr.path_to_archieve+"/msg_fes_rgb_"+layer+"/"+img2
                self._user = user
                break
            
            count+=1

        
    
    # Getters
    def get_layer(self):
        return self._layer
    
    def get_fin_archive(self):
        return self._fin_archive
    
    def get_dt1(self):
        return self._dt1

    def get_dt2(self):
        return self._dt2
    
    def get_img1(self):
        return self._img1

    def get_img2(self):
        return self._img2

    def get_percentage(self):
        return self._percentage

    def get_label(self):
        return self._label
    
    def get_user(self):
        return self._user


    # Setters
    def set_layer(self, value):
        self._layer = value

    def set_dt1(self, value):
        self._dt1 = value

    def set_dt2(self, value):
        self._dt2 = value

    def set_percentage(self, value):
        self._percentage = value

    def set_label(self, value):
        self._label = value


    def add(self):
        workbook = load_workbook(rqr.path_to_excel)
        sheet = workbook[self.get_layer()]
        nouvelle_ligne = [self.get_dt1(), self.get_dt2(), self.get_percentage(), self.get_label(), self.get_user(), datetime.now().isoformat()]
        new_df = pd.DataFrame([nouvelle_ligne], columns=['Datetime1', 'Datetime2', 'Similarity_percentage', 'Similarity_label','User','DatetimeAdded'])
        for row in dataframe_to_rows(new_df, index=False, header=False):
            sheet.append(row)

        workbook.save(rqr.path_to_excel)