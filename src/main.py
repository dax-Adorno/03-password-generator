import random
import string


def solicitar_longitud() -> int:
    while True:
        try:
            longitud = int(input("Ingresa la longitud de la contraseña:🛅🆗🆙🆒 "))
            if longitud < 4:
                print("La longitud mínima recomendada es 4.🕓")
                continue
            return longitud
        except ValueError:
            print("Entrada inválida. Debes ingresar un número entero.🥅")


def solicitar_confirmacion(mensaje: str) -> bool:
    while True:
        respuesta = input(f"{mensaje} (s/n): ").strip().lower()
        if respuesta in ("s", "n"):
            return respuesta == "s"
        print("Entrada inválida. Escribe 's' para sí o 'n' para no.")


def construir_pool(
    usar_mayusculas: bool,
    usar_numeros: bool,
    usar_simbolos: bool
) -> str:
    pool = string.ascii_lowercase

    if usar_mayusculas:
        pool += string.ascii_uppercase
    if usar_numeros:
        pool += string.digits
    if usar_simbolos:
        pool += string.punctuation

    return pool


def generar_contrasena(longitud: int, pool: str) -> str:
    return "".join(random.choice(pool) for _ in range(longitud))


def main() -> None:
    print("=" * 45)
    print("        GENERADOR DE CONTRASEÑAS😎🤖👾🟰👱🤷")
    print("=" * 45)

    longitud = solicitar_longitud()
    usar_mayusculas = solicitar_confirmacion("¿Incluir letras mayúsculas?🅰️🅱️")
    usar_numeros = solicitar_confirmacion("¿Incluir números?🔢")
    usar_simbolos = solicitar_confirmacion("¿Incluir símbolos?🟰❗❓")

    pool = construir_pool(usar_mayusculas, usar_numeros, usar_simbolos)
    contrasena = generar_contrasena(longitud, pool)

    print("\n--- CONTRASEÑA GENERADA ---💚👌🆗")
    print(contrasena)
    
    
          
print("\nSi te resultó útil, visita mi portfolio con más proyectos:")
print("https://dax-adorno.github.io/")
    
    
if __name__ == "__main__":
    main()
      #si quieren establecer un limite de tamaño pueden cambiar la funcion por esta
    """  def solicitar_longitud() -> int:
    while True:
        try:
            longitud = int(input("Ingresa la longitud de la contraseña (4-128): "))
            if longitud < 4:
                print("La longitud mínima recomendada es 4.")
                continue
            if longitud > 128:
                print("La longitud máxima permitida es 128.")
                continue
            return longitud
        except ValueError:
            print("Entrada inválida. Debes ingresar un número entero.")"""
   
