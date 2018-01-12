import csv

fieldnames = [
    'Lead_ID', 'Condition_Type__c', 'Bank_Name__c', 'Contains_clients_name_physical_address__c',
    'Current_Balance__c', 'Current_Debt_Credit_Ratio__c', 'Current_Limit__c', 'Equifax__c',
    'Experian__c', 'Indicates_current_balance__c', 'New_Balance__c', 'Notes__c', 'Official_Bank_Letterhead__c',
    'Pay_Off_Amount__c', 'Required_Balance__c', 'Required_Paydown_Amount__c', 'Transunion__c', 'Vendor__c',
    'Shows_last_four_digits_of_Account_Number__c'
]

C_SUFFIX = '__C'

# Fields
CONDITION_TYPE = 'CONDITION_TYPE'
BANK_NAME = 'BANK_NAME'
CURRENT_BALANCE = 'CURRENT_BALANCE'
CURRENT_DEBT_CREDIT_RATIO = 'CURRENT_DEBT_CREDIT_RATIO'
CURRENT_LIMIT = 'CURRENT_LIMIT'
EQUIFAX = 'EQUIFAX'
EXPERIAN = 'EXPERIAN'
NEW_BALANCE = 'NEW_BALANCE'
PAYDOWN_CONDITIONS_NOTES = 'PAYDOWN_CONDITIONS_NOTES'
PAY_OFF_AMOUNT = 'PAY_OFF_AMOUNT'
REQUIRED_BALANCE = 'REQUIRED_BALANCE'
REQUIRED_PAYDOWN_AMOUNT = 'REQUIRED_PAYDOWN_AMOUNT'
TRANSUNION = 'TRANSUNION'
VENDOR = 'VENDOR'
CONDITIONS_NEEDED = 'CONDITIONS_NEEDED' + C_SUFFIX
CONTAINS_CLIENT_S_NAME = 'CONTAINS_CLIENT_S_NAME'
INDICATES_CURRENT_BALANCE_OF_ACCOUNT = 'INDICATES_CURRENT_BALANCE_OF_ACCOUNT'
MUST_BE_ON_OFFICIAL_BANK_LETTERHEAD = 'MUST_BE_ON_OFFICIAL_BANK_LETTERHEAD'
SHOWS_LAST_FOR_DIGITS_OF_ACCOUNT_NUMBER = 'SHOWS_LAST_FOR_DIGITS_OF_ACCOUNT_NUMBER'

MAX_LOOP = 11

