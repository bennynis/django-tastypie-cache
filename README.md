## Django Tastypie Cache


This is a front end cache implementation for Django Tastypie.  This isn't an ideal solution
as putting a front end HTTP cache such as Varnish is much more appropriate.  However, I've found
that this solution works quite well to reduce response time for incoming API requests.  The premise
is fairly simple.  We cache the entire serialized response for a period of time.  When new requests
come in we check the cache for an existing computed key and if found return that serialized response.  Due
to caching the serialized response, several methods inside the Resource object had to be over ridden.


### Installation

To utilize the cache resource, you can either download the mixin, or install from source

	pip install git+git://github.com/dstegelman/django-tastypie-cache.git@master
	
Import the cache mixin and inherit it before the Resource

	class EventResource(CachedResource, Resource):
	
### Settings

There are two settings used in this mixin.  

	API_CACHE_ENABLE = True
	
This setting enables the cache altogether.  It is disabled by default, to enable
caching you'll need to set this to True.
	
	API_CACHE_LENGTH = 900
	
This setting dictates the length of the cache. By default its set to 900.
