import csv


def prepare_mapping(mapping_file):
    """
    Import csv file with old & new statuses
    :return: dictionary
    """
    ids_map = {}
    with open('input/' + mapping_file + '.csv', 'rb') as f:
        reader = csv.DictReader(f)
        for row in reader:
            ids_map[row['OLD_ORG_ID__C']] = row['ID']

    return ids_map

def main():
    lead_mapping = 'all_lead_ids'
    opp_mapping = 'all_opp_ids'

    lead_ids_map = prepare_mapping(lead_mapping)
    opp_ids_map = prepare_mapping(opp_mapping)
    total_counter = 0
    found = 0

    input_file = 'old_ids'
    column = 'OLD_ORG_ID__C'


    with open('output/' + input_file + '_merged.csv', 'wb') as file_output:
        with open('input/' + input_file + '.csv', 'rb') as file_input:
            reader = csv.DictReader(file_input)
            fieldnames = ['LEAD_ID', 'OPP_ID']

            writer = csv.DictWriter(file_output, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
            writer.writeheader()

            for row in reader:
                if row[column] in lead_ids_map and row[column] in opp_ids_map:
                    new_row = {}
                    new_row['LEAD_ID'] = lead_ids_map[row[column]]
                    new_row['OPP_ID'] = opp_ids_map[row[column]]
                    writer.writerow(new_row)

                    found += 1
                    print (found)

                total_counter += 1

    print ("\nTotal rows processed: " + str(total_counter))
    print ("Total rows found: " + str(found))

if __name__ == "__main__":
    main()
