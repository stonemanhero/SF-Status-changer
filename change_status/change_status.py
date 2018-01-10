import csv


def prepare_mapping():
    """
    Import csv file with old & new statuses
    :return: dictionary
    """
    status_map = {}
    with open('mapping.csv', 'rb') as f:
        reader = csv.DictReader(f)
        for row in reader:
            status_map[row['Old World Statuses'].strip()] = row['Equivalent New World Statuses'].strip()

    return status_map


def main():
    status_map = prepare_mapping()
    missing_statuses = {}
    counter = 1

    with open('lead_new.csv', 'wb') as output_lead:
        with open('lead.csv', 'rb') as f:
            lead_reader = csv.DictReader(f)
            fieldnames = lead_reader.fieldnames

            lead_writer = csv.DictWriter(output_lead, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
            lead_writer.writeheader()

            for row in lead_reader:
                if row['DISPOSITION_TYPE__C'].strip() in status_map:
                    row['DISPOSITION_TYPE__C'] = status_map[row['DISPOSITION_TYPE__C'].strip()]
                else:
                    missing_statuses[row['DISPOSITION_TYPE__C'].strip()] = row['DISPOSITION_TYPE__C'].strip()

                print str(counter)

                counter += 1
                lead_writer.writerow(row)

    with open('missing_statuses.txt', 'w') as f:
        for key, value in missing_statuses.iteritems():
            f.write(key + '\n')

if __name__ == "__main__":
    main()
