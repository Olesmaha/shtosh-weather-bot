from datetime import datetime

# tme = datetime.fromtimestamp(1669823906, datetime.astimezone(tz=-18000))
# print(tme.tzinfo)
# print(tme)

print(datetime.fromtimestamp(1669827253))
print(datetime.utcfromtimestamp(1669827253))
print(datetime.utcfromtimestamp(1669827253 +14400))
print(datetime.utcfromtimestamp(1669781106+14400))
print(datetime.utcfromtimestamp(1669814918+14400))

print(datetime.utcfromtimestamp(1669823906-18000))
print(datetime.utcfromtimestamp(1669809456 + -18000))
print(datetime.utcfromtimestamp(1669844897 + -18000).strftime('%c'))
print(datetime.utcfromtimestamp(1669844897 + -18000))

print(str(273.15))

print(round( 275.22999999999996, 2))