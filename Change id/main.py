import csv


def prepare_mapping():
    """
    Import csv file with old & new statuses
    :return: dictionary
    """
    ids_map = {}
    with open('input/user_mapping_2.csv', 'rb') as f:
        reader = csv.DictReader(f)
        for row in reader:
            ids_map[row['OLD_ID']] = row['ID']

    return ids_map

def main():
    ids_map = prepare_mapping()
    counter = 0
    found = 0
    missing = 0
    file = 'missing_all_processed_found'
    column = 'InsertedById'

    with open('output/not_usage.csv', 'wb') as missing_file_output:
        with open('output/' + file + '_changes_user.csv', 'wb') as file_output:
            with open('input/' + file + '.csv', 'rb') as file_input:
                reader = csv.DictReader(file_input)
                fieldnames = reader.fieldnames

                writer = csv.DictWriter(file_output, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
                writer.writeheader()

                writer_missing = csv.DictWriter(missing_file_output, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
                writer_missing.writeheader()

                for row in reader:
                    if row[column] in ids_map:
                        row[column] = ids_map[row[column]]

                        writer.writerow(row)
                        found += 1

                        print (found)
                    else:
                        row[column] = '005f4000000QbEhAAK'
                        writer.writerow(row)
                        missing += 1

                    counter += 1

    print ("\nTotal rows processed: " + str(counter))
    print ("Total rows found: " + str(found))
    print("Total rows missing: " + str(missing))

if __name__ == "__main__":
    main()
