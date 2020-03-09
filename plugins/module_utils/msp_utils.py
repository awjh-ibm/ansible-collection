#!/usr/bin/python
#
# SPDX-License-Identifier: Apache-2.0
#

from __future__ import absolute_import, division, print_function
__metaclass__ = type

import base64
import os
import tempfile

fake_cacert = '''
-----BEGIN CERTIFICATE-----
MIICCTCCAa+gAwIBAgIULtfu81UTt2IcdiWK7GYQU77HhscwCgYIKoZIzj0EAwIw
WjELMAkGA1UEBhMCVVMxFzAVBgNVBAgTDk5vcnRoIENhcm9saW5hMRQwEgYDVQQK
EwtIeXBlcmxlZGdlcjEPMA0GA1UECxMGRmFicmljMQswCQYDVQQDEwJjYTAeFw0y
MDAzMDYwODU1MDBaFw0zNTAzMDMwODU1MDBaMFoxCzAJBgNVBAYTAlVTMRcwFQYD
VQQIEw5Ob3J0aCBDYXJvbGluYTEUMBIGA1UEChMLSHlwZXJsZWRnZXIxDzANBgNV
BAsTBkZhYnJpYzELMAkGA1UEAxMCY2EwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNC
AATq6LSk5TeYmcsSbmLJdwTVoS3pCHNlzZY4m1bkRgvjk8bU3+1vvhKTL3OAGpKZ
L8FM7KaH9jmztT23IgmkZZ7zo1MwUTAOBgNVHQ8BAf8EBAMCAQYwDwYDVR0TAQH/
BAUwAwEB/zAdBgNVHQ4EFgQU6AC52T9R5Y3K4XGNPqh3bBJR7DIwDwYDVR0RBAgw
BocEfwAAATAKBggqhkjOPQQDAgNIADBFAiEA7OHP7yH7tE0ko6Gp98o/EkhTqo4o
6cGACl2wEnq4tpsCIEStfRFHHweEFuPkf4Ab+nrXTGovTg35WIP+5XkpQOZf
-----END CERTIFICATE-----
'''

def convert_identity_to_msp_path(identity):

    # Create a temporary directory.
    msp_path = tempfile.mkdtemp()

    # Create the admin certificates directory (ideally would be empty, but
    # needs something in it to keep the CLI quiet).
    admincerts_path = os.path.join(msp_path, 'admincerts')
    os.mkdir(admincerts_path)
    with open(os.path.join(admincerts_path, 'cert.pem'), 'wb') as file:
        file.write(identity.cert)

    # Create the CA certificates directory.
    cacerts_path = os.path.join(msp_path, 'cacerts')
    os.mkdir(cacerts_path)
    with open(os.path.join(cacerts_path, 'cert.pem'), 'wb') as file:
        file.write(identity.ca)

    # Create the signing certificates directory.
    signcerts_path = os.path.join(msp_path, 'signcerts')
    os.mkdir(signcerts_path)
    with open(os.path.join(signcerts_path, 'cert.pem'), 'wb') as file:
        file.write(identity.cert)

    # Create the key store directory.
    keystore_path = os.path.join(msp_path, 'keystore')
    os.mkdir(keystore_path)
    with open(os.path.join(keystore_path, 'key.pem'), 'wb') as file:
        file.write(identity.private_key)

    # Return the temporary directory (user must delete).
    return msp_path