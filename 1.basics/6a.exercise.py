def walletw():
    print("Simple Wallet")
    wallet = []
    Choose = None
    while Choose != '0':
        print("1.Deposit \n2.Withdrawal \n3.Saldo ")
        Choose = input("Choose number:")
        if Choose == "1":
            cash = input("Add Cash:")
            wallet.append(int(cash))
        if Choose == "2":
            withdrawal = input("Withdrawal: ")
            wallet.append(-int(withdrawal))
        if Choose == '3':
            print(wallet)


walletw()
