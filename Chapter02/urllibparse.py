Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import urllb.request
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import urllb.request
ModuleNotFoundError: No module named 'urllb'
>>> import urllib.request
>>> import os
>>> link="https://www.samsclub.com/robots.txt"
>>> linkRequest = urllib.request.urlopen(link)
>>> linkResponse = urllib.request.urlopen(link).read()
>>> requestObj = urllib.request.Request(link)
>>> requestObjResponse = urllib.request.urlopen(requestObj).read()
>>> requestObj.full_url
'https://www.samsclub.com/robots.txt'
>>> dir(requestObj)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_data', '_full_url', '_parse', '_tunnel_host', 'add_header', 'add_unredirected_header', 'data', 'fragment', 'full_url', 'get_full_url', 'get_header', 'get_method', 'has_header', 'has_proxy', 'header_items', 'headers', 'host', 'origin_req_host', 'remove_header', 'selector', 'set_proxy', 'timeout', 'type', 'unredirected_hdrs', 'unverifiable']
>>> requestObj.full_url
'https://www.samsclub.com/robots.txt'
>>> requestObj.type
'https'
>>> requestObj.host
'www.samsclub.com'
>>> requestObj.get_metod()
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    requestObj.get_metod()
AttributeError: 'Request' object has no attribute 'get_metod'
>>> requestObj.get_method()
'GET'
>>> dir(linkRequest)
['__abstractmethods__', '__class__', '__del__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_abc_impl', '_checkClosed', '_checkReadable', '_checkSeekable', '_checkWritable', '_check_close', '_close_conn', '_get_chunk_left', '_method', '_peek_chunked', '_read1_chunked', '_read_and_discard_trailer', '_read_next_chunk_size', '_read_status', '_readall_chunked', '_readinto_chunked', '_safe_read', '_safe_readinto', 'begin', 'chunk_left', 'chunked', 'close', 'closed', 'code', 'debuglevel', 'detach', 'fileno', 'flush', 'fp', 'getcode', 'getheader', 'getheaders', 'geturl', 'headers', 'info', 'isatty', 'isclosed', 'length', 'msg', 'peek', 'read', 'read1', 'readable', 'readinto', 'readinto1', 'readline', 'readlines', 'reason', 'seek', 'seekable', 'status', 'tell', 'truncate', 'url', 'version', 'will_close', 'writable', 'write', 'writelines']
>>> linkRequest.headers()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    linkRequest.headers()
TypeError: 'HTTPMessage' object is not callable
>>> linkResponse.headers()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    linkResponse.headers()
AttributeError: 'bytes' object has no attribute 'headers'
>>> linkRequest.getheaders()
[('Content-Type', 'text/plain'), ('Forcelegacy', 'false'), ('Samsheader', 'TB-DAL'), ('Strict-Transport-Security', 'max-age=86400'), ('X-Frame-Options', 'SAMEORIGIN'), ('X-Tb', '0'), ('Vary', 'Accept-Encoding'), ('Cache-Control', 'max-age=1200'), ('Date', 'Sun, 30 Dec 2018 06:51:03 GMT'), ('Content-Length', '336'), ('Connection', 'close'), ('Set-Cookie', 'NSC_JOxs2zfhe1jdcygeqrfzgndx0hpxlbc=7c02a3dcbd468cdf6abb052f7eda0697875a3e1933985bf70d66fcd9189125c4c3981037;expires=Sun, 30-Dec-2018 12:51:03 GMT;path=/;secure;httponly'), ('Set-Cookie', 'TS01f4281b=0103fe05472857cb28c5e6ea8b9bf77c546da7d991d0beb2003d52baab99e34219a1e867891dbbc12cf771a04553a82c077c33dd11; Path=/; Secure'), ('Set-Cookie', 'dcenv=TB-DAL; path=/; domain=samsclub.com'), ('Set-Cookie', 'akavpau_P3=1546153263~id=e80887aba5911e0e7cba05eec1755be1; Path=/')]
>>> linkRequest = urllib.request.urlopen(link)
>>> linkRequest.headers()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    linkRequest.headers()
TypeError: 'HTTPMessage' object is not callable
>>> linkRequest = urllib.request.urlopen(link)
>>> linkRequest.headers()
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    linkRequest.headers()
TypeError: 'HTTPMessage' object is not callable
>>> linkRequest.getheaders()
[('Content-Type', 'text/plain'), ('Forcelegacy', 'false'), ('Samsheader', 'TB-DAL'), ('Strict-Transport-Security', 'max-age=86400'), ('X-Frame-Options', 'SAMEORIGIN'), ('X-Tb', '0'), ('Vary', 'Accept-Encoding'), ('Cache-Control', 'max-age=1200'), ('Date', 'Sun, 30 Dec 2018 06:59:51 GMT'), ('Content-Length', '336'), ('Connection', 'close'), ('Set-Cookie', 'dcenv=TB-DAL; path=/; domain=samsclub.com'), ('Set-Cookie', 'akavpau_P3=1546153791~id=8709c5576f8a88a160bbc8f11ac662e4; Path=/')]
>>> link="https://www.samsclub.com/robots.txt"
>>> link="https://www.google.com"
>>> linkRequest = urllib.request.urlopen(link)
>>> linkRequest.headers()
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    linkRequest.headers()
TypeError: 'HTTPMessage' object is not callable
>>> linkRequest.getheaders()
[('Date', 'Sun, 30 Dec 2018 07:00:25 GMT'), ('Expires', '-1'), ('Cache-Control', 'private, max-age=0'), ('Content-Type', 'text/html; charset=ISO-8859-1'), ('P3P', 'CP="This is not a P3P policy! See g.co/p3phelp for more info."'), ('Server', 'gws'), ('X-XSS-Protection', '1; mode=block'), ('X-Frame-Options', 'SAMEORIGIN'), ('Set-Cookie', '1P_JAR=2018-12-30-07; expires=Tue, 29-Jan-2019 07:00:25 GMT; path=/; domain=.google.com'), ('Set-Cookie', 'NID=152=DANr9NtDzU-_glKFRgVsOm2eJQpyLijpRav7OAAd97QXGX6WwYMC59dDPemaGxr5VS3wNBb2PnbRQcVB8XXN_uo0RWyBAGD87jYTc1vUMxhEkc1w5Wo5JdPBdcr5mYDSKfgZztsf-TDo3LyXMEuOe8czouFcOWsLXWcCJS2Io1w; expires=Mon, 01-Jul-2019 07:00:25 GMT; path=/; domain=.google.com; HttpOnly'), ('Alt-Svc', 'quic=":443"; ma=2592000; v="44,43,39,35"'), ('Accept-Ranges', 'none'), ('Vary', 'Accept-Encoding'), ('Connection', 'close')]
>>> linkRequest.getheader("Content-Type)
			  
SyntaxError: EOL while scanning string literal
>>> linkRequest.getheader("Content-Type")
			  
'text/html; charset=ISO-8859-1'
>>> dir(linkRequest)
			  
['__abstractmethods__', '__class__', '__del__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_abc_impl', '_checkClosed', '_checkReadable', '_checkSeekable', '_checkWritable', '_check_close', '_close_conn', '_get_chunk_left', '_method', '_peek_chunked', '_read1_chunked', '_read_and_discard_trailer', '_read_next_chunk_size', '_read_status', '_readall_chunked', '_readinto_chunked', '_safe_read', '_safe_readinto', 'begin', 'chunk_left', 'chunked', 'close', 'closed', 'code', 'debuglevel', 'detach', 'fileno', 'flush', 'fp', 'getcode', 'getheader', 'getheaders', 'geturl', 'headers', 'info', 'isatty', 'isclosed', 'length', 'msg', 'peek', 'read', 'read1', 'readable', 'readinto', 'readinto1', 'readline', 'readlines', 'reason', 'seek', 'seekable', 'status', 'tell', 'truncate', 'url', 'version', 'will_close', 'writable', 'write', 'writelines']
>>> linkRequest.url
			  
'https://www.google.com'
>>> linkRequest.code
			  
200
>>> linkRequest.status
			  
200
>>> linkResponse = urllib.request.urlopen(link).read()
			  
>>> dir(linkResponse)
			  
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'center', 'count', 'decode', 'endswith', 'expandtabs', 'find', 'fromhex', 'hex', 'index', 'isalnum', 'isalpha', 'isascii', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> dir(urllib.request)
			  
['AbstractBasicAuthHandler', 'AbstractDigestAuthHandler', 'AbstractHTTPHandler', 'BaseHandler', 'CacheFTPHandler', 'ContentTooShortError', 'DataHandler', 'FTPHandler', 'FancyURLopener', 'FileHandler', 'HTTPBasicAuthHandler', 'HTTPCookieProcessor', 'HTTPDefaultErrorHandler', 'HTTPDigestAuthHandler', 'HTTPError', 'HTTPErrorProcessor', 'HTTPHandler', 'HTTPPasswordMgr', 'HTTPPasswordMgrWithDefaultRealm', 'HTTPPasswordMgrWithPriorAuth', 'HTTPRedirectHandler', 'HTTPSHandler', 'MAXFTPCACHE', 'OpenerDirector', 'ProxyBasicAuthHandler', 'ProxyDigestAuthHandler', 'ProxyHandler', 'Request', 'URLError', 'URLopener', 'UnknownHandler', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__', '_cut_port_re', '_ftperrors', '_have_ssl', '_localhost', '_noheaders', '_opener', '_parse_proxy', '_proxy_bypass_macosx_sysconf', '_randombytes', '_safe_gethostbyname', '_thishost', '_url_tempfiles', 'addclosehook', 'addinfourl', 'base64', 'bisect', 'build_opener', 'contextlib', 'email', 'ftpcache', 'ftperrors', 'ftpwrapper', 'getproxies', 'getproxies_environment', 'getproxies_registry', 'hashlib', 'http', 'install_opener', 'io', 'localhost', 'noheaders', 'os', 'parse_http_list', 'parse_keqv_list', 'pathname2url', 'posixpath', 'proxy_bypass', 'proxy_bypass_environment', 'proxy_bypass_registry', 'quote', 're', 'request_host', 'socket', 'splitattr', 'splithost', 'splitpasswd', 'splitport', 'splitquery', 'splittag', 'splittype', 'splituser', 'splitvalue', 'ssl', 'string', 'sys', 'tempfile', 'thishost', 'time', 'to_bytes', 'unquote', 'unquote_to_bytes', 'unwrap', 'url2pathname', 'urlcleanup', 'urljoin', 'urlopen', 'urlparse', 'urlretrieve', 'urlsplit', 'urlunparse', 'warnings']
>>> urllib.request.getproxies()
			  
{}
>>> urllib.request.getproxies_environment()
			  
{}
>>> urllib.request._tishost
			  
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    urllib.request._tishost
AttributeError: module 'urllib.request' has no attribute '_tishost'
>>> urllib.request._thishost
			  
>>> ['AbstractBasicAuthHandler', 'AbstractDigestAuthHandler', 'AbstractHTTPHandler', 'BaseHandler', 'CacheFTPHandler', 'ContentTooShortError', 'DataHandler', 'FTPHandler', 'FancyURLopener', 'FileHandler', 'HTTPBasicAuthHandler', 'HTTPCookieProcessor', 'HTTPDefaultErrorHandler', 'HTTPDigestAuthHandler', 'HTTPError', 'HTTPErrorProcessor', 'HTTPHandler', 'HTTPPasswordMgr', 'HTTPPasswordMgrWithDefaultRealm', 'HTTPPasswordMgrWithPriorAuth', 'HTTPRedirectHandler', 'HTTPSHandler', 'MAXFTPCACHE', 'OpenerDirector', 'ProxyBasicAuthHandler', 'ProxyDigestAuthHandler', 'ProxyHandler', 'Request', 'URLError', 'URLopener', 'UnknownHandler', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__', '_cut_port_re', '_ftperrors', '_have_ssl', '_localhost', '_noheaders', '_opener', '_parse_proxy', '_proxy_bypass_macosx_sysconf', '_randombytes', '_safe_gethostbyname', '_thishost', '_url_tempfiles', 'addclosehook', 'addinfourl', 'base64', 'bisect', 'build_opener', 'contextlib', 'email', 'ftpcache', 'ftperrors', 'ftpwrapper', 'getproxies', 'getproxies_environment', 'getproxies_registry', 'hashlib', 'http', 'install_opener', 'io', 'localhost', 'noheaders', 'os', 'parse_http_list', 'parse_keqv_list', 'pathname2url', 'posixpath', 'proxy_bypass', 'proxy_bypass_environment', 'proxy_bypass_registry', 'quote', 're', 'request_host', 'socket', 'splitattr', 'splithost', 'splitpasswd', 'splitport', 'splitquery', 'splittag', 'splittype', 'splituser', 'splitvalue', 'ssl', 'string', 'sys', 'tempfile', 'thishost', 'time', 'to_bytes', 'unquote', 'unquote_to_bytes', 'unwrap', 'url2pathname', 'urlcleanup', 'urljoin', 'urlopen', 'urlparse', 'urlretrieve', 'urlsplit', 'urlunparse', 'warnings']
			  
['AbstractBasicAuthHandler', 'AbstractDigestAuthHandler', 'AbstractHTTPHandler', 'BaseHandler', 'CacheFTPHandler', 'ContentTooShortError', 'DataHandler', 'FTPHandler', 'FancyURLopener', 'FileHandler', 'HTTPBasicAuthHandler', 'HTTPCookieProcessor', 'HTTPDefaultErrorHandler', 'HTTPDigestAuthHandler', 'HTTPError', 'HTTPErrorProcessor', 'HTTPHandler', 'HTTPPasswordMgr', 'HTTPPasswordMgrWithDefaultRealm', 'HTTPPasswordMgrWithPriorAuth', 'HTTPRedirectHandler', 'HTTPSHandler', 'MAXFTPCACHE', 'OpenerDirector', 'ProxyBasicAuthHandler', 'ProxyDigestAuthHandler', 'ProxyHandler', 'Request', 'URLError', 'URLopener', 'UnknownHandler', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__', '_cut_port_re', '_ftperrors', '_have_ssl', '_localhost', '_noheaders', '_opener', '_parse_proxy', '_proxy_bypass_macosx_sysconf', '_randombytes', '_safe_gethostbyname', '_thishost', '_url_tempfiles', 'addclosehook', 'addinfourl', 'base64', 'bisect', 'build_opener', 'contextlib', 'email', 'ftpcache', 'ftperrors', 'ftpwrapper', 'getproxies', 'getproxies_environment', 'getproxies_registry', 'hashlib', 'http', 'install_opener', 'io', 'localhost', 'noheaders', 'os', 'parse_http_list', 'parse_keqv_list', 'pathname2url', 'posixpath', 'proxy_bypass', 'proxy_bypass_environment', 'proxy_bypass_registry', 'quote', 're', 'request_host', 'socket', 'splitattr', 'splithost', 'splitpasswd', 'splitport', 'splitquery', 'splittag', 'splittype', 'splituser', 'splitvalue', 'ssl', 'string', 'sys', 'tempfile', 'thishost', 'time', 'to_bytes', 'unquote', 'unquote_to_bytes', 'unwrap', 'url2pathname', 'urlcleanup', 'urljoin', 'urlopen', 'urlparse', 'urlretrieve', 'urlsplit', 'urlunparse', 'warnings']
>>> urllib.request.thishost
			  
<function thishost at 0x009BCD68>
>>> urllib.request.thishost()
			  
('172.25.182.97', '192.168.99.1', '172.18.160.1', '192.168.1.3')
>>> help(urllib.request.thishost())
			  
Help on tuple object:

class tuple(object)
 |  tuple(iterable=(), /)
 |  
 |  Built-in immutable sequence.
 |  
 |  If no argument is given, the constructor returns an empty tuple.
 |  If iterable is specified the tuple is initialized from iterable's items.
 |  
 |  If the argument is a tuple, the return value is the same object.
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(self, key, /)
 |      Return self[key].
 |  
 |  __getnewargs__(self, /)
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  count(self, value, /)
 |      Return number of occurrences of value.
 |  
 |  index(self, value, start=0, stop=2147483647, /)
 |      Return first index of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.

>>> linkRequest = urllib.request.urlopen(link)
			  
>>> linkRequest.getheaders()
			  
[('Date', 'Sun, 30 Dec 2018 07:20:42 GMT'), ('Expires', '-1'), ('Cache-Control', 'private, max-age=0'), ('Content-Type', 'text/html; charset=ISO-8859-1'), ('P3P', 'CP="This is not a P3P policy! See g.co/p3phelp for more info."'), ('Server', 'gws'), ('X-XSS-Protection', '1; mode=block'), ('X-Frame-Options', 'SAMEORIGIN'), ('Set-Cookie', '1P_JAR=2018-12-30-07; expires=Tue, 29-Jan-2019 07:20:42 GMT; path=/; domain=.google.com'), ('Set-Cookie', 'NID=152=c_vwIX0GiJ2xmQyBBJ429uUzmaeoj5WHKUkfVr96uyQK8qmBeR7Qdao_WoIHUh89t-EsQWHpLUQgIg_38EJp8AePN8jAyVBkeDfs2swiZ0s1EYNAHLp4Ho-xl2awX-DTsnNKp6F1FqHt_OLL-kkS3sOz6185UdztMGAHkXK1I-M; expires=Mon, 01-Jul-2019 07:20:42 GMT; path=/; domain=.google.com; HttpOnly'), ('Alt-Svc', 'quic=":443"; ma=2592000; v="44,43,39,35"'), ('Accept-Ranges', 'none'), ('Vary', 'Accept-Encoding'), ('Connection', 'close')]
>>> linkRequest
			  
<http.client.HTTPResponse object at 0x00F08ED0>
>>> linkRequest.getproxies()
			  
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    linkRequest.getproxies()
AttributeError: 'HTTPResponse' object has no attribute 'getproxies'
>>> help(urllib.request.pathname2url)
			  
Help on function pathname2url in module nturl2path:

pathname2url(p)
    OS-specific conversion from a file system path to a relative URL
    of the 'file' scheme; not recommended for general use.

>>> url = urllib.request
			  
>>> path="C:\\Docs\Tests"
			  
>>> url.pathname2url(path)
			  
'///C:/Docs/Tests'
>>> path="C:\\Users\\joey\\Desktop\\school\\ICOMMH"
			  
>>> url.pathname2url(path)
			  
'///C:/Users/joey/Desktop/school/ICOMMH'
>>> link
			  
'https://www.google.com'
>>> url.url2pathname(path)
			  
'C:\\\\Users\\joey\\Desktop\\school\\ICOMMH'
>>> url.url2pathname(link)
			  
'S:\\www.google.com'
>>> dir(urls)
			  
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    dir(urls)
NameError: name 'urls' is not defined
>>> dir(url)
			  
['AbstractBasicAuthHandler', 'AbstractDigestAuthHandler', 'AbstractHTTPHandler', 'BaseHandler', 'CacheFTPHandler', 'ContentTooShortError', 'DataHandler', 'FTPHandler', 'FancyURLopener', 'FileHandler', 'HTTPBasicAuthHandler', 'HTTPCookieProcessor', 'HTTPDefaultErrorHandler', 'HTTPDigestAuthHandler', 'HTTPError', 'HTTPErrorProcessor', 'HTTPHandler', 'HTTPPasswordMgr', 'HTTPPasswordMgrWithDefaultRealm', 'HTTPPasswordMgrWithPriorAuth', 'HTTPRedirectHandler', 'HTTPSHandler', 'MAXFTPCACHE', 'OpenerDirector', 'ProxyBasicAuthHandler', 'ProxyDigestAuthHandler', 'ProxyHandler', 'Request', 'URLError', 'URLopener', 'UnknownHandler', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__', '_cut_port_re', '_ftperrors', '_have_ssl', '_localhost', '_noheaders', '_opener', '_parse_proxy', '_proxy_bypass_macosx_sysconf', '_randombytes', '_safe_gethostbyname', '_thishost', '_url_tempfiles', 'addclosehook', 'addinfourl', 'base64', 'bisect', 'build_opener', 'contextlib', 'email', 'ftpcache', 'ftperrors', 'ftpwrapper', 'getproxies', 'getproxies_environment', 'getproxies_registry', 'hashlib', 'http', 'install_opener', 'io', 'localhost', 'noheaders', 'os', 'parse_http_list', 'parse_keqv_list', 'pathname2url', 'posixpath', 'proxy_bypass', 'proxy_bypass_environment', 'proxy_bypass_registry', 'quote', 're', 'request_host', 'socket', 'splitattr', 'splithost', 'splitpasswd', 'splitport', 'splitquery', 'splittag', 'splittype', 'splituser', 'splitvalue', 'ssl', 'string', 'sys', 'tempfile', 'thishost', 'time', 'to_bytes', 'unquote', 'unquote_to_bytes', 'unwrap', 'url2pathname', 'urlcleanup', 'urljoin', 'urlopen', 'urlparse', 'urlretrieve', 'urlsplit', 'urlunparse', 'warnings']
>>> help9url.urljoin)
SyntaxError: invalid syntax
>>> help(url.urljoin)
Help on function urljoin in module urllib.parse:

urljoin(base, url, allow_fragments=True)
    Join a base URL and a possibly relative URL to form an absolute
    interpretation of the latter.

>>> 
>>> link="https://www.samsclub.com/sitemap.xml"
>>> import requests
>>> content = requests.get(link).text
>>> content
'<?xml version="1.0" encoding="UTF-8"?>\n<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n<sitemap><loc>https://www.samsclub.com/sitemap_categories.xml</loc></sitemap>\n<sitemap><loc>https://www.samsclub.com/sitemap_products_1.xml</loc></sitemap>\n<sitemap><loc>https://www.samsclub.com/sitemap_products_2.xml</loc></sitemap>\n<sitemap><loc>https://www.samsclub.com/sitemap_locators.xml</loc></sitemap>\n</sitemapindex>'
>>> content.decode()
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    content.decode()
AttributeError: 'str' object has no attribute 'decode'
>>> content = requests.get(link).content
>>> content.decode()
'<?xml version="1.0" encoding="UTF-8"?>\n<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n<sitemap><loc>https://www.samsclub.com/sitemap_categories.xml</loc></sitemap>\n<sitemap><loc>https://www.samsclub.com/sitemap_products_1.xml</loc></sitemap>\n<sitemap><loc>https://www.samsclub.com/sitemap_products_2.xml</loc></sitemap>\n<sitemap><loc>https://www.samsclub.com/sitemap_locators.xml</loc></sitemap>\n</sitemapindex>'
>>> urlparse = urllib.parse
>>> dir(urlparse)
['DefragResult', 'DefragResultBytes', 'MAX_CACHE_SIZE', 'ParseResult', 'ParseResultBytes', 'Quoter', 'ResultBase', 'SplitResult', 'SplitResultBytes', '_ALWAYS_SAFE', '_ALWAYS_SAFE_BYTES', '_DefragResultBase', '_NetlocResultMixinBase', '_NetlocResultMixinBytes', '_NetlocResultMixinStr', '_ParseResultBase', '_ResultMixinBytes', '_ResultMixinStr', '_SplitResultBase', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_asciire', '_coerce_args', '_decode_args', '_encode_result', '_hexdig', '_hextobyte', '_hostprog', '_implicit_encoding', '_implicit_errors', '_noop', '_parse_cache', '_portprog', '_safe_quoters', '_splitnetloc', '_splitparams', '_typeprog', 'clear_cache', 'collections', 'namedtuple', 'non_hierarchical', 'parse_qs', 'parse_qsl', 'quote', 'quote_from_bytes', 'quote_plus', 're', 'scheme_chars', 'splitattr', 'splithost', 'splitnport', 'splitpasswd', 'splitport', 'splitquery', 'splittag', 'splittype', 'splituser', 'splitvalue', 'sys', 'to_bytes', 'unquote', 'unquote_plus', 'unquote_to_bytes', 'unwrap', 'urldefrag', 'urlencode', 'urljoin', 'urlparse', 'urlsplit', 'urlunparse', 'urlunsplit', 'uses_fragment', 'uses_netloc', 'uses_params', 'uses_query', 'uses_relative']
>>> link1 = 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Dstripbooks-intl-ship&field-keywords=Packt+Books'
>>> urlparse.uses_query(link1)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    urlparse.uses_query(link1)
TypeError: 'list' object is not callable
>>> urlparse.urlparse
<function urlparse at 0x03815468>
>>> urlparse.urlparse()
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    urlparse.urlparse()
TypeError: urlparse() missing 1 required positional argument: 'url'
>>> urlparse.urlparse(link1)
ParseResult(scheme='https', netloc='www.amazon.com', path='/s/ref=nb_sb_noss', params='', query='url=search-alias%3Dstripbooks-intl-ship&field-keywords=Packt+Books', fragment='')
>>> urlparse.splitattr(link1)
('https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Dstripbooks-intl-ship&field-keywords=Packt+Books', [])
>>> urlparse.splithost(link1)
(None, 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Dstripbooks-intl-ship&field-keywords=Packt+Books')
>>> urlparse.splithost(link)
(None, 'https://www.samsclub.com/sitemap.xml')
>>> urlparse.urlsplit(link)
SplitResult(scheme='https', netloc='www.samsclub.com', path='/sitemap.xml', query='', fragment='')
>>> urlparse.urlparse(link)
ParseResult(scheme='https', netloc='www.samsclub.com', path='/sitemap.xml', params='', query='', fragment='')
>>> content.decode('utf-8')
'<?xml version="1.0" encoding="UTF-8"?>\n<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n<sitemap><loc>https://www.samsclub.com/sitemap_categories.xml</loc></sitemap>\n<sitemap><loc>https://www.samsclub.com/sitemap_products_1.xml</loc></sitemap>\n<sitemap><loc>https://www.samsclub.com/sitemap_products_2.xml</loc></sitemap>\n<sitemap><loc>https://www.samsclub.com/sitemap_locators.xml</loc></sitemap>\n</sitemapindex>'
>>> dir(urllib)
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'error', 'parse', 'request', 'response']
>>> dir(urlparse)
['DefragResult', 'DefragResultBytes', 'MAX_CACHE_SIZE', 'ParseResult', 'ParseResultBytes', 'Quoter', 'ResultBase', 'SplitResult', 'SplitResultBytes', '_ALWAYS_SAFE', '_ALWAYS_SAFE_BYTES', '_DefragResultBase', '_NetlocResultMixinBase', '_NetlocResultMixinBytes', '_NetlocResultMixinStr', '_ParseResultBase', '_ResultMixinBytes', '_ResultMixinStr', '_SplitResultBase', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_asciire', '_coerce_args', '_decode_args', '_encode_result', '_hexdig', '_hextobyte', '_hostprog', '_implicit_encoding', '_implicit_errors', '_noop', '_parse_cache', '_portprog', '_safe_quoters', '_splitnetloc', '_splitparams', '_typeprog', 'clear_cache', 'collections', 'namedtuple', 'non_hierarchical', 'parse_qs', 'parse_qsl', 'quote', 'quote_from_bytes', 'quote_plus', 're', 'scheme_chars', 'splitattr', 'splithost', 'splitnport', 'splitpasswd', 'splitport', 'splitquery', 'splittag', 'splittype', 'splituser', 'splitvalue', 'sys', 'to_bytes', 'unquote', 'unquote_plus', 'unquote_to_bytes', 'unwrap', 'urldefrag', 'urlencode', 'urljoin', 'urlparse', 'urlsplit', 'urlunparse', 'urlunsplit', 'uses_fragment', 'uses_netloc', 'uses_params', 'uses_query', 'uses_relative']
>>> type(linkRequest)
<class 'http.client.HTTPResponse'>
>>> type(linkResponse)
<class 'bytes'>
>>> type(requestObj)
<class 'urllib.request.Request'>
>>> type(requestObjResponse)
<class 'bytes'>
>>> help(linkRequest.urlretrive)
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    help(linkRequest.urlretrive)
AttributeError: 'HTTPResponse' object has no attribute 'urlretrive'
>>> help(linkRequest.urlretrieve)
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    help(linkRequest.urlretrieve)
AttributeError: 'HTTPResponse' object has no attribute 'urlretrieve'
>>> dir(linkRequest)
['__abstractmethods__', '__class__', '__del__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_abc_impl', '_checkClosed', '_checkReadable', '_checkSeekable', '_checkWritable', '_check_close', '_close_conn', '_get_chunk_left', '_method', '_peek_chunked', '_read1_chunked', '_read_and_discard_trailer', '_read_next_chunk_size', '_read_status', '_readall_chunked', '_readinto_chunked', '_safe_read', '_safe_readinto', 'begin', 'chunk_left', 'chunked', 'close', 'closed', 'code', 'debuglevel', 'detach', 'fileno', 'flush', 'fp', 'getcode', 'getheader', 'getheaders', 'geturl', 'headers', 'info', 'isatty', 'isclosed', 'length', 'msg', 'peek', 'read', 'read1', 'readable', 'readinto', 'readinto1', 'readline', 'readlines', 'reason', 'seek', 'seekable', 'status', 'tell', 'truncate', 'url', 'version', 'will_close', 'writable', 'write', 'writelines']
>>> link1
'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Dstripbooks-intl-ship&field-keywords=Packt+Books'
>>> dir(urlparse)
['DefragResult', 'DefragResultBytes', 'MAX_CACHE_SIZE', 'ParseResult', 'ParseResultBytes', 'Quoter', 'ResultBase', 'SplitResult', 'SplitResultBytes', '_ALWAYS_SAFE', '_ALWAYS_SAFE_BYTES', '_DefragResultBase', '_NetlocResultMixinBase', '_NetlocResultMixinBytes', '_NetlocResultMixinStr', '_ParseResultBase', '_ResultMixinBytes', '_ResultMixinStr', '_SplitResultBase', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_asciire', '_coerce_args', '_decode_args', '_encode_result', '_hexdig', '_hextobyte', '_hostprog', '_implicit_encoding', '_implicit_errors', '_noop', '_parse_cache', '_portprog', '_safe_quoters', '_splitnetloc', '_splitparams', '_typeprog', 'clear_cache', 'collections', 'namedtuple', 'non_hierarchical', 'parse_qs', 'parse_qsl', 'quote', 'quote_from_bytes', 'quote_plus', 're', 'scheme_chars', 'splitattr', 'splithost', 'splitnport', 'splitpasswd', 'splitport', 'splitquery', 'splittag', 'splittype', 'splituser', 'splitvalue', 'sys', 'to_bytes', 'unquote', 'unquote_plus', 'unquote_to_bytes', 'unwrap', 'urldefrag', 'urlencode', 'urljoin', 'urlparse', 'urlsplit', 'urlunparse', 'urlunsplit', 'uses_fragment', 'uses_netloc', 'uses_params', 'uses_query', 'uses_relative']
>>> amazonUrl = link1
>>> amazonUrl
'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Dstripbooks-intl-ship&field-keywords=Packt+Books'
>>> print(urlparse.urlsplit(amazonUrl))
SplitResult(scheme='https', netloc='www.amazon.com', path='/s/ref=nb_sb_noss', query='url=search-alias%3Dstripbooks-intl-ship&field-keywords=Packt+Books', fragment='')
>>> print(urlparse.urlparse(amazonUrl))
ParseResult(scheme='https', netloc='www.amazon.com', path='/s/ref=nb_sb_noss', params='', query='url=search-alias%3Dstripbooks-intl-ship&field-keywords=Packt+Books', fragment='')
>>> walmartUrl="https://www.walmart.com/browse/dolls-dollhouses/barbie/4171_4187_1953337/?page=2&cat_id=4171_4187_1953337"
>>> print(urlparse.urlsplit(walmartUrl))
SplitResult(scheme='https', netloc='www.walmart.com', path='/browse/dolls-dollhouses/barbie/4171_4187_1953337/', query='page=2&cat_id=4171_4187_1953337', fragment='')
>>> print(urlparse.urlparse(walmartUrl))
ParseResult(scheme='https', netloc='www.walmart.com', path='/browse/dolls-dollhouses/barbie/4171_4187_1953337/', params='', query='page=2&cat_id=4171_4187_1953337', fragment='')
>>> walmart = urlparse.urlsplit(walmartUrl)
>>> walmart
SplitResult(scheme='https', netloc='www.walmart.com', path='/browse/dolls-dollhouses/barbie/4171_4187_1953337/', query='page=2&cat_id=4171_4187_1953337', fragment='')
>>> walmart.scheme
'https'
>>> walmart.path
'/browse/dolls-dollhouses/barbie/4171_4187_1953337/'
>>> walmart.query
'page=2&cat_id=4171_4187_1953337'
>>> puurl="http://docs.pyspider.org/en/latest/tutorial/HTML-and-CSS-Selector/"
>>> pyurl="http://docs.pyspider.org/en/latest/tutorial/HTML-and-CSS-Selector/"
>>> print(urlparse.urlsplit(pyurl))
SplitResult(scheme='http', netloc='docs.pyspider.org', path='/en/latest/tutorial/HTML-and-CSS-Selector/', query='', fragment='')
>>> print(urlparse.urlparse(pyurl))
ParseResult(scheme='http', netloc='docs.pyspider.org', path='/en/latest/tutorial/HTML-and-CSS-Selector/', params='', query='', fragment='')
>>> walmart.query
'page=2&cat_id=4171_4187_1953337'
>>> page="page="
>>> url="https://www.sitename.com"
>>> urlparse.urljoin(page,url)
'https://www.sitename.com'
>>> url2 = 'http://localhost/books;2018?browse=yes&sort=ASC'
>>> print(urlparse.urlsplit(urls2))
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    print(urlparse.urlsplit(urls2))
NameError: name 'urls2' is not defined
>>> print(urlparse.urlsplit(url2))
SplitResult(scheme='http', netloc='localhost', path='/books;2018', query='browse=yes&sort=ASC', fragment='')
>>> print(urlparse.urlparse(url2))
ParseResult(scheme='http', netloc='localhost', path='/books', params='2018', query='browse=yes&sort=ASC', fragment='')
>>> url2 = 'http://localhost/books;2018?browse=yes&sort=ASC#scroll'
>>> print(urlparse.urlsplit(url2))
SplitResult(scheme='http', netloc='localhost', path='/books;2018', query='browse=yes&sort=ASC', fragment='scroll')
>>> url2 = 'http://localhost/books;2018?browse=yes&sort=ASC#scroll'
>>> print(urlparse.urlsplit(url2))
SplitResult(scheme='http', netloc='localhost', path='/books;2018', query='browse=yes&sort=ASC', fragment='scroll')
>>> url2 = 'http://localhost/programming/books;2018?browse=yes&sort=ASC#scroll'
>>> print(urlparse.urlsplit(url2))
SplitResult(scheme='http', netloc='localhost', path='/programming/books;2018', query='browse=yes&sort=ASC', fragment='scroll')
>>> print(urlparse.urlparse(url2))
ParseResult(scheme='http', netloc='localhost', path='/programming/books', params='2018', query='browse=yes&sort=ASC', fragment='scroll')
>>> urlparse.urljoin('https','www.google.com')
'www.google.com'
>>> help(urlparse.urljoin)
Help on function urljoin in module urllib.parse:

urljoin(base, url, allow_fragments=True)
    Join a base URL and a possibly relative URL to form an absolute
    interpretation of the latter.

>>> urlparse.urljoin('https//www.google.com','search?q=web scraping')
'https/search?q=web scraping'
>>> urlparse.urljoin('www.google.com','search?q=web scraping')
'search?q=web scraping'
>>> urlparse.urljoin('https://www.google.com/','search?q=web scraping')
'https://www.google.com/search?q=web scraping'
>>> print(urlparse.urlsplit('https://www.google.com/search?q=web scraping'))
SplitResult(scheme='https', netloc='www.google.com', path='/search', query='q=web scraping', fragment='')
>>> print(urlparse.urlparse('https://www.google.com/search?q=web scraping'))
ParseResult(scheme='https', netloc='www.google.com', path='/search', params='', query='q=web scraping', fragment='')
>>> us = urlparse.urlsplit('https://www.google.com/search?q=web scraping')
>>> urlparse.urljoin("https://www.google.com",us.path+'?'+us.query)
'https://www.google.com/search?q=web scraping'
>>> urlparse.urljoin("https://www.google.com",us.path+'?'+urlparse.urlenode(us.query))
Traceback (most recent call last):
  File "<pyshell#137>", line 1, in <module>
    urlparse.urljoin("https://www.google.com",us.path+'?'+urlparse.urlenode(us.query))
AttributeError: module 'urllib.parse' has no attribute 'urlenode'
>>> urlparse.urljoin("https://www.google.com",us.path+'?'+urlparse.urlencode(us.query))
Traceback (most recent call last):
  File "C:\Python37\lib\urllib\parse.py", line 858, in urlencode
    raise TypeError
TypeError

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#138>", line 1, in <module>
    urlparse.urljoin("https://www.google.com",us.path+'?'+urlparse.urlencode(us.query))
  File "C:\Python37\lib\urllib\parse.py", line 866, in urlencode
    "or mapping object").with_traceback(tb)
  File "C:\Python37\lib\urllib\parse.py", line 858, in urlencode
    raise TypeError
TypeError: not a valid non-string sequence or mapping object
>>> urlparse.urljoin("https://www.google.com",us.path+'?'+urlparse.urlencode(str(us.query)))
Traceback (most recent call last):
  File "C:\Python37\lib\urllib\parse.py", line 858, in urlencode
    raise TypeError
TypeError

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#139>", line 1, in <module>
    urlparse.urljoin("https://www.google.com",us.path+'?'+urlparse.urlencode(str(us.query)))
  File "C:\Python37\lib\urllib\parse.py", line 866, in urlencode
    "or mapping object").with_traceback(tb)
  File "C:\Python37\lib\urllib\parse.py", line 858, in urlencode
    raise TypeError
TypeError: not a valid non-string sequence or mapping object
>>> data={'param1':'value1','param2':'value2'}
>>> urlparse.urlencode(data)
'param1=value1&param2=value2'
>>> us = urlparse.urlsplit('https://www.google.com/search?q=web scraping')
>>> us
SplitResult(scheme='https', netloc='www.google.com', path='/search', query='q=web scraping', fragment='')
>>> us.query
'q=web scraping'
>>> print(urlparse.urlsplit('https://www.google.com/search?q=web scraping').query)
q=web scraping
>>> url2 = 'http://localhost/programming/books;2018?browse=yes&sort=ASC#footer'
>>> print(urlparse.urlsplit(url2))
SplitResult(scheme='http', netloc='localhost', path='/programming/books;2018', query='browse=yes&sort=ASC', fragment='footer')
>>> localSplit = urlparse.urlsplit(url2)
>>> localSplit.fragment
'footer'
>>> localSplit.fragment=uper
Traceback (most recent call last):
  File "<pyshell#150>", line 1, in <module>
    localSplit.fragment=uper
NameError: name 'uper' is not defined
>>> localSplit.fragment=upper
Traceback (most recent call last):
  File "<pyshell#151>", line 1, in <module>
    localSplit.fragment=upper
NameError: name 'upper' is not defined
>>> localSplit.fragment='upper'
Traceback (most recent call last):
  File "<pyshell#152>", line 1, in <module>
    localSplit.fragment='upper'
AttributeError: can't set attribute
>>> localSplit['fragment']
Traceback (most recent call last):
  File "<pyshell#153>", line 1, in <module>
    localSplit['fragment']
TypeError: tuple indices must be integers or slices, not str
>>> localSplit[fragment]
Traceback (most recent call last):
  File "<pyshell#154>", line 1, in <module>
    localSplit[fragment]
NameError: name 'fragment' is not defined
>>> localSplit.fragment
'footer'
>>> url2 = 'http://localhost:80/programming/books;2018?browse=yes&sort=ASC#footer'
>>> print(urlparse.urlsplit(url2))
SplitResult(scheme='http', netloc='localhost:80', path='/programming/books;2018', query='browse=yes&sort=ASC', fragment='footer')
>>> localSplit.path
'/programming/books;2018'
>>> data={'param1':'value1','param2':'value2'}
>>> data.urlencode()
Traceback (most recent call last):
  File "<pyshell#160>", line 1, in <module>
    data.urlencode()
AttributeError: 'dict' object has no attribute 'urlencode'
>>> data
{'param1': 'value1', 'param2': 'value2'}
>>> urlparse.urlencode(data)
'param1=value1&param2=value2'
>>> urlparse.parse_qs(urlparse.urlencode(data))
{'param1': ['value1'], 'param2': ['value2']}
>>> urlparse.parse_qsl(urlparse.urlencode(data))
[('param1', 'value1'), ('param2', 'value2')]
>>> local = "http://localhost:8080/~cache/data"
>>> urlparse.quote(local)
'http%3A//localhost%3A8080/~cache/data'
>>> urlparse.quote_plus(local)
'http%3A%2F%2Flocalhost%3A8080%2F~cache%2Fdata'
>>> localfile = "http://localhost:8080/~cache/data file"
>>> urlparse.quote(localfile)
'http%3A//localhost%3A8080/~cache/data%20file'
>>> urlparse.quote_plus(localfile)
'http%3A%2F%2Flocalhost%3A8080%2F~cache%2Fdata+file'
>>> urlparse.unquote_plus(localfile)
'http://localhost:8080/~cache/data file'
>>> help(urlparse.parse_qs)
Help on function parse_qs in module urllib.parse:

parse_qs(qs, keep_blank_values=False, strict_parsing=False, encoding='utf-8', errors='replace')
    Parse a query given as a string argument.
    
    Arguments:
    
    qs: percent-encoded query string to be parsed
    
    keep_blank_values: flag indicating whether blank values in
        percent-encoded queries should be treated as blank strings.
        A true value indicates that blanks should be retained as
        blank strings.  The default false value indicates that
        blank values are to be ignored and treated as if they were
        not included.
    
    strict_parsing: flag indicating what to do with parsing errors.
        If false (the default), errors are silently ignored.
        If true, errors raise a ValueError exception.
    
    encoding and errors: specify how to decode percent-encoded sequences
        into Unicode characters, as accepted by the bytes.decode() method.
    
    Returns a dictionary.

>>> help(urlparse.parse_qs)
Help on function parse_qs in module urllib.parse:

parse_qs(qs, keep_blank_values=False, strict_parsing=False, encoding='utf-8', errors='replace')
    Parse a query given as a string argument.
    
    Arguments:
    
    qs: percent-encoded query string to be parsed
    
    keep_blank_values: flag indicating whether blank values in
        percent-encoded queries should be treated as blank strings.
        A true value indicates that blanks should be retained as
        blank strings.  The default false value indicates that
        blank values are to be ignored and treated as if they were
        not included.
    
    strict_parsing: flag indicating what to do with parsing errors.
        If false (the default), errors are silently ignored.
        If true, errors raise a ValueError exception.
    
    encoding and errors: specify how to decode percent-encoded sequences
        into Unicode characters, as accepted by the bytes.decode() method.
    
    Returns a dictionary.

>>> help(urlparse.parse_qss)
Traceback (most recent call last):
  File "<pyshell#174>", line 1, in <module>
    help(urlparse.parse_qss)
AttributeError: module 'urllib.parse' has no attribute 'parse_qss'
>>> help(urlparse.parse_qsl)
Help on function parse_qsl in module urllib.parse:

parse_qsl(qs, keep_blank_values=False, strict_parsing=False, encoding='utf-8', errors='replace')
    Parse a query given as a string argument.
    
    Arguments:
    
    qs: percent-encoded query string to be parsed
    
    keep_blank_values: flag indicating whether blank values in
        percent-encoded queries should be treated as blank strings.
        A true value indicates that blanks should be retained as blank
        strings.  The default false value indicates that blank values
        are to be ignored and treated as if they were  not included.
    
    strict_parsing: flag indicating what to do with parsing errors. If
        false (the default), errors are silently ignored. If true,
        errors raise a ValueError exception.
    
    encoding and errors: specify how to decode percent-encoded sequences
        into Unicode characters, as accepted by the bytes.decode() method.
    
    Returns a list, as G-d intended.

>>> localfile = "http://localhost:8080/~cache/data file?display=yes&expiry=false"
>>> localfile = "http://localhost:8080/~cache/data file?id=1345322&display=yes&expiry=false"
>>> urlparse.quote(localfile)
'http%3A//localhost%3A8080/~cache/data%20file%3Fid%3D1345322%26display%3Dyes%26expiry%3Dfalse'
>>> urlparse.quote_plus(localfile)
'http%3A%2F%2Flocalhost%3A8080%2F~cache%2Fdata+file%3Fid%3D1345322%26display%3Dyes%26expiry%3Dfalse'
>>> urlparse.unquote_plus(localfile)
'http://localhost:8080/~cache/data file?id=1345322&display=yes&expiry=false'
>>> help(urlparse.quote)
Help on function quote in module urllib.parse:

quote(string, safe='/', encoding=None, errors=None)
    quote('abc def') -> 'abc%20def'
    
    Each part of a URL, e.g. the path info, the query, etc., has a
    different set of reserved characters that must be quoted.
    
    RFC 3986 Uniform Resource Identifiers (URI): Generic Syntax lists
    the following reserved characters.
    
    reserved    = ";" | "/" | "?" | ":" | "@" | "&" | "=" | "+" |
                  "$" | "," | "~"
    
    Each of these characters is reserved in some component of a URL,
    but not necessarily in all of them.
    
    Python 3.7 updates from using RFC 2396 to RFC 3986 to quote URL strings.
    Now, "~" is included in the set of reserved characters.
    
    By default, the quote function is intended for quoting the path
    section of a URL.  Thus, it will not encode '/'.  This character
    is reserved, but in typical usage the quote function is being
    called on a path where the existing slash characters are used as
    reserved characters.
    
    string and safe may be either str or bytes objects. encoding and errors
    must not be specified if string is a bytes object.
    
    The optional encoding and errors parameters specify how to deal with
    non-ASCII characters, as accepted by the str.encode method.
    By default, encoding='utf-8' (characters are encoded with UTF-8), and
    errors='strict' (unsupported characters raise a UnicodeEncodeError).

>>> help(urlparse.quote_plus)
Help on function quote_plus in module urllib.parse:

quote_plus(string, safe='', encoding=None, errors=None)
    Like quote(), but also replace ' ' with '+', as required for quoting
    HTML form values. Plus signs in the original string are escaped unless
    they are included in safe. It also does not have safe default to '/'.

>>> help(urlparse.unquote_plus)
Help on function unquote_plus in module urllib.parse:

unquote_plus(string, encoding='utf-8', errors='replace')
    Like unquote(), but also replace plus signs by spaces, as required for
    unquoting HTML form values.
    
    unquote_plus('%7e/abc+def') -> '~/abc def'

>>> help(urlparse.unquote)
Help on function unquote in module urllib.parse:

unquote(string, encoding='utf-8', errors='replace')
    Replace %xx escapes by their single-character equivalent. The optional
    encoding and errors parameters specify how to decode percent-encoded
    sequences into Unicode characters, as accepted by the bytes.decode()
    method.
    By default, percent-encoded sequences are decoded with UTF-8, and invalid
    sequences are replaced by a placeholder character.
    
    unquote('abc%20def') -> 'abc def'.

>>> urlparse.unquote(localfile)
'http://localhost:8080/~cache/data file?id=1345322&display=yes&expiry=false'
>>> urlparse.unquote_plus(localfile)
'http://localhost:8080/~cache/data file?id=1345322&display=yes&expiry=false'
>>> localfile = "http://localhost:8080/~cache/data file?id=1345322&display=yes&expiry=false"
>>> urlparse.urljoin('http://localhost:8080/~cache/data file','id=1345322&display=yes')
'http://localhost:8080/~cache/id=1345322&display=yes'
>>> urlparse.urljoin('http://localhost:8080/~cache/data file/','id=1345322&display=yes')
'http://localhost:8080/~cache/data file/id=1345322&display=yes'
>>> help(urlparse.urljoin)
Help on function urljoin in module urllib.parse:

urljoin(base, url, allow_fragments=True)
    Join a base URL and a possibly relative URL to form an absolute
    interpretation of the latter.

>>> urlparse.urljoin('http://localhost:8080/~cache/data file/','id=1345322&display=yes',true)
Traceback (most recent call last):
  File "<pyshell#191>", line 1, in <module>
    urlparse.urljoin('http://localhost:8080/~cache/data file/','id=1345322&display=yes',true)
NameError: name 'true' is not defined
>>> urlparse.urljoin('http://localhost:8080/~cache/data file/','id=1345322&display=yes','#footer')
'http://localhost:8080/~cache/data file/id=1345322&display=yes'
>>> urlparse.urljoin('http://localhost:8080/~cache/data file/','id=1345322&display=yes','#footer')
'http://localhost:8080/~cache/data file/id=1345322&display=yes'
>>> import httplib2
Traceback (most recent call last):
  File "<pyshell#194>", line 1, in <module>
    import httplib2
ModuleNotFoundError: No module named 'httplib2'
>>> linkResponse
b'<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="ne"><head><meta content="text/html; charset=UTF-8" http-equiv="Content-Type"><meta content="/images/branding/googleg/1x/googleg_standard_color_128dp.png" itemprop="image"><title>Google</title><script nonce="+qjUq5XdVZcU6gnMDG3k7Q==">(function(){window.google={kEI:\'tW0oXJDUMcvlvASGppKQDA\',kEXPI:\'0,18168,1335578,58,1958,1016,1406,698,527,731,325,293,1180,30,524,28,631,45,805,95,235,305,6,2335609,238,32,68,329226,1294,12383,4855,32692,15247,867,12163,16521,363,3320,1263,4242,1111,130,1201,260,5107,575,835,284,2,579,727,2432,1361,1740,2583,3390,8,1569,774,2115,136,2848,1500,395,525,626,2,1965,528,2067,182,283,3136,669,535,515,464,1344,386,743,268,81,7,28,463,620,29,1853,3204,644,4289,314,876,412,2,554,33,2601,381,286,310,638,12,1208,38,363,557,573,145,155,499,718,1364,484,47,884,196,2369,323,44,790,9,2,258,499,764,432,10,300,2,363,265,217,942,279,824,141,159,2,676,44,18,31,168,117,38,106,538,740,23,408,252,97,249,247,1158,369,716,8,22,478,758,849,632,447,17,87,302,244,317,6,38,331,135,1,420,105,245,188,19,574,2,83,340,1445,132,157,144,5970775,2554,95,27,101,22,5997356,90,2800095,4,1572,549,332,445,1,2,80,1,506,394,580,12,304,1,8,1,2,2132,1,1,1,1,1,414,1,748,141,59,353,373,3,7,362,81,3,6,71,1,9,9,2,1,18,1,2,4,1,1,2,1,1,100,1,29,8,21,2,1,1,1,1,1,1,1,1,1,1,1,4,26,1,1,3,1,2,1,1,1,1,1,1,68,8,6,2,2,2,1,1,1,3,1,2,30,12,6,4,2,2,2,2,4,12,4,3\',authuser:0,kscs:\'c9c918f0_tW0oXJDUMcvlvASGppKQDA\',kGL:\'NP\'};google.kHL=\'ne\';})();google.time=function(){return(new Date).getTime()};(function(){google.lc=[];google.li=0;google.getEI=function(a){for(var b;a&&(!a.getAttribute||!(b=a.getAttribute("eid")));)a=a.parentNode;return b||google.kEI};google.getLEI=function(a){for(var b=null;a&&(!a.getAttribute||!(b=a.getAttribute("leid")));)a=a.parentNode;return b};google.https=function(){return"https:"==window.location.protocol};google.ml=function(){return null};google.log=function(a,b,e,c,g){if(a=google.logUrl(a,b,e,c,g)){b=new Image;var d=google.lc,f=google.li;d[f]=b;b.onerror=b.onload=b.onabort=function(){delete d[f]};google.vel&&google.vel.lu&&google.vel.lu(a);b.src=a;google.li=f+1}};google.logUrl=function(a,b,e,c,g){var d="",f=google.ls||"";e||-1!=b.search("&ei=")||(d="&ei="+google.getEI(c),-1==b.search("&lei=")&&(c=google.getLEI(c))&&(d+="&lei="+c));c="";!e&&google.cshid&&-1==b.search("&cshid=")&&"slh"!=a&&(c="&cshid="+google.cshid);a=e||"/"+(g||"gen_204")+"?atyp=i&ct="+a+"&cad="+b+d+f+"&zx="+google.time()+c;/^http:/i.test(a)&&google.https()&&(google.ml(Error("a"),!1,{src:a,glmm:1}),a="");return a};}).call(this);(function(){google.y={};google.x=function(a,b){if(a)var c=a.id;else{do c=Math.random();while(google.y[c])}google.y[c]=[a,b];return!1};google.lm=[];google.plm=function(a){google.lm.push.apply(google.lm,a)};google.lq=[];google.load=function(a,b,c){google.lq.push([[a],b,c])};google.loadAll=function(a,b){google.lq.push([a,b])};}).call(this);google.f={};</script><script nonce="+qjUq5XdVZcU6gnMDG3k7Q==">var a=window.location,b=a.href.indexOf("#");if(0<=b){var c=a.href.substring(b+1);/(^|&)q=/.test(c)&&-1==c.indexOf("#")&&a.replace("/search?"+c.replace(/(^|&)fp=[^&]*/g,"")+"&cad=h")};</script><style>#gbar,#guser{font-size:13px;padding-top:1px !important;}#gbar{height:22px}#guser{padding-bottom:7px !important;text-align:right}.gbh,.gbd{border-top:1px solid #c9d7f1;font-size:1px}.gbh{height:0;position:absolute;top:24px;width:100%}@media all{.gb1{height:22px;margin-right:.5em;vertical-align:top}#gbar{float:left}}a.gb1,a.gb4{text-decoration:underline !important}a.gb1,a.gb4{color:#00c !important}.gbi .gb4{color:#dd8e27 !important}.gbf .gb4{color:#900 !important}\n</style><style>body,td,a,p,.h{font-family:arial,sans-serif}body{margin:0;overflow-y:scroll}#gog{padding:3px 8px 0}td{line-height:.8em}.gac_m td{line-height:17px}form{margin-bottom:20px}.h{color:#36c}.q{color:#00c}.ts td{padding:0}.ts{border-collapse:collapse}em{font-weight:bold;font-style:normal}.lst{height:25px;width:496px}.gsfi,.lst{font:18px arial,sans-serif}.gsfs{font:17px arial,sans-serif}.ds{display:inline-box;display:inline-block;margin:3px 0 4px;margin-left:4px}input{font-family:inherit}a.gb1,a.gb2,a.gb3,a.gb4{color:#11c !important}body{background:#fff;color:black}a{color:#11c;text-decoration:none}a:hover,a:active{text-decoration:underline}.fl a{color:#36c}a:visited{color:#551a8b}a.gb1,a.gb4{text-decoration:underline}a.gb3:hover{text-decoration:none}#ghead a.gb2:hover{color:#fff !important}.sblc{padding-top:5px}.sblc a{display:block;margin:2px 0;margin-left:13px;font-size:11px}.lsbb{background:#eee;border:solid 1px;border-color:#ccc #999 #999 #ccc;height:30px}.lsbb{display:block}.ftl,#fll a{display:inline-block;margin:0 12px}.lsb{background:url(/images/nav_logo229.png) 0 -261px repeat-x;border:none;color:#000;cursor:pointer;height:30px;margin:0;outline:0;font:15px arial,sans-serif;vertical-align:top}.lsb:active{background:#ccc}.lst:focus{outline:none}.tiah{width:458px}</style><script nonce="+qjUq5XdVZcU6gnMDG3k7Q=="></script></head><body bgcolor="#fff"><script nonce="+qjUq5XdVZcU6gnMDG3k7Q==">(function(){var src=\'/images/nav_logo229.png\';var iesg=false;document.body.onload = function(){window.n && window.n();if (document.images){new Image().src=src;}\nif (!iesg){document.f&&document.f.q.focus();document.gbqf&&document.gbqf.q.focus();}\n}\n})();</script><div id="mngb"> <div id=gbar><nobr><b class=gb1>&#2326;&#2379;&#2332;</b> <a class=gb1 href="https://www.google.com.np/imghp?hl=ne&tab=wi">&#2340;&#2360;&#2381;&#2348;&#2367;&#2352;</a> <a class=gb1 href="https://maps.google.com.np/maps?hl=ne&tab=wl">&#2344;&#2325;&#2381;&#2360;&#2366;</a> <a class=gb1 href="https://mail.google.com/mail/?tab=wm">Gmail</a> <a class=gb1 href="https://drive.google.com/?tab=wo">&#2337;&#2381;&#2352;&#2366;&#2311;&#2349;</a> <a class=gb1 href="https://www.google.com/calendar?tab=wc">&#2346;&#2366;&#2340;&#2381;&#2352;&#2379;</a> <a class=gb1 href="https://translate.google.com.np/?hl=ne&tab=wT">&#2309;&#2344;&#2369;&#2348;&#2366;&#2342; &#2327;&#2352;&#2381;&#2344;&#2369;&#2361;&#2379;&#2360;&#2381;</a> <a class=gb1 href="https://www.blogger.com/?tab=wj">&#2348;&#2381;&#2354;&#2327;&#2352;</a> <a class=gb1 style="text-decoration:none" href="https://www.google.com.np/intl/en/about/products?tab=wh"><u>&#2341;&#2346;</u> &raquo;</a></nobr></div><div id=guser width=100%><nobr><span id=gbn class=gbi></span><span id=gbf class=gbf></span><span id=gbe></span><a href="http://www.google.com.np/history/optout?hl=ne" class=gb4>&#2357;&#2375;&#2348; &#2311;&#2340;&#2367;&#2361;&#2366;&#2360;</a> | <a  href="/preferences?hl=ne" class=gb4>&#2346;&#2381;&#2352;&#2366;&#2341;&#2350;&#2367;&#2325;&#2340;&#2366;&#2361;&#2352;&#2370;</a> | <a target=_top id=gb_70 href="https://accounts.google.com/ServiceLogin?hl=ne&passive=true&continue=https://www.google.com/" class=gb4>&#2360;&#2366;&#2311;&#2344; &#2311;&#2344;</a></nobr></div><div class=gbh style=left:0></div><div class=gbh style=right:0></div> </div><center><br clear="all" id="lgpd"><div id="lga"><img alt="Google" height="92" src="/images/branding/googlelogo/1x/googlelogo_white_background_color_272x92dp.png" style="padding:28px 0 14px" width="272" id="hplogo" onload="window.lol&&lol()"><br><br></div><form action="/search" name="f"><table cellpadding="0" cellspacing="0"><tr valign="top"><td width="25%">&nbsp;</td><td align="center" nowrap=""><input name="ie" value="ISO-8859-1" type="hidden"><input value="ne" name="hl" type="hidden"><input name="source" type="hidden" value="hp"><input name="biw" type="hidden"><input name="bih" type="hidden"><div class="ds" style="height:32px;margin:4px 0"><div style="position:relative;zoom:1"><input style="color:#000;margin:0;padding:5px 8px 0 6px;vertical-align:top;padding-right:38px" autocomplete="off" class="lst tiah" value="" title="Google &#2326;&#2379;&#2332;&#2368;" maxlength="2048" name="q" size="57"><img src="/textinputassistant/tia.png" style="position:absolute;cursor:pointer;right:5px;top:4px;z-index:300" onclick="(function(){var src=\'/textinputassistant/11/ne_tia.js\';var s=document.createElement(\'script\');s.src=src;(document.getElementById(\'xjsc\')||document.body).appendChild(s);})();" alt="" height="23" width="27"></div></div><br style="line-height:0"><span class="ds"><span class="lsbb"><input class="lsb" value="Google &#2326;&#2379;&#2332;&#2368;" name="btnG" type="submit"></span></span><span class="ds"><span class="lsbb"><input class="lsb" value="&#2350; &#2349;&#2366;&#2327;&#2381;&#2351;&#2350;&#2366;&#2344;&#2368; &#2309;&#2344;&#2369;&#2349;&#2370;&#2340;&#2367; &#2327;&#2352;&#2367;&#2352;&#2361;&#2375;&#2331;&#2369;" name="btnI" onclick="if(this.form.q.value)this.checked=1; else top.location=\'/doodles/\'" type="submit"></span></span></td><td class="fl sblc" align="left" nowrap="" width="25%"><a href="/advanced_search?hl=ne&amp;authuser=0">&#2313;&#2344;&#2381;&#2344;&#2340; &#2326;&#2379;&#2332; </a><a href="/language_tools?hl=ne&amp;authuser=0">&#2349;&#2366;&#2359;&#2366; &#2313;&#2346;&#2325;&#2352;&#2339;&#2361;&#2352;&#2369;</a></td></tr></table><input id="gbv" name="gbv" type="hidden" value="1"><script nonce="+qjUq5XdVZcU6gnMDG3k7Q==">(function(){var a,b="1";if(document&&document.getElementById)if("undefined"!=typeof XMLHttpRequest)b="2";else if("undefined"!=typeof ActiveXObject){var c,d,e=["MSXML2.XMLHTTP.6.0","MSXML2.XMLHTTP.3.0","MSXML2.XMLHTTP","Microsoft.XMLHTTP"];for(c=0;d=e[c++];)try{new ActiveXObject(d),b="2"}catch(h){}}a=b;if("2"==a&&-1==location.search.indexOf("&gbv=2")){var f=google.gbvu,g=document.getElementById("gbv");g&&(g.value=a);f&&window.setTimeout(function(){location.href=f},0)};}).call(this);</script></form><div id="gac_scont"></div><div style="font-size:83%;min-height:3.5em"><br><div id="gws-output-pages-elements-homepage_additional_languages__als"><style>#gws-output-pages-elements-homepage_additional_languages__als{font-size:small;margin-bottom:24px}#SIvCob{display:inline-block;line-height:28px;}#SIvCob a{padding:0 3px;}.H6sW5{display:inline-block;margin:0 2px;white-space:nowrap}.z4hgWe{display:inline-block;margin:0 2px}</style><div id="SIvCob">Google &#2351;&#2368; &#2349;&#2366;&#2359;&#2366;&#2350;&#2366; &#2313;&#2346;&#2354;&#2348;&#2381;&#2343; &#2331;:  <a href="https://www.google.com/setprefs?sig=0_smMYEKxjBG3tZWuImR_pe4vCt64%3D&amp;hl=en&amp;source=homepage&amp;sa=X&amp;ved=0ahUKEwjQgq6g_sbfAhXLMo8KHQaTBMIQ2ZgBCAU">English</a>  </div></div></div><span id="footer"><div style="font-size:10pt"><div style="margin:19px auto;text-align:center" id="fll"><a href="/intl/ne/about.html">Google&#2325;&#2379; &#2348;&#2366;&#2352;&#2375;&#2350;&#2366; &#2360;&#2350;&#2381;&#2346;&#2370;&#2352;&#2381;&#2339;</a><a href="https://www.google.com/setprefdomain?prefdom=NP&amp;prev=https://www.google.com.np/&amp;sig=K_rpe81GX--qvZtLLv0xYQapxHr-s%3D">Google.com.np</a></div></div><p style="color:#767676;font-size:8pt">&copy; 2018</p></span></center><script nonce="+qjUq5XdVZcU6gnMDG3k7Q==">(function(){window.google.cdo={height:0,width:0};(function(){var a=window.innerWidth,b=window.innerHeight;if(!a||!b){var c=window.document,d="CSS1Compat"==c.compatMode?c.documentElement:c.body;a=d.clientWidth;b=d.clientHeight}a&&b&&(a!=google.cdo.width||b!=google.cdo.height)&&google.log("","","/client_204?&atyp=i&biw="+a+"&bih="+b+"&ei="+google.kEI);}).call(this);})();(function(){var u=\'/xjs/_/js/k\\x3dxjs.hp.en.-PpIeOYp7rw.O/m\\x3dsb_he,d/am\\x3dYsAs/rt\\x3dj/d\\x3d1/rs\\x3dACT90oHak6Vea8_d5yZnUPgd2x9xqhMspg\';var b={gen204:"xjsls",clearcut:31};setTimeout(function(){var a=document.createElement("script");a.src=u;google.timers&&google.timers.load&&google.tick&&google.tick("load",b);document.body.appendChild(a)},0);})();(function(){window.google.xjsu=\'/xjs/_/js/k\\x3dxjs.hp.en.-PpIeOYp7rw.O/m\\x3dsb_he,d/am\\x3dYsAs/rt\\x3dj/d\\x3d1/rs\\x3dACT90oHak6Vea8_d5yZnUPgd2x9xqhMspg\';})();function _DumpException(e){throw e;}\n(function(){var pmc=\'{\\x22Qnk92g\\x22:{},\\x22U5B21g\\x22:{},\\x22YFCs/g\\x22:{},\\x22ZI/YVQ\\x22:{},\\x22d\\x22:{},\\x22sb_he\\x22:{\\x22agen\\x22:true,\\x22cgen\\x22:true,\\x22client\\x22:\\x22heirloom-hp\\x22,\\x22dh\\x22:true,\\x22dhqt\\x22:true,\\x22ds\\x22:\\x22\\x22,\\x22ffql\\x22:\\x22en\\x22,\\x22fl\\x22:true,\\x22host\\x22:\\x22google.com\\x22,\\x22isbh\\x22:28,\\x22jsonp\\x22:true,\\x22msgs\\x22:{\\x22cibl\\x22:\\x22&#2360;&#2381;&#2346;&#2359;&#2381;&#2335; &#2326;&#2379;&#2332;&#2368;\\x22,\\x22dym\\x22:\\x22&#2325;&#2375; &#2340;&#2346;&#2366;&#2312;&#2306; &#2354;&#2375; &#2351;&#2379; &#2349;&#2344;&#2381;&#2344; &#2326;&#2379;&#2332;&#2381;&#2344;&#2369; &#2349;&#2319;&#2325;&#2379; &#2361;&#2379; ?\\x22,\\x22lcky\\x22:\\x22&#2350; &#2349;&#2366;&#2327;&#2381;&#2351;&#2350;&#2366;&#2344;&#2368; &#2309;&#2344;&#2369;&#2349;&#2370;&#2340;&#2367; &#2327;&#2352;&#2367;&#2352;&#2361;&#2375;&#2331;&#2369;\\x22,\\x22lml\\x22:\\x22&#2341;&#2346; &#2332;&#2366;&#2344;&#2325;&#2366;&#2352;&#2368;\\x22,\\x22oskt\\x22:\\x22&#2310;&#2327;&#2340; &#2313;&#2346;&#2325;&#2352;&#2339;&#2361;&#2352;&#2370;\\x22,\\x22psrc\\x22:\\x22&#2351;&#2379; &#2326;&#2379;&#2332;&#2368; \\\\u003Ca href\\x3d\\\\\\x22/history\\\\\\x22\\\\u003E &#2340;&#2346;&#2366;&#2312;&#2325;&#2379; &#2357;&#2375;&#2348; &#2311;&#2340;&#2367;&#2361;&#2366;&#2360;\\\\u003C/a\\\\u003E&#2348;&#2366;&#2335; &#2361;&#2335;&#2366;&#2311;&#2351;&#2379;\\x22,\\x22psrl\\x22:\\x22&#2361;&#2335;&#2366;&#2313;&#2344;&#2369;&#2361;&#2379;&#2360;\\x22,\\x22sbit\\x22:\\x22&#2330;&#2367;&#2340;&#2381;&#2352;&#2342;&#2381;&#2357;&#2366;&#2352;&#2366; &#2326;&#2379;&#2332;&#2381;&#2344;&#2369;&#2361;&#2379;&#2360;&#2381;\\x22,\\x22srch\\x22:\\x22Google &#2326;&#2379;&#2332;&#2368;\\x22},\\x22ovr\\x22:{},\\x22pq\\x22:\\x22\\x22,\\x22refpd\\x22:true,\\x22rfs\\x22:[],\\x22sbpl\\x22:24,\\x22sbpr\\x22:24,\\x22scd\\x22:10,\\x22sce\\x22:5,\\x22stok\\x22:\\x22xfvSx4b_8t-izmZ4xe33_zkajJg\\x22,\\x22uhde\\x22:false}}\';google.pmc=JSON.parse(pmc);})();(function(){var r=[\'aa\',\'async\',\'ipv6\',\'mu\',\'sf\'];google.plm(r);})();</script>     </body></html>'
>>> linkRequest = urllib.request.urlopen(link)
>>> linkRequest.info()
<http.client.HTTPMessage object at 0x00B91A70>
>>> linkRequest.info()['date']
'Sun, 30 Dec 2018 15:53:48 GMT'
>>> linkRequest.info()['server']
>>> linkRequest.getheaders()
[('RTSS', '1-2-91'), ('Content-Type', 'text/xml'), ('Forcelegacy', 'false'), ('Samsheader', 'TB-DFW'), ('Strict-Transport-Security', 'max-age=86400'), ('X-Frame-Options', 'SAMEORIGIN'), ('X-Tb', '0'), ('Vary', 'Accept-Encoding'), ('Date', 'Sun, 30 Dec 2018 15:53:48 GMT'), ('Content-Length', '431'), ('Connection', 'close'), ('Set-Cookie', 'SSLB=1; path=/; domain=.samsclub.com'), ('Set-Cookie', 'NSC_JOqyreriep202r0eksinc1efkgrc2cc=3af6a3c8412137002eb6d88d1a646f1c3aae3d4ff5ecfba960817ed43be4da147d323574;expires=Sun, 30-Dec-2018 21:53:48 GMT;path=/;secure;httponly'), ('Set-Cookie', 'TS01f4281b=0130aff2321fbe1e85b82c56784c8ee75023de9a65282816af25832325b54b20299d329abb2b4a7cf522c1548b57a8f3daed99a2aa; Path=/; Secure'), ('Set-Cookie', 'dcenv=TB-DFW; path=/; domain=samsclub.com'), ('Set-Cookie', 'dcenv=TB-DFW; path=/; domain=samsclub.com'), ('Set-Cookie', 'akavpau_P3=1546185828~id=b756d5103e484ea7b05c762088c5ae37; Path=/')]
>>> linkRequest.info()['vary']
'Accept-Encoding'
>>> linkRequest.info()['content-type']
'text/xml'
>>> linkRequest.info()['cookie']
>>> linkRequest.info()['set-cookie']
'SSLB=1; path=/; domain=.samsclub.com'
>>> url1 = 'http://localhost:8080/?'
>>> url2 = urlparse.urlencode({'a':10,'b':'Book Name'})
>>> urlparse.urljoin(url1,url2)
'http://localhost:8080/a=10&b=Book+Name'
>>> url1 = 'http://localhost:8080/?/'
>>> urlparse.urljoin(url1,url2)
'http://localhost:8080/a=10&b=Book+Name'
>>> data = {'param1': 'value1', 'param2': 'value2'}
>>> urlparse.urlencode(data)
'param1=value1&param2=value2'
>>> urlparse.urlencode(data).encode('utf-8')
b'param1=value1&param2=value2'
>>> urlparse.parse_qs(urlparse.urlencode(data).encode('utf-8'))
{b'param1': [b'value1'], b'param2': [b'value2']}
>>> type(urlparse.parse_qs(urlparse.urlencode(data).encode('utf-8')))
<class 'dict'>
>>> type(urlparse.urlencode(data).encode('utf-8'))
<class 'bytes'>
>>> import urllib.error as error
>>> dir(error)
['ContentTooShortError', 'HTTPError', 'URLError', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'urllib']
>>> help(error)
Help on module urllib.error in urllib:

NAME
    urllib.error - Exception classes raised by urllib.

DESCRIPTION
    The base exception class is URLError, which inherits from OSError.  It
    doesn't define any behavior of its own, but is the base class for all
    exceptions defined in this package.
    
    HTTPError is an exception class that is also a valid HTTP response
    instance.  It behaves this way because HTTP protocol errors are valid
    responses, with a status code, headers, and a body.  In some contexts,
    an application may want to handle an exception like a regular
    response.

CLASSES
    builtins.OSError(builtins.Exception)
        URLError
            ContentTooShortError
            HTTPError(URLError, urllib.response.addinfourl)
    
    class ContentTooShortError(URLError)
     |  ContentTooShortError(message, content)
     |  
     |  Exception raised when downloaded size does not match content-length.
     |  
     |  Method resolution order:
     |      ContentTooShortError
     |      URLError
     |      builtins.OSError
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, message, content)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from URLError:
     |  
     |  __str__(self)
     |      Return str(self).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from URLError:
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.OSError:
     |  
     |  __reduce__(...)
     |      Helper for pickle.
     |  
     |  ----------------------------------------------------------------------
     |  Static methods inherited from builtins.OSError:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.OSError:
     |  
     |  characters_written
     |  
     |  errno
     |      POSIX exception code
     |  
     |  filename
     |      exception filename
     |  
     |  filename2
     |      second exception filename
     |  
     |  strerror
     |      exception strerror
     |  
     |  winerror
     |      Win32 exception code
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class HTTPError(URLError, urllib.response.addinfourl)
     |  HTTPError(url, code, msg, hdrs, fp)
     |  
     |  Raised when HTTP error occurs, but also acts like non-error return
     |  
     |  Method resolution order:
     |      HTTPError
     |      URLError
     |      builtins.OSError
     |      builtins.Exception
     |      builtins.BaseException
     |      urllib.response.addinfourl
     |      urllib.response.addinfo
     |      urllib.response.addbase
     |      tempfile._TemporaryFileWrapper
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, url, code, msg, hdrs, fp)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __repr__(self)
     |      Return repr(self).
     |  
     |  __str__(self)
     |      Return str(self).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  headers
     |  
     |  reason
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from URLError:
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.OSError:
     |  
     |  __reduce__(...)
     |      Helper for pickle.
     |  
     |  ----------------------------------------------------------------------
     |  Static methods inherited from builtins.OSError:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.OSError:
     |  
     |  characters_written
     |  
     |  errno
     |      POSIX exception code
     |  
     |  filename
     |      exception filename
     |  
     |  filename2
     |      second exception filename
     |  
     |  strerror
     |      exception strerror
     |  
     |  winerror
     |      Win32 exception code
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from urllib.response.addinfourl:
     |  
     |  getcode(self)
     |  
     |  geturl(self)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from urllib.response.addinfo:
     |  
     |  info(self)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from urllib.response.addbase:
     |  
     |  __enter__(self)
     |  
     |  __exit__(self, type, value, traceback)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from tempfile._TemporaryFileWrapper:
     |  
     |  __getattr__(self, name)
     |  
     |  __iter__(self)
     |      # iter() doesn't use __getattr__ to find the __iter__ method
     |  
     |  close(self)
     |      Close the temporary file, possibly deleting it.
    
    class URLError(builtins.OSError)
     |  URLError(reason, filename=None)
     |  
     |  Base class for I/O related errors.
     |  
     |  Method resolution order:
     |      URLError
     |      builtins.OSError
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, reason, filename=None)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __str__(self)
     |      Return str(self).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.OSError:
     |  
     |  __reduce__(...)
     |      Helper for pickle.
     |  
     |  ----------------------------------------------------------------------
     |  Static methods inherited from builtins.OSError:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.OSError:
     |  
     |  characters_written
     |  
     |  errno
     |      POSIX exception code
     |  
     |  filename
     |      exception filename
     |  
     |  filename2
     |      second exception filename
     |  
     |  strerror
     |      exception strerror
     |  
     |  winerror
     |      Win32 exception code
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args

DATA
    __all__ = ['URLError', 'HTTPError', 'ContentTooShortError']

FILE
    c:\python37\lib\urllib\error.py


>>> urllib.urlopen("https://www.pyhton.ogr')
		   
SyntaxError: EOL while scanning string literal
>>> urllib.urlopen("https://www.pyhton.ogr")
		   
Traceback (most recent call last):
  File "<pyshell#220>", line 1, in <module>
    urllib.urlopen("https://www.pyhton.ogr")
AttributeError: module 'urllib' has no attribute 'urlopen'
>>> urllib.request.urlopen("https://www.pyhton.ogr")
		   
Traceback (most recent call last):
  File "C:\Python37\lib\urllib\request.py", line 1317, in do_open
    encode_chunked=req.has_header('Transfer-encoding'))
  File "C:\Python37\lib\http\client.py", line 1229, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "C:\Python37\lib\http\client.py", line 1275, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "C:\Python37\lib\http\client.py", line 1224, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "C:\Python37\lib\http\client.py", line 1016, in _send_output
    self.send(msg)
  File "C:\Python37\lib\http\client.py", line 956, in send
    self.connect()
  File "C:\Python37\lib\http\client.py", line 1384, in connect
    super().connect()
  File "C:\Python37\lib\http\client.py", line 928, in connect
    (self.host,self.port), self.timeout, self.source_address)
  File "C:\Python37\lib\socket.py", line 707, in create_connection
    for res in getaddrinfo(host, port, 0, SOCK_STREAM):
  File "C:\Python37\lib\socket.py", line 748, in getaddrinfo
    for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
socket.gaierror: [Errno 11001] getaddrinfo failed

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#221>", line 1, in <module>
    urllib.request.urlopen("https://www.pyhton.ogr")
  File "C:\Python37\lib\urllib\request.py", line 222, in urlopen
    return opener.open(url, data, timeout)
  File "C:\Python37\lib\urllib\request.py", line 525, in open
    response = self._open(req, data)
  File "C:\Python37\lib\urllib\request.py", line 543, in _open
    '_open', req)
  File "C:\Python37\lib\urllib\request.py", line 503, in _call_chain
    result = func(*args)
  File "C:\Python37\lib\urllib\request.py", line 1360, in https_open
    context=self._context, check_hostname=self._check_hostname)
  File "C:\Python37\lib\urllib\request.py", line 1319, in do_open
    raise URLError(err)
