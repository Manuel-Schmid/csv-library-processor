import os


def main():
    pass


# Opens the CSV file with the name given as argument. If successful, returns the
# a tuple of four lists: The column names, column types, distinct column values
# (list of lists) and the records (list of lists). Otherwise, raises an
# exception.
def read_input_file(input_file):
    return [], [], [], []


# Parses the CSV header from the already opened file stream input_file.
# If successful, returns the list of column names.
# Otherwise, raises an exception.
def read_headers(input_file):
    return []


# Parses the CSV records from the already opened file stream input_file.
# It determines the column types based on the first record.
# If successful, returns the list of column types, distinct column
# values and records. Otherwise, raises an exception. Note: The implementation
# of this function handles multi-line string values in records.
def read_records(input_file, columns_count):
    return [], [], []


# Asks the user to input a comma-seperated list of unique integers between 1 and
# the given maximum value with the given minimum length using the given
# description, and returns the list of integers. Repeatedly asks the user upon
# invalid input.
def get_unique_integers_from_user(description, max_value, min_length):
    return []


# Checks that the given argument is a valid output file name. If this is not
# the case, raises an exception. Returns None.
def check_output_file(output_file):
    pass


# Writes the column names and the given records to the CSV file with the given
# name, only taking into account the given column indices in output columns and
# filters (a list of pairs of column indices and a list of corresponding values
# to exclude).
def write_output_file(output_file, column_names, records, output_columns, filters):
    with open(output_file, 'w') as output_csv:
        pass


# Prints a summary of the copying and filtering operations to be applied to
# generate the CSV file for the given column names, the column indices provided
# as output columns to be copied and the filters (a list of pairs of column
# indices and a list of corresponding values to exclude).
def print_operations(column_names, output_columns, filters):
    pass


if __name__ == '__main__':
    main()