from datetime import date

from matplotlib import pyplot as plt
from models import Conta, Historico, Status, Tipos, engine
from sqlmodel import Session, select

def criar_conta(conta: Conta):
    with Session(engine) as session:
        statement = select(Conta).where(Conta.banco==conta.banco)
        results = session.exec(statement).all()
        if results:
            print("Já existe uma conta nesse banco!")
            return
        session.add(conta)
        session.commit()
        return conta

def listar_contas():
    with Session(engine) as session:
        statement = select(Conta)
        results = session.exec(statement).all()
        return results
    
def desativar_conta(id):
    with Session(engine) as session:
        statement = select(Conta).where(Conta.id==id)
        conta = session.exec(statement).first()
        if conta.valor > 0:
            raise ValueError('Essa conta ainda possui saldo, não é possível desativar.')
        conta.status = Status.INATIVO
        session.commit()

def transferir_saldo(id_conta_saida, id_conta_entrada, valor):
    with Session(engine) as session:
        statement = select(Conta).where(Conta.id==id_conta_saida)
        conta_saida = session.exec(statement).first()
        if conta_saida.valor < valor:
            raise ValueError('Saldo insuficiente')
        statement = select(Conta).where(Conta.id==id_conta_entrada)
        conta_entrada = session.exec(statement).first()

        conta_saida.valor -= valor
        conta_entrada.valor += valor
        session.commit()
    
def movimentar_dinheiro(historico: Historico):
    with Session(engine) as session:
        statement = select(Conta).where(Conta.id==historico.conta_id)
        conta = session.exec(statement).first()
        if historico.tipo == Tipos.ENTRADA:
            conta.valor += historico.valor
        else:
            if conta.valor < historico.valor:
                raise ValueError("Saldo insuficiente")
            conta.valor -= historico.valor

        session.add(historico)
        session.commit()
        return historico
    
def total_contas():
    with Session(engine) as session:
        statement = select(Conta)
        contas = session.exec(statement).all()

    total = sum(conta.valor for conta in contas)

    return float(total)

def buscar_historicos_entre_datas(data_inicial: date, data_final: date):
    with Session(engine) as session:
        statement = select(Historico).where(
            Historico.data >= data_inicial,
            Historico.data <= data_final
        )
        historicos = session.exec(statement).all()
        return historicos

def criar_grafico_por_conta():
    with Session(engine) as session:
        statement = select(Conta).where(Conta.status==Status.ATIVO)
        contas = session.exec(statement).all()
        bancos = [i.banco.value for i in contas]
        total = [i.valor for i in contas]
        import matplotlib.pyplot as pl
        plt.bar(bancos, total)
        plt.show()