urllib.error.URLError: <urlopen error [Errno 11001] getaddrinfo failed>
>>> tyr:
	
SyntaxError: invalid syntax
>>> try:
	urllib.request.urlopen("https://www.python.ogr")
except URLError,e:
	
SyntaxError: invalid syntax
>>> try:
	urllib.request.urlopen("https://www.python.ogr")
except URLError e:
	
SyntaxError: invalid syntax
>>> try:
	urllib.request.urlopen("https://www.python.ogr")
except URLError, e:
	
SyntaxError: invalid syntax
>>> try:
	urllib.request.urlopen("https://www.python.ogr")
except URLError e:
	
SyntaxError: invalid syntax
>>> try:
	urllib.request.urlopen("https://www.python.ogr")
except URLError:
	print(URLError.reason)

	
Traceback (most recent call last):
  File "C:\Python37\lib\urllib\request.py", line 1317, in do_open
    encode_chunked=req.has_header('Transfer-encoding'))
  File "C:\Python37\lib\http\client.py", line 1229, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "C:\Python37\lib\http\client.py", line 1275, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "C:\Python37\lib\http\client.py", line 1224, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "C:\Python37\lib\http\client.py", line 1016, in _send_output
    self.send(msg)
  File "C:\Python37\lib\http\client.py", line 956, in send
    self.connect()
  File "C:\Python37\lib\http\client.py", line 1384, in connect
    super().connect()
  File "C:\Python37\lib\http\client.py", line 928, in connect
    (self.host,self.port), self.timeout, self.source_address)
  File "C:\Python37\lib\socket.py", line 707, in create_connection
    for res in getaddrinfo(host, port, 0, SOCK_STREAM):
  File "C:\Python37\lib\socket.py", line 748, in getaddrinfo
    for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
