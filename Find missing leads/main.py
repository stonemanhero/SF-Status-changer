import csv


def main():
    ids_map = dict()
    founded_counter = 0
    total_counter = 0

    output_file_name = 'missing_files'
    old_ids_file_name = 'all_opps_no_contacts'
    data_file_name = 'contactsAll_changed_ids'
    id_field = 'ID'
    mapping_field = 'ID'

    with open('output/' + output_file_name + '.csv', 'w') as file_output:
        with open('input/' + old_ids_file_name + '.csv', 'r') as file_input_lead:
            reader_input_lead = csv.DictReader(file_input_lead)

            for row in reader_input_lead:
                ids_map[row[mapping_field]] = row[mapping_field]

        with open('input/' + data_file_name + '.csv', 'r') as file_lead:
            reader_leads = csv.DictReader(file_lead)
            fieldnames = reader_leads.fieldnames

            writer_output = csv.DictWriter(file_output, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
            writer_output.writeheader()

            for row in reader_leads:
                if row[id_field] in ids_map:
                    writer_output.writerow(row)
                    founded_counter += 1

                total_counter += 1

    print("Total: " + str(total_counter))
    print("Founded: " + str(founded_counter))

if __name__ == "__main__":
    main()