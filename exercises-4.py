characters_file = open("meus-personagens-favoritos.txt", mode='w')

characters_file.write("Tio Patinhas")
characters_file.write("Neo")
characters_file.write("Homen Aranha")

print('Batman', file=characters_file)

characters_file.close()