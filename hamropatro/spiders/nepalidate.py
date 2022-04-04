import scrapy
from ..items import HamropatroItem

class NepalidateSpider(scrapy.Spider):
    name = 'nepalidate'
    allowed_domains = ['www.hamropatro.com']
    start_urls = ['https://www.hamropatro.com/calendar']
    dates = {}
    pageCounter = 1

    def parse(self, response):
        blocks = response.css(".dates li")
        temp = response.css(".newDateText::text").getall()
        nepMonth = temp[0][5:-3] + ' ' + temp[0][:4]
        engMonths = temp[1][1:4] + ' ' + temp[1][-5:-1] , temp[1][5:8] + ' ' + temp[1][-5:-1]
        monthInd = 0
        started = False
        limit = int(getattr(self, 'limit', 12))
        items = HamropatroItem()

        for block in blocks:
            nep = block.css(".nep::text").get()
            eng = block.css(".eng::text").get() 
            events = block.css(".event::text").get()
            tithi = block.css(".tithi::text").get()
            
            if nep == '१':
                if started:
                    break
                started = True

            # dates[eng + engMonths[monthInd]] = (nep + nepMonth, tithi, events)

            if started:
                if eng == '1':
                    monthInd = 1

                items['eng'] = eng + ' ' + engMonths[monthInd]
                items['nep'] = nep + ' ' + nepMonth
                items['tithi'] = tithi
                items['events']= events
                yield items

        nextPage = response.css(".arrowRight")[0].css("a::attr(href)").get()
        if (nextPage is not None) and (self.pageCounter < limit):
            nextPage = response.urljoin(nextPage)
            self.pageCounter += 1
            yield scrapy.Request(nextPage, callback=self.parse)