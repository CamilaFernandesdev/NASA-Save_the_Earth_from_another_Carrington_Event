# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 15:55:47 2022.

@author: Camila Fernandes
"""
import cdflib
#import spacepy
import numpy as np
#from spacepy import pycdf
from pathlib import Path
import xarray as xr


#end = "wi_h2_mfi_20220101_v04.cdf"
path = Path(r'C:/Workspace/NASA-Save_the_Earth_from_another_Carrington_Event/wi_h2_mfi_20220101_v04.cdf')
#teste_leitor = pycdf.CDF(end)
#print(teste_leitor)

teste_leitor2 = cdflib.CDF(path=path, validate=False, string_encoding='ascii')

data = cdflib.cdf_to_xarray(path)
c = cdflib.cdfastropy()
atributos = cdflib.CDF.print_attrs(teste_leitor2)

#%% tINFO

atributos_gloabal = teste_leitor2.globalattsget()
info = teste_leitor2.cdf_info()
basic_var = teste_leitor2.varinq(variable = 'SENS1_I')
selec_atributo = teste_leitor2.attget(attribute= 0, entry=0)
sens1_I = data.SENS1_I.to_numpy() #ndim = 3
a = data.SENS1_I
