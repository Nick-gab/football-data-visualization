import pandas as pd
import matplotlib.pyplot as plt


arquivo = r"d:\archive\campeonato-brasileiro-gols.csv"
df = pd.read_csv(arquivo)
 
# Extrai o número da rodada e converte para inteiro
df["rodada_num"] = df["rodata"].astype(str).str.extract(r"(\d+)").astype(int)

# Conta quantos gols foram feitos por rodada
gols_por_rodada = df["rodada_num"].value_counts().sort_index()

# Cria o gráfico
plt.figure(figsize=(10, 5))
plt.plot(gols_por_rodada.index, gols_por_rodada.values, color='orange', linewidth=2)

# Estilo semelhante ao da imagem
plt.title("Gols por Rodada no Campeonato Brasileiro 2003 a 2024", fontsize=14)
plt.xlabel("Rodada", fontsize=12)
plt.ylabel("Quantidade de Gols", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()

plt.show()
