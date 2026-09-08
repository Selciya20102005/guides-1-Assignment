# import frappe

# from frappe.search.full_text_search import FullTextSearch


# class StudentFullTextSearch(FullTextSearch):

#     def __init__(self):
#         super().__init__("student_index")

#     def get_items_to_index(self):
#         students = frappe.get_all(
#             "Student",
#             fields=["name", "student_name"]
#         )

#         return [
#             {
#                 "name": student.name,
#                 "content": student.student_name or ""
#             }
#             for student in students
#         ]

#     def get_document_to_index(self, doc_name):
#         student = frappe.get_doc("Student", doc_name)

#         return {
#             "name": student.name,
#             "content": student.student_name or ""
#         }

#     def get_fields_to_search(self):
#         return ["name", "content"]

#     def parse_result(self, result):
#         return {
#             "name": result["name"],
#             "content": result["content"]
#         }


# @frappe.whitelist()
# def build_student_index():

#     search_engine = StudentFullTextSearch()

#     search_engine.build()

#     return "Student index built successfully"


# @frappe.whitelist()
# def search_students(text):

#     search_engine = StudentFullTextSearch()

#     return search_engine.search(
#         text=text,
#         limit=20
#     )
# @frappe.whitelist()
# def update_student_index(doc_name):

#     search_engine = StudentFullTextSearch()

#     search_engine.update_index_by_name(doc_name)

#     return "Student index updated successfully"

# @frappe.whitelist()
# def remove_student_from_index(doc_name):

#     search_engine = StudentFullTextSearch()

#     search_engine.remove_document_from_index(doc_name)

#     return "Student removed from index successfully"





# my_app/search/sqlite_search.py

import frappe

from frappe.search.sqlite_search import SQLiteSearch


class StudentManagementSearch(SQLiteSearch):

    # =========================================================
    # INDEX CONFIGURATION
    # =========================================================

    INDEX_NAME = "student_management_search.db"

    INDEX_SCHEMA = {
        "text_fields": [
            "title",
            "content",
        ],

        "metadata_fields": [
            "owner",
            "status",
            "priority",
        ],

        "tokenizer": "unicode61 remove_diacritics 2 tokenchars '-_@.'",
    }

    # =========================================================
    # DOCTYPES TO INDEX
    # =========================================================

    INDEXABLE_DOCTYPES = {
        "Task": {
            "fields": [
                "name",

                # Task subject → search title
                {"title": "subject"},

                # Task description → search content
                {"content": "description"},

                # Used for recency boosting
                "modified",

                # Metadata
                "owner",
                "status",
                "priority",
            ],

            "filters": {
                "status": ("!=", "Cancelled"),
                "docstatus": ("!=", 2),
            },
        }
    }

    # =========================================================
    # PERMISSION FILTERING
    # =========================================================

    def get_search_filters(self):
        # For testing, allow all indexed documents.
        return {}

    # =========================================================
    # SEARCH ENABLED
    # =========================================================

    def is_search_enabled(self):
        """
        Check whether SQLite search is enabled.

        Returning True means search is enabled.
        You can add custom conditions here later.
        """

        return True

    # =========================================================
    # CHECK INDEX EXISTS
    # =========================================================

    def index_exists(self):
        """
        Check whether the SQLite search index exists.
        """

        return super().index_exists()

    # =========================================================
    # INDEX A SINGLE DOCUMENT
    # =========================================================

    def index_doc(self, doctype, docname):
        """
        Add or update a single document in the search index.

        Example:

            search.index_doc(
                "Task",
                "TASK-2026-00005"
            )
        """

        if not self.is_search_enabled():
            return

        return super().index_doc(doctype, docname)

    # =========================================================
    # REMOVE A SINGLE DOCUMENT
    # =========================================================

    def remove_doc(self, doctype, docname):
        """
        Remove a single document from the search index.

        Example:

            search.remove_doc(
                "Task",
                "TASK-2026-00005"
            )
        """

        if not self.is_search_enabled():
            return

        return super().remove_doc(doctype, docname)

    # =========================================================
    # CUSTOM PRIORITY SCORING
    # =========================================================

    @SQLiteSearch.scoring_function
    def get_priority_boost(self, row, query, query_words):

        try:
            priority = row["priority"]

        except (KeyError, IndexError):
            priority = "MISSING"

        # DEBUG INFORMATION
        print("========================================")
        print("PRIORITY SCORING")
        print("Document :", row["doc_id"])
        print("Priority :", priority)
        print("Query    :", query)
        print("========================================")

        # Priority multiplier
        if priority == "Urgent":
            return 1.8

        if priority == "High":
            return 1.5

        if priority == "Medium":
            return 1.1

        # Low or missing priority
        return 1.0