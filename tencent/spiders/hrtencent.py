# -*- coding: utf-8 -*-
import scrapy
from tencent.items import TencentItem
from scrapy.pipelines.images import ImagesPipeline

class HrtencentSpider(scrapy.Spider):
    name = "hrtencent"

    start_num = 0

    allowed_domains = ["hr.tencent.com"]
    start_urls = (
        'http://hr.tencent.com/position.php?&start=' + str(start_num),
    )

    def parse(self, response):
        zhiwei_list = response.xpath("//tr[@class='even']|//tr[@class='odd']")

        for zhiwei in zhiwei_list:
            item = TencentItem()

            name = zhiwei.xpath("./td[1]/a/text()").extract()[0]
            link = zhiwei.xpath("./td[1]/a/@href").extract()[0]

            if len(zhiwei.xpath("./td[2]/text()")) > 0:
                leibie = zhiwei.xpath("./td[2]/text()").extract()[0]
            else:
                leibie = "暂无"
            num = zhiwei.xpath("./td[3]/text()").extract()[0]
            addr = zhiwei.xpath("./td[4]/text()").extract()[0]
            date = zhiwei.xpath("./td[5]/text()").extract()[0]

            item['name'] = name
            item['link'] = link
            item['leibie'] = leibie
            item['num'] = num
            item['addr'] = addr
            item['date'] = date

            yield item
        if self.start_num < 2260:
            self.start_num += 10

        yield scrapy.Request("http://hr.tencent.com/position.php?&start=" + str(self.start_num))








