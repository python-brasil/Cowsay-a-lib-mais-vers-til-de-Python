import cowsay

personagens = ['beavis', 'cheese', 'cow', 'daemon', 'dragon', 'fox', 'ghostbusters', 'kitty',
'meow', 'miki', 'milk', 'octopus', 'pig', 'stegosaurus', 'stimpy', 'trex', 
'turkey', 'turtle', 'tux']


for personagem in personagens:
    funcao_cowsay = getattr(cowsay, personagem)
    funcao_cowsay("Python Brasil a melhor comunidade!")