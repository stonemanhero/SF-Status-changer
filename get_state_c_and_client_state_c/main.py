import csv

fieldnames = [
    'ID', 'STATE__C', 'CLIENT_STATE__C', 'MERGED_STATE'
]


def prepare_mapping():
    """
    Import csv file with old & new statuses
    :return: dictionary
    """
    ids_map = {}
    with open('input/svi_novi_leadovi.csv', 'rb') as f:
        reader = csv.DictReader(f)
        for row in reader:
            ids_map[row['OLD_ORG_ID__C'].strip()] = row['ID'].strip()

    return ids_map


def main():
    ids_map = prepare_mapping()
    missing_ids = {}
    founded_counter = 0
    total_counter = 0
    missing_counter = 0

    with open('output/missing_get_state.csv', 'wb') as file_missing:
        with open('output/get_state.csv', 'wb') as output_lead_conditions_changed:
            with open('input/lead.csv', 'rb') as input_lead_conditions:
                conditions_reader = csv.DictReader(input_lead_conditions)

                conditions_writer = csv.DictWriter(output_lead_conditions_changed, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
                conditions_writer.writeheader()

                missing_writer = csv.DictWriter(file_missing, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
                missing_writer.writeheader()

                for row in conditions_reader:
                    if row['ID'].strip() in ids_map:
                        new_row = dict()
                        new_row['ID'] = ids_map[row['ID'].strip()]
                        new_row['STATE__C'] = row['STATE__C']
                        new_row['Client_State__c'.upper()] = row['Client_State__c'.upper()]

                        if row['State__c'.upper()]:
                            new_row['MERGED_STATE'] = row['State__c'.upper()]
                        else:
                            new_row['MERGED_STATE'] = row['Client_State__c'.upper()]

                        founded_counter += 1
                        conditions_writer.writerow(new_row)

                    total_counter += 1

    print "Total counter: " + str(total_counter)
    print "Founded counter: " + str(founded_counter)
    print "Missing counter: " + str(missing_counter)


if __name__ == "__main__":
    main()
