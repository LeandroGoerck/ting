import sys


def txt_importer(path_file):
    if not path_file.endswith(".txt"):
        print("Formato inválido", file=sys.stderr)
        return None

    try:
        with open(path_file) as file:
            arquivo_txt = file.read().splitlines()
            return arquivo_txt

    except IOError:
        print("Arquivo " + path_file + " não encontrado", file=sys.stderr)
