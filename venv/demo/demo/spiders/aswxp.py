import scrapy

# Création de la class aswxp (pour Adley Salabi Work Experiences)
class aswxp(scrapy.Spider):
    name = "aswxp"
    # On renseigne l'url du portfolio 
    start_urls = ["http://adleysalabi.com//"]
    # On parse la réponse 
    def parse(self, response):
        # self.logger afin d'avooir un retour visuel que la spider à bien été lancée
            self.logger.info('Everything seems to be working :) ')
            # On décide de définir la class .workxp_one dans une variable 
            workxps = response.css('div.workxp_one')
            # Puis on boucle sur toutes les div .workxp_one
            for workxp_one in workxps:
                # On renseigne chaque élément souhaité à l'aide de sélecteurs css
                yield {
                    'job': workxp_one.css('.workxp_job::text').get(),
                    'contrat': workxp_one.css('.workxp_type::text').get(),
                    'dates': workxp_one.css('.workxp_company_date>span:last-child::text').get(),
                    'company_name': workxp_one.css('.workxp_company_date>a::text').get(),
                    'company_url': workxp_one.css('.workxp_company_date>a::attr(href)').get(),
                    'resume': workxp_one.css('p::text').get(),
                    'skills': workxp_one.css('.workxp_skills_wrapper>span:last-child::text').get(),
                }