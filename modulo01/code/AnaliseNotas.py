import numpy as np
import matplotlib.pyplot as mplot

# lista de notas de alunos
notas_alunos = (5.6, 7.2, 9.3, 6.8, 8.4, 7.5, 6.0, 5.1, 9.7, 8.2)

# convertendo para array
notas_como_array = np.array(notas_alunos)

# média das notas
media_notas = np.mean(notas_como_array)

# encontrando a maior nota
maior_nota = np.max(notas_como_array)
# encontrando a menor nota
menor_nota = np.min(notas_como_array)

# quantidade de alunos com nota acima da média
quantidade_alunos_acima_media = np.sum(notas_como_array > media_notas)

# aplicando acréscimo as notas
notas_acrescidas = np.multiply(notas_como_array, 1.10)
notas_acrescidas = np.minimum(notas_acrescidas, 10.0)

# geração do gráfico de barras
fig, ax = mplot.subplots()
bar_width = 0.35
indices = np.arange(len(notas_como_array))

ax.bar(indices - bar_width/2, notas_como_array, bar_width, label='Notas Originais')
ax.bar(indices + bar_width/2, notas_acrescidas, bar_width, label='Notas Ajustadas (+10%)')

# linha de corte (média)
ax.axhline(y=media_notas, color='red', linestyle='--', label=f'Média: {media_notas:.2f}')

# labels do gráfico
ax.set_title('Notas originais, ajustadas e média')
ax.set_xlabel('Alunos')
ax.set_ylabel('Notas')
ax.set_xticks(indices)
ax.set_xticklabels([f'Al.{i+1}' for i in range(len(notas_como_array))])
ax.legend()

# Apresentando o gráfico
mplot.tight_layout()
mplot.show()