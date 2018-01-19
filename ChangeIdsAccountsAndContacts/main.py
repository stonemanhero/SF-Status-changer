import csv

def prepare_mapping():
    """
    Import csv file with old & new statuses
    :return: dictionary
    """
    ids_map = {}
    with open('input/opp_ids.csv', 'rb') as f:
        reader = csv.DictReader(f)
        for row in reader:
            ids_map[row['OLD_ORG_ID__C'].strip()] = row['ID'].strip()

    return ids_map


def main():
    ids_map = prepare_mapping()
    counter = 0
    founded_counter = 0

    with open('output/contacts_with_new_ids.csv', 'wb') as file_output:
        with open('input/contacts.csv', 'rb') as file_input:
            reader_input = csv.DictReader(file_input)
            fieldnames = reader_input.fieldnames

            writer_output = csv.DictWriter(file_output, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
            writer_output.writeheader()

            for row in reader_input:
                if row['ID'] in ids_map:
                    row['ID'] = ids_map[row['ID']]
                    writer_output.writerow(row)
                    founded_counter += 1

                counter += 1
                print counter

    print "Total: " + str(counter)
    print "Founded: " + str(founded_counter)

if __name__ == "__main__":
    main()