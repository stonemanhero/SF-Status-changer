import csv


def prepare_mapping():
    """
    Import csv file with old & new statuses
    :return: dictionary
    """
    ids_map = {}
    with open('input/lead_map.csv', 'rb') as f:
        reader = csv.DictReader(f)
        for row in reader:
            ids_map[row['Old']] = row['New']

    return ids_map

def main():
    ids_map = prepare_mapping()
    counter = 0
    found = 0
    file = 'extracted_Lead_changed_statuses_fields'
    column = 'Id'

    with open('output/' + file + '_extracted.csv', 'wb') as file_output:
        with open('input/' + file + '.csv', 'rb') as file_input:
            reader = csv.DictReader(file_input)
            fieldnames = reader.fieldnames

            writer = csv.DictWriter(file_output, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
            writer.writeheader()

            for row in reader:
                if row[column] in ids_map:
                    writer.writerow(row)
                    found += 1

                    print (found)

                counter += 1

    print ("\nTotal rows processed: " + str(counter))
    print ("Total rows found: " + str(found))

if __name__ == "__main__":
    main()
