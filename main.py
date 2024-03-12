import re
import uuid
import enum
import datetime

exec = True

class StatusTarefa(enum.Enum):
    """Enumeração para os status das tarefas."""
    A_FAZER = 1
    CONCLUIDO = 2
    ATRASADO = 3


class Tarefa:
    """Classe que representa uma tarefa."""

    def __init__(self, titulo, descricao, dias_para_conclusao):
        """Inicializa uma nova instância de Tarefa.

        Args:
            titulo (str): O título da tarefa.
            descricao (str): A descrição da tarefa.
            dias_para_conclusao (int): O número de dias para a conclusão da tarefa.
        """
        self.id = uuid.uuid4()
        self.titulo = titulo
        self.descricao = descricao
        self.data_conclusao = datetime.datetime.now() + datetime.timedelta(days = dias_para_conclusao)
        self.status = StatusTarefa.A_FAZER


tarefas = []


def main():
    """Função principal do programa."""
    while exec:
        print("Selecione uma opção abaixo:\n")
        opc = int(input("1 - Criar uma tarefa\n"
                        "2 - Consultar uma tarefa pelo ID\n"
                        "3 - Listar as tarefa\n"
                        "4 - Modificar uma tarefa\n"
                        "5 - Apagar uma tarefa\n"
                        "6 - Sair do programa\n"))
        match opc:
            case 1:
                criar()
            case 2:
                consultar()
            case 3:
                listar()
            case 4:
                modificar()
            case 5:
                apagar()
            case 6:
                print("ATÉ BREVE!")
                sair()
            case _:
                print("Digite um valor válido.\n")


def criar():
    """Cria uma nova tarefa e a adiciona à lista de tarefas."""
    titulo = input("Digite o título da tarefa: \n")
    descricao = input("Digite a descrição resumida da tarefa: \n")
    data_limite = int(input("Digite qual é o prazo para a conclusão da tarefa, em dias: \n"))

    _tarefa = Tarefa(titulo, descricao, data_limite)
    tarefas.append(_tarefa)
    print(f"Tarefa {_tarefa.titulo} foi criada e adicionado à lista.\n")


def set_tarefa():
    """Define o status de uma tarefa.

    Retorna:
        StatusTarefa: O status selecionado para a tarefa.

    Exceções:
        ValueError: Caso o número do status fornecido não seja válido.
    """
    while True:
        print("Status disponíveis:\n1 - A Fazer\n2 - Concluído\n3 - Atrasado")
        opcao = int(input("Digite o número do status que deseja atribuir à tarefa: "))
        if opcao == 1:
            return StatusTarefa.A_FAZER
        elif opcao == 2:
            return StatusTarefa.CONCLUIDO
        elif opcao == 3:
            return StatusTarefa.ATRASADO
        else:
            print("Opção inválida. Tente novamente.")


def consultar():
    """Consulta uma tarefa pelo seu ID."""
    _id = input("Digite o ID da tarefa que deseja consultar: ")
    if(re.match(r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$', _id)):
        _id = uuid.UUID(_id)
        for tarefa in tarefas:
            if tarefa.id == _id:
                print(f"Id: {tarefa.id}\n"
                      f"Titulo: {tarefa.titulo}\n"
                      f"Data de conclusão: {tarefa.data_conclusao}\n"
                      f"Descrição: {tarefa.descricao}\n"
                      f"Status da tarefa: {tarefa.status}")
            else:
                print("Nenhuma tarefa encontrada com o Id informado.\n")
    else:
        print("Nenhuma tarefa encontrada com o Id informado.\n")


def listar():
    """Lista todas as tarefas."""
    if len(tarefas) > 0:
        for tarefa in tarefas:
            print(f"Id: {tarefa.id}\n"
                  f"Titulo: {tarefa.titulo}\n"
                  f"Data de conclusão: {tarefa.data_conclusao}\n"
                  f"Descrição: {tarefa.descricao}\n"
                  f"Status da tarefa: {tarefa.status}")
    else:
        print("Nenhuma tarefa na lista.\n")


def apagar():
    """Apaga uma tarefa da lista de tarefas."""
    _id = input("Digite o Id do registro que deseja apagar: \n")
    for tarefa in tarefas:
        if tarefa:
            tarefas.remove(tarefa)
            print(f"Objeto com o id {tarefa.id} removido da lista.\n")
        else:
            print("Nenhum registro encontrado com o Id informado.\n")


def modificar():
    """Modifica uma tarefa existente."""
    _id = input("Digite o ID do registro que deseja editar: \n")
    if (re.match(r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$', _id)):
        _id = uuid.UUID(_id)
        for tarefa in tarefas:
            if tarefa.id == _id:

                titulo = input("Digite o novo título da tarefa: \n")
                descricao = input("Digite a nova descrição resumida da tarefa: \n")
                data_limite = int(input("Digite qual é o novo prazo para a conclusão da tarefa, em dias: \n"))
                status = set_tarefa()

                tarefa.titulo = titulo
                tarefa.descricao = descricao
                tarefa.data_limite = datetime.datetime.now() + datetime.timedelta(days=data_limite)
                tarefa.status = status

                print(f"Id: {tarefa.id}\n"
                      f"Titulo: {tarefa.titulo}\n"
                      f"Data de conclusão: {tarefa.data_conclusao}\n"
                      f"Descrição: {tarefa.descricao}\n"
                      f"Status da tarefa: {tarefa.status}")

    else:
        print("Nenhum registro encontrado com o Id informado.\n")


def sair():
    """Sai do programa."""
    global exec
    exec = False


main()