socket.gaierror: [Errno 11001] getaddrinfo failed

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#231>", line 2, in <module>
    urllib.request.urlopen("https://www.python.ogr")
  File "C:\Python37\lib\urllib\request.py", line 222, in urlopen
    return opener.open(url, data, timeout)
  File "C:\Python37\lib\urllib\request.py", line 525, in open
    response = self._open(req, data)
  File "C:\Python37\lib\urllib\request.py", line 543, in _open
    '_open', req)
  File "C:\Python37\lib\urllib\request.py", line 503, in _call_chain
    result = func(*args)
  File "C:\Python37\lib\urllib\request.py", line 1360, in https_open
    context=self._context, check_hostname=self._check_hostname)
  File "C:\Python37\lib\urllib\request.py", line 1319, in do_open
    raise URLError(err)
urllib.error.URLError: <urlopen error [Errno 11001] getaddrinfo failed>

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#231>", line 3, in <module>
    except URLError:
NameError: name 'URLError' is not defined
>>> try:
	urllib.request.urlopen("https://www.python.ogr")
except URLError as e:
	print(e.reason)
	print(e.code)

	
Traceback (most recent call last):
  File "C:\Python37\lib\urllib\request.py", line 1317, in do_open
    encode_chunked=req.has_header('Transfer-encoding'))
  File "C:\Python37\lib\http\client.py", line 1229, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "C:\Python37\lib\http\client.py", line 1275, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "C:\Python37\lib\http\client.py", line 1224, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "C:\Python37\lib\http\client.py", line 1016, in _send_output
    self.send(msg)
  File "C:\Python37\lib\http\client.py", line 956, in send
    self.connect()
  File "C:\Python37\lib\http\client.py", line 1384, in connect
    super().connect()
  File "C:\Python37\lib\http\client.py", line 928, in connect
    (self.host,self.port), self.timeout, self.source_address)
  File "C:\Python37\lib\socket.py", line 707, in create_connection
    for res in getaddrinfo(host, port, 0, SOCK_STREAM):
  File "C:\Python37\lib\socket.py", line 748, in getaddrinfo
    for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
