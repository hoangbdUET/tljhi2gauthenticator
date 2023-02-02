from traitlets import Unicode

from jupyterhub.auth import Authenticator

from tornado import gen

import requests

from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class I2GAuthenticator(Authenticator):
    password = Unicode(
        None,
        allow_none=True,
        config=True,
        help="""
        Set a global password for all users wanting to log in.
        This allows users with any username to log in with the same static password.
        """
    )

    @gen.coroutine
    def authenticate(self, handler, data):
        def login(username, password):
            r = login_RAW(username, password)
            if r['code'] == 200:
                return True, r['content']
            return False, r['reason']
        def login_RAW(username, password):
            payload = {
                "username": username,
                "password": password
            }
            url = 'https://users.i2g.cloud' + '/login'
            r = requests.post(url, json = payload, verify=False, headers = {'Service': 'WI_AUTH'})
            return r.json()
        if self.password:
            logged, user = login(data['username'],data['password'])
            if logged :
                print("I2G Login OK =====")
                return data['username']
            else :
                print("I2g Login FAIL =======")
                return None
            #if data['password'] == self.password:
            #    return data['username']
            #return None
        #return data['username']