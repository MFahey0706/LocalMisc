'''Edit this file to complete the exercises in
'Reading and Writing Files - the Basics'
'''

#import any modules you need
import csv
import json
#read a csv file
def read_csv(filename):
    '''
    reads a comma-separated-value (CSV) file, then returns the
    total number of lines in the file.

    Arguments:
    filename: The path to the file you want to read, as a string.
        If the file is in a different directory than where you're
        running this code from, you'll need to use either the
        full or relative path to the file.

    Returns:
    num_lines: The number of lines in the file specified by 'filename'

    Example:
    print(read_csv('data/old_transactions.csv'))
    -> 26
    '''
    num_lines=0
    with open(filename, "rb") as input:
        reader = csv.reader(input)
        for row in reader:
            num_lines += 1
    return num_lines
#read a json file
def read_json(filename):
    '''
    Reads a JavaScript Object Notation (JSON) file, and
    returns the contents of the file itself as a dictionary.

    Arguments:
    filename: The path to the file you want to read, as a string.
        If the file is in a different directory than where you're
        running this code from, you'll need to use either the
        full or relative path to the file.

    Returns:
    file_dict: A dictionary containing the contents of the JSON file.

    Example:
    File 'test.json' contains the following:
    {
    "examples": [ {'one':1, 'two':2}, {'a':'a', 'b':'b'}]
    }

    test_dict = read_json('test.json')
    print(test_dict['examples'][0]['one'])
    -> 1
    print(test_dict['examples'][1]['b'])
    -> b
    '''
    with open(filename, "r") as input:
        file_dict = json.load(input)
    return file_dict

def write_csv(data_list, output_csv_filename):
    '''
    Takes in a list of lists, and saves that to a CSV file where each
    element in the list is a line in the file and every element in the
    sub-list is separated by a comma

    Arguments:
    data_list: Input data list. Each element is itself a list, representing
        a single row of data, and every item in a sublist represents the data
        in that column and row.
    output_csv_filename: The filename to save the data to, as a CSV.

    Returns:
    None

    Example:
    data_list = [[1, 2, 3], [4, 5, 6]]
    write_csv(data_list,'test.csv')

    File 'test.csv' now contains the following:
    1,2,3
    4,5,6
    ''' 
    with open(output_csv_filename, "wb") as out_csv:
        writer=csv.writer(out_csv)
        for row in data_list:
            writer.writerow(row)
    return None


if __name__ == "__main__":
    pass
