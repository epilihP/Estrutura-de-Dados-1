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


def buscar_chamado(id_chamado=None, descricao=None):
    encontrados = []
    for chamado in chamados:
        if id_chamado and chamado['id'] == id_chamado:
            encontrados.append(chamado)
        elif descricao and descricao.lower() in chamado['descricao'].lower():
            encontrados.append(chamado)
    return encontrados


    global chamados
    chamados = [chamado for chamado in chamados if not chamado['finalizado']]
    print("Chamados finalizados removidos com sucesso.")


def listar_chamados_por_prioridade():# Função para listae chamados do > pro <
    chamados_ordenados = sorted(chamados, key=lambda x: x['prioridade'], reverse=True)
    return chamados_ordenados


def exibir_estatisticas():
    total_chamados = len(chamados)
    chamados_finalizados = sum(1 for chamado in chamados if chamado['finalizado'])
    chamados_nao_finalizados = total_chamados - chamados_finalizados
    print(f"Total de chamados: {total_chamados}")
    print(f"Chamados finalizados: {chamados_finalizados}")
    print(f"Chamados não finalizados: {chamados_nao_finalizados}")


def reverter_e_limpar():
    global chamados, id_cliente
    chamados.clear()  
    id_cliente= 1  # Reseta o contador de IDs n confunde
    print("Todos os chamados foram revertidos e a lista foi limpa.")
