def registrar_leitura(titulo,paginas_tot,paginas_lid):
    progresso = paginas_lid*100/paginas_tot
    
    print(f'Leitura do livro {titulo}:')
    print(f'PROGRESSO: {int(progresso)}% lido!')

N = int(input('De quantos livros você quer registrar a leitura? '))
for i in range(N):
    print('=============================')
    titulo = input(f'Diga o título do {i+1}º livro: ')
    paginas = int(input(f'A quantidade de paginas ele tem no total: '))
    lidas = int(input('Diga quantas páginas você já leu: '))
    print('')
    registrar_leitura(titulo,paginas,lidas)