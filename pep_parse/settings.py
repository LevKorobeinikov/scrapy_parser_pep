from pathlib import Path

NAME_PEP = 'pep'
DOMAINS = ['peps.python.org']
RESULTS = 'results'

BOT_NAME = 'pep_parse'
NEWSPIDER_MODULE = 'pep_parse.spiders'
SPIDER_MODULES = [NEWSPIDER_MODULE]
ROBOTSTXT_OBEY = True
SPIDER_MIDDLEWARES = {
    'pep_parse.middlewares.CreateResultsDirOnOpenMiddleware': 500,
}


BASE_DIR = Path(__file__).parent.parent
RESULTS_DIR = BASE_DIR / RESULTS

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
