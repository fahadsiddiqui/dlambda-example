import sys

def handler(event, context):
    print("Hello from lambda_func.py")
    print("event: ", event)
    print("context: ", context)
    print("sys.version: ", sys.version)
    
    return "Hello from lambda_func.py"