from pathlib import Path

NAME_PEP = 'pep'
DOMAINS = ['peps.python.org']
RESULTS = 'results'

BOT_NAME = 'pep_parse'
NEWSPIDER_MODULE = 'pep_parse.spiders'
SPIDER_MODULES = [NEWSPIDER_MODULE]
ROBOTSTXT_OBEY = True


BASE_DIR = Path(__file__).parent.parent
RESULTS_DIR = BASE_DIR / RESULTS
RESULTS_DIR.mkdir(parents=True, exist_ok=True)

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
