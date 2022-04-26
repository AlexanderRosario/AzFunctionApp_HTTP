
import logging

from config import connection

import azure.functions as func
from .uploadBlob import upload_blob


def main(req: func.HttpRequest) -> func.HttpResponse:

    # logging.info('Python HTTP trigger function processed a request.')
    conn = connection()
    name = req.params.get('name')
    cedula = req.params.get('cedula')

    dataset = select(conn ,name,cedula)

    if not dataset :
        return func.HttpResponse("no se pudo ejecutar el query o no hay nada en el select")

    if upload_blob(dataset) != True :
        return func.HttpResponse("Error subiendo los archivos")

    return func.HttpResponse("subio todo correctamente")

    # if not name:
    #     try:
    #         req_body = req.get_json()
    #     except ValueError:
    #         pass
    #     else:
    #         name = req_body.get('name')

    # if name:
    #     return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    # else:
    #     return func.HttpResponse(
    #          "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
    #          status_code=200
        # )


def select(conn,name,cedula):
    
    query = """ Select * from tablename where name = '{}' and cedula = '{}' """.format(name,cedula)
    cursor = conn.cursor()

    try:
        cursor.execute(query)
        row = cursor.fetchone()
        return row
    except Exception as e :
        return None
    
    finally:
        conn.close()


