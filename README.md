# python-scrapy-project

## To start the project : 

Be sure that you are in the good directory : 
`cd venv`

Be sure that venv is install : 
`python3.6 -m venv venv`

Start the virtual environment with this command : 
`source venv/bin/activate`

## In the virtual env : 

Go to the directory demo where the childrens directory are the folder `demo` and `scrapy.cfg`. 

In the folder `demo/demo/spiders` you will find the `aswxp.py` file. In this file there is a script thath will catch all the work experience from the website `adleysalabi.com`.  

To visualise what data we are scraping, in the root `venv/demo/`, lunch the command `scrapy crawl aswxp`. 

Then, if you want to extract the data into a json file :
`scrapy crawl aswxp -o quotes.json`