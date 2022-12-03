# proxy-servant
proxy-servant is your best friend that will give you a working proxy every time you request it

## Why and For What?
Proxy-servant developed for a community from a part of that community
My main goal was to develop a package that would accept a set of proxy data, 
send thousands http requests throught those proxies, and know which ones were alive

## Which proxies are supported?
* SOCKS5
* SOCKS4
* HTTP

## How to use?
### Load dataset

```
http://127.0.0.1
http://127.0.0.2
http://127.0.0.3
http://127.0.0.4
```
*dataset.txt*

```py
import proxy_servant

data = proxy_servant.FileDataSource("./proxies.csv")
```

### Instantiate checker
```py
pc = proxy_servant.BasicProxyChecker(data, "https://google.com", timeout=aiohttp.ClientTimeout(connect=8))
```

### Send requests
If you in async function
```py
check_result = await pc.check()
```
or
```
import asyncio
check_result = asyncio.run(pc.check())
```
Now you have list with result of proxy-checking

### Iterate over working proxy
```py
pp = proxy_servant.BasicProxyProvider(check_result) # filtering and saves only working proxies
pp.get_all()

# or

next(pp)

# or

for proxy in pp:
    pass
```

To manage an infinite or finite loop, use the `remove_proxy_after_use` parameter in `BasicProxyProvider`
