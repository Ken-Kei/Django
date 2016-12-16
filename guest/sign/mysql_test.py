import pymysql.cursors


# Connect to the database
connection = pymysql.connect(host='106.75.139.202:3311',
                             user='root',
                             password='mllm',
                             db='test',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursor:
        # Create a new record

        