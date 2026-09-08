import frappe


def clear_cache(path=None):

    print("Website cache clear hook called")
    print("Path:", path)