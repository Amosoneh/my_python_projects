customers = [
    {
        'name': 'Amos Oneh',
        'acct_num': '001',
        'age': 23,
        'balance': 10_000_000,
        'type': 'savings',
        'gender': 'male',
        'is_married': False
    },
    {
        'name': 'Amos Monday',
        'acct_num': '002',
        'age': 33,
        'balance': 100_000_000,
        'type': 'savings',
        'gender': 'male',
        'is_married': False
    },
    {
        'name': 'Monday Khaled',
        'acct_num': '003',
        'age': 32,
        'balance': 1_000_000,
        'type': 'current',
        'gender': 'male',
        'is_married': True
    },
    {
        'name': 'Abigail Oneh',
        'acct_num': '004',
        'age': 23,
        'balance': 2_000_000,
        'type': 'savings',
        'gender': 'female',
        'is_married': True
    },
    {
        'name': 'Amos Diego',
        'acct_num': '006',
        'age': 31,
        'balance': 10_000_000,
        'type': 'savings',
        'gender': 'male',
        'is_married': False
    },
]
names = [customer['name'] for customer in customers]
avg_age = sum(customer['age'] for customer in customers) / len(customers)
savings_acct_holders = [customer for customer in customers if customer['type'] == 'savings']
savings_acct_holders_balance = [dict(name=customer['name'], balance=customer['balance']) for customer in customers if
                                customer['type'] == 'savings']


print(names)
print(avg_age)
print(savings_acct_holders)
print(savings_acct_holders_balance)


def get_balance(dict_: dict) -> int:
    return dict_['balance']


customers.sort(key=get_balance, reverse=True)
print(customers)

print(sorted(customers, key=get_balance, reverse=True))
print(max(customers, key=get_balance))
