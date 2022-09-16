from ting_file_management.queue import Queue


def exists_word(word, instance):
    print(type(instance))
    if isinstance(instance, Queue):
        result = []
        queue = instance.get_queue()

        for element in queue:
            a_word_was_found = False
            ocorrencias = []
            file_lines = element["linhas_do_arquivo"]
            for index, line in enumerate(file_lines):
                line_in_lower_case = line.lower()
                word_in_lower_case = word.lower()
                if word_in_lower_case in line_in_lower_case:
                    ocorrencias.append({"linha": (index + 1)})
                    a_word_was_found = True
            if a_word_was_found == True:
                result.append(
                    {
                        "palavra": word,
                        "arquivo": element["nome_do_arquivo"],
                        "ocorrencias": ocorrencias,
                    }
                )

        return result
    else:
        return None


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
