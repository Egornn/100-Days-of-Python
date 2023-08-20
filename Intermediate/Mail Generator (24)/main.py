from os import path, makedirs


def get_names(path_names):
    with open(path_names, mode='r', encoding='utf-8') as f:
        names = []
        for line in f:
            names.append(line.replace('\n', ""))
    return names


def generate_letters(names, template_path, output_folder):
    lines = []
    with open(template_path, mode='r', encoding='utf-8') as f:
        for line in f:
            lines.append(line)

    output_path = f"{output_folder}/{template_path[template_path.rfind('/') + 1:template_path.rfind('.')]}"
    if not path.exists(output_path):
        makedirs(output_path)

    for name in names:
        output_lines = []
        with open(f'{output_path}/{name}.txt', mode="a", encoding='utf-8') as out:
            for line in lines:
                output_lines.append(line.replace("[name]", f'{name}'))
            out.writelines(output_lines)


template = 'Templates/Birthday Invitation.txt'

generate_letters(get_names('./names.txt'), './Templates/Birthday Invitation.txt', './Output')
