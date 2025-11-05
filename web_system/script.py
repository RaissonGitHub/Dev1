# Necessário apenas se for executar sem o comando shell
from manage import *
import contextlib, io

saida = io.StringIO()

# Inicialização do django e definição das configurações
with contextlib.redirect_stdout(saida):
    main()

# Seus imports necessários
from relacionamentos.models.reporter import Reporter
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


def criarReporter(name, email, cod, cpf):
    try:
        if len(Reporter.objects.find_by_name(name)) == 0:
            r = Reporter()
            r.name = name
            r.email = email
            r.cod = cod
            r.cpf = cpf
            r.full_clean()
            r.save()
            return r
        else:
            return "Usuário já cadastrado"
    except ValidationError as e:
        print(e)
        raise e


def __main__():
    flag = True
    while flag:
        print("\n== MENU ===")
        print("1. Criar Reporters")
        print("2. Criar Super usuário")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("=== Criando registros para Reporters ===")
            print(criarReporter("Jorge Nunes","jorge.nunes@gmail.com", "arefv43", "07974923059"))
            print(criarReporter("Matheus Pinto","matheus.pinto@gmail.com", "efdf34c", "04610693003"))
            print(criarReporter("Ana Navalha","ana.navalha@gmail.com", "cvfg31", "73686695014"))

        if opcao == "2":
            print("=== Criando super usuário ===")
            nome = 'ifrs'
            senha = 'ifrs'
            User = get_user_model()
            User.objects.create_superuser(nome, '', senha)
            print(f"Usuário criado com nome: {nome} e senha: {senha}")

        elif opcao == "0":
            print("Saindo do script...")
            flag = False
    print("Fim do script.")


if __name__ == "__main__":
    __main__()
