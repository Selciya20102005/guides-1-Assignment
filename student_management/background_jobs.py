import frappe
import time

def test_background_job(message):
    print(f"========== JOB STARTED: {message} ==========")

    time.sleep(10)

    print(f"========== JOB FINISHED: {message} ==========")




def test_custom_queue(message):
    print(f"========== CUSTOM JOB STARTED: {message} ==========")

    time.sleep(10)

    print(f"========== CUSTOM JOB FINISHED: {message} ==========")