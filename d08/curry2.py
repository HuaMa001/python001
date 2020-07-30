#admin can get 100 dollar
#hacker login failed get 0 dollar
def login(username):
    def loginpass(money):
        return 100 if money>100 else money
    def loginfail(money):
        return 0
    return loginpass if username == "admin" else  loginfail

print(login('admin')(100))
print(login('hacker')(100))















