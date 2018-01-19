import csv


def prepare_mapping():
    """
    Import csv file with old & new statuses
    :return: dictionary
    """
    ids_map = {}
    with open('input/imported_files.csv', 'rb') as f:
        reader = csv.DictReader(f)
        for row in reader:
            ids_map[row['EXTERNALDOCUMENTINFO1'].strip()] = row['ID'].strip()

    return ids_map


def main():
    ids_map = prepare_mapping()
    total_counter = 0
    founded_counter = 0

    with open('output/missing_files.csv', 'wb') as output_file:
        with open('input/ContentVersion.csv', 'rb') as input_file:
            input_reader = csv.DictReader(input_file)
            fieldnames = input_reader.fieldnames

            output_writer = csv.DictWriter(output_file, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
            output_writer.writeheader()

            for row in input_reader:
                if row['Id'] not in ids_map:
                    #row['Id'] = ids_map['ID']
                    output_writer.writerow(row)
                    founded_counter += 1

                total_counter += 1
                print total_counter

    print 'Founded counter: ' + str(founded_counter)

if __name__ == "__main__":
    main()
