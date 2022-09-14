import sys


def txt_importer(path_file):
    if not path_file.endswith(".txt"):
        return print("Formato inválido", file=sys.stderr)

    try:
        with open(path_file) as file:
            arquivo_txt = file.read().splitlines()
            return arquivo_txt

    except IOError:
        print("Arquivo " + path_file + " não encontrado", file=sys.stderr)
