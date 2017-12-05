import plivo
from time import  sleep

class SmsAccount(object):

  """
    On init getting the rest api call using auth id and token
    rest call is saved in the class object.
  """
  def __init__(self):
    auth_id = 'xxxxxxxxxxxxxxxxxxxx'
    auth_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    self.plivo_rest = plivo.RestAPI(auth_id, auth_token)
    sleep(0.1)

  """
    sending the sms by passing the from mobile to mobile and message 
    and return the message uuid
  """
  def sms_send(self, fromMobile, toMobile, message):
    params = {
      'src': fromMobile,
      'dst': toMobile,
      'text': message
    }
    resp = self.plivo_rest.send_message(params)
    sleep(1)
    return resp[1]['message_uuid'][0]

  """
    checking the message status if it is queued, 
    keep on looping until status is change to sent or faild or other status.
    or counting of 100 times
    getting the sms cost.
  """
  def sms_status(self, uuid):
    wait_print = '.'
    params = {
      'message_uuid': uuid
    }
    resp = self.plivo_rest.get_message(params)
    sleep(1)
    print(wait_print)
    while resp[0] != 200 or resp[1]['message_state'] == 'queued':
      if len(wait_print) > 99:
        break;
      params = {
        'message_uuid': uuid
      }
      resp = self.plivo_rest.get_message(params)
      sleep(1)
      wait_print = wait_print+'.'
      print(wait_print)
      if resp[0] != 200 :
        sleep(5)

    return resp[1]['total_amount']

  """
    getting the total amount in the current account.
  """
  def sms_account(self):
    resp = self.plivo_rest.get_account()
    sleep(1)
    return resp[1]['cash_credits']
