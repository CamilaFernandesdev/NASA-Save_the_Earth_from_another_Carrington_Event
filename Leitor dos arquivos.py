# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 15:55:47 2022.

@author: Camila Fernandes
"""
import cdflib
import spacepy
from spacepy import pycdf
from pathlib import Path


end = "wi_h2_mfi_20220101_v04.cdf"
path = Path(r'C:/Workspace/NASA-Save_the_Earth_from_another_Carrington_Event/wi_h2_mfi_20220101_v04.cdf')
teste_leitor = pycdf.CDF(end)

print(teste_leitor)