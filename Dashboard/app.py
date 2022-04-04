from datetime import date
from pyparsing import col
import streamlit as st
import pandas as pd
import numpy as np
import spacy
from wordcloud import WordCloud
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt


def load_data():

    data = pd.read_csv('data_sentimento.csv')

    return data

data = load_data()
st.cache(persist = True)    


st.sidebar.title('Monitoramento das reviews do Mouse')
st.sidebar.subheader('Ednael Vieira e Priscilla Amarante')

page = st.sidebar.selectbox("Opções", ["Score", "Nuvem de palavras", "Resultado dos modelos"]) 


if page == "Score":
    st.title('Analise de sentimento')

    select = st.sidebar.selectbox('Vizualização', ['line chart'], key=1)

    mes_cont = pd.read_csv('mes_cont.csv')

    line_plot = px.line(data_frame=mes_cont, 
                        x='novas_data', 
                        y='mes_perc', 
                        color='sentimento',
                        markers=True,
                        labels={'novas_data' : 'mes',
                                'mes_perc' : 'Porcentagem score (%)'},
                        color_discrete_sequence=['red', 'green', 'blue'],
                        title='Score por mes',
                        )

    st.plotly_chart(line_plot)

elif page == 'Nuvem de palavras':
    st.title('Nuvem de palavras')
    
    select = st.sidebar.selectbox('Sentimento', ['Bom','Ruim'], key=1)

    mes_cont = pd.read_csv('mes_cont.csv')
    
    # Create stopword set
    nlp = spacy.load('pt_core_news_sm')
    stopwords = set(nlp.Defaults.stop_words)
    stopwords.update(['mouse', 'custo', 'produto', 'bom', 'dia', 'funciona'])
    
    if(select == 'Bom'):
        text_bom = " ".join(str(description) for description in data[data['sentimento'] == 'Bom']['description'])
        wc = WordCloud(stopwords=stopwords, background_color="white").generate(text_bom)

    else:
        text_ruim = " ".join(str(description) for description in data[data['sentimento'] == 'Ruim']['description'])
        wc = WordCloud(stopwords=stopwords, background_color="white").generate(text_ruim)
    
    fig, ax = plt.subplots(figsize = (12, 8))
    ax.imshow(wc, interpolation = 'bilinear')
    plt.axis('off')
    st.pyplot(fig)


elif page == "Resultado dos Modelos":
    st.title("Modelos")
    
    
else:
    st.title("Modelos")
    
    modelo = pd.read_csv('modelo.csv',encoding='latin-1')
    st.table(modelo)

    




    


    
    



    


