class Category:
    def __init__(self,category=""):
        self.category= category
        self.ledger=[]
        self.fund =0
        self.total_spent = 0
    def __str__(self):
        stars=""
        for i in range(round((30-len(self.category))/2)):
            stars= stars + "*"
        check = stars + self.category + stars+"\n"
        for item in self.ledger:
            if len(item["description"])<23:
                number_of_space = 30 - len(item["description"]) - len(str(item["amount"]))
                spaces=""
                for j in range(number_of_space):
                    spaces= spaces+" "
                check = check + item["description"]+ spaces + str(item["amount"])+"\n"
            else:
                descrpt = item["description"][0:23]
                number_of_space = 30 - 23 - len(str(item["amount"]))
                spaces=""
                for j in range(number_of_space):
                    spaces= spaces+" "
                check = check + descrpt+ spaces + str(item["amount"])+"\n"
        check = check + "Total: "+str(self.fund)

        
        return check

    
    def deposit(self, amount, description=""):
        self.ledger.append({"amount":amount, "description": description})
        self.fund = self.fund + amount
    
    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount":-amount, "description":description})
            self.fund = self.fund - amount
            self.total_spent = self.total_spent + amount
            return True
            
        else:
            return False
            
    def get_balance(self):
        return self.fund

    def check_funds(self, amount):
        if amount> self.get_balance():
            return False
        else:
            return True  
    def transfer(self, amnt, cat):
        if self.withdraw(amnt, "Tranfser to "+cat.category):
            cat.deposit(amnt, "Transfer from "+ self.category)
            return True
        else:
            return False




def create_spend_chart(categories):
    list_of_dict=[]
    total_with=0
    for category in categories:
        total_with= total_with+ category.total_spent
    for category in categories:
        dc={}
        dc["category"]= category.category
        dc["percentage"]=round(category.total_spent/total_with*10)*10
        list_of_dict.append(dc)
    
    percentage_bar = ["100|"," 90|"," 80|"," 70|"," 60|"," 50|"," 40|"," 30|"," 20|"," 10|","  0|"]
    categ_list_of_lists=[]
    for cat in list_of_dict:
        cat_list=[]
        for i in range(10-int(cat['percentage']/10)):
            cat_list.append(" ")
        for j in range(int(cat['percentage']/10)+1):
            cat_list.append("0")
        categ_list_of_lists.append(cat_list)
        
    
    bill=""
    for i in range(11):
        bill = bill+percentage_bar[i] +" "
        for j in range(len(categ_list_of_lists)):
            bill = bill+categ_list_of_lists[j][i]+"  "
        bill = bill+"\n"
    
    dashes="    -"
    for i in range(len(categ_list_of_lists)):
        dashes= dashes+"---"
    bill = bill + dashes+"\n     "
    ranges=[]
    for category in categories:
        ranges.append(len(category.category))
    rng_max=max(ranges)
    big_lst=[]
    for i in range(rng_max):
        lst=[]
        for j in range(len(list_of_dict)):
            try:
                lst.append(list_of_dict[j]["category"][i])
            except:
                lst.append(" ")

        big_lst.append(lst)
    
    for i in range(len(big_lst)):
        for j in range(len(big_lst[0])):
            bill= bill + big_lst[i][j]+"  "
        bill = bill+"\n     "

    return bill
    


    

    

