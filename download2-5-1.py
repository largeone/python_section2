from urllib.parse import urljoin

baseUrl = "http://test.com/html/a.html"
print(">>", urljoin(baseUrl, "b.htnl"))
print(">>", urljoin(baseUrl, "sub/b.htnl"))
print(">>", urljoin(baseUrl, "../index.html"))
print(">>", urljoin(baseUrl, "../img/img.jpg"))
print(">>", urljoin(baseUrl, "../css/img.css"))
