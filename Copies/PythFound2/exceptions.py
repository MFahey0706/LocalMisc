#Edit this file to complete the exercises in
#'Controlling for Unintended Behaviors'

def normalize_rectangle(rect):
    '''
    Normalizes a rectangle so that it's bottom left corner is at
    the origin and it's 1.0 units long on its longest axis.

    Arguments:
    rect: A tuple of values defining the two corners of the rectangle:
        (x0, y0, x1, y1). x0 and y0 must always be less than x1 and y1.

    Returns:
    scaled_rect: A tuple of values defining the two corners of the scaled rectangle:
        (0, 0, scaled_x1, scaled_y1)

    Examples:
    print(normalize_rectangle(0, 0, 1.0, 5.0))
    -> (0, 0, 0.2, 1.0)
    print(normalize_rectangle(2, 1, 12.0, 6.0))
    -> (0, 0, 1.0, 0.5)
    '''
    assert len(rect) == 4, 'Rectangles must contain 4 coordinates'
    x0, y0, x1, y1 = rect
    assert x0 < x1, 'Invalid X coordinates'
    assert y0 < y1, 'Invalid Y coordinates'

    dx = x1 - x0
    dy = y1 - y0
    if dx > dy:
        scaled = float(dy) / dx
        upper_x, upper_y = 1.0, scaled
    else:
        scaled = float(dx) / dy
        upper_x, upper_y = scaled, 1.0

    assert 0 < upper_x <= 1.0, 'Calculated upper X coordinate invalid'
    assert 0 < upper_y <= 1.0, 'Calculated upper Y coordinate invalid'

    return (0, 0, upper_x, upper_y)

def file_read_backup(filename, backup_filename):
    '''
    Read the contents of a file, but if there is a problem reading the
    file fallback to a backup file.

    Arguments:
    filename: The name of the file (as a string) you want to read.
    backup_filename: The name of the backup file (as a string) to be
        read in if reading the first file causes an exception.

    Returns:
    file_contents: The output of the .read() function applied to the file.

    Examples:
    if 'goodfile.txt' contains:
    Hello I am a good file

    if 'backupfile.txt' contains:
    I'm the understudy!

    and 'badfile.txt' doesn't exist, then:
    print(file_read_backup('goodfile.txt', 'backupfile.txt'))
    -> Hello I am a good file
    print(file_read_backup('badfile.txt', 'backupfile.txt'))
    -> I'm the understudy!
    print(file_read_backup('badfile.txt', 'badfile.txt'))
    ->Traceback (most recent call last):
        File "exercises/exceptions.py", line 78, in <module>
          print(file_read_backup('badfile.txt','badfile.txt'))
        File "exercises/exceptions.py", line 74, in file_read_backup
          handle = open(backup_filename,'r')
      IOError: [Errno 2] No such file or directory: 'badfile.txt'
    '''
    try:
        with open(filename, "r") as input:
            file_contents = input.read()
            input.close()
    except IOError:
        print("Problem reading the file. Perhaps it doesn't exist. \n Switching to backup file.") 
        with open(backup_filename, "r") as backup_input:
            file_contents = backup_input.read()
            backup_input.close()
    return file_contents
    
if __name__ == "__main__":
    print(file_read_backup('badfile.txt','badfile.txt'))
