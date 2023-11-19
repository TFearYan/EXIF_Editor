from exif import Image


def main():
    execute_number = int(input('''Select an action:
1 - Display all EXIF data
2 - Change EXIF parameter
3 - Delete EXIF parameter
4 - Delete all EXIF parameters
Write the action number: '''))
    path = input('Write the full path to the image: ')

    with open(path, 'rb') as file:
        image_bytes = file.read()

    file = Image(image_bytes)

    if file.has_exif:
        print(f'EXIF version in this file is {file.exif_version}.')

    else:
        print('The file does not have an exif version.')
        return

    if execute_number == 1:
        result_file = input('Write the full path to the file where the results will be saved: ')
        read_exif(file, result_file)
    elif execute_number == 2:
        tag = input('Write the parameter you want to change: ')
        value = input('Write the value you want to write to the parameter: ')
        set_exif(file, tag, value, path)
    elif execute_number == 3:
        tag = input('Write the parameter you want to change: ')
        delete_exif(file, tag, path)
    elif execute_number == 4:
        delete_all(file, path)


def read_exif(file, result_file):
    with open(result_file, 'w') as res_file:
        res_file.write(f'EXIF version in this file is {file.exif_version}.\n\n\n')
        for tag in dir(file):
            if tag != '_segments' and tag != 'y_resolution':
                res_file.write(f'{tag}: {file.get(tag)}\n')
            elif tag == 'y_resolution':
                res_file.write(f'{tag}: {file.get(tag)}\n')
                break


def set_exif(file, tag, value, path):  # Set parameter of EXIF metadata
    file.set(tag, value)
    write_exif_b(file, path)


def delete_exif(file, tag, path):  # Delete parameter of EXIF metadata
    file.delete(tag)
    write_exif_b(file, path)


def delete_all(file, path):  # Delete all parameters of EXIF metadata
    file.delete_all()
    write_exif_b(file, path)


def write_exif_b(file, path):  # Save changes to a file
    with open(path, 'wb') as new_image_file:
        new_image_file.write(file.get_file())


if __name__ == '__main__':
    main()
