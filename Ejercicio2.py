calificacion = float(input("Ingrese la calificación: "))

if calificacion > 9.0:
    print("La calificación es A.")
elif calificacion > 8.0:
    print("La calificación es B.")
elif calificacion >= 7.5:
    print("La calificación es C.")
else:
    print("La calificación es R.")
