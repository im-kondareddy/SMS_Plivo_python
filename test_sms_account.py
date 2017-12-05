from com.sms_account import SmsAccount

sms_test1 = SmsAccount()
print('Your Amount: ', sms_test1.sms_account())
message_uuid = sms_test1.sms_send('+13238318440', '+13252210570', 'Hello World 2')
sms_cost = sms_test1.sms_status(message_uuid)
print("SMS Cost:", sms_cost)
print('Total Amount: ', sms_test1.sms_account())
print('--------------------------------------------')
