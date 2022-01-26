#!/usr/bin/env python
# coding: utf-8

# In[196]:


import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sn
import calendar
from datetime import datetime


# In[157]:


tabela_1 = pd.read_csv('desafio_details.csv.xls')


# In[158]:


tabela_2 = pd.read_csv('desafio_priceav.csv.xls')


# In[159]:


faturamento = tabela_2
tabela3 = pd.merge(faturamento, tabela_1, how='left', on='airbnb_listing_id')
display(tabela3[tabela3.occupied == 1])


# In[160]:


#1. Ordene os bairros em ordem crescente de número de listings
crescente_listing = tabela3[['airbnb_listing_id','suburb','price_string']].groupby(['airbnb_listing_id', 'suburb']).sum()
display(crescente_listing)


# In[165]:


#2. Ordene os bairros em ordem crescente de faturamento médio dos listings
crescente_faturamento = crescente_listing.sort_values(['price_string'])
display(crescente_faturamento)


# In[184]:


#3.Existem correlações entre as características de um anúncio e seu faturamento?
características_anuncio = tabela3[['airbnb_listing_id','star_rating','price_string', 'number_of_reviews', 'is_superhost','ad_name']].groupby(['airbnb_listing_id', 'star_rating','is_superhost','number_of_reviews','ad_name']).sum()
Crescente = características_anuncio.sort_values(['price_string'],ascending=False)
display(Crescente)


# In[185]:


#3.Existem correlações entre as características de um anúncio e seu faturamento?
correlação = Crescente.corr(method='pearson')
plt.matshow(correlação)
plt.show()


# In[362]:


Datas = tabela3[['date','booked_on','airbnb_listing_id','occupied']]
Datas.drop(Datas.loc[Datas['booked_on']=='blank'].index, inplace=True)
Datas['booked_on']=pd.to_datetime(Datas['booked_on'].astype(str), format='%Y-%m-%d')
Datas['date']=pd.to_datetime(Datas['date'].astype(str), format='%Y-%m-%d')
display(Datas)


# In[359]:


Datas['Difference'] = Datas['date'].sub(Datas['booked_on'], axis=0)

