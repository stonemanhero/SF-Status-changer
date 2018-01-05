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
            status_map[row['Old World Statuses']] = row['Equivalent New World Statuses']

    return status_map


def main():
    status_map = prepare_mapping()
    counter = 1

    with open('lead_new.csv', 'wb') as output_lead:
        with open('lead.csv', 'rb') as f:
            lead_reader = csv.DictReader(f)
            fieldnames = lead_reader.fieldnames

            lead_writer = csv.DictWriter(output_lead, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
            lead_writer.writeheader()

            for row in lead_reader:
                if row['DISPOSITION_TYPE__C'] in status_map:
                    row['DISPOSITION_TYPE__C'] = status_map[row['DISPOSITION_TYPE__C']]

                print str(counter)

                counter += 1
                lead_writer.writerow(row)


if __name__ == "__main__":
    main()
