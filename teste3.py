import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Datas planejadas para a conclusão das tarefas e a quantidade planejada de trabalho restante
datas_planejadas = [
    ("2024-02-01", 100),
    ("2024-02-05", 80),
    ("2024-02-10", 60),
    ("2024-02-15", 40),
    ("2024-02-20", 20),
    ("2024-02-25", 0)
]

# Converter as datas para objetos datetime
datas, trabalho_restante = zip(*datas_planejadas)
datas = [datetime.strptime(data, "%Y-%m-%d") for data in datas]

# Calcular a quantidade de trabalho restante em cada data
trabalho_acumulado = list(trabalho_restante)
for i in range(1, len(trabalho_acumulado)):
    trabalho_acumulado[i] += trabalho_acumulado[i - 1]

# Plotar o gráfico de burndown
plt.plot(datas, trabalho_acumulado, marker='o')
plt.title('Gráfico de Burndown')
plt.xlabel('Data')
plt.ylabel('Trabalho Restante')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('burndown.png')
