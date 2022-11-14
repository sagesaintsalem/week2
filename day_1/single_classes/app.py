from modules.bank_account import *

bank_account1 = BankAccount("John", 500, "business")
bank_account2 = BankAccount("Steve", 5, "personal")


bank_account1.holder_name = "Babs"
#print(bank_account2.holder_name)
bank_account1.pay_in(20)
print(bank_account1)
bank_account1.pay_monthly_fee()
print(bank_account1)
bank_account2.pay_in(435)
bank_account2.pay_monthly_fee()
print(bank_account2)

# account = {
#     "holder_name":"John",
#     "balance":500,
#     "type":"business"
# }

# print(get_account_name(account))