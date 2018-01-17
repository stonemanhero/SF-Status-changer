import csv


def prepare_mapping():
    """
    Import csv file with old & new statuses
    :return: dictionary
    """
    ids_map = {}
    with open('input/leadID.csv', 'rb') as f:
        reader = csv.DictReader(f)
        for row in reader:
            #ids_map[row['ID'].strip()] = row['OLD_ORG_ID__C'].strip()
            ids_map[row['OLD_ORG_ID__C'].strip()] = row['ID'].strip()

    return ids_map


def main():
    ids_map = prepare_mapping()
    missing_ids = {}
    counter = 1
    counter_conditions_found = 0
    counter_invoices_found = 0

    with open('output/lead_conditions_changed.csv', 'wb') as output_lead_conditions_changed:
        with open('input/lead_conditions.csv', 'rb') as input_lead_conditions:
            conditions_reader = csv.DictReader(input_lead_conditions)
            fieldnames = conditions_reader.fieldnames

            conditions_writer = csv.DictWriter(output_lead_conditions_changed, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
            conditions_writer.writeheader()

            for row in conditions_reader:
                if row['Lead_ID'].strip() in ids_map:
                    row['Lead_ID'] = ids_map[row['Lead_ID'].strip()]
                    print "Conditions found: " + row['Lead_ID']
                    counter_conditions_found += 1
                    conditions_writer.writerow(row)
                else:
                    missing_ids[row['Lead_ID'].strip()] = row['Lead_ID'].strip()



    with open('output/lead_invoice_changed.csv', 'wb') as output_lead_invoice_changed:
        with open('input/lead_invoice.csv', 'rb') as input_lead_invoice:
            invoice_reader = csv.DictReader(input_lead_invoice)
            fieldnames = invoice_reader.fieldnames

            invoice_writer = csv.DictWriter(output_lead_invoice_changed, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
            invoice_writer.writeheader()

            for row in invoice_reader:
                if row['Lead_ID'].strip() in ids_map:
                    row['Lead_ID'] = ids_map[row['Lead_ID'].strip()]
                    print "Invoice found: " + row['Lead_ID']
                    counter_invoices_found += 1
                    invoice_writer.writerow(row)
                else:
                    missing_ids[row['Lead_ID'].strip()] = row['Lead_ID'].strip()


    with open('output/missing_ids.txt', 'w') as f:
        for key, value in missing_ids.iteritems():
            f.write(key + '\n')

    print "Conditions found: " + str(counter_conditions_found)
    print "Invoices found: " + str(counter_invoices_found)

if __name__ == "__main__":
    main()
