import csv

C_SUFFIX = '__C'

# Fields
XERO_CONTACTID = 'XERO_CONTACTID'


def main():
    counter = 1
    lead_c_ids = {}

    with open('output/lead_c_fix.csv', 'wb') as file_lead_c_fix_invoice:
        fieldnames = ['LEAD_ID']

        for i in range(1, 5):
            fieldnames.append(XERO_CONTACTID + str(i) + C_SUFFIX)


        lead_c_writer = csv.DictWriter(file_lead_c_fix_invoice, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        lead_c_writer.writeheader()

        with open('input/lead_c_to_extract_xero.csv', 'rb') as file_lead_c:
            reader_lead_c = csv.DictReader(file_lead_c)

            for row in reader_lead_c:
                if row['LEAD__C'] != "":
                    if row['LEAD__C'] in lead_c_ids:
                        print "Duplicate: " + row['LEAD__C']
                    else:
                        lead_c_ids[row['LEAD__C']] = {}

                        for i in range(1, 5):
                            write_status = False

                            if row[XERO_CONTACTID + str(i) + C_SUFFIX]:
                                write_status = True
                                break

                        if write_status:
                            lead_c_ids[row['LEAD__C']]['LEAD_ID'] = row['LEAD__C']

                            for i in range(1, 5):
                                lead_c_ids[row['LEAD__C']][XERO_CONTACTID + str(i) + C_SUFFIX] = row[XERO_CONTACTID + str(i) + C_SUFFIX]

                print counter
                counter += 1

            for key, value in lead_c_ids.iteritems():
                if value:
                    lead_c_writer.writerow(value)

if __name__ == "__main__":
    main()