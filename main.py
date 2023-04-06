def import_data(filename='albums_data.txt'):
    data = []
    with open(filename, 'r') as x:
        for line in x:
            album_data = line.strip().split(',')
            data.append(album_data)
    return data