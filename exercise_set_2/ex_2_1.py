def basename(*args):
    n = len(args)
    if n > 1:
        names = list()
        for file_name in args:
            name = extract_basename(file_name)
            names.append(name)
        return names
    else:
        file_name = args[0]
        return extract_basename(file_name)


def extract_basename(file_name):
    file_name_parts = file_name.split('.')
    return file_name_parts[0]
