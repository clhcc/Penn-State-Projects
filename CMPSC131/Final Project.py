# This project is to use two files and turn them into a table and analyze it.

# Author: Linhan Cai

# Get the data.
def get_IDs(filename):
    id_list = []
    sales_data = []
    with open(filename,'r') as id_file:
        for lines in id_file:
            id_list.append(int(lines.rstrip('\n')))
    for i in range(len(id_list)):
        sales_data.append([0.0]*4)
    return id_list,sales_data

# Process the data.
def process_sales_data(filename, id_list, sales_data):
    with open(filename,'r') as data_file:
        for lines in data_file:
            data_list = lines.split()
            for i in range(len(id_list)):
                if int(data_list[0]) == id_list[i]:
                    month = int(data_list[1])
                    sales_amount = float(data_list[2])
                    if month >= 1 and month <= 3:
                        quarter = 0
                    elif month >= 4 and month <= 6:
                        quarter = 1
                    elif month >= 7 and month <= 9:
                        quarter = 2
                    else:
                        quarter = 3
                    sales_data[i][quarter] += sales_amount

# Report the data.
def print_report(id_list, sales_data):
    print('--------Annual Sales Report--------' + '\n')
    print('ID\tQT1\tQT2\tQT3\tQT4\tTotal')
    for i in range(len(id_list)):
        print(id_list[i],
              round(sales_data[i][0], 2),
              round(sales_data[i][1], 2),
              round(sales_data[i][2], 2),
              round(sales_data[i][3], 2),
              round(sum(sales_data[i]), 2),
              sep = '\t',)

    SalesbyQtr = ([0.0] * 4)
    for i in range(4):
        for j in range(6):
            SalesbyQtr[i] += sales_data[j][i]
    print('Total', end='\t')
    for i in range(4):
        print(round(SalesbyQtr[i], 2), end='\t')
    print(round(sum(SalesbyQtr), 2))
    print('\n')

    MaxAmountbyPerson = 0.0
    MaxPersonID = 0
    for i in range(6):
        for j in range(4):
            if sales_data[i][j] > MaxAmountbyPerson:
                MaxAmountbyPerson = sales_data[i][j]
                MaxPersonID = id_list[i]
    print('Max sales by Salesperson: ID = ', MaxPersonID, ', Amount = $', round(MaxAmountbyPerson, 2))

    MaxAmountbyQtr = 0.0
    MaxQtr = 0
    for i in range(4):
        if SalesbyQtr[i] > MaxAmountbyQtr:
            MaxAmountbyQtr = SalesbyQtr[i]
            MaxQtr = i+1
    print('Max sales by Quarter: Quarter = ', MaxQtr, ', Amount = $', round(MaxAmountbyQtr, 2))

# Run the program.
def main():
    IDFile = input('Enter the name of the sales ids file: ')
    SalesData = input('Enter the name of the sales data file: ')
    id_list, sales_data = get_IDs(IDFile)
    process_sales_data(SalesData,id_list,sales_data)
    print_report(id_list,sales_data)
    
main()
