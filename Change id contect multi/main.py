import csv


def prepare_mapping():
    """
    Import csv file with old & new statuses
    :return: dictionary
    """
    ids_map = {}
    with open('input/contect_ver_id.csv', 'rb') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['EXTERNALDOCUMENTINFO1'] != '':
                ids_map[row['EXTERNALDOCUMENTINFO1']] = [row['ID'], row['CONTENTDOCUMENTID']]

    return ids_map

def main():
    ids_map = prepare_mapping()
    counter = 0
    found = 0
    missing = 0
    file = 'missing_all'
    column = 'RelatedRecordId'

    with open('output/missing_all_processed.csv', 'wb') as missing_file_output:
        with open('output/' + file + '_processed_found.csv', 'wb') as file_output:
            with open('input/' + file + '.csv', 'rb') as file_input:
                reader = csv.DictReader(file_input)
                fieldnames = reader.fieldnames

                writer = csv.DictWriter(file_output, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
                writer.writeheader()

                writer_missing = csv.DictWriter(missing_file_output, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
                writer_missing.writeheader()

                for row in reader:
                    if row[column] in ids_map:
                        tempId = row[column]
                        row[column] = ids_map[row[column]][0]
                        row['ContentId'] = ids_map[tempId][1]

                        writer.writerow(row)
                        found += 1

                        print (found)
                    else:
                        writer.writerow(row)
                        writer_missing.writerow(row)
                        missing += 1

                    counter += 1

    print ("\nTotal rows processed: " + str(counter))
    print ("Total rows found: " + str(found))
    print("Total rows missing: " + str(missing))

if __name__ == "__main__":
    main()
