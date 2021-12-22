import base64

username = input("username: ")
password = input("password: ")

# Basic認証用の文字列を作成.
basic_username_and_password = base64.b64encode('{}:{}'.format(username, password).encode('utf-8'))

print({"Authorization": "Basic " + basic_username_and_password.decode('utf-8')})
