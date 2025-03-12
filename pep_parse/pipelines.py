import csv
from datetime import datetime
from collections import defaultdict

from pep_parse.settings import BASE_DIR, RESULTS

DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
STATUS = 'Статус'
COUNT = 'Количество'
TOTAL = 'ИТОГО'


class PepParsePipeline:
    def open_spider(self, spider):
        self.results = defaultdict(int)

    def process_item(self, item, spider):
        pep_status = item['status']
        self.results[pep_status] += 1
        return item

    def close_spider(self, spider):
        results_dir = BASE_DIR / RESULTS
        results_dir.mkdir(parents=True, exist_ok=True)
        filename = 'status_summary_{}.csv'.format(
            datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        )
        file_path = results_dir / filename

        with open(file_path, mode='w', encoding='utf-8') as file:
            writer = csv.writer(file, dialect=csv.excel)
            writer.writerows(
                (
                    (STATUS, COUNT),
                    *self.results.items(),
                    (TOTAL, sum(self.results.values()))
                )
            )
