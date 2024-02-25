import matplotlib.pyplot as plt
from datetime import datetime

# Datas planejadas para a conclusão das tarefas e a quantidade planejada de trabalho restante
datas_planejadas = ["2024-02-01", "2024-02-05", "2024-02-10", "2024-02-15", "2024-02-20", "2024-02-25"]
trabalho_planejado = [100, 80, 60, 40, 20, 0]

# Datas reais de conclusão das tarefas e quantidade real de trabalho restante
datas_reais = ["2024-02-01", "2024-02-06", "2024-02-11", "2024-02-16", "2024-02-21", "2024-02-25"]
trabalho_real = [90, 75, 55, 35, 15, 0]

# Converter datas para objetos datetime
datas_planejadas = [datetime.strptime(data, "%Y-%m-%d") for data in datas_planejadas]
datas_reais = [datetime.strptime(data, "%Y-%m-%d") for data in datas_reais]

# Plotar o gráfico de burnup
plt.plot(datas_planejadas, trabalho_planejado, marker='o', label='Planejado')
plt.plot(datas_reais, trabalho_real, marker='o', linestyle='--', color='orange', label='Real')
plt.title('Gráfico de Burnup')
plt.xlabel('Data')
plt.ylabel('Trabalho Restante')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("burnup.png")
