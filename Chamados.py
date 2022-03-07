import os
def porcentagem(chamados_analista, total):
    return str(round(chamados_analista*100/total))

def media(total, chamados):
    return int(round(total/chamados))


if os.path.exists('Analista.txt'):
    analistas_espacos_txt = open('Analista.txt', 'r')
    analistas_espacos = analistas_espacos_txt.read().split('\n')

    if len(analistas_espacos) > 0:
        info_relatorio = open('resultado.txt', 'wt')
        info_relatorio.write('Safeware Tecnologia\n')
        info_relatorio.write('Data de Início: 01/02/2022 \nData Final 28/02/2022\n')
        info_relatorio.write('\n\n              Quantidade de Chamadors por Analista\n')
        info_relatorio.write('-' * 75 + '\n')

        info_relatorio.write('Nr.'.ljust(5))
        info_relatorio.write('Analista'.ljust(15))
        info_relatorio.write('Quantidade de Chamados'.ljust(27))
        info_relatorio.write('% Dos Chamados'.ljust(15) + '\n\n')

        chamados_total = 0

        for analista_espaco in analistas_espacos:
            chamados_total += int(analista_espaco.split()[1])

        for indice_analista_espaco in range(len(analistas_espacos)):
            analista_espaco = analistas_espacos[indice_analista_espaco].split()

            analista = analista_espaco[0]
            chamado = analista_espaco[1]

            info_relatorio.write(str(indice_analista_espaco+1).ljust(5))
            info_relatorio.write(analista.ljust(25))
            info_relatorio.write(chamado.ljust(23))
            info_relatorio.write(porcentagem(int(chamado), chamados_total).ljust(3) + '%\n')

        info_relatorio.write('\n\nChamados Totais: ' + str(chamados_total))
        info_relatorio.write('\nMedia de Chamados: ' + str(media(chamados_total, len(analistas_espacos))))

        info_relatorio.close()
else:
    print('Arquivo Não Existe')


