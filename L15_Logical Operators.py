# Logical and: Both conditions should be true
# Logical or: Atleast one conditions should be true
# Logical not: Converts a true value to false & viceversa

# If an applicant has high income & good gredit & no criminal record
high_income = True
good_credit = True
criminal_record = False

if high_income and good_credit and not criminal_record:       # logical and & or operators
    print("Eligible for Loan")
else:
    print("Not Eligible for Loan")

# If an applicant has high income or good gredit & no criminal record
high_income = True
good_credit = False
criminal_record = False

if high_income or good_credit and not criminal_record:        # logical or & not operators
    print("Eligible for Loan")
else:
    print("Not Eligible for Loan")