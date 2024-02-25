import matplotlib.pyplot as plt

def plotar_eap(eap, nivel=0, posicao=(0, 0)):
    if eap:
        for chave, valor in eap.items():
            plt.text(posicao[0], posicao[1], chave, va='center', ha='left', fontsize=10, fontweight='bold')
            if valor:
                novo_y = posicao[1] - 1
                plt.plot([posicao[0], posicao[0] + 1], [posicao[1], novo_y], linestyle='-', color='black')
                plotar_eap(valor, nivel + 1, (posicao[0] + 1, novo_y))

# Estrutura Analítica do Projeto (EAP)
eap = {
    "Projeto": {
        "Entregável 1": {
            "Tarefa 1.1": {},
            "Tarefa 1.2": {}
        },
        "Entregável 2": {
            "Tarefa 2.1": {},
            "Tarefa 2.2": {
                "Subtarefa 2.2.1": {},
                "Subtarefa 2.2.2": {}
            }
        }
    }
}

# Configurações do gráfico
plt.figure(figsize=(10, 6))
plt.axis('off')

# Plotar EAP
plotar_eap(eap)

# Exibir o gráfico
plt.savefig('eap.png')

