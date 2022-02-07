#!/usr/bin/python3
'''
Name: Victor Li
Date: 07/02/2022
Description: A simple script that automatically posts a Kijiji with a provided config
'''

from selenium import webdriver

PATH = r"C:\Users\Windows\Downloads\PythonScripts\PythonScripts\geckodriver.exe"
driver = webdriver.Firefox(PATH)
driver.get("http://www.python.org")