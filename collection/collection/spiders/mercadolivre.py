import scrapy


class MercadolivreSpider(scrapy.Spider):
    name = "mercadolivre"
    allowed_domains = ["lista.mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/tenis-corrida-masculino"]

    def parse(self, response):
        products = response.css('div.poly-card__content')

        for product in products:
            yield{
                'brand':                 products.css('span.poly-component__brand::text').get(),
                'name':                  products.css('a.poly-component__title::text').get(),
                'old_price':             products.css('span.andes-money-amount__fraction::text').get(),
                'old_price_cents':       products.css('span.andes-money-amount__cents::text').get(),
                'new_price':             products.css('::text').get(),
                'new_price_cents':       products.css('::text').get(),
                'reviews_rating_number': products.css('::text').get(),
                'reviews_amount':        products.css('::text').get()
            }

