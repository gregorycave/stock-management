
import StockItem
import pickle
FILENAME = 'stocklevel.dat'

def main():
  valid=False
  while not valid:
    print("\n***MENU***")
    print("1. Print current stock level.")
    print("2. Add stock to the current stock level.")
    print("3. Remove stock from the current stock level.")
    print("9. Quit")
    print("***Menu***")
    choice=input("\nPlease enter your choice: ")
    if choice=='1':
      printStock(FILENAME)
    elif choice=='2':
      addStock(FILENAME)
    elif choice=='3':
      removeStock(FILENAME)
    elif choice=='9':
      end=input("Are you sure? (y/n)")
      if end.lower() == 'y':
        break
        valid=True
      else:
        print()
    else:
      print("Incorrect input, please try again.")
      print()

def printStock(FILENAME):
  end_of_file = False
  stock_file=open(FILENAME, 'rb')
  while not end_of_file:
    try:
      stock = pickle.load(stock_file)
      print("\nStockID: {0}".format(stock.get_stockID()))
      print("Category: {0}".format(stock.get_category()))
      print("Description: {0}".format(stock.get_description()))
      print("Level of stock: {0}".format(stock.get_qtyInStock()))
    except EOFError:
      end_of_file = True
      print("\nThere is no more stock to print!")
      stock_file.close()

def addStock(FILENAME):
    again= 'y'
    stock_file = open(FILENAME, 'wb')
    while again.lower() == 'y':
      stockID=input("Enter StockID: ")
      category=input("Enter Category: ")
      description=input("Enter Description: ")
      qtyInStock=input("Enter level of stock: ")
      stock=StockItem.StockItem(stockID,category,description,qtyInStock)
      pickle.dump(stock, stock_file)
      again = input('Enter more data? (y/n): ')
    print('The data was written to', FILENAME)
    stock_file.close()
    

def removeStock(FILENAME):
  stock_file = open(FILENAME, 'wb')
  stock=StockItem.StockItem('','','','')
  print('The file {0} has been deleted.'.format(FILENAME))
  stock_file.close()

def other():    
  stockID=int(input("Enter StockID: "))
  category=input("Enter Category: ")
  description=input("Enter description: ")
  qtyInStock=int(input("Enter level of stock: "))
  stock=StockItem.StockItem(stockID,category,description,qtyInStock)
  print("StockID: {0}".format(stock.get_stockID()))
  print("Category: {0}".format(stock.get_category()))
  print("Description: {0}".format(stock.get_description()))
  print("Level of stock: {0}".format(stock.get_qtyInStock()))

if __name__ == "__main__":
  main()
