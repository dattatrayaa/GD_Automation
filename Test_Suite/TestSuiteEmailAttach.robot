*** Settings ***
Library   ../Master/SendEmailWithAttachment.py

** Test Cases **
To Send email 
    Send Mail     ${report}     ${log}