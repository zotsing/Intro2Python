
# coding: utf-8

# In[2]:

##selenium is mostly used for writing test cases
###webdriver module provides WebDriver implementations
import os
###currently support Firefox, Chrome, Ie and Remote
from selenium import webdriver
###Keys class provide keys in the keyboard like RETURN,F1,ALT etc
from selenium.webdriver.common.keys import Keys
###unittest provide a testing tool/framework
import unittest


# In[3]:

###create instance of chrome WebDriver
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
#driver = webdriver.Chrome(chrome_options=options)
#driver.get("http://www.google.com")
##print (driver.page_source.encode('utf-8'))


# In[4]:

###writing a test for python.org search functionality
class PythonOrgSearch(unittest.TestCase):
    '''test case is inherited from unittest.TestCase
    ...tell unittest module that this is a test case
    ...setUP is initialization, get called before each test function'''
    def setUp(self):
        #self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome(chrome_options=options)
    def test_search_in_python_org(self):
        '''test case methon, always start with characters tet
        ...first line create a local reference to driver object'''
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    def tearDown(self):
        self.driver.close()



# In[5]:

######running in command line
#if __name__ == "__main__":
#    unittest.main()
    
#####running in notebook, using TextTestRunner
suite = unittest.TestLoader().loadTestsFromTestCase(PythonOrgSearch)
unittest.TextTestRunner(verbosity=2).run(suite)


# In[6]:




# In[7]:




# In[8]:

sum(a)


# In[9]:




# In[10]:




# In[ ]:




# In[11]:




# In[12]:




# In[13]:




# In[ ]:



