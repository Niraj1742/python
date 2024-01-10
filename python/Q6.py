# If cost price and selling price of an item is input through the keyboard, write a program to determine whether the seller has made profit or incurred loss or no profit no loss. Also determine how much profit he made or loss he incurred.
cp=int(input("Enter the Cost price"))
sp=int(input("Enter the Selling price"))

if sp>cp:
    profit=sp-cp
    print("Profit is ",profit)
else:
    loss=cp-sp
    print("Loss is ",loss)