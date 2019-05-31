Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import urllib
>>> import requests
>>> dir(urllib)
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'error', 'parse', 'request', 'response']
>>> dir(requests)
['ConnectTimeout', 'ConnectionError', 'DependencyWarning', 'FileModeWarning', 'HTTPError', 'NullHandler', 'PreparedRequest', 'ReadTimeout', 'Request', 'RequestException', 'RequestsDependencyWarning', 'Response', 'Session', 'Timeout', 'TooManyRedirects', 'URLRequired', '__author__', '__author_email__', '__build__', '__builtins__', '__cached__', '__cake__', '__copyright__', '__description__', '__doc__', '__file__', '__license__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__title__', '__url__', '__version__', '_check_cryptography', '_internal_utils', 'adapters', 'api', 'auth', 'certs', 'chardet', 'check_compatibility', 'codes', 'compat', 'cookies', 'delete', 'exceptions', 'get', 'head', 'hooks', 'logging', 'models', 'options', 'packages', 'patch', 'post', 'put', 'request', 'session', 'sessions', 'status_codes', 'structures', 'urllib3', 'utils', 'warnings']
>>> requests.info
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    requests.info
AttributeError: module 'requests' has no attribute 'info'
>>> requests.info()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    requests.info()
AttributeError: module 'requests' has no attribute 'info'
>>> info(requests)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    info(requests)
NameError: name 'info' is not defined
>>> requests.__version__
'2.19.1'
>>> urllib.__version__
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    urllib.__version__
AttributeError: module 'urllib' has no attribute '__version__'
>>> help(urllib)
Help on package urllib:

NAME
    urllib

PACKAGE CONTENTS
    error
    parse
    request
    response
    robotparser

FILE
    c:\python37\lib\urllib\__init__.py


