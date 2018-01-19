import csv

fields_output_account = [
    'ID',
    'Name',
    'Source_Lead__c',
    'Google_Ad_Keyword__c',
    'Personal_Credit_Score__c',
    'Purpose_of_Funds__c',
    'Desired_Loan_Amount__c',
    'industry',
    'Business_Name__c',
    'Client_code__c',
    'Monthly_Revenue__c',
    # 'Annual_Revenue__c',
    'Monthly_Profit__c',
    'X12_Month_Revenue_Forecast__c',
    'Minimum_Funds_Required__c',
    'Ideal_Funding_Amount__c',
    'Looking_for_Funds_time__c',
    'When_are_Funds_Needed__c',
    'How_Critical_Are_Funds__c',
    'Purpose_of_Funds__c',
    'How_Long_Funds_needed__c',
    'Authorized_Person_First_Name__c',
    'Authorized_Person_Last_Name__c',
    'Authorized_Person_Email_Address__c',
    'Authorized_Person_Phone_Number__c',
    'Debt_Type_Lender_1__c',
    'Debt_Type_Lender_2__c',
    # 'Debt_Type_Lender_3__c',
    # 'Debt_Type_Lender_4__c',
    'Lender_1__c',
    'Lender_2__c',
    'Lender_3__c',
    'Lender_4__c',
    'Limit_1__c',
    'Limit_2__c',
    'Limit_3__c',
    'Limit_4__c',
    'Lender_1_Balance__c',
    'Lender_2_Balance__c',
    'Lender_3_Balance__c',
    'Lender_4_Balance__c',
    'Phone'
]

fields_output_contact = [
    'ID',
    'FirstName',
    'LastName',
    'Phone',
    'MobilePhone',
    'email',
    'Annual_Household_Income__c',
    'Own_min_25__c',
    'X401k_Account__c',
    'X401k_Amount__c',
    'Permission_to_Pre_Qual_Credit__c',
    'DOB__c',
    'Birthdate',
    'experian_score__c',
    'Source_Lead__c',
    'Business_Name__c',
    'Client_Code__c',
    # 'LASERCA__Co_Applicant_DOB__c',
    # 'LASERCA__Co_Applicant_Last_Name__c',
    # 'LASERCA__Co_Applicant_Social_Security_Number__c',
    'DOB__c',
    'HasOptedOutOfFax',
    'Google_Ad_Keyword__c',
    'LASERCA__Home_Address__c',
    'LASERCA__Home_City__c',
    'LASERCA__Home_Country__c',
    'Phone',
    'LASERCA__Home_State__c',
    'LASERCA__Home_Zip__c',
    'Industry__c',
    'LASERCA__Middle_Initial__c',
    'Military_Affiliation__c',
    'MobilePhone',
    'Mobile_Phone__c',
    'Own_min_25__c',
    'Permission_to_Pre_Qual_Credit__c',
    'Personal_Credit_Score__c',
    # 'LASERCA__Pull_Credit_Report__c',
    'LASERCA__Social_Security_Number__c'
]


