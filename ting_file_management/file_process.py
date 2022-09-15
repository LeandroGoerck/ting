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
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
