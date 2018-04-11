from pycoin import key as pykey
from blockchain import blockexplorer as be
from blockchain import exceptions as ex
import requests

keys = dict()
faultykeys = set()

with open(r'results.csv', encoding="utf8") as f:
    for line in f.read().split('\n'):
        if line:
            try:
                repo, file, pkey = line.split(",")
                p = pykey.Key.from_text(pkey)
                pub = p.address()
                keys[pub] = {'priv': pkey}
            except:
                faultykeys.add(pkey)
                pass

print('Keys: {}'.format(len(keys)))
print('Faulty Keys: {}'.format(len(faultykeys)))

for pub in keys:
    try:
        addbal = be.get_balance(pub)
        keys[pub]['balance'] = addbal[pub].final_balance
        keys[pub]['ntx'] = addbal[pub].n_tx
        keys[pub]['total_received'] = addbal[pub].total_received
        print("Address: %s has %s satoshis, with %s transactions. total received %s" % (pub, addbal[pub].final_balance, addbal[pub].n_tx, addbal[pub].total_received))
        if addbal[pub].final_balance > 0:
            print('\nWe Got Money!!!\n')
    except ex.APIException as e:
        print('catched a API error')
        print(e)
        #keys.pop(pub, None)
        pass