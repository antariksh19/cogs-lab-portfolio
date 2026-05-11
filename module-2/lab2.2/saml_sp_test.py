from flask import Flask, request, redirect
import urllib.parse, base64, zlib

app = Flask(__name__)

@app.route('/saml/login')
def saml_login():
    idp_url = 'http://localhost:8080/realms/instasafe-lab/protocol/saml'
    
    # Added 'Destination' attribute (Required by Keycloak 23+)
    xml_request = f'<samlp:AuthnRequest xmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol" ID="id123" Version="2.0" IssueInstant="2026-05-05T12:00:00Z" Destination="{idp_url}"><saml:Issuer xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion">https://sp.instasafe.local/saml</saml:Issuer></samlp:AuthnRequest>'
    
    # Compress and encode perfectly for HTTP-Redirect
    deflated = zlib.compress(xml_request.encode('utf-8'))[2:-4]
    saml_request = base64.b64encode(deflated).decode('utf-8').strip()
    
    redirect_url = f'{idp_url}?SAMLRequest={urllib.parse.quote(saml_request)}'
    
    print("\n--- GENERATED REDIRECT URL ---")
    print(redirect_url)
    print("------------------------------\n")
    
    return redirect(redirect_url)

@app.route('/saml/callback', methods=['POST'])
def saml_callback():
    saml_response = request.form.get('SAMLResponse', '')
    decoded = base64.b64decode(saml_response).decode('utf-8')
    return f'<pre>SAML Response received!\n{decoded[:2000]}</pre>'

if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=9090)