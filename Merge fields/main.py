import csv


def main():
    lead_map = {}
    file_for_merge1 = 'extracted_extract_stari_org'
    id_field1 = 'ID'
    file_for_merge2 = 'extracted_extract_stari_org_lead_c'
    id_field2 = 'LEAD__C'
    total_counter = 0

    with open('input/' + file_for_merge1 + '.csv', 'r') as file_input1:
        file_input_reader1 = csv.DictReader(file_input1)
        filednames = file_input_reader1.fieldnames

        for row in file_input_reader1:
            lead_map[row[id_field1]] = {}

            for field in row:
                if field:
                    lead_map[row[id_field1]][field] = row[field]

    with open('input/' + file_for_merge2 + '.csv', 'r') as file_input2:
        file_input_reader2 = csv.DictReader(file_input2)

        for row in file_input_reader2:
            if row[id_field2] in lead_map:
                for field in row:
                    if field != id_field2 and field != 'NAME':
                        if row[field]:
                            lead_map[row[id_field2]][field] = row[field]

    with open('output/merged_lead_fieldnames.csv', 'w') as file_output:
        filednames.append('STAGENAME')
        filednames.append('CLOSEDATE')

        output_file = csv.DictWriter(file_output, fieldnames=filednames, quoting=csv.QUOTE_ALL)
        output_file.writeheader()

        for key, value in lead_map.items():
            value['STAGENAME'] = 'Qualification'
            value['CLOSEDATE'] = '2030-09-12T16:52:40.000Z'

            output_file.writerow(value)
            total_counter += 1

    print("Total: " + str(total_counter))


if __name__ == "__main__":
    main()