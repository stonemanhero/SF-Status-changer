import csv


def prepare_mapping():
    """
    Import csv file with old & new statuses
    :return: dictionary
    """
    status_map = {}
    with open('input/mapping.csv', 'rb') as f:
        reader = csv.DictReader(f)
        for row in reader:
            status_map[row['Old World Statuses'].strip()] = row['Equivalent New World Statuses'].strip()

    return status_map


def main():
    status_map = prepare_mapping()
    missing_statuses = {}
    counter = 1
    input_file = 'Lead'
    column = 'Disposition_Type__c'

    with open('output/' + input_file + '_changed_statuses.csv', 'wb') as output_lead:
        with open('input/' + input_file + '.csv', 'rb') as f:
            lead_reader = csv.DictReader(f)
            fieldnames = lead_reader.fieldnames

            lead_writer = csv.DictWriter(output_lead, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
            lead_writer.writeheader()

            for row in lead_reader:
                if row[column].strip() in status_map:
                    row[column] = status_map[row[column].strip()]
                else:
                    missing_statuses[row[column].strip()] = row[column].strip()

                print(str(counter))

                counter += 1
                lead_writer.writerow(row)

    with open('missing_statuses.txt', 'w') as f:
        for key, value in missing_statuses.iteritems():
            f.write(key + '\n')

if __name__ == "__main__":
    main()
