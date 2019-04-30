from time import time
import urllib.request
import re


class Browser:
    url_data = {}
    __regex_pat = r"href=['\"]?(https?[^'\" >]+)"

    def __init__(self, url):
        self.url = url.lower()
        self.data = None

        if self.url not in self.url_data:
            self.url_data.update({self.url: None})

    @property
    def context(self):
        if self.url_data[self.url] is None:
            with urllib.request.urlopen(self.url) as data:
                out = data.read().decode('utf8')
                self.url_data[self.url] = out
            return out
        else:
            return self.url_data[self.url]

    @property
    def links(self):
        result = re.findall(self.__regex_pat, self.context)
        return_list = []
        for link in result:
            return_list.append(Browser(link))
        return return_list


a = Browser('https://python.org')
b = Browser('https://python.org')
c = Browser('https://stackoverflow.com')
d = Browser('https://stackoverflow.com')
e = Browser('https://python.org')

tic1 = time()
x1 = a.context
toc1 = time()
time1 = (toc1 - tic1) * 1000
print(a.url + ":\t\t\t", time1, "MS")

tic2 = time()
x2 = b.context
toc2 = time()
time2 = (toc2 - tic2) * 1000
print(b.url + ":\t\t\t", time2, "MS")

tic3 = time()
x3 = c.context
toc3 = time()
time3 = (toc3 - tic3) * 1000
print(c.url + ":\t", time3, "MS")

tic4 = time()
x4 = d.context
toc4 = time()
time4 = (toc4 - tic4) * 1000
print(d.url + ":\t", time4, "MS")

tic5 = time()
x5 = e.context
toc5 = time()
time5 = (toc5 - tic5) * 1000
print(e.url + ":\t\t\t", time5, "MS")

print()
for _ in e.links:
    print(_.url)
