def currency_converter(amount):
    with open('currency.txt') as f:
        lines=f.readlines()
    currency_dict={}
    print('here is the available list :\n')
    for line in lines:
        data=line.split('\t')
        currency_dict[data[0]]=data[1]
    for key in currency_dict:
        print(key)
    select_country=input('\nselect the county :\n')
    result=amount * float(currency_dict[select_country])
    return (f'The {amount} Indian Rupees In {select_country} is {result}')
if __name__ == "__main__":
    amount=int(input('enter the amount :\n'))
    print(currency_converter(amount))