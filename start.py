from grabber import Grabber
from processor.zcool import ZCool
from supplier import Supplier

resources = Supplier.get_resources()

for resource in resources:
    grabber = Grabber(resource)
    grabber.get()
    ZCool.parse_article_list(grabber.content)
    break
    # grabber.write()