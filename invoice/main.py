import csv

fieldnames = [
    'Lead_ID', 'Amount_Due__c', 'Amount_Invoiced__c', 'Amount_Paid__c', 'Collected__c', 'Date_Invoiced__c',
    'Date_Paid__c', 'Expected_Pay_Date__c', 'Invoice_Link__c', 'Invoice_Notes__c', 'Invoiced__c',
    'Partial_Payment_Amount__c', 'Partial_Payment_Date__c', 'XERO_ContactID__c'
]

C_SUFFIX = '__C'

# Fields
AMOUNT_DUE = 'AMOUNT_DUE'
AMOUNT_INVOICED = 'AMOUNT_INVOICED'
AMOUNT_PAID = 'AMOUNT_PAID'
COLLECTED = 'COLLECTED'
DATE_INVOICED = 'DATE_INVOICED'
DATE_PAID = 'DATE_PAID'
EXPECTED_PAY_DATE = 'EXPECTED_PAY_DATE'
EXPECTED_PAYMENT_DUE_DATE = 'EXPECTED_PAYMENT_DUE_DATE'
INVOICE_LINK = 'INVOICE_LINK'
INVOICE_NOTES = 'INVOICE_NOTES'
INVOICED = 'INVOICED'
PARTIAL_PAYMENT_AMOUNT = 'PARTIAL_PAYMENT_AMOUNT'
PARTIAL_PAYMENT_DATE = 'PARTIAL_PAYMENT_DATE'
XERO_CONTACTID = 'XERO_CONTACTID'

MAX_LOOP = 11

