# basic-selenium-tests
Those tests are executing some basic scenarios agains google search page and it is generaing a basic report in allure with scenarios results. 

## What is required in order to be able to execute the tests?
In order to execute the tests, it is required to install some python libs, those requirements will be installed executing the script  deploy.sh using the following command:

`sh deploy.sh`

## How execute the test?
It is possible to execute test using any of the two following ways:

 1. **Execute Test Suite**
    
    `python3 -m pytest test_suite.py --alluredir ./results`

 2. **Execute one by one**
 
    `python3 -m pytest google_search.py --alluredir ./results`

    `python3 -m pytest google_search_suggestions.py --alluredir ./results`
 
## How generate and see the report?
Using the command `--alluredir ./results`the test is able to generate automatically some JSON files with the tests results, those files are read by Allure and showing in a nice way using the following command:

`allure serve results/`

Of course previous command should be executed once the test finish and results folder contains the files that Allure will be reading.