socket.gaierror: [Errno 11001] getaddrinfo failed

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#234>", line 2, in <module>
    urllib.request.urlopen("https://www.python.ogr")
  File "C:\Python37\lib\urllib\request.py", line 222, in urlopen
    return opener.open(url, data, timeout)
  File "C:\Python37\lib\urllib\request.py", line 525, in open
    response = self._open(req, data)
  File "C:\Python37\lib\urllib\request.py", line 543, in _open
    '_open', req)
  File "C:\Python37\lib\urllib\request.py", line 503, in _call_chain
    result = func(*args)
  File "C:\Python37\lib\urllib\request.py", line 1360, in https_open
    context=self._context, check_hostname=self._check_hostname)
  File "C:\Python37\lib\urllib\request.py", line 1319, in do_open
    raise URLError(err)
urllib.error.URLError: <urlopen error [Errno 11001] getaddrinfo failed>

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#234>", line 3, in <module>
    except URLError as e:
NameError: name 'URLError' is not defined
>>> import os
>>> try:
	urllib.request.urlopen("https://www.python.ogr")
except URLError as e:
	print(e.reason)
	print(e.code)

	
Traceback (most recent call last):
  File "C:\Python37\lib\urllib\request.py", line 1317, in do_open
    encode_chunked=req.has_header('Transfer-encoding'))
  File "C:\Python37\lib\http\client.py", line 1229, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "C:\Python37\lib\http\client.py", line 1275, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "C:\Python37\lib\http\client.py", line 1224, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "C:\Python37\lib\http\client.py", line 1016, in _send_output
    self.send(msg)
  File "C:\Python37\lib\http\client.py", line 956, in send
    self.connect()
  File "C:\Python37\lib\http\client.py", line 1384, in connect
    super().connect()
  File "C:\Python37\lib\http\client.py", line 928, in connect
    (self.host,self.port), self.timeout, self.source_address)
  File "C:\Python37\lib\socket.py", line 707, in create_connection
    for res in getaddrinfo(host, port, 0, SOCK_STREAM):
  File "C:\Python37\lib\socket.py", line 748, in getaddrinfo
    for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
