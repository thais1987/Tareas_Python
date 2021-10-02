'''
Tarea 1
Pedirle al usuario que entre la info de una nom_peli
Nombre, Año, Puntuacion(debe estar entre 1 y 5), director, genero(debe ser comedia, drama, terror, accion)
'''
list_gen = {"comedia", "drama", "terror", "accion"}
print("Por favor introduzca los siguientes datos de una peli: ")
nom_peli = input("Nombre: ")
year = int(input("Año: "))
punt = float (input("Puntuación (valor entre 1 y 5): "))
while punt < 1 or punt > 5:
  punt = float(input("Puntuación (valor entre 1 y 5): "))
direc = input("Director: ")
gene = input("Género(Comedia, Drama, Terror ó Accion): ")
while gene.lower() not in list_gen:
  gene = input("Género(Comedia, Drama, Terror ó Accion): ")
fav_movie = {
  "Nombre": nom_peli,
  "Año": year,
  "Puntuacion": punt,
  "Director": direc,
  "Genero": gene
}
print(fav_movie.values())
