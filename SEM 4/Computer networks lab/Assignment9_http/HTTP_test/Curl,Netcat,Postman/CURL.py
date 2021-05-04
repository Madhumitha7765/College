import pycurl
from io import BytesIO
import certifi

headers = {}

def curl_get():
    crl = pycurl.Curl()
    # setopt- set url,which file,write read file in bytes object
    # certifi - validate and perform safe transfers
    crl.setopt(pycurl.CAINFO, certifi.where())
    # set URL value
    crl.setopt(pycurl.URL, 'http://127.0.0.1:9000/test.html')
    # Write bytes that are utf-8 encoded
    crl.setopt(crl.WRITEDATA, b_obj)
    # Perform a file transfer
    # return bytes object output stream
    crl.perform()
    # End curl session
    crl.close()
    # Get the content stored in the BytesIO object (in byte characters)
    get_body = b_obj.getvalue()
    # Decode the bytes stored in get_body to HTML and print the result
    print('Output of GET request:\n', get_body.decode('utf8'))


def display_header(header_line):
    header_line = header_line.decode('iso-8859-1')
    # Ignore all lines without a colon
    if ':' not in header_line:
        return
    # Break the header line into header name and value
    h_name, h_value = header_line.split(':', 1)
    # Remove whitespace that may be present
    h_name = h_name.strip()
    h_value = h_value.strip()
    h_name = h_name.lower() # Convert header names to lowercase
    headers[h_name] = h_value # Header name and value.

def curl_header():
    crl = pycurl.Curl()
    crl.setopt(crl.URL, "http://127.0.0.1:9000/test.html")
    crl.setopt(crl.HEADERFUNCTION, display_header)
    crl.setopt(crl.WRITEDATA, b_obj)
    crl.perform()
    print('Header values:-')
    print(headers)

def curl_delete():
    choice = input("\nDo you want to delete file : ")
    if choice == "Y" or choice == "y":
        crl = pycurl.Curl()
        crl.setopt(crl.URL, "http://127.0.0.1:9000/test.html")
        crl.setopt(crl.CUSTOMREQUEST, "DELETE")
        crl.perform()
        print("File deleted successfully")
        crl.close()

if __name__=="__main__":

    b_obj = BytesIO()
    print("\n1.GET file content")
    print("\n2.View HEADERS of file")
    print("\n3.DELETE the file")
    choice =input("\nEnter the action you wish to perform : ")
    if int(choice)==1:curl_get()
    elif int(choice)==2:curl_header()
    elif int(choice)==3:curl_delete()
    else: exit()






