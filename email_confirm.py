from itsdangerous import URLSafeTimedSerializer
import time
secretkey = 'SecretKey'
securitysalt = 'SK'


def generate_confirmation_token(email):
    serizlizer = URLSafeTimedSerializer(secretkey)
    return serizlizer.dumps(email, salt=securitysalt)


def comfirm_teken(token, expiration=10):
    serizlizer = URLSafeTimedSerializer(secretkey)
    try:
        email = serizlizer.loads(token, salt=securitysalt, max_age=expiration)
    except Exception as e:
        return False
    return email


email = 'none@gamial.com'
print('The email: {}'.format(email))
token = generate_confirmation_token(email)
print('Token: {}'.format(token))
timesleep = 9
print('Time sleep {}'.format(timesleep))
time.sleep(timesleep)
comfirm_email = comfirm_teken(token)
print('Confirm email: {}'.format(comfirm_email))
print(email == comfirm_email)
