# python-scrapy-project

To start the project : 

Be sure that you are in the good directory : 

`cd venv`

Be sure that venv is install : 

`python3.6 -m venv venv`

Start the virtual environment with this command : 

`source venv/bin/activate`

In the virtual env : 




________________________________________


response.xpath("//div[@class='workxp_one']").get()
// Toute la div avec les work experience 

workxp = response.xpath("//div[@class='workxp_one']")
// assigne à une variable 

workxp[0].css(".workxp_company_date > a::text").getall()
