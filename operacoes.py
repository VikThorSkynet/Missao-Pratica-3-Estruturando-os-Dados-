def calcular_media(notas):
    return sum(notas) / len(notas)

def verificar_reprovacao(media):
    return media < 6

def identificar_reprovados(dados_alunos, matriculas_reprovados):
    mensagens = []
    for matricula in matriculas_reprovados:
        aluno = dados_alunos[matricula]
        mensagem = f"Aluno Reprovado: {aluno['nome']} – Matrícula: {matricula} – Média Final: {aluno['media']:.2f}"
        mensagens.append(mensagem)
    return "\n".join(mensagens)
