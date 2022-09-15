from symbol import try_stmt
import sys
from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue


def process(path_file, instance):
    if isinstance(instance, Queue):
        queue = instance.get_queue()

        for element in queue:
            if element["nome_do_arquivo"] == path_file:
                return None

        file = txt_importer(path_file)

        new_element = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(file),
            "linhas_do_arquivo": file,
        }

        instance.enqueue(new_element)
        print(new_element, file=sys.stdout)


def remove(instance):
    if isinstance(instance, Queue):
        if len(instance) == 0:
            print("Não há elementos", file=sys.stdout)
            return None

        removed_file = instance.dequeue()
        nome_do_arquivo = removed_file["nome_do_arquivo"]
        print(
            "Arquivo " + nome_do_arquivo + " removido com sucesso",
            file=sys.stdout,
        )
    return None


def file_metadata(instance, position):
    if isinstance(instance, Queue):
        try:
            file = instance.search(position)
            print(file, file=sys.stdout)
            return None
        except IndexError:
            print("Posição inválida", file=sys.stderr)
    return None
