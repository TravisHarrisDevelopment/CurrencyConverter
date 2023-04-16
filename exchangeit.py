import currency

src = input("3-letter code for original currency: ")
dst = input("3-letter code for the new currency: ")
amt = input("Amount of the original currency: ")

exchangeAmount = currency.exchange(src, dst, float(amt))
exchangeAmount = round(exchangeAmount, 3)

print("You can exchange "+amt+" "+src+" for "+str(exchangeAmount)+" "+dst+".")
print("You can exchange 2.5 USD for 2.216 EUR.")