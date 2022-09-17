def exists_word(word, instance):
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
        if a_word_was_found:
            result.append(
                {
                    "palavra": word,
                    "arquivo": element["nome_do_arquivo"],
                    "ocorrencias": ocorrencias,
                }
            )

    return result


def search_by_word(word, instance):
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
                ocorrencias.append({"linha": (index + 1), "conteudo": line})
                a_word_was_found = True
        if a_word_was_found:
            result.append(
                {
                    "palavra": word,
                    "arquivo": element["nome_do_arquivo"],
                    "ocorrencias": ocorrencias,
                }
            )

    return result
