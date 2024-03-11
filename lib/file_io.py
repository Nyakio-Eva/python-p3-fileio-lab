

def write_file(file_name, file_content):
    #adding txt extension
    text_file = str(file_name) + '.txt'

    with open(text_file, mode='w', encoding='utf-8')  as file:

        file.write(file_content)

def append_file(file_name, append_content):
    text_file = str(file_name) + '.txt'

    with open(text_file, mode='a', encoding='utf-8') as file:
        file.write(append_content)



def read_file(file_name):
    text_file = str(file_name) + '.txt'
    with open(text_file, encoding='utf-8') as file:
        file_content = file.read()
        return file_content

