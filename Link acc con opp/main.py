import csv


def main():
    ids_map = dict()
    founded_counter = 0
    total_counter = 0

    output_file_name = 'extracted_con'
    old_ids_file_name = 'opp_lead'
    data_file_name = 'contact_ids_opps'
    id_field = 'OPPORTUNITY__C'

    with open('output/' + output_file_name + '.csv', 'w') as file_output:
        with open('input/' + old_ids_file_name + '.csv', 'r') as file_input_lead:
            reader_input_lead = csv.DictReader(file_input_lead)

            for row in reader_input_lead:
                ids_map[row['ID']] = row['SOURCE_LEAD__C']

        with open('input/' + data_file_name + '.csv', 'r') as file_lead:
            reader_leads = csv.DictReader(file_lead)
            #fieldnames = reader_leads.fieldnames
            fieldnames = []
            fieldnames.append('CONTACT_ID')
            fieldnames.append('LEAD_SOURCE')

            writer_output = csv.DictWriter(file_output, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
            writer_output.writeheader()

            for row in reader_leads:
                if row[id_field] in ids_map:
                    new_row = {}
                    new_row['CONTACT_ID'] = row['ID']
                    new_row['LEAD_SOURCE'] = ids_map[row['OPPORTUNITY__C']]
                    writer_output.writerow(new_row)
                    founded_counter += 1

                total_counter += 1

    print("Total: " + str(total_counter))
    print("Founded: " + str(founded_counter))

if __name__ == "__main__":
    main()