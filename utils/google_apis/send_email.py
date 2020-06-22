import what_you_need
    
# see https://developers.google.com/gmail/api/guides/sending

def create_message_with_inline_image(
    sender, to, subject, message_text, file, table):
    """Create a message for an email with inline image

    Returns:
      An object containing a base64url encoded email object.
    """
    message = MIMEMultipart()
    message['to'] = to
    message['from'] = sender

    message['subject'] = subject

    html_part = MIMEMultipart(_subtype='related')

    # in case there are tables
    head = """<head><style>
            table {
              font-family: arial, sans-serif;
              border-collapse: collapse;
              width: 80%;
            }
            
            td, th {
              border: 2px solid #dddddd;
              text-align: left;
              padding: 8px;
            }
            
            tr:nth-child(even) {
              background-color: #dddddd;
            }
            </style></head>"""

    html = '''
        <html>
        {head}
          <body>
            <p></p>
            <h3>Images:</h3> 
            <img src="cid:myimage1" width="70%" height="70%"/>
            {table}
            <p></br></br></p>
          </body>
        </html>
        '''.format(head=head, 
                   table=table)

    mime_text = MIMEText(html, "html")
    html_part.attach(mime_text)

    img_data_1 = open('image_1.png', 'rb').read()
  
    img1 = MIMEImage(img_data_1, 'png')
    img1.add_header('Content-Id', '<myimage1>')
    img1.add_header("Content-Disposition", "inline", filename="myimage1")
    html_part.attach(img1)

    message.attach(html_part)

    return {'raw': base64.urlsafe_b64encode(message.as_bytes())}
