import phonenumbers
from phonenumbers import carrier, geocoder, timezone

mobileNumber=input('Enter Mobile Number with Country code: ')
mobileNumber=phonenumbers.parse(mobileNumber)

#Get time zone
print(timezone.time_zones_for_number(mobileNumber))

#Get Phone's Carrier
print(carrier.name_for_number(mobileNumber, 'en'))

#Get Region Info
print(geocoder.description_for_number(mobileNumber, 'en'))

#Validate a phone number
print('Valid Mobile Number: ', phonenumbers.is_valid_number(mobileNumber))

#Checking possibility of a number
print('Checking possibility of Number: ', phonenumbers.is_possible_number(mobileNumber))
