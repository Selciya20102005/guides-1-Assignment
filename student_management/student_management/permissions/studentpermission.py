import frappe


def get_permission_query_conditions(user):

    return "`tabStudent`.department = 'AI&DS'"


def has_permission(doc, user=None, permission_type=None):

    print("Has Permission Hook Executed")

    return True

def has_permission(doc, user=None, permission_type=None):

    print("Access Denied")

    return False