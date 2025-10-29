# ===================================================================================================
#   CLI Que dada una IP por terminal en formato: py main.py <IP>, comprueba si es correcta y deuelve
#   el tipo de clase (A, B, C o D. Devuelve un mensaje de salida del tipo de clase.
#
#   - Input: IPv4
#   - Output: Mensaje diciendo el tipo de clase (A, B, C o D)
#
#   By: Gonzalo Blanco
# ===================================================================================================
from sys import argv


def get_param() -> list[int] | None:
    """
    Obtiene la ip dada por terminal, gestiona y controla los posibles errores.

    Returns:
        list[int]: Lista con los octetos
    Raises:
        Exception: Lanza un tipo de error generico, en formato: "[ERROR] <error interpretado>".
    """

    try:
        msg = "[ERROR]: La IP debe de estar separada por '.', tener 4 octetos entre [0, 255]"

        if len(argv) != 2:
            raise Exception("[ERROR]: Formato incorrecto")

        try:
            ip_octetos = argv[1].split(".")
            ip_octetos = [int(octeto) for octeto in ip_octetos]
        except Exception:
            raise Exception(msg)

        if len(ip_octetos) != 4:
            raise Exception(msg)
        elif any(not 0 <= octeto <= 255 for octeto in ip_octetos):
            raise Exception(msg)

        # Hacer sin ceros a la izquierda por octeto

        # ip_octetos = argv[1].split(".")
        # [int(octeto) for octeto in ip_octetos 0 <= int(octeto) <= 255 and len(ip_octetos) == 4]

        return ip_octetos
    except Exception as error:
        print(error)
        exit(1)


def type_of_ip(octetos: list[int]) -> str:
    """
    Comprueba dado el parametro que clase de IP es.

    Args:
        octetos (list[int]): Lista con los octetos
    Returns:
        str: Clase de IP
    """

    if 1 <= octetos[0] <= 127:
        if octetos[0] == 127:
            return "IP Clase A con loopback"
        else:
            return "IP Clase A"
    elif 128 <= octetos[0] <= 191:
        return "IP Clase B"
    elif 192 <= octetos[0] <= 223:
        return "IP Clase C"
    else:
        return "IP Clase D o E, con proposito multidifusion o experimental respectivamente"


if "__main__" == __name__:
    octetos = get_param()
    clase_ip = type_of_ip(octetos)
    print(clase_ip)