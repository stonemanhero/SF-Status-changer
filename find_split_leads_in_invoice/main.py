import csv


def prepare_mapping():
    """
    Import csv file with old & new statuses
    :return: dictionary
    """
    leads = {}
    with open('input/lead_conditions.csv', 'rb') as f:
        reader = csv.DictReader(f)
        for row in reader:
            leads[row['Lead_ID']] = row['Lead_ID']

    return leads


def main():
    invoice_map = prepare_mapping()
    missing_ids = {}
    counter = 1
    counter_conditions_found = 0
    counter_invoices_found = 0

    with open('output/leads_founded_invoice.csv', 'wb') as output_lead_conditions_changed:
        with open('input/leads_output.csv', 'rb') as input_lead_conditions:
            conditions_reader = csv.DictReader(input_lead_conditions)
            fieldnames = conditions_reader.fieldnames

            conditions_writer = csv.DictWriter(output_lead_conditions_changed, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
            conditions_writer.writeheader()

            for row in conditions_reader:
                print counter
                counter += 1

                if row['ID'].strip() in invoice_map:
                    conditions_writer.writerow(row)
                    print "Founded: " + row['ID']
                    counter_invoices_found += 1

    #print "Conditions found: " + str(counter_conditions_found)
    print "Invoices found: " + str(counter_invoices_found)

if __name__ == "__main__":
    main()
