import pandas as pd 
import matplotlib.pyplot as plt 


arquivo = r"d:\archive\campeonato-brasileiro-gols.csv"
df = pd.read_csv(arquivo)


top_artilheiros = df['atleta'].value_counts().head(10)

plt.figure(figsize=(12, 6))
barras = plt.bar(top_artilheiros.index, top_artilheiros.values, color="seagreen")

plt.title("Top 10 Artilheiros do Campeonato Brasileiro 2003 à 2024", fontsize=14)
plt.xlabel("Jogador")
plt.ylabel("Total de Gols")
plt.xticks(rotation=45, ha="right")


plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.show()
