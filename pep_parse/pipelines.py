import csv
from datetime import datetime
from collections import defaultdict

from sqlalchemy import Column, Integer, String, Text, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declared_attr, sessionmaker

from pep_parse.settings import BASE_DIR, STATUS_PEP, NAME, NUMBER_PEP

DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
RESULT_DIR = 'results'
STATUS = 'Статус'
COUNT = 'Количество'
TOTAL = 'ИТОГО'


class Base:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()
    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=Base)


class Pep(Base):
    status = Column(Text)
    number = Column(Integer)
    name = Column(String(200))


class PepsToDBPipeline:

    def open_spider(self, spider):
        engine = create_engine('sqlite:///sqlite.db')
        Base.metadata.create_all(engine)
        Session = sessionmaker(engine)
        self.session = Session()

    def process_item(self, item, spider):
        peps = Pep(
            number=item[NUMBER_PEP],
            name=item[NAME],
            status=item[STATUS_PEP],
        )
        self.session.add(peps)
        self.session.commit()
        return item

    def close_spider(self, spider):
        self.session.close()


class PepParsePipeline:
    def open_spider(self, spider):
        self.results = defaultdict(int)

    def process_item(self, item, spider):
        pep_status = item[STATUS_PEP]
        self.results[pep_status] = self.results.get(pep_status, 0) + 1
        return item

    def close_spider(self, spider):
        results_dir = BASE_DIR / RESULT_DIR
        filename = (
            f'status_summary_'
            f'{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.csv'
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
