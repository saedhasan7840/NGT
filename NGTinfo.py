import requests
logo = ("""
███████╗ █████╗ ███████╗██████╗ 
██╔════╝██╔══██╗██╔════╝██╔══██╗
███████╗███████║█████╗  ██║  ██║
╚════██║██╔══██║██╔══╝  ██║  ██║
███████║██║  ██║███████╗██████╔╝
╚══════╝╚═╝  ╚═╝╚══════╝╚═════╝ 
""")
print(logo)
num = input("Enter Your Number: ")
api = f"https://flaneroo.com/attack.php?number={num}"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

response = requests.get(api, headers=headers)

if response.status_code == 200:
    data = response.json()
    print("Name: ",data["name"])
    print("Status: ",data["status"])
    print("User Type: ",data["userType"])
    print("User Id:",data["userId"])
    print("rbBase:",data["rbBase"])
    print("Token Info:",data["authTokenInfo"])
    print(" Varification Status: ",data["verificationStatus"])
else:
    print("Failed to retrieve information for Number:", num)
