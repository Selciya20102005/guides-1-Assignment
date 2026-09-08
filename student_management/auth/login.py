import frappe


# def on_login(login_manager):

#     print("User Logged In")

#     print(login_manager.user)



# def on_login_failed(login_manager):

#     print("Login Failed!")

#     print("Username:", login_manager.user)






def validate():
    print("===== AUTH HOOK EXECUTED =====")

    auth = frappe.get_request_header("Authorization")

    print("Authorization Header:", auth)