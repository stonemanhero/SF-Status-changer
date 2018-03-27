import csv

def main():
    counter = 0
    founded_counter = 0

    file = 'ALL_OPPS'
    column = 'BUSINESS_NAME__C'

    with open('output/' + file + '_processed.csv', 'wb') as file_output:
        with open('input/' + file + '.csv', 'rb') as file_input:
            reader_input = csv.DictReader(file_input)
            fieldnames = reader_input.fieldnames

            writer_output = csv.DictWriter(file_output, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
            writer_output.writeheader()

            for row in reader_input:
                if row[column] == "":
                    row[column] = 'N/A'
                    founded_counter += 1

                writer_output.writerow(row)
                counter += 1
                print(counter)

    print ("Total: " + str(counter))
    print ("Founded: " + str(founded_counter))

if __name__ == "__main__":
    main()