from src.LogInPage import LogInPage

"""Initial File which shows welcome msg, accepts the userType (admin or customer), gets the userName and 
UserPassword. After getting userName and userPassword triggers Login Page"""

if __name__ == '__main__':
    print('\n' + "--*---Welcome to the Shopping Mart ----*-----".center(120) + '\n')
    print("Please specify who are you?"
          "\n1] Admin"
          "\n2] Customer\n")

    userType = input('ans (write admin/customer)-> ')
    userName = input("Enter your userName: \n")
    userPass = input("\n1Enter your password: \n")

    # # log_data = LogInPage('admin', 'admin1', 'admin123')
    log_data = LogInPage(userType.lower(), userName, userPass)

    print('\n' + "----------@@ Welcome to the Demo Marketplace @@---------".center(120) + '\n')
    log_data.login()
