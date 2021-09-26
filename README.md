Django project, which call the remote api method using the attached certificate + key pair for authorization ("two-way TLS", endpoint: https://slb.medv.ru/api/v2/)
The certificate and key are written in the settings.py of the project modules.

In the settings.py:

CLIENT_SECURITY_CERTIFICATE_FILE = ''  # input full path to client *.crt file
CLIENT_SECURITY_KEY_FILE = ''  # input full path to client *.key file
SECURITY_CERTIFICATE_FILE = ''  # input full path to your *.crt file
