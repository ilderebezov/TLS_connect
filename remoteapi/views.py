from django.shortcuts import render
import ssl
import socket
from django.conf import settings as conf_settings
from .models import api_request


def index(request):
    return render(request, 'index.html')


def api_tls_request(request):
    client_crt = conf_settings.CLIENT_SECURITY_CERTIFICATE_FILE
    client_key = conf_settings.CLIENT_SECURITY_KEY_FILE
    cert_ca = conf_settings.SECURITY_CERTIFICATE_FILE
    url = '/api/v2/'
    hostname = 'slb.medv.ru'
    ip = '92.53.120.119'
    port = 443
    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH, cafile=cert_ca)
    context.load_cert_chain(certfile=client_crt, keyfile=client_key)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn = context.wrap_socket(s, server_side=False, server_hostname=hostname)
    conn.connect((ip, port))

    headers = {'content-type': 'application/json'}
    payload = {
        "method": "auth.check",
        "params": ["echome!"],
        "jsonrpc": "2.0",
        "id": 0,
    }
    answer = api_request(hostname, url, payload, headers)
    return render(request, "result.html", {'result': answer[0], 'result_json': answer[1]})
    conn.close()
