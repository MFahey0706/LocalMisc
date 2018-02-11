'''
Edit this file to complete the exercises in
'Using Numpy for Fast Array Manipulation'
'''

import numpy as np

def create_array():
    '''
    Create and return a numpy array that meets the
    following criteria:
    1. Is one-dimensional.
    2. Starts from zero, and contains every third number
        (i.e. 0, 3, 6, 9...).
    3. Ends with 1101.
    4. Is an array of integers.

    Arguments:
    None

    Returns:
    output_array: An array meeting the specifications in this
        docstring.
    '''
    output_array = np.arange(0,1102,3)
    return output_array
    
def compute_avg_length(input_array):
    '''
    For any given numpy array, compute the average number
    of elements along each axis. For example, if a 2D array
    has a shape of (12,4), then the average number of elements
    would be 8. If a 3D array has a shape of (12,4,14), then the
    average number of elements would be 10.

    Arguments:
    input_array: The numpy array to get the average number of
        elements of.

    Returns:
    avg_length: The average number of elements along each axis.
    '''
    return np.mean(input_array.shape)

def filter_array(array_to_filter, equal_array, not_equal_array=None):
    '''
    Filter a 1D Numpy array element-by-element, returning only elements
    that are also in a second Numpy array and not in an optional third
    Numpy array.

    Arguments:
    array_to_filter: The 1D Numpy array to be filtered.
    equal_array: A 1D Numpy array, of the same length as array_to_filter,
        where elements in array_to_filter that equal those in this array
        will be returned.
    not_equal_array (None): If not None, is a 1D Numpy array, of the same
        length as array_to_filter, where elements in array_to_filter that
        equal those in equal_array but *do not* equal those in this array
        will be returned.

    Returns:
    filtered_array: elements in array_to_filter that match the elements in
        equal_array and optionally do not match the elements in not_equal_array.

    Examples:
    import numpy as np
    array_to_filter = np.array([1,2,3,4,5])
    equal_array = np.array([1,2,5,5,5])
    not_equal_array = np.array([2,2,3,4,1])
    filter_array(array_to_filter, equal_array) # returns np.array([1,2,5])
    filter_array(array_to_filter, equal_array, not_equal_array) # returns np.array([1,5])
    filter_array(array_to_filter, not_equal_array, equal_array) # returns np.array([3,4])
    '''
    if not_equal_array is None:
        return array_to_filter[array_to_filter==equal_array]
    else:
        return array_to_filter[(array_to_filter==equal_array) & (array_to_filter!=not_equal_array)]
        
def reverse_multiply(input_array):
    '''
    Multiply each element in a 1D Numpy array (of floats or ints) by the element at the
    same index of the array when reversed, then return the result.

    Arguments:
    input_array: The 1D Numpy array to have this operation performed
        on it.

    Returns:
    output_array: The result of the operation.

    Example:
    import numpy as np
    input_array = np.array([1,2,3,4,5])
    reverse_multiply(input_array) # returns np.array([5,8,9,8,5])
    '''
    return input_array*input_array[::-1]
    
def compute_set_intersection(array_1, array_2):
    '''
    Compute the set intersection of two 1D Numpy arrays. The
    set intersection is defined as all unique values which appear
    in both arrays.

    Arguments:
    array_1, array_2: 1D Numpy arrays of integers

    Returns
    set_intersection: the set intersection of the two input arrays.
    '''
    return np.intersect1d(array_1,array_2)
    
def save_multiple_medians(input_array, filename):
    '''
    Compute the median of every row of a 2D Numpy array,
    then save the result to a file.

    Arguments:
    input_array: A 2D Numpy array of integers.
    filename: The name of the file to save the medians to.

    Returns:
    None

    Example:
    import numpy as np
    input_array = np.arange(25).reshape(5,5)
    save_multiple_medians(input_array,'test.txt') # Creates file in the current
                                                  # working directory named "test.txt"
                                                  # which contains:
                                                  # 2
                                                  # 7
                                                  # 12
                                                  # 17
                                                  # 22
    '''
    np.savetxt(filename, np.median(input_array, axis=1))
    return None

if __name__ == "__main__":
    pass
