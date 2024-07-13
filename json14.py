# import requests module to send request to URL
import requests
#import re module to use regular expression
import re

#creating a class
class Brewery:
   
   #creating init constructor
   def __init__(self,state,url):
      self.url=url
      self.state=state
      #list to store name of brewery list
      self.brewery_name=[]
      #list to store types of breweries
      self.brewery_type=[]
      #List to store website name of breweries
      self.website_list=[]

   #function to check url is accesible or not
   def  api_status_code(self):
       response=requests.get(self.url)
       return response.status_code  
   
   # function to fetch api data
   def fetch_api_data(self):
       return requests.get(self.url).json()
    
 # function to get list of breweries state wise
   def list_brewery_state(self):
        if self.api_status_code()==200:
          brewery_data=self.fetch_api_data()
    
          for data in brewery_data:
              self.brewery_name.append(data["name"])
          print("List of Breweries in  "+self.state+" ",len(self.brewery_name))
        
          return self.brewery_name
        else:
          return "error"
       
 # function to get count of different brewery types
   def brewery_types(self):
      if self.api_status_code()==200:
          brewery_data=self.fetch_api_data()
          for data in brewery_data:
              self.brewery_type.append(data["brewery_type"])
              uniqe_brewerytype = list(set(self.brewery_type))
          return "count of Breweries_types in  "+self.state+" ",len(uniqe_brewerytype)
      else:
          return"error"
   
   
    #function to get brewery list and count of breweries who have websites names
   def  brewery_website(self):
        if self.api_status_code()==200:
           brewery_data=self.fetch_api_data()
           for data in brewery_data:
                 if re.findall(r"\Ahttp",str(data["website_url"])):
                       self.website_list.append(data["website_url"])
           print("count of breweries who have websites of  "+self.state+" ",len(self.website_list))
           return self.website_list
        else:
           return "error"

                     
                 
#start of the program
if __name__== '__main__':
   
  ## Creating an instance of the Brewery class 
  state=Brewery("Alaska","https://api.openbrewerydb.org/v1/breweries?by_state=alaska")
  state1=Brewery("maine","https://api.openbrewerydb.org/v1/breweries?by_state=maine")
  state2=Brewery("New York","https://api.openbrewerydb.org/v1/breweries?by_state=new%20york")

  #printing and calling different methods of class
  print("count and List of Breweries present in states alaska,Maine,New york")
  #calling different methods of class and printing the output
  print(str(state.list_brewery_state())+"\n")
  print(str(state1.list_brewery_state())+"\n")
  print(str(state2.list_brewery_state())+"\n")
  print("count of no. of types pf breweries present in states alaska,Maine,New york")
  print(str(state.brewery_types())+"\n")
  print(str(state1.brewery_types())+"\n")
  print(str(state2.brewery_types())+"\n")
  print(str(state.brewery_website())+"\n")
  print(str(state1.brewery_website())+"\n")
  print(state2.brewery_website())