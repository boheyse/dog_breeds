# -*- coding: utf-8 -*-


class Spider:
    
    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()
    
    def __init__ (self):
        