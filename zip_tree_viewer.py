from zipfile import ZipFile

def convert_bytes(size):
    units = ['B', 'KB', 'MB', 'GB']
    for i in range(4):
        full_size = str(round(size)) + ' ' + units[i]
        if size <= 1024:
            break
        size /= 1024
    return full_size

with ZipFile('desktop.zip') as zip_file:
    info = zip_file.infolist()

    for file in info:
        name = file.filename
        cnt = name.count('/') - 1

        if file.is_dir():
            space = '  ' * cnt
            print(f'{space}{name.split("/")[-2]}')
        else:
            size = convert_bytes(file.file_size)
            space = '  ' * (cnt + 1)
            print(f'{space}{name.split("/")[-1]} {size}')
