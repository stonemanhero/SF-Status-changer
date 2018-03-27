import csv


def prepare_mapping():
    """
    Import csv file with old & new statuses
    :return: dictionary
    """
    ids_map = {}
    with open('input/user_mapping.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            ids_map[row['OLD_ORG_ID']] = row['NEW_ORG_ID']

    return ids_map


def main():
    ids_map = prepare_mapping()
    counter = 0
    found = 0
    file = 'FeedPost'
    column = 'InsertedById'
    igor_id = '005f4000000QbEhAAK'

    with open('output/' + file + '_changed_ids.csv', 'w') as file_output:
        with open('input/' + file + '.csv', 'r') as file_input:
            reader = csv.DictReader(file_input)
            fieldnames = reader.fieldnames

            writer = csv.DictWriter(file_output, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
            writer.writeheader()

            for row in reader:
                if row[column] in ids_map:
                    row[column] = ids_map[row[column]]

                    writer.writerow(row)
                    found += 1

                    print (found)
                else:
                    row[column] = igor_id
                    writer.writerow(row)

                counter += 1

    print ("\nTotal rows processed: " + str(counter))
    print ("Total rows found: " + str(found))

if __name__ == "__main__":
    main()
