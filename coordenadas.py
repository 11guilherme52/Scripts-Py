print("""
░█▀▀█ 　 █░░█ █▀▀█ █░░ 　 █░░█ █▀▀█ █▀▀▄ █▀▀█ █▀▀█ █▀▀▄ ▀▀█▀▀ █▀▀█ █▀▀ 　 █▀▀▄ █▀▀█ 
▒█▄▄█ 　 █░░█ █▄▄█ █░░ 　 █░░█ █▄▄█ █░░█ █▄▄▀ █▄▄█ █░░█ ░░█░░ █▄▄▀ █▀▀ 　 █░░█ █░░█ 
▒█░▒█ 　 ░▀▀▀ ▀░░▀ ▀▀▀ 　 ░▀▀▀ ▀░░▀ ▀▀▀░ ▀░▀▀ ▀░░▀ ▀░░▀ ░░▀░░ ▀░▀▀ ▀▀▀ 　 ▀▀▀░ ▀▀▀▀ 

█▀▀█ █░░ █▀▀█ █▀▀▄ █▀▀█ 　 █▀▀ █▀▀█ █▀▀█ ▀▀█▀▀ █▀▀ █▀▀ ░▀░ █▀▀█ █▀▀▄ █▀▀█ 　 ▀█░█▀ █▀▀█ █▀▀ █▀▀ 
█░░█ █░░ █▄▄█ █░░█ █░░█ 　 █░░ █▄▄█ █▄▄▀ ░░█░░ █▀▀ ▀▀█ ▀█▀ █▄▄█ █░░█ █░░█ 　 ░█▄█░ █░░█ █░░ █▀▀ 
█▀▀▀ ▀▀▀ ▀░░▀ ▀░░▀ ▀▀▀▀ 　 ▀▀▀ ▀░░▀ ▀░▀▀ ░░▀░░ ▀▀▀ ▀▀▀ ▀▀▀ ▀░░▀ ▀░░▀ ▀▀▀▀ 　 ░░▀░░ ▀▀▀▀ ▀▀▀ ▀▀▀ 

█▀▀█ █▀▀ █▀▀█ ▀▀█▀▀ █▀▀ █▀▀▄ █▀▀ █▀▀ ▀█ ▀█ 
█░░█ █▀▀ █▄▄▀ ░░█░░ █▀▀ █░░█ █░░ █▀▀ █▀ █▀ 
█▀▀▀ ▀▀▀ ▀░▀▀ ░░▀░░ ▀▀▀ ▀░░▀ ▀▀▀ ▀▀▀ ▄░ ▄░\n""")

x = int(input('Longitude: '))
y = int(input('Latitude: '))

if x > 0 and y > 0:
    print('Quadrante 1')
elif x < 0 and y > 0:
    print('Quadrante 2')
elif x < 0 and y < 0:
    print('Quadrante 3')
elif x > 0 and y < 0:
    print('Quadrante 4')
else:
    print('Localização: ORIGEM')