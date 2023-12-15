transactions = open("acounts.txt","r")
transactionsList = []
for line in transactions:
    transactionsList.append(line)
transactions.close()
transcationsList = [transaction.strip() for transaction in transactionsList]

transactionsListv2 = []
for transaction in transactionsList:
    temp = transaction.split()
    transactionsListv2.append(temp)

dictionary = {'a': 500,
              'b': 500,
              'c': 500}

for list in transactionsListv2:
    if list[0] in dictionary:
        if list[1] == '<':
            


