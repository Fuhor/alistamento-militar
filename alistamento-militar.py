import datetime
ano = int(input('Em que ano vc nasceu: '))
data = datetime.datetime.now().year
idade = data - ano 
if idade == 18:
    print('Você precisa se alistar ainda esse ano.')
elif idade > 18:
    print('Você já se alistou. Ufa!')
    alistei = int(input('Caso você tenha se alistado já, diga que ano: '))
    ano_alistei = data - alistei
    print('Você se alistou a {} ano(s).'.format(ano_alistei))
elif idade < 18:
    print('Voce ainda precisa se alistar futuramente!')
    ano_alistar = 18 - idade
    print('Você terá que se alistar daqui {} ano(s)'.format(ano_alistar))

