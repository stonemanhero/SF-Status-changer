import csv


def main():
    header = []
    filednames_map = {}
    file_map = 'map_origination'
    file_input_to_process = 'Lead'
    id_field = 'Id'
    founded_counter = 0
    total_counter = 0

    with open('input/' + file_map + '.csv', 'r') as file_input_map:
        map_reader = csv.DictReader(file_input_map)

        print("Loading map...")
        for row in map_reader:
            filednames_map[row['Old']] = row['New']
            header.append(row['New'])

        header.append(id_field)
        #header.append('NAME')

    print("Processing input file...")
    with open('output/extracted_' + file_input_to_process + '_origination.csv', 'w') as file_output:
        output_file = csv.DictWriter(file_output, fieldnames=header, quoting=csv.QUOTE_ALL)
        output_file.writeheader()

        with open('input/' + file_input_to_process + '.csv', 'r') as file_input:
            file_input_reader = csv.DictReader(file_input)

            for row in file_input_reader:
                new_row = {}
                new_row[id_field] = row[id_field]

                for field in row:
                    if field in filednames_map:
                        new_row[filednames_map[field]] = row[field]

                output_file.writerow(new_row)
                total_counter += 1

    print("Total: " + str(total_counter))


if __name__ == "__main__":
    main()