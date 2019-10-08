
"""
This is a Python program to fetch web contents by using Regular Expressions.

We have a separate YAML config file that mainly contents 2 types of data.
    1. List if URL
    2. List of Regular Expressions or RegEx

The following program will go to all the URL one by one, and then will use the 
regular expressions to find the content as we needed. For example, in this program,
we tried to fetch the <h1> header and <title> information from the URL.

Example output:

Data Fetching:
URL:  https://www.example.com
Example Domain
Example Domain

URL:  https://www.cgi.fi/fi
IT- ja liiketoimintakonsultoinnin palvelut | CGI FI
<span>Kaikki pilveistymisen elementit</span>\n

"""

# Importing libraries 

import re
import yaml
import urllib.request
from datetime import datetime



# Getting data from configuration file
class Content_searcher():
    """ This class takes the YAML confiuration file as the argument, 
    and extract the list of url and regex. Then regex is used to 
    find content from the URL.
    """
    
    def __init__(self, config_file, url_key, regex_key, output_file):
        """Initializes the Content_searcher class with the parameters
        
        Args: 
        config_file = Name of the YAML config file with URLs and regex 
        url_key = key to access the list of URLs from YAML config file
        regex_key = key to access the list of regex from YAML config file
        output_file = Name of the file that will be saved as output
        
        """

        self.config_file = config_file
        self.url_key = url_key
        self.regex_key = regex_key
        self.output_file = output_file

        
    def search_content(self):
        """ This function fetch the contents from the list of URLs in according to 
        the regular expressions of the YAML config file.
        """        
        
        try:

            with open(self.output_file, 'a') as f:
                time = datetime.now().strftime("Date: %d-%m-%Y Time: %I:%M:%S:%f_%p")

                with open(self.config_file) as config_file:

                    data = yaml.load(config_file, yaml.FullLoader)
                    

                    # Extracting the list of URLs

                    url_list = data.get(url_key)
                    print('List of URLs:')
                    for url in url_list:
                        print(url)

                        
                    # Extracting the list of regular expressions 
                    
                    regex_list = data.get(regex_key)
                    print('List of RegGex:')
                    for regex in regex_list:
                        print(regex)
                        

                    # Fetching the contest 
                    
                    print('Data Fetching:')

                    for url in url_list:
                        print('URL: ', url)
                        req = urllib.request.Request(url)
                        resp = urllib.request.urlopen(req)
                        respData = resp.read()

                        for regex in regex_list:
                            contents  = re.findall( regex,str(respData))
                            if not contents:
                                print('Cannot find content using regex: ', regex)
                            else:    
                                for content in contents:
                                    print(content)
                                    
                                    # Writing the outputs in the file
                                    print('Contents: ', time, content, file = f)

                print('\nProgram executed successfully')

        except:
            print('\nOops, ERROR! ')

        
# Passing the arguments values

configFile_path = r'C:\Users\Anik Barua\Desktop\Content_Searcher\config.yaml'
url_key = 'URLs'
regex_key = 'RegEx'
output_file = 'result.txt'

Content_searcher(configFile_path,url_key,regex_key,output_file).search_content()
