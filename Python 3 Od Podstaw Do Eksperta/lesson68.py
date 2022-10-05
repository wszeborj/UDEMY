
with open('test', 'w') as file:
    all_data = file.read()
    data_list_by_space = file.read().splitlines()
    data_line1 = file.readline() #read only one line
    data_line2 = file.readline()    # second call read next line nas so go on
    data_lines_list = file.readlines() # read all lines but split it by enter and it leaves '\n' in string
