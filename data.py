import pandas as pd
import requests
data={
    'id':[1,2,3],
    'name':['a','b','c'],
    'address':['pune','mumbai','latur']
}
print("student detaials")
pf=pd.DataFrame(data)
print(data)

print('API data')
response=requests.get('https://jsonplaceholder.typicode.com/users')
print(response.json())