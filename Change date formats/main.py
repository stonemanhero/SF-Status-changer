import csv

"""
important_fields = [
    'AGREEMENT_EXPIRATION_DATE__C',
    'DATE_INVOICED_2__C',
    'DATE_INVOICED_3__C',
    'DATE_INVOICED_4__C',
    'DATE_INVOICED__C',
    'DATE_PAID_2__C',
    'DATE_PAID_3__C',
    'DATE_PAID_4__C',
    'DATE_PAID__C',
    'DATE_RECEIVED_FROM_BUREAU__C',
    'DATE_SENT_TO_BUREAU__C',
    'EXPECTED_PAY_DATE1__C',
    'EXPECTED_PAY_DATE_2__C',
    'EXPECTED_PAY_DATE_3__C',
    'EXPECTED_PAY_DATE_4__C',
    'EXPERIAN_COMPLETE_DATE__C',
    'FULLY_PAID_AMOUNT_DATE__C',
    'PAYMENT_DATE__C',
    'EXPECTED_PAYMENT_DUE_DATE_2__C',
    'CREATEDDATE__C',
    'DATE_OF_BIRTH__C',
    'EXPECTED_PAYDOWN_DATE__C',
    'PARTIAL_PAYMENT_DATE__C'
]
"""
important_fields = ['DATE_OF_BIRTH__C']


def main():
    base_fieldnames = []
    leads = {}
    counter = 1
    input_file = 'errors_3'

    with open('output/' + input_file + '_formated.csv', 'w') as file_output:
        with open('input/' + input_file + '.csv', 'r') as file_input:
            reader_input = csv.DictReader(file_input)
            fieldnames = reader_input.fieldnames
            writer_output = csv.DictWriter(file_output, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
            writer_output.writeheader()

            for row in reader_input:
                leads[row['ID']] = {}
                for field in fieldnames:
                    if field in important_fields:
                        if row[field]:
                            # d, m, y
                            # 2016-09-13T18:14:36.000Z

                            parts = row[field].split('-')
                            day = parts[0]
                            month = parts[1]
                            #year = int(parts[2][:2])
                            year = int(parts[2])

                            if year >= 30:
                                formated_date = '19' + str(year) + '-' + month + '-' + day + 'T00:00:00.000Z'
                            else:
                                formated_date = '20' + str(year) + '-' + month + '-' + day + 'T00:00:00.000Z'

                            leads[row['ID']][field] = formated_date

                        else:
                            leads[row['ID']][field] = ""
                    else:
                        leads[row['ID']][field] = row[field]

                print (counter)
                counter += 1

        for key, value in leads.iteritems():
            writer_output.writerow(value)

if __name__ == "__main__":
    main()
