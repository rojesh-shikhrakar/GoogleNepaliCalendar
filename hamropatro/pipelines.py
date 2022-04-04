# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from datetime import datetime, timedelta
import uuid
from itemadapter import ItemAdapter
from icalendar import Calendar, Event, vText



class HamropatroPipeline:
    def __init__(self):
        self.cal = Calendar()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        event = Event()
        event['uid'] = uuid.uuid1()
        event.add('DTSTART', datetime.strptime(item['eng'], '%d %b %Y').date())
        event.add('SUMMARY', vText(item['nep']+ ' | ' + item['tithi'] ))
        self.cal.add_component(event)

        if item['events'] != "--":
            event = Event()
            event['uid'] = uuid.uuid1()
            event.add('DTSTART', datetime.strptime(item['eng'], '%d %b %Y').date())
            event.add('SUMMARY', vText( item['events']))
            self.cal.add_component(event)

        return item
    
    def close_spider(self, spider):
        with open("NepDate.ical",mode='wb') as f:
            f.write(self.cal.to_ical())

