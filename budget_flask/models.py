from budget_flask import mongo

cash = mongo.db.main_collection.find_one({'cash': {'$exists': 'true', '$ne': 'null'}})['cash']
cc_citi = mongo.db.main_collection.find_one({'cc_citi': {'$exists': 'true', '$ne': 'null'}})['cc_citi']
cc_chase = mongo.db.main_collection.find_one({'cc_chase': {'$exists': 'true', '$ne': 'null'}})['cc_chase']
cc_discover = mongo.db.main_collection.find_one({'cc_discover': {'$exists': 'true', '$ne': 'null'}})['cc_discover']