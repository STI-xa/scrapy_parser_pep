import csv
import datetime
from collections import defaultdict
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent


class PepParsePipeline:
    def open_spider(self, spider):
        self.statuses = defaultdict(int)

    def process_item(self, item, spider):
        key = item.get('status')
        self.statuses[key] += 1
        return item

    def close_spider(self, spider):
        results_dir = BASE_DIR / 'results'
        time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        file_name = results_dir / f'status_summary_{time}.csv'
        results_dir.mkdir(exist_ok=True)
        with open(file_name, 'w', encoding='utf-8') as file:
            results_writer = csv.writer(file)
            results_writer.writerows(
                (
                    ('Статус', 'Количество'),
                    *sorted(self.statuses.items()),
                    ('Total', sum(self.statuses.values()))
                )
            )
