import os

"""urls"""
urls = {'1c_prod': 'https://1cgames.net/'}

"""drivers"""
driver_chrome = os.path.abspath(os.curdir + '/drivers/chromedriver.exe')
driver_firefox = os.path.abspath(os.curdir + '/drivers/geckodriver.exe')

"""data"""
user_login = {'correct_login': 'alexander.markov@1cog.games', 'uncorrect_login': 'test@test.com'}
user_password = {'correct_password': '123123', 'uncorrect_password': 'qwerty'}
