from random import randint as ran, randrange
import time as tm
import os

os.system('cls')
turno = 1
rodadas = 0
escolhas = ('atacar', 'curar')

#vida do player
vida = 100

#vida do boss
bossvida = 100


#história--------------------------------------------------------------------------------------------------------------
print('-='*60)
print('''
    ...Lucian tinha apenas 7 anos.

''')
tm.sleep(2)

print('''Naquela época seu pai, Albus que era um homem, forte, viril e sério.
Logicamente era a sua maior representação de respeito e dignidade, embora talvez Albus não fosse tão digno assim...''')
tm.sleep(2.5)

print('''
Lucian não entendia muito bem na época sobre financias e dinheiro, mas sabia muito bem que o
jeito que seu pai lidava com isso não era nem um pouco limpo.''')
tm.sleep(3)

print('''

Já a sua personificação de afeto e amor vinha de sua mãe, Violet. Tão linda e cheirosa
quanto as próprias violetas... era tão doce e gentil... quase angelical, exceto pelo fato de não ter asas.''')
tm.sleep(2.5)

print('''


''')
print('''No entanto... a vida que Albus levava trouxe a ruína de sua família.''')
tm.sleep(2.5)

print('''
Violet foi assassinada enquanto Albus e Lucian assistiam toda a atrocidade.''')
tm.sleep(2.5)

print('''
Logo após sua mãe foi a vez de seu pai...''')
tm.sleep(2)

print('''Lucian foi o único poupado.
''')
tm.sleep(2.5)

print('''

Motivado pela raiva, hoje Lucian busca vingança contra Amaymon, responsável pela morte de seus pais.''')
tm.sleep(2)
print('''
Em uma tentativa de dar valor a morte daqueles que um dia eram o motivo de sua felicidade''')
tm.sleep(2)
print('''Lucian o encontra...
''')
tm.sleep(2)
print('''e assim começa sua tão desejada vendeta...
''')

print('-='*60)
tm.sleep(3)
print('''
''')
#fim da história--------------------------------------------------------------------------------------------------------



while(bossvida>0) or (vida>0):
  #dados do player
    d20 = randrange(0, 20)
    d12 = randrange(0,12)

  #dados do boss
    boss = ran(0,1)
    d20boss = randrange(-20, 0)
    d12boss = randrange(0, 12)
    
  #turno do jogador
    if turno == 1:
        jogador = int(input('''
    Você deseja:
       [0] atacá-lo    
       [1] curar-se
       
       '''))
       
      #ataque
        if jogador == 0:
            print('''Você tirou...''')
            tm.sleep(2)
            print(d20, '''PONTOS DE VIDA DE AMAYMON!''')
            v = bossvida-d20
            bossvida = v
            print('AMAYMON FICOU COM', bossvida, 'DE VIDA!')
            print('')
            tm.sleep(1.5)

      #cura
        elif jogador == 1:
            print('')
            c = vida+d12
            vida = c
            tm.sleep(1)
            print('...')
            tm.sleep(2)
            print('VOCÊ CUROU: ', d12, 'PONTOS DE VIDA')
            print('')
            tm.sleep(1.5)
            
        if bossvida <= 0 or vida <= 0:
            print('Parabéns! Você derrotou Amaymon!')
            tm.sleep(3)
            print('''
            
            ''')
            print('''Posteriormente ao realizar seu maior desejo, Lucian percebe que sua vida tornou-se sem rumo.''')
            tm.sleep(2.5)
            print('''
            A única coisa que o motivava era a vingança...''')
            tm.sleep(2)
            print('''
            Sem rumo... só... vazio...''')
            tm.sleep(3)
            print('''
            era tudo o que sentia... -Se é que pode-se dizer que "sentia" algo-.''')
            tm.sleep(2)
            print('''

            Lucian, totalmente abalado por quem se tornara, decide viver como andarilho em busca da solitude
            ''')
            tm.sleep(3)
            print('''
            E desde então, nunca se soube mais nada sobre ele...''')
            tm.sleep(3)
            break
        turno = 2


  #turno do boss
    if turno == 2:
        print('Amaymon escolheu: {}'.format(escolhas[boss]))

      #ataque
        if boss == 0:
            print('Amaymon tirou', d20boss,'!')
            tm.sleep(2)
            c = vida+d20boss
            vida = c
            print('VOCÊ FICOU COM ', vida,'DE VIDA!')
            tm.sleep(1.5)

      #cura
        elif boss == 1:
            tm.sleep(1)
            print('...')
            tm.sleep(2)
            v = bossvida+d12boss
            bossvida = v
            print('AMAYMON CUROU', d12boss, ' PONTOS DE VIDA!')
            tm.sleep(1.5)

        if vida <= 0 or bossvida <= 0:
            print('O jogo acabou! Infelizmente Lucian foi derrotado...')
            tm.sleep(2)
            
            break
        turno = 1
        rodadas+=1
    print('''
    ''')
    print('*--------------------*')
    print(' Número de rodadas: ' + str(rodadas))
    print(' Sua vida: ' + str(vida))
    print(' Vida de Amaymon: ' + str(bossvida))
    print('*--------------------*')
    print('')