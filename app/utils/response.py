from flask import  Response,json

'''
helper functions for response 
'''
def success_response_builder(status,message):
    return Response(
                response = json.dumps({'status':"Success", 'data':message}),
                status = status,
                mimetype = 'application/json'
                )

def failure_response_builder(status,message):
    return Response(
                response = json.dumps({'status':"Failure", 'error':message}),
                status = status,
                mimetype = 'application/json'
                )
