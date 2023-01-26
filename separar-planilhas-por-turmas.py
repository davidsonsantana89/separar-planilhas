#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import pandas as pd


# In[3]:


caminho = r'C:\Users\david\OneDrive\ESCOLA\ETE LAL\CONTROLE DE FREQUÊNCIAS E NOTAS\2021\ELETIVAS\ANUAL\TURMAS\geral-anual.xlsx'


# In[4]:


df = pd.read_excel(caminho)


# In[5]:


df.head()


# In[6]:


turmas = df['TURMA'].unique()


# In[10]:


for turma in turmas:
    df[df['TURMA'] == turma].to_excel(r"C:\Users\david\OneDrive\ESCOLA\ETE LAL\CONTROLE DE FREQUÊNCIAS E NOTAS\2021\ELETIVAS\ANUAL\TURMAS" + '\\' + f'{turma}.xlsx', index=False)


# In[11]:


df.to_excel(r'C:\Users\david\OneDrive\ESCOLA\ETE LAL\CONTROLE DE FREQUÊNCIAS E NOTAS\2021\ELETIVAS\ANUAL\TURMAS\geral-anual.xlsx', index=False)


# In[ ]:




