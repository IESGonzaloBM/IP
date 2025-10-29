# Comprobacion de IP y clases (Python) — README

> CLI Que dada una IP por terminal en formato: py main.py <IP>, comprueba si es correcta y deuelve el tipo de clase (A, B, C o D)
> Devuelve un mensaje de salida del tipo de clase.

---

## 1) Descripción del módulo

Este proyecto implementa una comprobacion de IP y clase.
- El comando sigue el siguiente formato: **py main.py <IP>**
- La IP debe de cumplir que sea 4 octetos entre 0 y 255 cada uno separado por puntos.

---

## 2) Requisitos

- **Python 3.10 o superior**.
- **Sin dependencias externas obligatorias.**
- Si en algún momento se añaden librerías, se listarán en el archivo **`dependecias.txt`** (ver sección 5).

---

## 3) Instalación de Python

### 3.1 Linux

#### Debian/Ubuntu (y derivados)
```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv
python3 --version
python3 -m pip --version
```

#### Fedora
```bash
sudo dnf install -y python3 python3-pip python3-virtualenv
python3 --version
python3 -m pip --version
```

#### Arch/Manjaro
```bash
sudo pacman -S --needed python python-pip
python --version
python -m pip --version
```

> **Entorno virtual (opcional recomendado)**
```bash
python3 -m venv .venv
# Activar:
# Linux/macOS:
source .venv/bin/activate
# (Salir: 'deactivate')
```

### 3.2 Windows

#### Opción A — Microsoft Store
1. Abrir **Microsoft Store**, buscar **Python 3.x** (Python Software Foundation).
2. Instalar y verificar:
```powershell
py --version
py -m pip --version
```

#### Opción B — Instalador oficial
1. Descargar desde **https://www.python.org/downloads/** el instalador de Python 3.x.
2. **Marcar** “**Add Python to PATH**” durante la instalación.
3. Verificar:
```powershell
py --version
py -m pip --version
```

> **Entorno virtual (opcional)**
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
# (Salir: 'deactivate')
```

---

## 4) Ejecución del módulo

### Sintaxis general
```bash
python main.py <IP>
```
- `main.py` archivo `.py` donde esta el codigo
- `IP` dirección en formato Ipv4

> En Windows puedes usar `py` en lugar de `python`.
> En Linux, si conviven varias versiones, usa `python3`.

### Ejemplos

**Suma explícita**
```bash
# Linux/macOS
python main.py 123.56.45.3

# Windows
py main.py 235.2.32.87
```
Salida esperada:
```
123.56.45.3 => IP Clase A
235.2.32.87 => IP Clase D o E, con proposito multidifusion o experimental respectivamente
```

## 6) Mensajes de error y códigos de salida

- **Formato en terminal incorrecto** ->
- Mensaje: `[ERROR]: Formato incorrecto` →
- **Tipo de dato**, **rango numerico**, **numero de octetos** ->
- Mensaje Generico: `[ERROR]: La IP debe de estar separada por '.', tener 4 octetos entre [0, 255]`

---

## 7) Problemas frecuentes (FAQ)

- **“python: command not found” / “py no se reconoce”** → Instala Python o ajusta el **PATH** (ver sección 3).
- **“pip no se reconoce”** → Usa `python -m pip` (o `py -m pip` en Windows).

---