>>> import urllib2
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    import urllib2
ModuleNotFoundError: No module named 'urllib2'
>>> import urllib.request as request
>>> dir(request)
['AbstractBasicAuthHandler', 'AbstractDigestAuthHandler', 'AbstractHTTPHandler', 'BaseHandler', 'CacheFTPHandler', 'ContentTooShortError', 'DataHandler', 'FTPHandler', 'FancyURLopener', 'FileHandler', 'HTTPBasicAuthHandler', 'HTTPCookieProcessor', 'HTTPDefaultErrorHandler', 'HTTPDigestAuthHandler', 'HTTPError', 'HTTPErrorProcessor', 'HTTPHandler', 'HTTPPasswordMgr', 'HTTPPasswordMgrWithDefaultRealm', 'HTTPPasswordMgrWithPriorAuth', 'HTTPRedirectHandler', 'HTTPSHandler', 'MAXFTPCACHE', 'OpenerDirector', 'ProxyBasicAuthHandler', 'ProxyDigestAuthHandler', 'ProxyHandler', 'Request', 'URLError', 'URLopener', 'UnknownHandler', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__', '_cut_port_re', '_ftperrors', '_have_ssl', '_localhost', '_noheaders', '_opener', '_parse_proxy', '_proxy_bypass_macosx_sysconf', '_randombytes', '_safe_gethostbyname', '_thishost', '_url_tempfiles', 'addclosehook', 'addinfourl', 'base64', 'bisect', 'build_opener', 'contextlib', 'email', 'ftpcache', 'ftperrors', 'ftpwrapper', 'getproxies', 'getproxies_environment', 'getproxies_registry', 'hashlib', 'http', 'install_opener', 'io', 'localhost', 'noheaders', 'os', 'parse_http_list', 'parse_keqv_list', 'pathname2url', 'posixpath', 'proxy_bypass', 'proxy_bypass_environment', 'proxy_bypass_registry', 'quote', 're', 'request_host', 'socket', 'splitattr', 'splithost', 'splitpasswd', 'splitport', 'splitquery', 'splittag', 'splittype', 'splituser', 'splitvalue', 'ssl', 'string', 'sys', 'tempfile', 'thishost', 'time', 'to_bytes', 'unquote', 'unquote_to_bytes', 'unwrap', 'url2pathname', 'urlcleanup', 'urljoin', 'urlopen', 'urlparse', 'urlretrieve', 'urlsplit', 'urlunparse', 'warnings']
>>> dir(urllib.response)
['__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'addbase', 'addclosehook', 'addinfo', 'addinfourl', 'tempfile']
>>> url = "https://www.google.com"
>>> sp = request.urlsplit()
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    sp = request.urlsplit()
TypeError: urlsplit() missing 1 required positional argument: 'url'
>>> sp = request.urlsplit(url)
>>> sp
SplitResult(scheme='https', netloc='www.google.com', path='', query='', fragment='')
>>> sp[0]
'https'
>>> sp[1]
'www.google.com'
>>> sp[2]
''
>>> url1="https://stackoverflow.com/questions/34475051/need-to-install-urllib2-for-python-3-5-1"
>>> sp = request.urlsplit(url1)
>>> sp
SplitResult(scheme='https', netloc='stackoverflow.com', path='/questions/34475051/need-to-install-urllib2-for-python-3-5-1', query='', fragment='')
>>> url1="https://stackoverflow.com/questions/34475051/need-to-install-urllib2-for-python-3-5-1?admin=no&param=yes:8000"
>>> sp = request.urlsplit(url1)
>>> sp
SplitResult(scheme='https', netloc='stackoverflow.com', path='/questions/34475051/need-to-install-urllib2-for-python-3-5-1', query='admin=no&param=yes:8000', fragment='')
>>> sp.admin
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    sp.admin
AttributeError: 'SplitResult' object has no attribute 'admin'
>>> type(sp[3])
<class 'str'>
>>> sp1=request.splitquery()
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    sp1=request.splitquery()
TypeError: splitquery() missing 1 required positional argument: 'url'
>>> sp1=request.splitquery(url1)
>>> spl
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    spl
NameError: name 'spl' is not defined
>>> sp1
('https://stackoverflow.com/questions/34475051/need-to-install-urllib2-for-python-3-5-1', 'admin=no&param=yes:8000')
>>> dir(request)
['AbstractBasicAuthHandler', 'AbstractDigestAuthHandler', 'AbstractHTTPHandler', 'BaseHandler', 'CacheFTPHandler', 'ContentTooShortError', 'DataHandler', 'FTPHandler', 'FancyURLopener', 'FileHandler', 'HTTPBasicAuthHandler', 'HTTPCookieProcessor', 'HTTPDefaultErrorHandler', 'HTTPDigestAuthHandler', 'HTTPError', 'HTTPErrorProcessor', 'HTTPHandler', 'HTTPPasswordMgr', 'HTTPPasswordMgrWithDefaultRealm', 'HTTPPasswordMgrWithPriorAuth', 'HTTPRedirectHandler', 'HTTPSHandler', 'MAXFTPCACHE', 'OpenerDirector', 'ProxyBasicAuthHandler', 'ProxyDigestAuthHandler', 'ProxyHandler', 'Request', 'URLError', 'URLopener', 'UnknownHandler', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__', '_cut_port_re', '_ftperrors', '_have_ssl', '_localhost', '_noheaders', '_opener', '_parse_proxy', '_proxy_bypass_macosx_sysconf', '_randombytes', '_safe_gethostbyname', '_thishost', '_url_tempfiles', 'addclosehook', 'addinfourl', 'base64', 'bisect', 'build_opener', 'contextlib', 'email', 'ftpcache', 'ftperrors', 'ftpwrapper', 'getproxies', 'getproxies_environment', 'getproxies_registry', 'hashlib', 'http', 'install_opener', 'io', 'localhost', 'noheaders', 'os', 'parse_http_list', 'parse_keqv_list', 'pathname2url', 'posixpath', 'proxy_bypass', 'proxy_bypass_environment', 'proxy_bypass_registry', 'quote', 're', 'request_host', 'socket', 'splitattr', 'splithost', 'splitpasswd', 'splitport', 'splitquery', 'splittag', 'splittype', 'splituser', 'splitvalue', 'ssl', 'string', 'sys', 'tempfile', 'thishost', 'time', 'to_bytes', 'unquote', 'unquote_to_bytes', 'unwrap', 'url2pathname', 'urlcleanup', 'urljoin', 'urlopen', 'urlparse', 'urlretrieve', 'urlsplit', 'urlunparse', 'warnings']
>>> sp1=request.splitattr(url1)
>>> sp1
('https://stackoverflow.com/questions/34475051/need-to-install-urllib2-for-python-3-5-1?admin=no&param=yes:8000', [])
>>> sp1=request.splithost(url1)
>>> sp1
(None, 'https://stackoverflow.com/questions/34475051/need-to-install-urllib2-for-python-3-5-1?admin=no&param=yes:8000')
>>> sp1=request.splittag(url1)
>>> sp1
('https://stackoverflow.com/questions/34475051/need-to-install-urllib2-for-python-3-5-1?admin=no&param=yes:8000', None)
>>> sp1=request.urlcleanup(url1)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    sp1=request.urlcleanup(url1)
TypeError: urlcleanup() takes 0 positional arguments but 1 was given
>>> sp1=request.urlparse(url1)
>>> p1
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    p1
NameError: name 'p1' is not defined
>>> sp1
ParseResult(scheme='https', netloc='stackoverflow.com', path='/questions/34475051/need-to-install-urllib2-for-python-3-5-1', params='', query='admin=no&param=yes:8000', fragment='')
>>> urllib.parse.urlencode("this is anish")
Traceback (most recent call last):
  File "C:\Python37\lib\urllib\parse.py", line 858, in urlencode
    raise TypeError
TypeError

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    urllib.parse.urlencode("this is anish")
  File "C:\Python37\lib\urllib\parse.py", line 866, in urlencode
    "or mapping object").with_traceback(tb)
  File "C:\Python37\lib\urllib\parse.py", line 858, in urlencode
    raise TypeError
TypeError: not a valid non-string sequence or mapping object
>>> import urllib.parse as parse
>>> dir(parse)
['DefragResult', 'DefragResultBytes', 'MAX_CACHE_SIZE', 'ParseResult', 'ParseResultBytes', 'Quoter', 'ResultBase', 'SplitResult', 'SplitResultBytes', '_ALWAYS_SAFE', '_ALWAYS_SAFE_BYTES', '_DefragResultBase', '_NetlocResultMixinBase', '_NetlocResultMixinBytes', '_NetlocResultMixinStr', '_ParseResultBase', '_ResultMixinBytes', '_ResultMixinStr', '_SplitResultBase', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_asciire', '_coerce_args', '_decode_args', '_encode_result', '_hexdig', '_hextobyte', '_hostprog', '_implicit_encoding', '_implicit_errors', '_noop', '_parse_cache', '_portprog', '_safe_quoters', '_splitnetloc', '_splitparams', '_typeprog', 'clear_cache', 'collections', 'namedtuple', 'non_hierarchical', 'parse_qs', 'parse_qsl', 'quote', 'quote_from_bytes', 'quote_plus', 're', 'scheme_chars', 'splitattr', 'splithost', 'splitnport', 'splitpasswd', 'splitport', 'splitquery', 'splittag', 'splittype', 'splituser', 'splitvalue', 'sys', 'to_bytes', 'unquote', 'unquote_plus', 'unquote_to_bytes', 'unwrap', 'urldefrag', 'urlencode', 'urljoin', 'urlparse', 'urlsplit', 'urlunparse', 'urlunsplit', 'uses_fragment', 'uses_netloc', 'uses_params', 'uses_query', 'uses_relative']
>>> dir(request)
['AbstractBasicAuthHandler', 'AbstractDigestAuthHandler', 'AbstractHTTPHandler', 'BaseHandler', 'CacheFTPHandler', 'ContentTooShortError', 'DataHandler', 'FTPHandler', 'FancyURLopener', 'FileHandler', 'HTTPBasicAuthHandler', 'HTTPCookieProcessor', 'HTTPDefaultErrorHandler', 'HTTPDigestAuthHandler', 'HTTPError', 'HTTPErrorProcessor', 'HTTPHandler', 'HTTPPasswordMgr', 'HTTPPasswordMgrWithDefaultRealm', 'HTTPPasswordMgrWithPriorAuth', 'HTTPRedirectHandler', 'HTTPSHandler', 'MAXFTPCACHE', 'OpenerDirector', 'ProxyBasicAuthHandler', 'ProxyDigestAuthHandler', 'ProxyHandler', 'Request', 'URLError', 'URLopener', 'UnknownHandler', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__', '_cut_port_re', '_ftperrors', '_have_ssl', '_localhost', '_noheaders', '_opener', '_parse_proxy', '_proxy_bypass_macosx_sysconf', '_randombytes', '_safe_gethostbyname', '_thishost', '_url_tempfiles', 'addclosehook', 'addinfourl', 'base64', 'bisect', 'build_opener', 'contextlib', 'email', 'ftpcache', 'ftperrors', 'ftpwrapper', 'getproxies', 'getproxies_environment', 'getproxies_registry', 'hashlib', 'http', 'install_opener', 'io', 'localhost', 'noheaders', 'os', 'parse_http_list', 'parse_keqv_list', 'pathname2url', 'posixpath', 'proxy_bypass', 'proxy_bypass_environment', 'proxy_bypass_registry', 'quote', 're', 'request_host', 'socket', 'splitattr', 'splithost', 'splitpasswd', 'splitport', 'splitquery', 'splittag', 'splittype', 'splituser', 'splitvalue', 'ssl', 'string', 'sys', 'tempfile', 'thishost', 'time', 'to_bytes', 'unquote', 'unquote_to_bytes', 'unwrap', 'url2pathname', 'urlcleanup', 'urljoin', 'urlopen', 'urlparse', 'urlretrieve', 'urlsplit', 'urlunparse', 'warnings']
>>> read = request.urlopen(url1)
>>> read
<http.client.HTTPResponse object at 0x0487FC50>
>>> read.getcode()
200
>>> read.getheaders()
[('Cache-Control', 'private'), ('Content-Type', 'text/html; charset=utf-8'), ('Last-Modified', 'Sat, 27 Oct 2018 15:56:33 GMT'), ('X-Frame-Options', 'SAMEORIGIN'), ('X-Request-Guid', '1358a96d-ef20-40c9-8b86-e7f68734f61b'), ('Strict-Transport-Security', 'max-age=15552000'), ('Content-Security-Policy', 'upgrade-insecure-requests'), ('Accept-Ranges', 'bytes'), ('Age', '0'), ('Content-Length', '139930'), ('Accept-Ranges', 'bytes'), ('Date', 'Sun, 23 Dec 2018 12:02:00 GMT'), ('Via', '1.1 varnish'), ('Age', '0'), ('Connection', 'close'), ('X-Served-By', 'cache-ams21030-AMS'), ('X-Cache', 'MISS'), ('X-Cache-Hits', '0'), ('X-Timer', 'S1545566521.706377,VS0,VE93'), ('Vary', 'Fastly-SSL'), ('X-DNS-Prefetch-Control', 'off'), ('Set-Cookie', 'prov=ad65a8f3-fce0-2f55-2767-72a0fb787aaf; domain=.stackoverflow.com; expires=Fri, 01-Jan-2055 00:00:00 GMT; path=/; HttpOnly')]
>>> read.getheader()
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    read.getheader()
TypeError: getheader() missing 1 required positional argument: 'name'
>>> read.getheader('Content-Type')
'text/html; charset=utf-8'
>>> read.geturl()
'https://stackoverflow.com/questions/34475051/need-to-install-urllib2-for-python-3-5-1?admin=no&param=yes:8000'
>>> read.info()
<http.client.HTTPMessage object at 0x0487FDD0>
>>> read.readline()
b'<!DOCTYPE html>\r\n'
>>> read.readlines()
[b'\r\n', b'\r\n', b'    ]


import requests
import simplejson

r = requests.get('https://github.com/timeline.json')
c = r.content
j = simplejson.loads(c)
print(j)
print(j['message'])

r = requests.get('https://api.github.com', auth=('user', 'pass'))
print r.status_code
print r.headers['content-type']

import requests
import simplejson
import urllib.request as urllib2
from xml.dom import minidom

r = requests.get('https://github.com/timeline.json')
c = r.content
j = simplejson.loads(c)
print(j)
print(j['message'])

url = 'https://www.boardgamegeek.com/xmlapi2/thing?id=13&stats=1' # define XML location
dom = minidom.parse(urllib2.urlopen(url))
link = dom.getElementsByTagName('link')
categories = [items.attributes['value'].value for items in link if items.attributes['type'].value == "boardgamecategory"]
print(categories)



import requests

url = 'http://maps.googleapis.com/maps/api/directions/json'

params = dict(
    origin='Chicago,IL',
    destination='Los+Angeles,CA',
    waypoints='Joplin,MO|Oklahoma+City,OK',
    sensor='false'
)

resp = requests.get(url=url, params=params)
data = resp.json() # Check the JSON Response Content documentation below


 with urllib.request.urlopen('http://www.python.org/') as f:
...     print(f.read(100).decode('utf-8'))

 >>> import urllib.request
>>> local_filename, headers = urllib.request.urlretrieve('http://python.org/')
>>> html = open(local_filename)
>>> html.close()


link="https://www.samsclub.com/robots.txt"
import requests
content = requests.get(link).content
content = requests.get(link).text
content = requests.get(link).content.decode() 
 
