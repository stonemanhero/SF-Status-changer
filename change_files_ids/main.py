import csv


def prepare_mapping():
    """
    Import csv file with old & new statuses
    :return: dictionary
    """
    ids_map = {}
    with open('input/opportunityID.csv', 'rb') as f:
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

    with open('output/missing_attachments_ids_after_opportunity.csv', 'wb') as file_missing:
        with open('output/attachments_changed_ids_opportunity.csv', 'wb') as output_lead_conditions_changed:
            with open('input/attachments_for_leads.csv', 'rb') as input_lead_conditions:
                conditions_reader = csv.DictReader(input_lead_conditions)
                fieldnames = conditions_reader.fieldnames

                conditions_writer = csv.DictWriter(output_lead_conditions_changed, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
                conditions_writer.writeheader()

                missing_writer = csv.DictWriter(file_missing, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
                missing_writer.writeheader()

                for row in conditions_reader:
                    if row['ParentId'].strip() in ids_map:
                        row['ParentId'] = ids_map[row['ParentId'].strip()]
                        print "Found: " + row['ParentId']
                        founded_counter += 1
                        conditions_writer.writerow(row)
                    else:
                        missing_ids[row['ParentId'].strip()] = row['ParentId'].strip()
                        missing_writer.writerow(row)
                        missing_counter += 1

                    total_counter += 1

    print "Total counter: " + str(total_counter)
    print "Founded counter: " + str(founded_counter)
    print "Missing counter: " + str(missing_counter)


if __name__ == "__main__":
    main()
