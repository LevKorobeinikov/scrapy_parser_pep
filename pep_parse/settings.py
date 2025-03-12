from pathlib import Path

NAME_PEP = 'pep'
DOMAINS = ['peps.python.org']
RESULTS = 'results'

BOT_NAME = 'pep_parse'
SPIDERS_MODULE = 'pep_parse.spiders'
SPIDER_MODULES = [SPIDERS_MODULE]
NEWSPIDER_MODULE = SPIDERS_MODULE
ROBOTSTXT_OBEY = True


BASE_DIR = Path(__file__).parent.parent

FEEDS = {
    f'{RESULTS}/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
    # 'pep_parse.pipelines.PepsToDBPipeline': 300,
}
