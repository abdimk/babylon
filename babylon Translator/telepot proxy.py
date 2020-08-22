'''
This proxy will help you to run your telegram bot on pythonanywhere no free hosting
'''
# start of online server proxy config

import urllib3
import telepot.api
proxy_url = 'http://proxy.server:3128'

telepot.api._pools = {
    'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30), }

telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1,
                                                             retries=False, timeout=30))

# end of online server proxy config
