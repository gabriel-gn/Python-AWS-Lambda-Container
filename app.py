# curl --request POST \
#   --url http://localhost:9001/2015-03-31/functions/function/invocations \
#   --header 'Content-Type: application/json' \
#   --cookie csrftoken=NNSI5ErloePKFcj2B34RK21857qnVF3UfYdDOk46TetT3I7LqCZiT5PWW2hLoehK \
#   --data '{
# 	"payload": "hello world!"
# }'

import sys
def handler(event, context):
    return 'Hello from AWS Lambda using Python' + sys.version + '!'        
