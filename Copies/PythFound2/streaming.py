#Edit this file to complete the exercises in
#'Processing Data on an As-Needed Basis'
import csv

def triplicate(input_iterable):
    '''
    A generator which yields three copies of each element
    from an input iterable.

    Arguments:
    input_iterable: An iterable to be tripled.

    Yields:
    each element in the source iterable, repeated three times.
    
    Important -- this doesn't return a single value, it yields
    three times as many values as are present in the source iterable.

    Examples:
    triplicate_generator = triplicate([1,2,3])
    for i in triplicate_generator:
        print(i),
    -> 1 1 1 2 2 2 3 3 3

    triplicate_generator = triplicate({"Age":30, "Gender":"Male"})
    for i in triplicate_generator:
        print(i),
    -> Gender Gender Gender Age Age Age #your results may be reversed
    
    '''
    for i in input_iterable:
        yield i
        yield i
        yield i
        
#triplicate_generator = triplicate([1,2,3])
#for i in triplicate_generator:
    #print(i)
        
def records_from_file(fname, column_names):
    '''
    A generator which yields a stream of dictionaries,
    one for each line in a file.

    Arguments:
    fname: The filename of a comma-delimited text file.
    column_names: A list of names to be used as the key for each
        column in the file

    Yields:
    record_stream: each line of the file, as a dictionary with keys given by
        column_names

    Example:

    If the file "baby_names.csv" contains the following lines:
    "Andrew",11
    "Matt",14
    "Devin",17
    "Andrew",20
    "Geoff",5
    "Geoff",10

    record_stream = records_from_file('baby_names.csv',['Name', 'Count'])
    for record in record_stream:
        print(record)
    -> {'Name': 'Andrew', 'Count': '11'}
    -> {'Name': 'Matt', 'Count': '14'}
    -> {'Name': 'Devin', 'Count': '17'}
    -> {'Name': 'Andrew', 'Count': '20'}
    -> {'Name': 'Geoff', 'Count': '5'}
    -> {'Name': 'Geoff', 'Count': '10'}
    #Note that the order of the key-value pairs in each dictionary may vary.
    '''
    with open(fname, 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            yield {column_names[i]:element for i,element in enumerate(row)}
    
def cast_fields(record_stream, columns_to_convert):
    '''
    A generator which takes in a iterable of dictionaries,
    then casts the values of any keys specified in a list
    into integers.

    Arguments:
    record_stream: An iterable, where each element is a dictionary.
    columns_to_convert: a list of keys in the dictionaries in record_stream
        that should be converted into integers.

    Yields:
    cast_record_stream: each element of the iterable, with the specified
        values cast to integers.

    Example:
    
    If the file "baby_names.csv" contains the following lines:
    "Andrew",11
    "Matt",14
    "Devin",17
    "Andrew",20
    "Geoff",5
    "Geoff",10

    record_stream = records_from_file('baby_names.csv',['Name', 'Count'])
    cast_record_stream = cast_fields(record_stream, ['Count'])
    for record in cast_record_stream:
        print(record)
    -> {'Name': 'Andrew', 'Count': 11}
    -> {'Name': 'Matt', 'Count': 14}
    -> {'Name': 'Devin', 'Count': 17}
    -> {'Name': 'Andrew', 'Count': 20}
    -> {'Name': 'Geoff', 'Count': 5}
    -> {'Name': 'Geoff', 'Count': 10}
    #Note that the order of the key-value pairs in each dictionary may vary.
    '''
    for r in record_stream:
        for c in columns_to_convert:
            if c in r:
                r[c] = int(r[c])
        yield r
        
def aggregate_counts(record_stream, sum_column, group_by_column):
    '''
    A *regular* function which iterates through an iterable
    of dictionaries, and returns the sum of all values in a
    given key, grouped by all unique values of another key.

    Arguments:
    record_stream: An iterable, where each element is a dictionary.
    sum_column: The key in the dictionaries whose values should be
        summed up.
    group_by_column: The key in the dictionaries to group the sums by.

    Returns:
    grouped_counts: A dictionary, where each key is the group_by_key
        and the value is the sum of the values in the sum_key for
        that group

    Example:
    If the file "baby_names.csv" contains the following lines:
    "Andrew",11
    "Matt",14
    "Devin",17
    "Andrew",20
    "Geoff",5
    "Geoff",10

    record_stream = records_from_file('baby_names.csv',['Name', 'Count'])
    cast_record_stream = cast_fields(record_stream, ['Count'])
    grouped_counts = aggregate_counts(cast_record_stream,'Count','Name')
    for key in grouped_counts:
        print("{0}: {1}".format(key,grouped_counts[key]))
    -> "Andrew: 31"
    -> "Matt: 14"
    -> "Devin: 17"
    -> "Geoff: 15"
    #Note that the order of the key-value pairs in the dictionary may vary.
    '''
    grouped_counts = {}
    for r in record_stream:
        if r[group_by_column] in grouped_counts:
            grouped_counts[r[group_by_column]] += r[sum_column]
        else:
            grouped_counts[r[group_by_column]] = r[sum_column]
    return grouped_counts
        

def aggregate_counts_from_file(fname, column_names, columns_to_convert,
                               sum_column, group_by_column):
    '''
    Take in a CSV filename and a list of column names, create a
    generator that yields a dictionary for each line of the file
    with the column name list as keys and each element
    in the line as the value. Then make a generator that casts the values
    of a list of columns to integers. Finally, return the sum of all
    elements in a given column, grouped by unique values in another column.

    Arguments:
    fname: The filename of a comma-delimited text file.
    column_names: A list of names to be used as the key for each
        column in the file
    columns_to_convert: a list of keys in the dictionaries in record_stream
        that should be converted into integers.
    sum_column: The key in the dictionaries whose values should be
        summed up.
    group_by_column: The key in the dictionaries to group the sums by.

    Returns:
    grouped_counts: A dictionary, where each key is the group_by_key
        and the value is the sum of the values in the sum_key for
        that group

    Example:
    If the file "baby_names.csv" contains the following lines:
    "Andrew",11
    "Matt",14
    "Devin",17
    "Andrew",20
    "Geoff",5
    "Geoff",10
    
    grouped_counts = aggregate_counts_from_file('baby_names.csv',
                                                ['Name', 'Count'],
                                                ['Count'],
                                                'Count',
                                                'Name')
    for key in grouped_counts:
        print("{0}: {1}".format(key,grouped_counts[key])
    -> "Andrew: 31"
    -> "Matt: 14"
    -> "Devin: 17"
    -> "Geoff: 15"
    #Note that the order of the key-value pairs in the dictionary may vary.
    '''
    return aggregate_counts(cast_fields(records_from_file(fname,column_names),columns_to_convert),sum_column, group_by_column)