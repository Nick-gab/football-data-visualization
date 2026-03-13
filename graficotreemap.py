import pandas as pd
import plotly.express as px


arquivo = r"d:\archive\campeonato-brasileiro-gols.csv"
df = pd.read_csv(arquivo)
 
# Remove os gols contra
df_validos = df[df['tipo_de_gol'] != 'Gol Contra']

# Conta os gols por atleta
goleadores = df_validos['atleta'].value_counts().reset_index()
goleadores.columns = ['Atleta', 'Quantidade']

# Seleciona os 20 maiores goleadores
top_goleadores = goleadores.head(20)

# Gera o Treemap
fig = px.treemap(
    top_goleadores,
    path=['Atleta'],
    values='Quantidade',
    title='Top 20 Goleadores - Campeonato Brasileiro 2003 a 2024',
    color='Quantidade',
    color_continuous_scale='Reds'
)

fig.show()