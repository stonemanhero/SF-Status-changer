import csv


def main():
    ids_map = dict()
    founded_counter = 0
    total_counter = 0

    output_file_name = 'founded_ids_opp'
    old_ids_file_name = 'all_opp_ids'
    data_file_name = 'missing_leads'
    id_field = 'Id'

    with open('output/' + output_file_name + '.csv', 'w') as file_output:
        with open('input/' + old_ids_file_name + '.csv', 'r') as file_input_lead:
            reader_input_lead = csv.DictReader(file_input_lead)

            for row in reader_input_lead:
                ids_map[row['OLD_ORG_ID__C']] = row['ID']

        with open('input/' + data_file_name + '.csv', 'r') as file_lead:
            reader_leads = csv.DictReader(file_lead)
            #fieldnames = reader_leads.fieldnames
            fieldnames = []
            fieldnames.append('OLD_ORG_ID')
            fieldnames.append('NEW_ORG_ID')

            writer_output = csv.DictWriter(file_output, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
            writer_output.writeheader()

            for row in reader_leads:
                if row[id_field] in ids_map:
                    new_row = {}
                    new_row['OLD_ORG_ID'] = row[id_field]
                    new_row['NEW_ORG_ID'] = ids_map[row[id_field]]
                    writer_output.writerow(new_row)
                    founded_counter += 1

                total_counter += 1

    print("Total: " + str(total_counter))
    print("Founded: " + str(founded_counter))

if __name__ == "__main__":
    main()