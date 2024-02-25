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

def exibir_eap(eap, nivel=0):
    for chave, valor in eap.items():
        print("  " * nivel + "- " + chave)
        exibir_eap(valor, nivel + 1) if valor else None

exibir_eap(eap)
