# GoogleNepaliCalendar

Scrapes www.hamropatro.com and add events to google calendar

## Usage

```scrapy crawl nepalidate -o dates.csv -a limit=12```

-a `limit=12`[default] is the number of months to scrape [optional]

```scrapy crawl nepalidate -a limit=12```

generates ical file that can be imported in google calendar
