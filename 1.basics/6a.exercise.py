print("Simple Wallet")
wallet = []

Choose = None
while Choose != '0':
    Choose = input("Choose number:")
    print("1.Deposit \n2.Withdrawal \n3.Saldo ")
    if Choose == "1":
        cash = input("Add Cash:")
        wallet.append(int(cash))
    if Choose == "2":
        withdrawal = input("Withdrawal: ")
        wallet.append(-int(withdrawal))
    if Choose == '3':
        print(wallet)

print(wallet)
