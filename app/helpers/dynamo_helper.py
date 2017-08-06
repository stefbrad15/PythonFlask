import boto.dynamodb2
from boto.dynamodb2.fields import HashKey, RangeKey, KeysOnlyIndex, GlobalAllIndex
from boto.dynamodb2.table import Table
from boto.dynamodb2.types import NUMBER

class DynamoInterface():
    def __init__(self):
        # Provide a way to list_tables
        self.conn = boto.dynamodb.connect_to_region('us-east-1') #N Virginia region

    def list_tables(self):
        """
        List tables to determine if a table should be created
        This will need to be done if for instance we switch from a beta instance to prod
        """
        return self.conn.list_tables()
    
    def get_table(self, table_name):
        return Table(table_name) 

    def create_table(self, table_name, hashkey, rangekey, throughput_dict):
        schema_list = [
            HashKey(hashkey),
            RangeKey(rangekey)
        ]
        return Table.create(table_name, schema=schema_list, throughput=throughput_dict)
    
    def get_all_items(self, table_name, attributes=None):
        table = Table(table_name)
        items = table.scan(attributes = attributes)
        to_list = list()
        for i in items:
            to_list.append(dict(i))

        return to_list

if __name__ == "__main__":
    iDynamo = DynamoInterface()
    print iDynamo.list_tables()