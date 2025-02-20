chamados=[]
id_cliente= 1

def cadastrar_chamados (descricao, prioridade):
    global id_cliente
    chamado ={
        "id": id_cliente,
        "descricao" : descricao,
        "prioridade" : prioridade,
        "finalizado" : False
    }
    chamados.append(chamado)
    id_clientes += 1
    print(f"Chamado{chamado[id]} cadastrado com sucesso." )