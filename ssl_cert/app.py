import json
import OpenSSL
import ssl

def lambda_handler(event, context):

    siteId = event['queryStringParameters']['siteId']
    cert=ssl.get_server_certificate((siteId, 443))
    x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
    date_byte = str(x509.get_notAfter())
    date = str(date_byte)
    year = date_byte[2:6]
    month = date_byte[6:8]
    day = date_byte[8:10]
    date = month+"-"+day+"-"+year

    return {
        "statusCode": 200,
        "body": json.dumps({
            "--SSL Expiration Date of "+ siteId: date  ,
        }),
    }
