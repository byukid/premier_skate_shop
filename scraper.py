# This is a template for a Python scraper on Morph (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
import lxml.html

# # Read in a page
html = scraperwiki.scrape("http://thepremierstore.com")
#
# # Find something on the page using css selectors
root = lxml.html.fromstring(html)
root.cssselect(/html/head/h2/text()).extract()

for sel in response.xpath('//ul/li')
    title = sel.xpath('a/text()').extract()
    link = sel.xpath('a/@href').extract()
    desc = sel.xpath('text()').extract()
    print title, link, desc
#
# # Write out to the sqlite database using scraperwiki library
scraperwiki.sqlite.save()
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries. You can use whatever libraries are installed
# on Morph for Python (https://github.com/openaustralia/morph-docker-python/blob/master/pip_requirements.txt) and all that matters
# is that your final data is written to an Sqlite database called data.sqlite in the current working directory which
# has at least a table called data.
