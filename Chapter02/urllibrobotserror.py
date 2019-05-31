Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import urllib.parse
>>> import urllib.parse as urlparse
>>> dir(urlparse)
['DefragResult', 'DefragResultBytes', 'MAX_CACHE_SIZE', 'ParseResult', 'ParseResultBytes', 'Quoter', 'ResultBase', 'SplitResult', 'SplitResultBytes', '_ALWAYS_SAFE', '_ALWAYS_SAFE_BYTES', '_DefragResultBase', '_NetlocResultMixinBase', '_NetlocResultMixinBytes', '_NetlocResultMixinStr', '_ParseResultBase', '_ResultMixinBytes', '_ResultMixinStr', '_SplitResultBase', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_asciire', '_coerce_args', '_decode_args', '_encode_result', '_hexdig', '_hextobyte', '_hostprog', '_implicit_encoding', '_implicit_errors', '_noop', '_parse_cache', '_portprog', '_safe_quoters', '_splitnetloc', '_splitparams', '_typeprog', 'clear_cache', 'collections', 'namedtuple', 'non_hierarchical', 'parse_qs', 'parse_qsl', 'quote', 'quote_from_bytes', 'quote_plus', 're', 'scheme_chars', 'splitattr', 'splithost', 'splitnport', 'splitpasswd', 'splitport', 'splitquery', 'splittag', 'splittype', 'splituser', 'splitvalue', 'sys', 'to_bytes', 'unquote', 'unquote_plus', 'unquote_to_bytes', 'unwrap', 'urldefrag', 'urlencode', 'urljoin', 'urlparse', 'urlsplit', 'urlunparse', 'urlunsplit', 'uses_fragment', 'uses_netloc', 'uses_params', 'uses_query', 'uses_relative']
>>> import urllib
>>> dir(urllib)
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'parse']
>>> import urllib.request
>>> dir(urllib.request)
['AbstractBasicAuthHandler', 'AbstractDigestAuthHandler', 'AbstractHTTPHandler', 'BaseHandler', 'CacheFTPHandler', 'ContentTooShortError', 'DataHandler', 'FTPHandler', 'FancyURLopener', 'FileHandler', 'HTTPBasicAuthHandler', 'HTTPCookieProcessor', 'HTTPDefaultErrorHandler', 'HTTPDigestAuthHandler', 'HTTPError', 'HTTPErrorProcessor', 'HTTPHandler', 'HTTPPasswordMgr', 'HTTPPasswordMgrWithDefaultRealm', 'HTTPPasswordMgrWithPriorAuth', 'HTTPRedirectHandler', 'HTTPSHandler', 'MAXFTPCACHE', 'OpenerDirector', 'ProxyBasicAuthHandler', 'ProxyDigestAuthHandler', 'ProxyHandler', 'Request', 'URLError', 'URLopener', 'UnknownHandler', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__', '_cut_port_re', '_ftperrors', '_have_ssl', '_localhost', '_noheaders', '_opener', '_parse_proxy', '_proxy_bypass_macosx_sysconf', '_randombytes', '_safe_gethostbyname', '_thishost', '_url_tempfiles', 'addclosehook', 'addinfourl', 'base64', 'bisect', 'build_opener', 'contextlib', 'email', 'ftpcache', 'ftperrors', 'ftpwrapper', 'getproxies', 'getproxies_environment', 'getproxies_registry', 'hashlib', 'http', 'install_opener', 'io', 'localhost', 'noheaders', 'os', 'parse_http_list', 'parse_keqv_list', 'pathname2url', 'posixpath', 'proxy_bypass', 'proxy_bypass_environment', 'proxy_bypass_registry', 'quote', 're', 'request_host', 'socket', 'splitattr', 'splithost', 'splitpasswd', 'splitport', 'splitquery', 'splittag', 'splittype', 'splituser', 'splitvalue', 'ssl', 'string', 'sys', 'tempfile', 'thishost', 'time', 'to_bytes', 'unquote', 'unquote_to_bytes', 'unwrap', 'url2pathname', 'urlcleanup', 'urljoin', 'urlopen', 'urlparse', 'urlretrieve', 'urlsplit', 'urlunparse', 'warnings']
>>> link="https://www.google.com"
>>> urllinb.request.thishost(link)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    urllinb.request.thishost(link)
NameError: name 'urllinb' is not defined
>>> urllib.request.thishost(link)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    urllib.request.thishost(link)
TypeError: thishost() takes 0 positional arguments but 1 was given
>>> urllib.request.thishost()
('172.25.182.97', '192.168.99.1', '172.18.160.1', '192.168.0.106')
>>> urllib.request.splithost(link)
(None, 'https://www.google.com')
>>> link="https://www.google.com?search=Web Scraping"
>>> urllib.request.splithost(link)
(None, 'https://www.google.com?search=Web Scraping')
>>> urllib.request.splitquery(link)
('https://www.google.com', 'search=Web Scraping')
>>> urllib.request.requesthost(link)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    urllib.request.requesthost(link)
AttributeError: module 'urllib.request' has no attribute 'requesthost'
>>> urllib.request.request_host(link)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    urllib.request.request_host(link)
  File "C:\Python37\lib\urllib\request.py", line 314, in request_host
    url = request.full_url
AttributeError: 'str' object has no attribute 'full_url'
>>> help(urllib.request.urlcleanup)
Help on function urlcleanup in module urllib.request:

urlcleanup()
    Clean up temporary files from urlretrieve calls.

>>> 
 RESTART: C:/Users/PETERCHAPAGAIN/Desktop/WebBook/Chapter2-RequestUrllib/urlerror.py 
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
  File "C:/Users/PETERCHAPAGAIN/Desktop/WebBook/Chapter2-RequestUrllib/urlerror.py", line 5, in <module>
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
  File "C:/Users/PETERCHAPAGAIN/Desktop/WebBook/Chapter2-RequestUrllib/urlerror.py", line 6, in <module>
    except error.URLError as e:
NameError: name 'error' is not defined
>>> 
 RESTART: C:/Users/PETERCHAPAGAIN/Desktop/WebBook/Chapter2-RequestUrllib/urlerror.py 
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
  File "C:/Users/PETERCHAPAGAIN/Desktop/WebBook/Chapter2-RequestUrllib/urlerror.py", line 5, in <module>
    request.urlopen("https://www.python.ogr")
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
  File "C:/Users/PETERCHAPAGAIN/Desktop/WebBook/Chapter2-RequestUrllib/urlerror.py", line 8, in <module>
    print(e.code)
AttributeError: 'URLError' object has no attribute 'code'
>>> 
 RESTART: C:/Users/PETERCHAPAGAIN/Desktop/WebBook/Chapter2-RequestUrllib/urlerror.py 
[Errno 11001] getaddrinfo failed
>>> 
 RESTART: C:/Users/PETERCHAPAGAIN/Desktop/WebBook/Chapter2-RequestUrllib/urlerror.py 
['ContentTooShortError', 'HTTPError', 'URLError', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'urllib']
[Errno 11001] getaddrinfo failed
>>> 
 RESTART: C:/Users/PETERCHAPAGAIN/Desktop/WebBook/Chapter2-RequestUrllib/urlerror.py 
['__cause__', '__class__', '__context__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__suppress_context__', '__traceback__', '__weakref__', 'args', 'characters_written', 'errno', 'filename', 'filename2', 'strerror', 'winerror', 'with_traceback']
[Errno 11001] getaddrinfo failed
>>> 
 RESTART: C:/Users/PETERCHAPAGAIN/Desktop/WebBook/Chapter2-RequestUrllib/urlerror.py 
['__cause__', '__class__', '__context__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__suppress_context__', '__traceback__', '__weakref__', 'args', 'characters_written', 'errno', 'filename', 'filename2', 'strerror', 'winerror', 'with_traceback']
Error Occurred:  [Errno 11001] getaddrinfo failed
>>> 
 RESTART: C:/Users/PETERCHAPAGAIN/Desktop/WebBook/Chapter2-RequestUrllib/urlerror.py 
['__cause__', '__class__', '__context__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__suppress_context__', '__traceback__', '__weakref__', 'args', 'characters_written', 'errno', 'filename', 'filename2', 'strerror', 'winerror', 'with_traceback']
Error Occurred:  unknown url type: htps
>>> import urllib.request as request
>>> import urllib.error as error

>>> try:
    request.urlopen("https://www.python.ogr")
except error.URLError as e:
    print("Error Occurred: ",e.reason)

    
Error Occurred:  [Errno 11001] getaddrinfo failed
>>> import urllib,robotparser as robot
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    import urllib,robotparser as robot
ModuleNotFoundError: No module named 'robotparser'
>>> import urllib.robotparser as robot
>>> parser = robot.RobotFileParser("httpe://www.samsclub.com/robots.txt")
>>> dir(parser)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_add_entry', 'allow_all', 'can_fetch', 'crawl_delay', 'default_entry', 'disallow_all', 'entries', 'host', 'last_checked', 'modified', 'mtime', 'parse', 'path', 'read', 'request_rate', 'set_url', 'url']
>>> parser = robot.RobotFileParser("https://www.samsclub.com/robots.txt")
>>> dir(parser)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_add_entry', 'allow_all', 'can_fetch', 'crawl_delay', 'default_entry', 'disallow_all', 'entries', 'host', 'last_checked', 'modified', 'mtime', 'parse', 'path', 'read', 'request_rate', 'set_url', 'url']
>>> parser.can_fetch('*','')
False
>>> parser.can_fetch('*','https://www.samsclub.com/sitemap.xml')
False
>>> parser.can_fetch('*','https://www.samsclub.com/')
False
>>> parser.can_fetch('*','https://www.samsclub.com/sama/account/signin/createSession.jsp')
False
>>> parser = robot.RobotFileParser("https://www.diply.com/robots.txt")
>>> parser.can_fetch('*','https://www.diply.com/')
False
>>> parser.can_fetch('*','https://www.diply.com/static/cookiepolicy')
False
>>> parser.can_fetch('*','https://www.diply.com/static/cookiepolicy/')
False
>>> parser = robot.RobotFileParser()
>>> p = parser.set_url('https://www.diply.com/robots.txt')
>>> p
>>> dir(p)
['__bool__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
>>> type(p)
<class 'NoneType'>
>>> p.can_fetch('*','https://www.diply.com/static/cookiepolicy/')
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    p.can_fetch('*','https://www.diply.com/static/cookiepolicy/')
AttributeError: 'NoneType' object has no attribute 'can_fetch'
>>> p.read()
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    p.read()
AttributeError: 'NoneType' object has no attribute 'read'
>>> parser.set_url('https://www.diply.com/robots.txt')
>>> parser.read()
>>> parser.can_fetch('*','https://www.diply.com/static/cookiepolicy/')
True
>>> parser.can_fetch('*','https://www.samsclub.com/sama/account/signin/createSession.jsp')
True
>>> parser.can_fetch('*','https://www.samsclub.com/sitemap.xml')
True
>>> parser.can_fetch('*','https://www.samsclub.com/category')
True
>>> dir(parser)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_add_entry', 'allow_all', 'can_fetch', 'crawl_delay', 'default_entry', 'disallow_all', 'entries', 'host', 'last_checked', 'modified', 'mtime', 'parse', 'path', 'read', 'request_rate', 'set_url', 'url']
>>> print parser
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(parser)?
>>> print(parser)
User-agent: *
Allow: 


>>> parser.set_url('https://www.samsclub.com/robots.txt')
>>> parser.read()
>>> print(parser)
User-agent: *
Allow: 


>>> par = robot.RobotFileParser()
>>> par.set_url('https://www.samsclub.com/robots.txt')
>>> par.read()
>>> print(par)
User-agent: *
Allow: /sams/account/signin/createSession.jsp
Disallow: /cgi-bin/
Disallow: /sams/checkout/
Disallow: /sams/account/
Disallow: /sams/cart/
Disallow: /sams/eValues/clubInsiderOffers.jsp
Disallow: /friend
Allow: /sams/account/referal/


>>> par.can_fetch('*','https://www.samsclub.com/category')
True
>>> par.can_fetch('*','https://www.samsclub.com/friend')
False
>>> par.crawl_delay(*)
SyntaxError: invalid syntax
>>> par.crawl_delay('*')
>>> par.request_rate('*')
>>> rr=par.request_rate('*')
>>> rr.seconds
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    rr.seconds
AttributeError: 'NoneType' object has no attribute 'seconds'
>>> 
