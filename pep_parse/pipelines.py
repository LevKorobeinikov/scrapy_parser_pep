import csv
from datetime import datetime
from collections import defaultdict

from pep_parse.settings import RESULTS_DIR

DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
STATUS = 'Статус'
COUNT = 'Количество'
TOTAL = 'ИТОГО'


class PepParsePipeline:
    def __init__(self):
        RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    def open_spider(self, spider):
        spider.logger.info(f'Results directory created at {RESULTS_DIR}')
        self.results = defaultdict(int)

    def process_item(self, item, spider):
        pep_status = item['status']
        self.results[pep_status] += 1
        return item

    def close_spider(self, spider):
        filename = 'status_summary_{}.csv'.format(
            datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        )
        file_path = RESULTS_DIR / filename

        with open(file_path, mode='w', encoding='utf-8') as file:
            csv.writer(
                file, dialect=csv.excel
            ).writerows((
                (STATUS, COUNT),
                *self.results.items(),
                (TOTAL, sum(self.results.values()))
            ))
