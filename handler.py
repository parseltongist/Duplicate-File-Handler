# write your code here
import os
import sys


def check_directory():
    # this function checks whether the directory argument provided and
    # continues execution fun main()  or prints an error message & exit the program
    args = sys.argv
    if len(args) < 2:  # 2 here because counting starts from 0, and args[0] is the name of a python3 script
        print("Directory is not specified")
        exit()
    else:
        pass


def obtaining_data_list(file_extension):
    # this function scans provided directory and creates the list of absolut paths to all files in directory
    # if arg file_extension is empty - all paths kept, else - lst will keep only paths to files with a specified extension
    lst = []
    for root, dirs, files in os.walk('.', topdown=True):
        for name in files:
            lst.append(os.path.join(root, name))
    if file_extension != "":
        lst = [x for x in lst if file_extension == os.path.splitext(x)[1][1:]]
    else:
        lst = [x for x in lst if os.path.splitext(x)[1][1:] != ""]
    print("")
    # returns a filtered list of absolut paths to all files with the requested extension in directory
    return lst


def sort_list(sizes):
    # this function takes list of file sizes and sort it in Descending or Ascending order
    # returns sorted list
    sort_by = int(input("""Size sorting options:
1. Descending
2. Ascending\n"""))
    if sort_by == 1:
        sizes = sorted(sizes, reverse=True)
        return sizes
    elif sort_by == 2:
        sizes = sorted(sizes, reverse=False)
        return sizes
    else:
        print("\nWrong option")
        sort_list(sizes)


def creating_sorted_dict(data_list):
    # this function takes a filtered list of absolut paths, produced by obtaining_data_list() function
    # create a list of unique file sizes and creates and empty dict using the list of sizes as keys
    # appends lists of paths values to their keys in paths_dict
    file_sizes = sort_list(list(set(os.path.getsize(x) for x in data_list)))
    paths_dict = dict.fromkeys(file_sizes, [])
    # paths_dict = dict.fromkeys(sort_list(list(set(os.path.getsize(x) for x in data_list))), [])
    for x in paths_dict:
        paths_dict[x] = [y for y in data_list if str(x) == str(os.path.getsize(y))]
        # returns dict of file sizes as keys and lists of absolut paths as values
    return paths_dict


def print_results(paths_dict):
    # this function prints the output(result) of the program. if a format key: \n values
    print()
    for x in paths_dict:
        if len(paths_dict[x]) > 1:
            print(int(x), "bytes")
            for y in paths_dict[x]:
                if len(y) > 1:
                    print(y)
            print()
    print()


def main():
    # this is the main function which calls other functions in a defined order
    check_directory()
    full_data = obtaining_data_list(input("Enter the file format:\n"))
    paths_dict = creating_sorted_dict(full_data)
    print_results(paths_dict)


if __name__ == "__main__":
    main()