def main(fieldnames_param):
    counter = 1

    lead_ids = {}
    lead_c_ids = {}

    with open('input/lead_fix_invoice.csv', 'rb') as file_lead:
        reader_lead = csv.DictReader(file_lead)

        for row in reader_lead:
            lead_ids[row['ID']] = {}
            lead_ids[row['ID']]['LEAD_ID'] = row['ID']

            for i in range(1, 6):
                lead_ids[row['ID']][AMOUNT_DUE + str(i) + C_SUFFIX] = row[AMOUNT_DUE + str(i) + C_SUFFIX]
                lead_ids[row['ID']][AMOUNT_INVOICED + str(i) + C_SUFFIX] = row[AMOUNT_INVOICED + str(i) + C_SUFFIX]
                lead_ids[row['ID']][AMOUNT_PAID + str(i) + C_SUFFIX] = row[AMOUNT_PAID + str(i) + C_SUFFIX]
                lead_ids[row['ID']][INVOICE_LINK + str(i) + C_SUFFIX] = row[INVOICE_LINK + str(i) + C_SUFFIX]
                lead_ids[row['ID']][INVOICE_NOTES + str(i) + C_SUFFIX] = row[INVOICE_NOTES + str(i) + C_SUFFIX]

                if i in [1, 2, 3]:
                    lead_ids[row['ID']][COLLECTED + str(i) + C_SUFFIX] = row[COLLECTED + str(i) + C_SUFFIX]
                else:
                    lead_ids[row['ID']][COLLECTED + str(i) + C_SUFFIX] = ""

                if i in [1, 2, 3, 4]:
                    lead_ids[row['ID']][DATE_INVOICED + str(i) + C_SUFFIX] = row[DATE_INVOICED + str(i) + C_SUFFIX]
                    lead_ids[row['ID']][DATE_PAID + str(i) + C_SUFFIX] = row[DATE_PAID + str(i) + C_SUFFIX]
                    lead_ids[row['ID']][EXPECTED_PAY_DATE + str(i) + C_SUFFIX] = row[EXPECTED_PAY_DATE + str(i) + C_SUFFIX]
                else:
                    lead_ids[row['ID']][DATE_INVOICED + str(i) + C_SUFFIX] = ""
                    lead_ids[row['ID']][DATE_PAID + str(i) + C_SUFFIX] = ""
                    lead_ids[row['ID']][EXPECTED_PAY_DATE + str(i) + C_SUFFIX] = ""

                if i in [1, 2]:
                    lead_ids[row['ID']][INVOICED + str(i) + C_SUFFIX] = row[INVOICED + str(i) + C_SUFFIX]
                else:
                    lead_ids[row['ID']][INVOICED + str(i) + C_SUFFIX] = ""

                if i in [2, 3, 4]:
                    lead_ids[row['ID']][EXPECTED_PAYMENT_DUE_DATE + str(i) + C_SUFFIX] = row[EXPECTED_PAYMENT_DUE_DATE + str(i) + C_SUFFIX]
                else:
                    lead_ids[row['ID']][EXPECTED_PAYMENT_DUE_DATE + str(i) + C_SUFFIX] = ""

                if i == 1:
                    lead_ids[row['ID']][XERO_CONTACTID + str(i) + C_SUFFIX] = row[XERO_CONTACTID + str(i) + C_SUFFIX]
                    lead_ids[row['ID']][PARTIAL_PAYMENT_AMOUNT + str(i) + C_SUFFIX] = row[PARTIAL_PAYMENT_AMOUNT + str(i) + C_SUFFIX]
                    lead_ids[row['ID']][PARTIAL_PAYMENT_DATE + str(i) + C_SUFFIX] = row[PARTIAL_PAYMENT_DATE + str(i) + C_SUFFIX]
                else:
                    lead_ids[row['ID']][XERO_CONTACTID + str(i) + C_SUFFIX] = ""
                    lead_ids[row['ID']][PARTIAL_PAYMENT_AMOUNT + str(i) + C_SUFFIX] = ""
                    lead_ids[row['ID']][PARTIAL_PAYMENT_DATE + str(i) + C_SUFFIX] = ""

            print counter
            counter += 1

    with open('input/lead_c_fix_invoice.csv', 'rb') as file_lead_c:
        counter = 0
        reader_lead_c = csv.DictReader(file_lead_c)

        for row in reader_lead_c:
            for i in range(2, 6):
                lead_ids[row['LEAD_ID']][XERO_CONTACTID + str(i) + C_SUFFIX] = row[XERO_CONTACTID + str(i) + C_SUFFIX]

            print counter
            counter += 1

    with open('output/lead_invoice.csv', 'wb') as file_lead_invoice:
        output_lead_writer = csv.DictWriter(file_lead_invoice, fieldnames=fieldnames_param, quoting=csv.QUOTE_ALL)
        output_lead_writer.writeheader()

        for key, value in lead_ids.iteritems():
            for i in range(1, 6):
                procced_status = False

                if value[AMOUNT_DUE + str(i) + C_SUFFIX] != "":
                    procced_status = True

                if value[AMOUNT_INVOICED + str(i) + C_SUFFIX] != "":
                    procced_status = True

                if value[AMOUNT_PAID + str(i) + C_SUFFIX] != "":
                    procced_status = True

                if value[COLLECTED + str(i) + C_SUFFIX] != "":
                    procced_status = True

                if value[DATE_INVOICED + str(i) + C_SUFFIX] != "":
                    procced_status = True

                if value[DATE_PAID + str(i) + C_SUFFIX] != "":
                    procced_status = True

                if value[EXPECTED_PAY_DATE + str(i) + C_SUFFIX] != "":
                    procced_status = True

                if value[EXPECTED_PAYMENT_DUE_DATE + str(i) + C_SUFFIX] != "":
                    procced_status = True

                if value[INVOICE_LINK + str(i) + C_SUFFIX] != "":
                    procced_status = True

                if value[INVOICE_NOTES + str(i) + C_SUFFIX] != "":
                    procced_status = True

                if value[INVOICED + str(i) + C_SUFFIX] != "":
                    procced_status = True

                if value[PARTIAL_PAYMENT_AMOUNT + str(i) + C_SUFFIX] != "":
                    procced_status = True

                if value[PARTIAL_PAYMENT_DATE + str(i) + C_SUFFIX] != "":
                    procced_status = True

                #if value[XERO_CONTACTID + str(i) + C_SUFFIX] != "":
                #    procced_status = True

                if procced_status:
                    output_lead = {
                                    'Lead_ID': value['LEAD_ID'],
                                    'Amount_Due__c': value[AMOUNT_DUE + str(i) + C_SUFFIX],
                                    'Amount_Invoiced__c': value[AMOUNT_INVOICED + str(i) + C_SUFFIX],
                                    'Amount_Paid__c': value[AMOUNT_PAID + str(i) + C_SUFFIX],
                                    'Collected__c': value[COLLECTED + str(i) + C_SUFFIX],
                                    'Date_Invoiced__c': value[DATE_INVOICED + str(i) + C_SUFFIX],
                                    'Date_Paid__c': value[DATE_PAID + str(i) + C_SUFFIX],
                                    'Expected_Pay_Date__c': value[EXPECTED_PAY_DATE + str(i) + C_SUFFIX],
                                    'Invoice_Link__c': value[INVOICE_LINK + str(i) + C_SUFFIX],
                                    'Invoice_Notes__c': value[INVOICE_NOTES + str(i) + C_SUFFIX],
                                    'Invoiced__c': value[INVOICED + str(i) + C_SUFFIX],
                                    'Partial_Payment_Amount__c': value[PARTIAL_PAYMENT_AMOUNT + str(i) + C_SUFFIX],
                                    'Partial_Payment_Date__c': value[PARTIAL_PAYMENT_DATE + str(i) + C_SUFFIX],
                                    'XERO_ContactID__c': value[XERO_CONTACTID + str(i) + C_SUFFIX]
                                }

                    output_lead_writer.writerow(output_lead)
if __name__ == "__main__":
    main(fieldnames)