def main(fieldnames_param):
    counter = 1

    lead_ids = {}
    bank_ids = {}
    lead_c_ids = {}

    with open('input/lead_fix.csv', 'rb') as file_lead:
        reader_lead = csv.DictReader(file_lead)

        for row in reader_lead:
            lead_ids[row['ID']] = {}
            lead_ids[row['ID']]['LEAD_ID'] = row['ID']

            for i in range(1, 11):
                lead_ids[row['ID']][CONDITION_TYPE + str(i) + C_SUFFIX] = row[CONDITION_TYPE + str(i) + C_SUFFIX]

            """
                lead_ids[row['ID']][BANK_NAME + str(i) + C_SUFFIX] = ""
                lead_ids[row['ID']][CURRENT_BALANCE + str(i) + C_SUFFIX] = ""
                lead_ids[row['ID']][CURRENT_DEBT_CREDIT_RATIO + str(i) + C_SUFFIX] = ""
                lead_ids[row['ID']][CURRENT_LIMIT + str(i) + C_SUFFIX] = ""
                lead_ids[row['ID']][EQUIFAX + str(i) + C_SUFFIX] = ""
                lead_ids[row['ID']][EXPERIAN + str(i) + C_SUFFIX] = ""

                if i in [7, 8]:
                    lead_ids[row['ID']][NEW_BALANCE + str(i) + C_SUFFIX] = ""
                else:
                    lead_ids[row['ID']][NEW_BALANCE + str(i) + C_SUFFIX] = ""

                lead_ids[row['ID']][PAYDOWN_CONDITIONS_NOTES + str(i) + C_SUFFIX] = ""
                lead_ids[row['ID']][PAY_OFF_AMOUNT + str(i) + C_SUFFIX] = ""
                lead_ids[row['ID']][REQUIRED_BALANCE + str(i) + C_SUFFIX] = ""
                lead_ids[row['ID']][REQUIRED_PAYDOWN_AMOUNT + str(i) + C_SUFFIX] = ""
                lead_ids[row['ID']][TRANSUNION + str(i) + C_SUFFIX] = ""
                lead_ids[row['ID']][VENDOR + str(i) + C_SUFFIX] = ""

            for i in range(1, 9):
                lead_ids[row['ID']][CONTAINS_CLIENT_S_NAME + str(i) + C_SUFFIX] = ""
                lead_ids[row['ID']][INDICATES_CURRENT_BALANCE_OF_ACCOUNT + str(i) + C_SUFFIX] = ""
                lead_ids[row['ID']][MUST_BE_ON_OFFICIAL_BANK_LETTERHEAD + str(i) + C_SUFFIX] = ""
                lead_ids[row['ID']][SHOWS_LAST_FOR_DIGITS_OF_ACCOUNT_NUMBER + str(i) + C_SUFFIX] = ""
            """

    with open('input/bank_fix.csv', 'rb') as file_bank:
        reader_bank = csv.DictReader(file_bank)

        for row in reader_bank:
            lead_ids[row['LEAD_ID']][CONDITIONS_NEEDED] = row[CONDITIONS_NEEDED]

            for i in range(1, 11):
                lead_ids[row['LEAD_ID']][BANK_NAME + str(i) + C_SUFFIX] = row[BANK_NAME + str(i) + C_SUFFIX]
                lead_ids[row['LEAD_ID']][CURRENT_BALANCE + str(i) + C_SUFFIX] = row[CURRENT_BALANCE + str(i) + C_SUFFIX]
                lead_ids[row['LEAD_ID']][CURRENT_DEBT_CREDIT_RATIO + str(i) + C_SUFFIX] = row[CURRENT_DEBT_CREDIT_RATIO + str(i) + C_SUFFIX]
                lead_ids[row['LEAD_ID']][CURRENT_LIMIT + str(i) + C_SUFFIX] = row[CURRENT_LIMIT + str(i) + C_SUFFIX]
                lead_ids[row['LEAD_ID']][EQUIFAX + str(i) + C_SUFFIX] = row[EQUIFAX + str(i) + C_SUFFIX]
                lead_ids[row['LEAD_ID']][EXPERIAN + str(i) + C_SUFFIX] = row[EXPERIAN + str(i) + C_SUFFIX]

                if i in [7, 8]:
                    lead_ids[row['LEAD_ID']][NEW_BALANCE + str(i) + C_SUFFIX] = ""
                else:
                    lead_ids[row['LEAD_ID']][NEW_BALANCE + str(i) + C_SUFFIX] = row[NEW_BALANCE + str(i) + C_SUFFIX]

                lead_ids[row['LEAD_ID']][PAYDOWN_CONDITIONS_NOTES + str(i) + C_SUFFIX] = row[PAYDOWN_CONDITIONS_NOTES + str(i) + C_SUFFIX]
                lead_ids[row['LEAD_ID']][PAY_OFF_AMOUNT + str(i) + C_SUFFIX] = row[PAY_OFF_AMOUNT + str(i) + C_SUFFIX]
                lead_ids[row['LEAD_ID']][REQUIRED_BALANCE + str(i) + C_SUFFIX] = row[REQUIRED_BALANCE + str(i) + C_SUFFIX]
                lead_ids[row['LEAD_ID']][REQUIRED_PAYDOWN_AMOUNT + str(i) + C_SUFFIX] = row[REQUIRED_PAYDOWN_AMOUNT + str(i) + C_SUFFIX]
                lead_ids[row['LEAD_ID']][TRANSUNION + str(i) + C_SUFFIX] = row[TRANSUNION + str(i) + C_SUFFIX]
                lead_ids[row['LEAD_ID']][VENDOR + str(i) + C_SUFFIX] = row[VENDOR + str(i) + C_SUFFIX]

    """
    with open('input/lead_c_fix.csv', 'rb') as file_lead_c:
        reader_lead_c = csv.DictReader(file_lead_c)

        for row in reader_lead_c:
            for i in range(1, 9):
                lead_ids[row['LEAD_ID']][CONTAINS_CLIENT_S_NAME + str(i) + C_SUFFIX] = row[CONTAINS_CLIENT_S_NAME + str(i) + C_SUFFIX]
                lead_ids[row['LEAD_ID']][INDICATES_CURRENT_BALANCE_OF_ACCOUNT + str(i) + C_SUFFIX] = row[INDICATES_CURRENT_BALANCE_OF_ACCOUNT + str(i) + C_SUFFIX]
                lead_ids[row['LEAD_ID']][MUST_BE_ON_OFFICIAL_BANK_LETTERHEAD + str(i) + C_SUFFIX] = row[MUST_BE_ON_OFFICIAL_BANK_LETTERHEAD + str(i) + C_SUFFIX]
                lead_ids[row['LEAD_ID']][SHOWS_LAST_FOR_DIGITS_OF_ACCOUNT_NUMBER + str(i) + C_SUFFIX] = row[SHOWS_LAST_FOR_DIGITS_OF_ACCOUNT_NUMBER + str(i) + C_SUFFIX]
    """

    with open('output/lead_conditions.csv', 'wb') as file_lead_conditions:

        output_lead_writer = csv.DictWriter(file_lead_conditions, fieldnames=fieldnames_param, quoting=csv.QUOTE_ALL)
        output_lead_writer.writeheader()

        for key, value in lead_ids.iteritems():
            if CONDITIONS_NEEDED in value:
                for i in range(1, int(value[CONDITIONS_NEEDED])):
                    output_lead = {
                                    'Lead_ID': value['LEAD_ID'],
                                    'Condition_Type__c': value[CONDITION_TYPE + str(i) + C_SUFFIX],
                                    'Bank_Name__c': value[BANK_NAME + str(i) + C_SUFFIX],
                                    'Current_Balance__c': value[CURRENT_BALANCE + str(i) + C_SUFFIX],
                                    'Current_Debt_Credit_Ratio__c': value[CURRENT_DEBT_CREDIT_RATIO + str(i) + C_SUFFIX],
                                    'Current_Limit__c': value[CURRENT_LIMIT + str(i) + C_SUFFIX],
                                    'Equifax__c' : value[EQUIFAX + str(i) + C_SUFFIX],
                                    'Experian__c' : value[EXPERIAN + str(i) + C_SUFFIX],
                                    'Notes__c': value[PAYDOWN_CONDITIONS_NOTES + str(i) + C_SUFFIX],
                                    'Pay_Off_Amount__c': value[PAY_OFF_AMOUNT + str(i) + C_SUFFIX],
                                    'Required_Balance__c': value[REQUIRED_BALANCE + str(i) + C_SUFFIX],
                                    'Required_Paydown_Amount__c' : value[REQUIRED_PAYDOWN_AMOUNT + str(i) + C_SUFFIX],
                                    'Transunion__c' : value[TRANSUNION + str(i) + C_SUFFIX],
                                    'Vendor__c': value[VENDOR + str(i) + C_SUFFIX]
                                }

                    if i in [7, 8]:
                        output_lead['New_Balance__c'] = ""
                    else:
                        output_lead['New_Balance__c'] = value[NEW_BALANCE + str(i) + C_SUFFIX]

                    output_lead_writer.writerow(output_lead)


if __name__ == "__main__":
    main(fieldnames)
