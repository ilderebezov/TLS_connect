Django project, which call the remote api method using the attached certificate + key pair for authorization ("two-way TLS", endpoint: https://slb.medv.ru/api/v2/)
The certificate and key are written in the settings.py of the project modules.

In the settings.py:

CLIENT_SECURITY_CERTIFICATE_FILE = '/home/.../cliet_name_file.crt'  # input full path to client *.crt file

SECURITY_CERTIFICATE_FILE = os.environ.get('your_CA.crt') # input name your name.crt file

PATH_CLIENT = '/home/key file folder/' # input path to client *.key file

CLIENT_SECURITY_KEY_FILE = os.environ.get(PATH_CLIENT, 'client_name_file.key') # input client name *.key file