def main():
    counter = 0

    with open('output/accounts.csv', 'wb') as file_output_accounts:
        with open('output/contacts.csv', 'wb') as file_output_contacts:

            with open('input/opportunity_output.csv', 'rb') as file_input:
                reader_input = csv.DictReader(file_input)
                fieldnames = fields_output_account

                writer_output_accounts = csv.DictWriter(file_output_accounts, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
                writer_output_accounts.writeheader()

                fieldnames = fields_output_contact
                writer_output_contacts = csv.DictWriter(file_output_contacts, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
                writer_output_contacts.writeheader()

                for row in reader_input:
                    new_row_account = dict()
                    new_row_account['ID'] = row['ID']
                    new_row_account['Name'] = row['Company'.upper()]
                    new_row_account['Source_Lead__c'] = row['Id'.upper()]
                    new_row_account['Google_Ad_Keyword__c'] = row['Google_Ad_Keyword__c'.upper()]
                    new_row_account['Personal_Credit_Score__c'] = row['Personal_Credit_Score__c'.upper()]
                    new_row_account['Purpose_of_Funds__c'] = row['Purpose_of_Funds__c'.upper()]
                    new_row_account['Desired_Loan_Amount__c'] = row['Desired_Loan_Amount__c'.upper()]
                    new_row_account['industry'] = row['industry__c'.upper()]
                    new_row_account['Business_Name__c'] = row['business_name__c'.upper()]
                    new_row_account['Client_code__c'] = row['client_code__c'.upper()]
                    new_row_account['Monthly_Revenue__c'] = row['monthly_revenue__c'.upper()]
                    # new_row_account['Annual_Revenue__c'] = row['Annual_Revenue__c'.upper()]
                    new_row_account['Monthly_Profit__c'] = row['Monthly_Profit__c'.upper()]
                    new_row_account['X12_Month_Revenue_Forecast__c'] = row['X12_Month_Revenue_Forecast__c'.upper()]
                    new_row_account['Minimum_Funds_Required__c'] = row['Minimum_Funding_Needed_Apx_A__c'.upper()]
                    new_row_account['Ideal_Funding_Amount__c'] = row['Ideal_Funding_Amount__c'.upper()]
                    new_row_account['Looking_for_Funds_time__c'] = row['Looking_for_Funds_time__c'.upper()]
                    new_row_account['When_are_Funds_Needed__c'] = row['When_are_Funds_Needed__c'.upper()]
                    new_row_account['How_Critical_Are_Funds__c'] = row['How_Critical_Are_Funds__c'.upper()]
                    new_row_account['Purpose_of_Funds__c'] = row['Purpose_of_Funds__c'.upper()]
                    new_row_account['How_Long_Funds_needed__c'] = row['How_Long_Funds_needed__c'.upper()]
                    new_row_account['Authorized_Person_First_Name__c'] = row['AUTHORIZED_PERSON__C']
                    new_row_account['Authorized_Person_Last_Name__c'] = row['Authorized_Person_Last_Name__c'.upper()]
                    new_row_account['Authorized_Person_Email_Address__c'] = row['Authorized_Person_Email_Address__c'.upper()]
                    new_row_account['Authorized_Person_Phone_Number__c'] = row['Authorized_Person_Phone_Number__c'.upper()]
                    new_row_account['Debt_Type_Lender_1__c'] = row['Debt_Type_Lender_1__c'.upper()]
                    new_row_account['Debt_Type_Lender_2__c'] = row['Debt_Type_Lender_2__c'.upper()]
                    # new_row_account['Debt_Type_Lender_3__c'] = row['Debt_Type_Lender_3__c'.upper()]
                    # new_row_account['Debt_Type_Lender_4__c'] = row['Debt_Type_Lender_4__c'.upper()]
                    new_row_account['Lender_1__c'] = row['lender_1__c'.upper()]
                    new_row_account['Lender_2__c'] = row['lender_2__c'.upper()]
                    new_row_account['Lender_3__c'] = row['lender_3__c'.upper()]
                    new_row_account['Lender_4__c'] = row['lender_4__c'.upper()]
                    new_row_account['Limit_1__c'] = row['LENDER_1_LIMIT__C'.upper()]
                    new_row_account['Limit_2__c'] = row['LENDER_2_LIMIT__C'.upper()]
                    new_row_account['Limit_3__c'] = row['LENDER_3_LIMIT__C'.upper()]
                    new_row_account['Limit_4__c'] = row['LENDER_4_LIMIT__C'.upper()]
                    new_row_account['Lender_1_Balance__c'] = row['Lender_1_Balance__c'.upper()]
                    new_row_account['Lender_2_Balance__c'] = row['Lender_2_Balance__c'.upper()]
                    new_row_account['Lender_3_Balance__c'] = row['Lender_3_Balance__c'.upper()]
                    new_row_account['Lender_4_Balance__c'] = row['Lender_4_Balance__c'.upper()]
                    new_row_account['Phone'] = row['Phone'.upper()]

                    writer_output_accounts.writerow(new_row_account)


                    new_row_contact = dict()
                    new_row_contact['ID'] = row['ID']
                    new_row_contact['FirstName'] = row['FirstName'.upper()]
                    new_row_contact['LastName'] = row['LastName'.upper()]
                    new_row_contact['Phone'] = row['phone'.upper()]
                    new_row_contact['MobilePhone'] = row['mobilephone'.upper()]
                    new_row_contact['email'] = row['email'.upper()]
                    new_row_contact['Annual_Household_Income__c'] = row['Annual_Household_Income__c'.upper()]
                    new_row_contact['Own_min_25__c'] = row['Own_min_25__c'.upper()]
                    new_row_contact['X401k_Account__c'] = row['X401k_Account__c'.upper()]
                    new_row_contact['X401k_Amount__c'] = row['X401k_Amount__c'.upper()]
                    new_row_contact['Permission_to_Pre_Qual_Credit__c'] = row['Permission_to_Pre_Qual_Credit__c'.upper()]
                    new_row_contact['DOB__c'] = row['dob__c'.upper()]
                    new_row_contact['Birthdate'] = row['LASERCA__Birthdate__c'.upper()]
                    new_row_contact['experian_score__c'] = row['experian_score__C'.upper()]
                    new_row_contact['Source_Lead__c'] = row['Id'.upper()]
                    new_row_contact['Business_Name__c'] = row['Business_Name__c'.upper()]
                    new_row_contact['Client_Code__c'] = row['Client_Code__c'.upper()]
                    # new_row_contact['LASERCA__Co_Applicant_DOB__c'] = row['LASERCA__Co_Applicant_DOB__c'.upper()]
                    # new_row_contact['LASERCA__Co_Applicant_Last_Name__c'] = row['LASERCA__Co_Applicant_Last_Name__c'.upper()]
                    # new_row_contact['LASERCA__Co_Applicant_Social_Security_Number__c'] = row['LASERCA__Co_Applicant_Social_Security_Number__c'.upper()]
                    new_row_contact['DOB__c'] = row['DOB__c'.upper()]
                    new_row_contact['HasOptedOutOfFax'] = row['HasOptedOutOfFax'.upper()]
                    new_row_contact['Google_Ad_Keyword__c'] = row['Google_Ad_Keyword__c'.upper()]
                    new_row_contact['LASERCA__Home_Address__c'] = row['LASERCA__Home_Address__c'.upper()]
                    new_row_contact['LASERCA__Home_City__c'] = row['LASERCA__Home_City__c'.upper()]
                    new_row_contact['LASERCA__Home_Country__c'] = row['LASERCA__Home_Country__c'.upper()]
                    new_row_contact['Phone'] = row['Phone'.upper()]
                    new_row_contact['LASERCA__Home_State__c'] = row['LASERCA__Home_State__c'.upper()]
                    new_row_contact['LASERCA__Home_Zip__c'] = row['LASERCA__Home_Zip__c'.upper()]
                    new_row_contact['Industry__c'] = row['Industry__c'.upper()]
                    new_row_contact['LASERCA__Middle_Initial__c'] = row['LASERCA__Middle_Initial__c'.upper()]
                    new_row_contact['Military_Affiliation__c'] = row['Military_Affiliation__c'.upper()]
                    new_row_contact['MobilePhone'] = row['MobilePhone'.upper()]
                    new_row_contact['Mobile_Phone__c'] = row['Mobile__c'.upper()]
                    new_row_contact['Own_min_25__c'] = row['Own_min_25__c'.upper()]
                    new_row_contact['Permission_to_Pre_Qual_Credit__c'] = row['Permission_to_Pre_Qual_Credit__c'.upper()]
                    new_row_contact['Personal_Credit_Score__c'] = row['Personal_Credit_Score__c'.upper()]
                    # new_row_contact['LASERCA__Pull_Credit_Report__c'] = row['LASERCA__Pull_Credit_Report__c'.upper()]
                    new_row_contact['LASERCA__Social_Security_Number__c'] = row['LASERCA__Social_Security_Number__c'.upper()]

                    writer_output_contacts.writerow(new_row_contact)

                    counter += 1
                    print counter

            with open('input/after_opportunity_output.csv', 'rb') as file_input:
                reader_input = csv.DictReader(file_input)

                for row in reader_input:
                    new_row_account = dict()
                    new_row_account['ID'] = row['ID']
                    new_row_account['Name'] = row['Company'.upper()]
                    new_row_account['Source_Lead__c'] = row['Id'.upper()]
                    new_row_account['Google_Ad_Keyword__c'] = row['Google_Ad_Keyword__c'.upper()]
                    new_row_account['Personal_Credit_Score__c'] = row['Personal_Credit_Score__c'.upper()]
                    new_row_account['Purpose_of_Funds__c'] = row['Purpose_of_Funds__c'.upper()]
                    new_row_account['Desired_Loan_Amount__c'] = row['Desired_Loan_Amount__c'.upper()]
                    new_row_account['industry'] = row['industry__c'.upper()]
                    new_row_account['Business_Name__c'] = row['business_name__c'.upper()]
                    new_row_account['Client_code__c'] = row['client_code__c'.upper()]
                    new_row_account['Monthly_Revenue__c'] = row['monthly_revenue__c'.upper()]
                    # new_row_account['Annual_Revenue__c'] = row['Annual_Revenue__c'.upper()]
                    new_row_account['Monthly_Profit__c'] = row['Monthly_Profit__c'.upper()]
                    new_row_account['X12_Month_Revenue_Forecast__c'] = row['X12_Month_Revenue_Forecast__c'.upper()]
                    new_row_account['Minimum_Funds_Required__c'] = row['Minimum_Funding_Needed_Apx_A__c'.upper()]
                    new_row_account['Ideal_Funding_Amount__c'] = row['Ideal_Funding_Amount__c'.upper()]
                    new_row_account['Looking_for_Funds_time__c'] = row['Looking_for_Funds_time__c'.upper()]
                    new_row_account['When_are_Funds_Needed__c'] = row['When_are_Funds_Needed__c'.upper()]
                    new_row_account['How_Critical_Are_Funds__c'] = row['How_Critical_Are_Funds__c'.upper()]
                    new_row_account['Purpose_of_Funds__c'] = row['Purpose_of_Funds__c'.upper()]
                    new_row_account['How_Long_Funds_needed__c'] = row['How_Long_Funds_needed__c'.upper()]
                    new_row_account['Authorized_Person_First_Name__c'] = row['AUTHORIZED_PERSON__C']
                    new_row_account['Authorized_Person_Last_Name__c'] = row['Authorized_Person_Last_Name__c'.upper()]
                    new_row_account['Authorized_Person_Email_Address__c'] = row[
                        'Authorized_Person_Email_Address__c'.upper()]
                    new_row_account['Authorized_Person_Phone_Number__c'] = row[
                        'Authorized_Person_Phone_Number__c'.upper()]
                    new_row_account['Debt_Type_Lender_1__c'] = row['Debt_Type_Lender_1__c'.upper()]
                    new_row_account['Debt_Type_Lender_2__c'] = row['Debt_Type_Lender_2__c'.upper()]
                    # new_row_account['Debt_Type_Lender_3__c'] = row['Debt_Type_Lender_3__c'.upper()]
                    # new_row_account['Debt_Type_Lender_4__c'] = row['Debt_Type_Lender_4__c'.upper()]
                    new_row_account['Lender_1__c'] = row['lender_1__c'.upper()]
                    new_row_account['Lender_2__c'] = row['lender_2__c'.upper()]
                    new_row_account['Lender_3__c'] = row['lender_3__c'.upper()]
                    new_row_account['Lender_4__c'] = row['lender_4__c'.upper()]
                    new_row_account['Limit_1__c'] = row['LENDER_1_LIMIT__C'.upper()]
                    new_row_account['Limit_2__c'] = row['LENDER_2_LIMIT__C'.upper()]
                    new_row_account['Limit_3__c'] = row['LENDER_3_LIMIT__C'.upper()]
                    new_row_account['Limit_4__c'] = row['LENDER_4_LIMIT__C'.upper()]
                    new_row_account['Lender_1_Balance__c'] = row['Lender_1_Balance__c'.upper()]
                    new_row_account['Lender_2_Balance__c'] = row['Lender_2_Balance__c'.upper()]
                    new_row_account['Lender_3_Balance__c'] = row['Lender_3_Balance__c'.upper()]
                    new_row_account['Lender_4_Balance__c'] = row['Lender_4_Balance__c'.upper()]
                    new_row_account['Phone'] = row['Phone'.upper()]

                    writer_output_accounts.writerow(new_row_account)

                    new_row_contact = dict()
                    new_row_contact['ID'] = row['ID']
                    new_row_contact['FirstName'] = row['FirstName'.upper()]
                    new_row_contact['LastName'] = row['LastName'.upper()]
                    new_row_contact['Phone'] = row['phone'.upper()]
                    new_row_contact['MobilePhone'] = row['mobilephone'.upper()]
                    new_row_contact['email'] = row['email'.upper()]
                    new_row_contact['Annual_Household_Income__c'] = row['Annual_Household_Income__c'.upper()]
                    new_row_contact['Own_min_25__c'] = row['Own_min_25__c'.upper()]
                    new_row_contact['X401k_Account__c'] = row['X401k_Account__c'.upper()]
                    new_row_contact['X401k_Amount__c'] = row['X401k_Amount__c'.upper()]
                    new_row_contact['Permission_to_Pre_Qual_Credit__c'] = row['Permission_to_Pre_Qual_Credit__c'.upper()]
                    new_row_contact['DOB__c'] = row['dob__c'.upper()]
                    new_row_contact['Birthdate'] = row['LASERCA__Birthdate__c'.upper()]
                    new_row_contact['experian_score__c'] = row['experian_score__C'.upper()]
                    new_row_contact['Source_Lead__c'] = row['Id'.upper()]
                    new_row_contact['Business_Name__c'] = row['Business_Name__c'.upper()]
                    new_row_contact['Client_Code__c'] = row['Client_Code__c'.upper()]
                    # new_row_contact['LASERCA__Co_Applicant_DOB__c'] = row['LASERCA__Co_Applicant_DOB__c'.upper()]
                    # new_row_contact['LASERCA__Co_Applicant_Last_Name__c'] = row['LASERCA__Co_Applicant_Last_Name__c'.upper()]
                    # new_row_contact['LASERCA__Co_Applicant_Social_Security_Number__c'] = row['LASERCA__Co_Applicant_Social_Security_Number__c'.upper()]
                    new_row_contact['DOB__c'] = row['DOB__c'.upper()]
                    new_row_contact['HasOptedOutOfFax'] = row['HasOptedOutOfFax'.upper()]
                    new_row_contact['Google_Ad_Keyword__c'] = row['Google_Ad_Keyword__c'.upper()]
                    new_row_contact['LASERCA__Home_Address__c'] = row['LASERCA__Home_Address__c'.upper()]
                    new_row_contact['LASERCA__Home_City__c'] = row['LASERCA__Home_City__c'.upper()]
                    new_row_contact['LASERCA__Home_Country__c'] = row['LASERCA__Home_Country__c'.upper()]
                    new_row_contact['Phone'] = row['Phone'.upper()]
                    new_row_contact['LASERCA__Home_State__c'] = row['LASERCA__Home_State__c'.upper()]
                    new_row_contact['LASERCA__Home_Zip__c'] = row['LASERCA__Home_Zip__c'.upper()]
                    new_row_contact['Industry__c'] = row['Industry__c'.upper()]
                    new_row_contact['LASERCA__Middle_Initial__c'] = row['LASERCA__Middle_Initial__c'.upper()]
                    new_row_contact['Military_Affiliation__c'] = row['Military_Affiliation__c'.upper()]
                    new_row_contact['MobilePhone'] = row['MobilePhone'.upper()]
                    new_row_contact['Mobile_Phone__c'] = row['Mobile__c'.upper()]
                    new_row_contact['Own_min_25__c'] = row['Own_min_25__c'.upper()]
                    new_row_contact['Permission_to_Pre_Qual_Credit__c'] = row['Permission_to_Pre_Qual_Credit__c'.upper()]
                    new_row_contact['Personal_Credit_Score__c'] = row['Personal_Credit_Score__c'.upper()]
                    # new_row_contact['LASERCA__Pull_Credit_Report__c'] = row['LASERCA__Pull_Credit_Report__c'.upper()]
                    new_row_contact['LASERCA__Social_Security_Number__c'] = row[
                        'LASERCA__Social_Security_Number__c'.upper()]

                    writer_output_contacts.writerow(new_row_contact)

                    counter += 1
                    print counter

if __name__ == "__main__":
    main()