import requests
#print(dir(requests))
url='https://cdn.dribbble.com/users/185738/screenshots/15298921/media/7b671f8fd03b8f9bdae94ec133e55acb.gif'
result=requests.get(url)
print(result.status_code)
with open('img.gif','wb') as  file:
    file.write(result.content)