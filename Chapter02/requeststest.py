Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import urllib
>>> dir(urllib)
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'parse']
>>> urllib.splithost
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    urllib.splithost
AttributeError: module 'urllib' has no attribute 'splithost'
>>> import requests
>>> url="https://www.python.org"
>>> link="https://www.python.org"
>>> r = requests.get(link)
>>> r.url
'https://www.python.org/'
>>> r.code
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    r.code
AttributeError: 'Response' object has no attribute 'code'
>>> r.status_code
200
>>> dir(r)
['__attrs__', '__bool__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__nonzero__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_content', '_content_consumed', '_next', 'apparent_encoding', 'close', 'connection', 'content', 'cookies', 'elapsed', 'encoding', 'headers', 'history', 'is_permanent_redirect', 'is_redirect', 'iter_content', 'iter_lines', 'json', 'links', 'next', 'ok', 'raise_for_status', 'raw', 'reason', 'request', 'status_code', 'text', 'url']
>>> r.raw
<urllib3.response.HTTPResponse object at 0x041A8F70>
>>> r.ok
True
>>> r.next
>>> r.links
{}
>>> r.reason
'OK'
>>> r.history()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    r.history()
TypeError: 'list' object is not callable
>>> r.headers
{'Server': 'nginx', 'Content-Type': 'text/html; charset=utf-8', 'X-Frame-Options': 'SAMEORIGIN', 'x-xss-protection': '1; mode=block', 'X-Clacks-Overhead': 'GNU Terry Pratchett', 'Via': '1.1 varnish, 1.1 varnish', 'Content-Length': '48884', 'Accept-Ranges': 'bytes', 'Date': 'Tue, 01 Jan 2019 09:00:01 GMT', 'Age': '418', 'Connection': 'keep-alive', 'X-Served-By': 'cache-iad2133-IAD, cache-ams21026-AMS', 'X-Cache': 'HIT, HIT', 'X-Cache-Hits': '2, 2', 'X-Timer': 'S1546333202.778832,VS0,VE0', 'Vary': 'Cookie', 'Strict-Transport-Security': 'max-age=63072000; includeSubDomains'}
>>> r.headers['Content-Type']
'text/html; charset=utf-8'
>>> r.is_redirect()
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    r.is_redirect()
TypeError: 'bool' object is not callable
>>> r.is_redirect
False
>>> r.raw.read(20)
b''
>>> r
<Response [200]>
>>> type(r)
<class 'requests.models.Response'>
>>> r.content[0:100]
b'<!doctype html>\n<!--[if lt IE 7]>   <html class="no-js ie6 lt-ie7 lt-ie8 lt-ie9">   <![endif]-->\n<!-'
>>> r.text[0:100]
'<!doctype html>\n<!--[if lt IE 7]>   <html class="no-js ie6 lt-ie7 lt-ie8 lt-ie9">   <![endif]-->\n<!-'
>>> r.encoding
'utf-8'
>>> amazon="https://www.amazon.com/Thinking-JavaScript-Aravind-Shenoy-ebook/dp/B00JUI6LUQ/"
>>> r = requests.get(link)
>>> r.url
'https://www.python.org/'
>>> r = requests.get(amazon)
>>> r.url
'https://www.amazon.com/Thinking-JavaScript-Aravind-Shenoy-ebook/dp/B00JUI6LUQ'
>>> r.is_rediect
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    r.is_rediect
AttributeError: 'Response' object has no attribute 'is_rediect'
>>> r.is_redirect
False
>>> r.links
{}
>>> r.next
>>> dir(r.next)
['__bool__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
>>> dir(r.links)
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> help(r.next)
Help on NoneType object:

class NoneType(object)
 |  Methods defined here:
 |  
 |  __bool__(self, /)
 |      self != 0
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.

>>> r.content[0:100]
b'<!doctype html><html lang="en-us" class="a-no-js" data-19ax5a9jf="dingo"><!-- sp:feature:head-start '
>>> help(r)
Help on Response in module requests.models object:

class Response(builtins.object)
 |  The :class:`Response <Response>` object, which contains a
 |  server's response to an HTTP request.
 |  
 |  Methods defined here:
 |  
 |  __bool__(self)
 |      Returns True if :attr:`status_code` is less than 400.
 |      
 |      This attribute checks if the status code of the response is between
 |      400 and 600 to see if there was a client error or a server error. If
 |      the status code, is between 200 and 400, this will return True. This
 |      is **not** a check to see if the response code is ``200 OK``.
 |  
 |  __enter__(self)
 |  
 |  __exit__(self, *args)
 |  
 |  __getstate__(self)
 |  
 |  __init__(self)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __iter__(self)
 |      Allows you to use a response as an iterator.
 |  
 |  __nonzero__(self)
 |      Returns True if :attr:`status_code` is less than 400.
 |      
 |      This attribute checks if the status code of the response is between
 |      400 and 600 to see if there was a client error or a server error. If
 |      the status code, is between 200 and 400, this will return True. This
 |      is **not** a check to see if the response code is ``200 OK``.
 |  
 |  __repr__(self)
 |      Return repr(self).
 |  
 |  __setstate__(self, state)
 |  
 |  close(self)
 |      Releases the connection back to the pool. Once this method has been
 |      called the underlying ``raw`` object must not be accessed again.
 |      
 |      *Note: Should not normally need to be called explicitly.*
 |  
 |  iter_content(self, chunk_size=1, decode_unicode=False)
 |      Iterates over the response data.  When stream=True is set on the
 |      request, this avoids reading the content at once into memory for
 |      large responses.  The chunk size is the number of bytes it should
 |      read into memory.  This is not necessarily the length of each item
 |      returned as decoding can take place.
 |      
 |      chunk_size must be of type int or None. A value of None will
 |      function differently depending on the value of `stream`.
 |      stream=True will read data as it arrives in whatever size the
 |      chunks are received. If stream=False, data is returned as
 |      a single chunk.
 |      
 |      If decode_unicode is True, content will be decoded using the best
 |      available encoding based on the response.
 |  
 |  iter_lines(self, chunk_size=512, decode_unicode=False, delimiter=None)
 |      Iterates over the response data, one line at a time.  When
 |      stream=True is set on the request, this avoids reading the
 |      content at once into memory for large responses.
 |      
 |      .. note:: This method is not reentrant safe.
 |  
 |  json(self, **kwargs)
 |      Returns the json-encoded content of a response, if any.
 |      
 |      :param \*\*kwargs: Optional arguments that ``json.loads`` takes.
 |      :raises ValueError: If the response body does not contain valid json.
 |  
 |  raise_for_status(self)
 |      Raises stored :class:`HTTPError`, if one occurred.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
 |  
 |  apparent_encoding
 |      The apparent encoding, provided by the chardet library.
 |  
 |  content
 |      Content of the response, in bytes.
 |  
 |  is_permanent_redirect
 |      True if this Response one of the permanent versions of redirect.
 |  
 |  is_redirect
 |      True if this Response is a well-formed HTTP redirect that could have
 |      been processed automatically (by :meth:`Session.resolve_redirects`).
 |  
 |  links
 |      Returns the parsed header links of the response, if any.
 |  
 |  next
 |      Returns a PreparedRequest for the next request in a redirect chain, if there is one.
 |  
 |  ok
 |      Returns True if :attr:`status_code` is less than 400, False if not.
 |      
 |      This attribute checks if the status code of the response is between
 |      400 and 600 to see if there was a client error or a server error. If
 |      the status code is between 200 and 400, this will return True. This
 |      is **not** a check to see if the response code is ``200 OK``.
 |  
 |  text
 |      Content of the response, in unicode.
 |      
 |      If Response.encoding is None, encoding will be guessed using
 |      ``chardet``.
 |      
 |      The encoding of the response content is determined based solely on HTTP
 |      headers, following RFC 2616 to the letter. If you can take advantage of
 |      non-HTTP knowledge to make a better guess at the encoding, you should
 |      set ``r.encoding`` appropriately before accessing this property.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __attrs__ = ['_content', 'status_code', 'headers', 'url', 'history', '...

>>> tpe(r)
		 
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    tpe(r)
NameError: name 'tpe' is not defined
>>> type(r)
		 
<class 'requests.models.Response'>
>>> r.headers
		 
{'Content-Type': 'text/html;charset=UTF-8', 'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive', 'Server': 'Server', 'Date': 'Tue, 01 Jan 2019 09:06:56 GMT', 'Strict-Transport-Security': 'max-age=47474747; includeSubDomains; preload', 'Vary': 'Accept-Encoding,User-Agent', 'P3P': 'policyref="https://www.amazon.com/w3c/p3p.xml",CP="CAO DSP LAW CUR ADM IVAo IVDo CONo OTPo OUR DELi PUBi OTRi BUS PHY ONL UNI PUR FIN COM NAV INT DEM CNT STA HEA PRE LOC GOV OTC "', 'Cache-Control': 'no-cache, no-transform', 'Content-Encoding': 'gzip', 'X-XSS-Protection': '1;', 'X-Content-Type-Options': 'nosniff', 'X-Frame-Options': 'SAMEORIGIN', 'x-amz-rid': 'FY7M1HTKW8W81QNB8DY7', 'X-Cache': 'Miss from cloudfront', 'Via': '1.1 7319819fad2b7a4ce76474209cc2df4b.cloudfront.net (CloudFront)', 'X-Amz-Cf-Id': 'xQL6mSAuUrDh4QL4C8uvNb9Hn7TPZ6nJXGRdGYlv-S1TGP6llvWAwA=='}
>>> r.request.headers
		 
{'User-Agent': 'python-requests/2.21.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
>>> dir(r)
		 
['__attrs__', '__bool__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__nonzero__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_content', '_content_consumed', '_next', 'apparent_encoding', 'close', 'connection', 'content', 'cookies', 'elapsed', 'encoding', 'headers', 'history', 'is_permanent_redirect', 'is_redirect', 'iter_content', 'iter_lines', 'json', 'links', 'next', 'ok', 'raise_for_status', 'raw', 'reason', 'request', 'status_code', 'text', 'url']
>>> r.reason
		 
'OK'
>>> r.links()
		 
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    r.links()
TypeError: 'dict' object is not callable
>>> r.links
		 
{}
>>> r.cookies
		 
<RequestsCookieJar[]>
>>> r.raw
		 
<urllib3.response.HTTPResponse object at 0x041CDBF0>
>>> type(r.content)
		 
<class 'bytes'>
>>> 

import urllib2

url = 'https://www.example.com'
username= 'user'
password = 'pass'

request = urllib2.Request(url)

password_manager = urllib2.HTTPPasswordMgrWithDefaultRealm()
password_manager.add_password(None, url, username, password)

auth_manager = urllib2.HTTPBasicAuthHandler(password_manager)
opener = urllib2.build_opener(auth_manager)

urllib2.install_opener(opener)

handler = urllib2.urlopen(request)

print handler.getcode()
print handler.headers.getheader('content-type')

Using Requests: The task of making a simple HTTP GET request can be accomplished in a single line when compared to the large code written using urllib2.

import requests

r = requests.get('https://www.example.com', auth=('user', 'pass'))

print r.status_code

print r.headers['content-type']

Example 2: Making a POST request

Using urllib2/urllib: Note that in this example we had to make use of both the urllib and urllib2 modules in order to write a script for a simple POST request:

import urllib

import urllib2

url = "http://www.example.com"

values = {"firstname":" abc ", "lastname":" xyz "}

header = {"User-Agent":"Mozilla/4.0 (compatible; MSIE 5.5;Windows NT)"}

values = urllib.urlencode(values)

request = urllib2.Request(url, values, header)

response = urllib2.urlopen(request)

html_content = response.read()

Using Requests: Here we do not require import multiple modules and a single requests module can accomplish the entire task:

import requests

values = {""firstname":" abc ", "lastname":" xyz "}

r = requests.post('https://www.example.com, data=values)