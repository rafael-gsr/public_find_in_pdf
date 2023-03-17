#!/usr/bin/env python
import PyPDF2 as pypdf
from datetime import datetime

palavras_file= 'palavras_a_procurar.txt'
pdf_file = 'pdf_analisado.pdf'
logs_file = 'log_pdf_reader.txt'

def escrever_logs(logs):
    try:
        lerArquivoAnterior = open(logs_file, 'r')
        texto = lerArquivoAnterior.readlines()
        lerArquivoAnterior.close()

        hora = datetime.now()
        dataDeCriacao = hora.strftime('%a %d/%m/%Y %H:%M:%S ')
        texto.append(f'\n {dataDeCriacao} : {logs} ')

        abrirArquivo = open(logs_file, 'w')
        abrirArquivo.writelines(texto)
        abrirArquivo.close()

    except FileNotFoundError:
        abrirArquivo = open(logs_file, 'w')

        hora = datetime.now()
        dataDeCriacao = hora.strftime('%a %d/%m/%-Y %H:%M:%S ')
        texto = f'\n ---- LOG DE BUSCA POR PALAVRA ---- \n \
        \n {dataDeCriacao} : {logs} '

        abrirArquivo.writelines(texto)
        abrirArquivo.close()

# Lê quais palavras devem ser procuradas
with open(palavras_file, 'r') as palavras_a_procurar:
    lista_a_procurar = palavras_a_procurar.readlines()
    
    escrever_logs('--- INÍCIO DA ANÁLISE ---')
    
    # perquisa por cada palavra da lista
    for nome_a_procurar in lista_a_procurar:
        nome_a_procurar = nome_a_procurar.replace('\n', '')
        
        pdf = pypdf.PdfFileReader(pdf_file)
        
        # percorre cada página do documento
        for page in range(0,pdf.getNumPages()):
            if len(nome_a_procurar.split()) > 1:
                pdf_page =' '.join(pdf.getPage(page).extractText().lower().split())
                if nome_a_procurar.lower() in pdf_page:
                    print(f' *{nome_a_procurar}* foi encontrado na página {int(page) + 1} ')
                    escrever_logs(f' *{nome_a_procurar}*  foi encontrado na página {int(page) + 1} ')
                    
            else:
                pdf_page = pdf.getPage(page).extractText().lower().split()
                # percorre cada palavra da página
                for index in range(0, len(pdf_page)) :          
                    if pdf_page[index] == nome_a_procurar.lower():
                        print(f' *{nome_a_procurar}* foi encontrado na página {int(page) + 1} ')
                        escrever_logs(f' *{nome_a_procurar}*  foi encontrado na página {int(page) + 1} ')

    escrever_logs('--- FIM DA ANÁLISE --- \n')    