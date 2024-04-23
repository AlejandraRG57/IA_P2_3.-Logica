#Alejandra Rodriguez Guevara 21310127 6E1

#La ingeniería del conocimiento es una disciplina que se centra en la creación, desarrollo y aplicación de sistemas basados en conocimiento, 
#los cuales utilizan el conocimiento experto y reglas lógicas para tomar decisiones o realizar tareas específicas.

#Base de conocimiento
base_conocimiento = {
    "comedia": ["The Hangover", "Superbad", "Anchorman"],
    "acción": ["The Dark Knight", "Inception", "Die Hard"],
    "drama": ["The Shawshank Redemption", "Forrest Gump", "The Godfather"],
    "ciencia ficción": ["Interstellar", "Blade Runner 2049", "The Matrix"]
}

#Función para recomendar películas
def recomendar_pelicula(preferencia):
    if preferencia in base_conocimiento:
        return base_conocimiento[preferencia]
    else:
        return "Lo siento, no puedo recomendarte películas en esa categoría."

preferencia_usuario = "acción"
peliculas_recomendadas = recomendar_pelicula(preferencia_usuario)
print("Películas recomendadas en la categoría de", preferencia_usuario + ":", peliculas_recomendadas)