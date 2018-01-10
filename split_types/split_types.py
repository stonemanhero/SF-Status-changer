import csv


def prepare_mapping():
    """
    Import csv file with statuses and types (lead or opportunity)
    :return: dictionary
    """
    status_map = {}
    with open('input/types.csv', 'rb') as f:
        reader = csv.DictReader(f)
        for row in reader:
            status_map[row['Status'].strip()] = row['Type']

    return status_map


def main():
    status_map = prepare_mapping()

    counter = 1

    with open('output/leads_output.csv', 'wb') as output_lead:
        with open('output/opportunity_output.csv', 'wb') as output_opportunity:
            with open('output/nontype_output.csv', 'wb') as output_nontype:

                with open('input/lead_new.csv', 'rb') as f:
                    lead_reader = csv.DictReader(f)
                    fieldnames = lead_reader.fieldnames

                    lead_writer = csv.DictWriter(output_lead, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
                    opportunity_writer = csv.DictWriter(output_opportunity, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
                    nontype_writer = csv.DictWriter(output_nontype, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)

                    lead_writer.writeheader()
                    opportunity_writer.writeheader()
                    nontype_writer.writeheader()

                    for row in lead_reader:
                        # If status start with DL send row to Opportunity
                        if row['DISPOSITION_TYPE__C'].strip()[0:2] == "DL":
                            opportunity_writer.writerow(row)
                            print str(counter) + ' --> Opportunity'
                        else:
                            if row['DISPOSITION_TYPE__C'].strip() in status_map:
                                if status_map[row['DISPOSITION_TYPE__C'].strip()] == "lead":
                                    lead_writer.writerow(row)
                                    print str(counter) + ' --> Lead'
                                elif status_map[row['DISPOSITION_TYPE__C'].strip()] == "opportunity":
                                    opportunity_writer.writerow(row)
                                    print str(counter) + ' --> Opportunity'
                                else:
                                    nontype_writer.writerow(row)
                                    print str(counter) + ' --> None'
                            else:
                                nontype_writer.writerow(row)
                                print str(counter) + ' --> None'

                        counter += 1


if __name__ == "__main__":
    main()
