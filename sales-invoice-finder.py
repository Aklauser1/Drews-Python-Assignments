recordsFound = 0

while True:
    searchType = input("Search by invoice id (id) or customer last name (lname)?")
    #loops untill id or lname is true
    while True:
        if searchType == "id" or searchType == "lname":
            print("success")
            break 
        print("ERROR: You must enter either 'id' for invoice id search or 'lname' for customer last name search")
        searchType = input("Search by invoice id (id) or customer last name (lname)?")
        
        # asks for the term input 
    searchTerm = input("Enter your search term here: ")
    salesFileName = "sales_data.csv"
    salesFile = open(salesFileName, "r")
    
    nextLine = salesFile.readlines()
    
    while nextLine != "":
        if searchType == "lname":
            for line in nextLine:
                singleLine = line.strip()
                singleLine = singleLine.split(",")
                for one in singleLine:
                    if searchTerm == singleLine[2]:
                        print(singleLine)
                        recordsFound = recordsFound + 1
                        break
            break
        if searchType == "id":
            for line in nextLine:
                singleLine = line.strip()
                singleLine = singleLine.split(",")
                for one in singleLine:
                    if searchTerm == singleLine[0]:
                        print(singleLine)
                        recordsFound = recordsFound + 1
                        break
            break
    break
    
print("{0} records found.".format(recordsFound))
salesFile.close()