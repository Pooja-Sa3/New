import requests

Base="/"

response= requests.put(Base + "payment/1", {"CreditCardNumber": 9856741236574895, "CardHolder": "Bob Ross", "ExpirationDate": "07/26", "Amount":723})
print(response.JSON())

response= requests.put(Base + "payment/2", {"CreditCardNumber": 898567412, "CardHolder": "Rose", "ExpirationDate": "03/26", "Amount":70})
print(response.JSON())

response= requests.put(Base + "payment/1", {"CreditCardNumber": 3657489578921456, "CardHolder": "Emily", "ExpirationDate": "07/23", "Amount":10})
print(response.JSON())

response= requests.put(Base + "payment/1", {"CreditCardNumber": 4123657245982136, "CardHolder": "Martina", "ExpirationDate": "07/20", "Amount":3})
print(response.JSON())

response= requests.put(Base + "payment/1", {"CreditCardNumber": 7412365748954536, "CardHolder": "Evelyn", "ExpirationDate": "03/27", "Amount":13})
print(response.JSON())

response= requests.put(Base + "payment/1", {"CreditCardNumber": 123657489525987, "CardHolder": "Ray", "ExpirationDate": "02/24", "Amount":455})
print(response.JSON())
