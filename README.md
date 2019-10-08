# web_content_search_regex
This is a Python program to fetch web contents by using Regular Expressions.

## Task
Developing in Python3 a script that takes a list of urls to check, for each url
it must be possible to specify regular expressions that are matched in the content.
The URLs and regex must be in a YAML configuration file. 
The results of the check must be stored somehow for later analysis.


## Features
* Python Program
* Regular Expressions or regex
* YAML configuration file for URL and regex
* Reading and writing in the files
* [PEP8] Style
* Less external dependencies
* Comments and documentations 
* Both Python and Jupyter notebook files 

## Sample Input/Output

### config.yaml: 

URLs:
  - https://www.example.com
  - https://www.cgi.fi/fi
  - https://yle.fi
  - https://www.linkedin.com
  - https://www.google.com
  - https://www.youtube.com
  - https://www.nordea.fi
  - https://www.tori.fi
  - https://www.hs.fi

RegEx: 
  - <title>(.*?)</title>



### Output: 

Contents:  Date: 09-10-2019 Time: 01:11:27:388485_AM Example Domain

Contents:  Date: 09-10-2019 Time: 01:11:27:388485_AM Example Domain

Contents:  Date: 09-10-2019 Time: 01:11:27:388485_AM IT- ja liiketoimintakonsultoinnin palvelut | CGI FI

Contents:  Date: 09-10-2019 Time: 01:11:27:388485_AM <span>Kaikki pilveistymisen elementit</span>\n

Contents:  Date: 09-10-2019 Time: 01:11:27:388485_AM Yle.fi - oivalla jotain uutta

Contents:  Date: 09-10-2019 Time: 01:11:27:388485_AM LinkedIn: Log In or Sign Up

Contents:  Date: 09-10-2019 Time: 01:11:27:388485_AM Google

Contents:  Date: 09-10-2019 Time: 01:11:27:388485_AM YouTube

Contents:  Date: 09-10-2019 Time: 01:11:27:388485_AM Tervetuloa Nordeaan - Palvelut henkil\xc3\xb6asiakkaille | Nordea.fi 

Contents:  Date: 09-10-2019 Time: 01:11:27:388485_AM Osta ja myy helposti. Ilmoita ilmaiseksi Torissa.

Contents:  Date: 09-10-2019 Time: 01:11:27:388485_AM Uutiset | HS.fi




## Project Status
The project is still going on and will be completed as a full application.

Also, UI, Asynchronous IO, Unit test and a seperate database will be added soon.
