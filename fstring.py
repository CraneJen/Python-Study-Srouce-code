from datetime import datetime
import requests

birthday = datetime(1990, 1, 1)

sentence = f'Jen has a birthday on {birthday: %b %d, %Y}'

print(sentence)