socket.gaierror: [Errno 11001] getaddrinfo failed

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#237>", line 2, in <module>
    urllib.request.urlopen("https://www.python.ogr")
  File "C:\Python37\lib\urllib\request.py", line 222, in urlopen
    return opener.open(url, data, timeout)
  File "C:\Python37\lib\urllib\request.py", line 525, in open
    response = self._open(req, data)
  File "C:\Python37\lib\urllib\request.py", line 543, in _open
    '_open', req)
  File "C:\Python37\lib\urllib\request.py", line 503, in _call_chain
    result = func(*args)
  File "C:\Python37\lib\urllib\request.py", line 1360, in https_open
    context=self._context, check_hostname=self._check_hostname)
  File "C:\Python37\lib\urllib\request.py", line 1319, in do_open
    raise URLError(err)
urllib.error.URLError: <urlopen error [Errno 11001] getaddrinfo failed>

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#237>", line 3, in <module>
    except URLError as e:
NameError: name 'URLError' is not defined
>>> try:
	urllib.request.urlopen("https://www.python.ogr")
except error.URLError as e:
	print(e.reason)
	print(e.code)

	
[Errno 11001] getaddrinfo failed
Traceback (most recent call last):
  File "C:\Python37\lib\urllib\request.py", line 1317, in do_open
    encode_chunked=req.has_header('Transfer-encoding'))
  File "C:\Python37\lib\http\client.py", line 1229, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "C:\Python37\lib\http\client.py", line 1275, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "C:\Python37\lib\http\client.py", line 1224, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "C:\Python37\lib\http\client.py", line 1016, in _send_output
    self.send(msg)
  File "C:\Python37\lib\http\client.py", line 956, in send
    self.connect()
  File "C:\Python37\lib\http\client.py", line 1384, in connect
    super().connect()
  File "C:\Python37\lib\http\client.py", line 928, in connect
    (self.host,self.port), self.timeout, self.source_address)
  File "C:\Python37\lib\socket.py", line 707, in create_connection
    for res in getaddrinfo(host, port, 0, SOCK_STREAM):
  File "C:\Python37\lib\socket.py", line 748, in getaddrinfo
    for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
