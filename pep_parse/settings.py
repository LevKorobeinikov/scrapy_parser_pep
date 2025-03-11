from pathlib import Path

NAME_PEP = 'pep'
DOMAINS = ['peps.python.org']
URLS = ['https://peps.python.org/']

BOT_NAME = 'pep_parse'
SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'
ROBOTSTXT_OBEY = True

STATUS_PEP = 'status'
NAME = 'name'
NUMBER_PEP = 'number'

BASE_DIR = Path(__file__).parent.parent

FEEDS = {
    'results/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': [NUMBER_PEP, NAME, STATUS_PEP],
        'overwrite': True
    },
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
    # 'pep_parse.pipelines.PepsToDBPipeline': 300,
}
