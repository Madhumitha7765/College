from urllib.parse import urlencode

import pycurl
from io import BytesIO
import certifi


headers = {}

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
    # In cases we have multiple  headers with the same name,
    # only the last header value will be stored.
    # To store all values in multi-valued headers,we use the below code
    if h_name in headers:
        if isinstance(headers[h_name], list):
            headers[h_name].append(h_value)
        else:
            headers[h_name] = [headers[h_name], h_value]
    else:
        headers[h_name] = h_value # Header name and value.



if __name__ == "__main__":

        b_obj = BytesIO()
        crl = pycurl.Curl()
        # Set URL value
        crl.setopt(pycurl.CAINFO, certifi.where())
        crl.setopt(crl.URL, 'http://127.0.0.1:9000/test.html')



        # POST method sends data to a web server by enclosing it in the body of the HTTP request
        data = {'field': 'value'}
        pf = urlencode(data)
        # Sets request method to POST,
        # Content-Type header to application/x-www-form-urlencoded
        # and data to send in request body.
        crl.setopt(crl.POSTFIELDS, pf)

        # put method for uploading data
        data = '{"person":{"name":"billy","email":"billy@example.com"}}'
        buffer = BytesIO(data.encode('utf-8'))
        crl.setopt(crl.UPLOAD, 1)
        crl.setopt(crl.READDATA, buffer)

        #delete method
        #crl.setopt(crl.CUSTOMREQUEST, "DELETE")


        # get header values
        crl.setopt(crl.HEADERFUNCTION, display_header)


        # Write bytes that are utf-8 encoded
        crl.setopt(crl.WRITEDATA, b_obj)
        # Perform a file transfer
        crl.perform()
        # End curl session
        crl.close()

        # Get the content stored in the BytesIO object (in byte characters)
        get_body = b_obj.getvalue()
        # Decode the bytes stored in get_body to HTML and print the result
        print('Output of GET aftre delete request:\n%s' % get_body.decode('utf8'))
        # Displaying header values
        print('Header values : \n',headers)