socket.gaierror: [Errno 11001] getaddrinfo failed

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#239>", line 2, in <module>
    urllib.request.urlopen("https://www.python.ogr")
  File "C:\Python37\lib\urllib\request.py", line 222, in urlopen
    return opener.open(url, data, timeout)
  File "C:\Python37\lib\urllib\request.py", line 525, in open
    response = self._open(req, data)
  File "C:\Python37\lib\urllib\request.py", line 543, in _open
    '_open', req)
  File "C:\Python37\lib\urllib\request.py", line 503, in _call_chain
    result = func(*args)
  File "C:\Python37\lib\urllib\request.py", line 1360, in https_open
    context=self._context, check_hostname=self._check_hostname)
  File "C:\Python37\lib\urllib\request.py", line 1319, in do_open
    raise URLError(err)
urllib.error.URLError: <urlopen error [Errno 11001] getaddrinfo failed>

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#239>", line 5, in <module>
    print(e.code)
AttributeError: 'URLError' object has no attribute 'code'
>>> import urllib.error
>>> try:
	urllib.request.urlopen("https://www.python.ogr")
except urllib.error.URLError as e:
	print(e.reason)
	print(e.code)

	
[Errno 11001] getaddrinfo failed
Traceback (most recent call last):
  File "C:\Python37\lib\urllib\request.py", line 1317, in do_open
    encode_chunked=req.has_header('Transfer-encoding'))
  File "C:\Python37\lib\http\client.py", line 1229, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "C:\Python37\lib\http\client.py", line 1275, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "C:\Python37\lib\http\client.py", line 1224, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "C:\Python37\lib\http\client.py", line 1016, in _send_output
    self.send(msg)
  File "C:\Python37\lib\http\client.py", line 956, in send
    self.connect()
  File "C:\Python37\lib\http\client.py", line 1384, in connect
    super().connect()
  File "C:\Python37\lib\http\client.py", line 928, in connect
    (self.host,self.port), self.timeout, self.source_address)
  File "C:\Python37\lib\socket.py", line 707, in create_connection
    for res in getaddrinfo(host, port, 0, SOCK_STREAM):
  File "C:\Python37\lib\socket.py", line 748, in getaddrinfo
    for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
