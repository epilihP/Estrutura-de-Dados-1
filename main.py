chamados=[]
id= 1

def cadastrar_chamados (descricao, prioridade):
    global id
    chamado ={
        "id": id,
        "descricao" : descricao,
        "prioridade" : prioridade,
        "finalizado" : False
    }
    chamados.append(chamado)
    id += 1
    print(f"Chamado{chamado['id']} cadastrado com sucesso." )


def buscar_chamado(id_chamado=None, descricao=None):
    encontrados = []
    for chamado in chamados:
        if id_chamado and chamado['id'] == id_chamado:
            encontrados.append(chamado)
        elif descricao and descricao.lower() in chamado['descricao'].lower():
            encontrados.append(chamado)
    return encontrados


def remover_chamados_finalizados(): # ------------- re-integrado
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
    global chamados, id
    chamados.clear()  
    id = 1  # Reseta did de IDs n confunde
    print("Todos os chamados foram revertidos e a lista foi limpa.")

cadastrar_chamados("Erro ao acessar a aplicação", 3)
cadastrar_chamados("Bug no sistema",7)
cadastrar_chamados("sobrecarga de servidor", 1)

# aqui buscar por ID
resultado = buscar_chamado(id_chamado=1)
for chamado in resultado:
    print(chamado)

# aqui busca por descrição - check
resultado = buscar_chamado(descricao="sistema")
for chamado in resultado:
    print(chamado)

    #
resultado = listar_chamados_por_prioridade()
for chamado in resultado:
    print(chamado)

#exibe as estatisticas - check
exibir_estatisticas()


#mostra um chamado como finalizado - check
chamados[0]['finalizado'] = True

print(chamados)

#remove os chamados finalizados -check
remover_chamados_finalizados()

print(chamados)

# Limpar lista de chamados -check
reverter_e_limpar()

