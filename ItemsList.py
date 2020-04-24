import openpyxl
import pickle

class ItemsList:
    
    def __init__ (self):
        self.items = {}

   
    def printkeys (self):
        i = 1
        for key in self.items:
            print  (str(i) + '. ' + str(key) + '    Prev prices: ', end = '$')
            print (*self.items[key], sep = ', $')
            i = i + 1
        print (str(i) + '. (new)')

    
    
    def addItem(self, name, price):
        if name in self.items.keys():
            self.items[name].append(price)
        else:
            self.items[name]=   [price]

    def load(self):
        try:
            with open("mySavedDict.txt", "rb") as myFile:
                self.items = pickle.load(myFile)
        except (OSError, EOFError) as e:
            print('File not found, starting new file...')

    def save(self):
        with open("mySavedDict.txt.", "wb") as myFile:
            pickle.dump(self.items, myFile)
    
    def saveToXl(self):
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        row = 1
        for key, values in self.items.items():
            sheet.cell(row = row, column = 1, value = key)
            column = 2
            for element in values:
                sheet.cell (row = row, column = column, value = element)
                column += 1
            row += 1
        workbook.save(filename = "prices.xlsx")

        
        
        