socket.gaierror: [Errno 11001] getaddrinfo failed

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#242>", line 2, in <module>
    urllib.request.urlopen("https://www.python.ogr")
  File "C:\Python37\lib\urllib\request.py", line 222, in urlopen
    return opener.open(url, data, timeout)
  File "C:\Python37\lib\urllib\request.py", line 525, in open
    response = self._open(req, data)
  File "C:\Python37\lib\urllib\request.py", line 543, in _open
    '_open', req)
  File "C:\Python37\lib\urllib\request.py", line 503, in _call_chain
    result = func(*args)
  File "C:\Python37\lib\urllib\request.py", line 1360, in https_open
    context=self._context, check_hostname=self._check_hostname)
  File "C:\Python37\lib\urllib\request.py", line 1319, in do_open
    raise URLError(err)
urllib.error.URLError: <urlopen error [Errno 11001] getaddrinfo failed>

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#242>", line 5, in <module>
    print(e.code)
AttributeError: 'URLError' object has no attribute 'code'
>>> try:
	urllib.request.urlopen("https://www.python.ogr")
except error.URLError as e:
	print(e.reason)
	print(e.code)

	
[Errno 11001] getaddrinfo failed
Traceback (most recent call last):
  File "C:\Python37\lib\urllib\request.py", line 1317, in do_open
    encode_chunked=req.has_header('Transfer-encoding'))
  File "C:\Python37\lib\http\client.py", line 1229, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "C:\Python37\lib\http\client.py", line 1275, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "C:\Python37\lib\http\client.py", line 1224, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "C:\Python37\lib\http\client.py", line 1016, in _send_output
    self.send(msg)
  File "C:\Python37\lib\http\client.py", line 956, in send
    self.connect()
  File "C:\Python37\lib\http\client.py", line 1384, in connect
    super().connect()
  File "C:\Python37\lib\http\client.py", line 928, in connect
    (self.host,self.port), self.timeout, self.source_address)
  File "C:\Python37\lib\socket.py", line 707, in create_connection
    for res in getaddrinfo(host, port, 0, SOCK_STREAM):
  File "C:\Python37\lib\socket.py", line 748, in getaddrinfo
    for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
socket.gaierror: [Errno 11001] getaddrinfo failed

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#244>", line 2, in <module>
    urllib.request.urlopen("https://www.python.ogr")
  File "C:\Python37\lib\urllib\request.py", line 222, in urlopen
    return opener.open(url, data, timeout)
  File "C:\Python37\lib\urllib\request.py", line 525, in open
    response = self._open(req, data)
  File "C:\Python37\lib\urllib\request.py", line 543, in _open
    '_open', req)
  File "C:\Python37\lib\urllib\request.py", line 503, in _call_chain
    result = func(*args)
  File "C:\Python37\lib\urllib\request.py", line 1360, in https_open
    context=self._context, check_hostname=self._check_hostname)
  File "C:\Python37\lib\urllib\request.py", line 1319, in do_open
    raise URLError(err)
urllib.error.URLError: <urlopen error [Errno 11001] getaddrinfo failed>

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#244>", line 5, in <module>
    print(e.code)
AttributeError: 'URLError' object has no attribute 'code'
>>> 
