import scrapy

class aswxp(scrapy.Spider):
    name = "aswxp"

    start_urls = ["http://adleysalabi.com//"]

    def parse(self, response):
            self.logger.info('hello this is my first spider')
            workxps = response.css('div.workxp_one')
            for workxp_one in workxps:
                yield {
                    'job': workxp_one.css('.workxp_job::text').get(),
                    'contrat': workxp_one.css('.workxp_type::text').get(),
                    'dates': workxp_one.css('.workxp_company_date.workxp_date::text').get(),
                    'company': workxp_one.css('.workxp_company_date>a::text').get(),
                    'resume': workxp_one.css('p::text').get(),
                    'skills': workxp_one.css('.workxp_skills_wrapper.workxp_skill_used::text').get(),
                }