import csv


def prepare_mapping():
    """
    Import csv file with old & new statuses
    :return: dictionary
    """
    ids_map = {}
    with open('input/ContentVersionIDs.csv', 'rb') as f:
        reader = csv.DictReader(f)
        for row in reader:
            ids_map[row['EXTERNALDOCUMENTINFO1'].strip()] = row['ID'].strip()

    return ids_map


def main():
    ids_map = prepare_mapping()
    founded_counter_lead = 0
    founded_counter_opp = 0
    total_counter = 0
    missing_counter = 0

    with open('output/missing_files_new.csv', 'wb') as file_missing:
        with open('output/files_changed_new_ids.csv', 'wb') as file_output:

            with open('input/files_changed_ids.csv') as file_input_opportunity:
                file_input_opportunity_reader = csv.DictReader(file_input_opportunity)
                fieldnames = file_input_opportunity_reader.fieldnames

                output_writer = csv.DictWriter(file_output, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
                output_writer.writeheader()

                missing_writer = csv.DictWriter(file_missing, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
                missing_writer.writeheader()

                for row in file_input_opportunity_reader:
                    if row['Id'] in ids_map:
                        row['Id'] = ids_map[row['Id']]

                        founded_counter_opp += 1
                        #print "Founded " + str(founded_counter_opp) + ": " + row['Id']
                        output_writer.writerow(row)
                    else:
                        missing_writer.writerow(row)
                        missing_counter += 1

                        print 'opp: '
                        print row

                    total_counter += 1

            with open('input/files_changed_ids_lead.csv') as file_input_lead:
                file_input_lead_reader = csv.DictReader(file_input_lead)

                for row in file_input_lead_reader:
                    if row['Id'] in ids_map:
                        row['Id'] = ids_map[row['Id']]

                        founded_counter_lead += 1
                        #print "Founded (Opp) " + str(founded_counter_lead) + ": " + row['Id']
                        output_writer.writerow(row)
                    else:
                        missing_writer.writerow(row)
                        missing_counter += 1
                        print 'lead: '
                        print row

                    total_counter += 1

        print "Total counter: " + str(total_counter)
        print "Founded counter lead: " + str(founded_counter_lead)
        print "Founded counter opp: " + str(founded_counter_opp)
        print "Total founded: " + str(founded_counter_opp + founded_counter_lead)
        print "Missing counter: " + str(missing_counter)


if __name__ == "__main__":
        main()