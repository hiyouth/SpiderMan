from resource import Resource

__author__ = 'bliss'

import configparser


class Supplier:

    @staticmethod
    def get_resources():
        # 获取需要下载网站的信息
        conf = configparser.ConfigParser()
        conf.read('grove.conf', 'utf-8')
        sections = conf.sections()
        resources = []
        for section in sections:
            items = Supplier.get_section_items(conf, section)
            resource = Supplier.assemble(section, items)
            resources.append(resource)
        return resources

    @staticmethod
    def get_section_items(conf, section):
        # 根绝配置文件节点获取网站配置信息
        opts = conf.items(section)
        return opts

    @staticmethod
    def hi(d, c):
        return None

    @staticmethod
    def assemble(section_name, items):
        # 将配置文件的数据组装成对象
        resource = Resource()
        resource.flag = section_name
        for item in items:
            setattr(resource, item[0], item[1])
        return resource

