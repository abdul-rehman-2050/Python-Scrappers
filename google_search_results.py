import urllib
import requests
from lxml import html
import matplotlib.pyplot as plt



search_engine = 'http://www.google.com/search?';
qlist = ['hello world in arduino',
         'arduino projects',
         'arduino tutorials',
         'best tutorial',
         'arduino',
         'arduino in pakistan',
         'hardware of arduino']


all_stat_list=[]
for query in qlist:
    try:
        qstr=urllib.urlencode({'q':query})
        cur_url = search_engine+qstr
        r=requests.get(cur_url)
        doc = html.fromstring(r.text)
        title = doc.xpath('//title')[0]
        stat = doc.xpath('//*[@id="resultStats"]')[0]
        print stat.text_content() + " for keyword \'"+ query+"\'"
        stat_list = stat.text_content().split(" ")
        cur_stat_int = int(stat_list[1].replace(',',''))
        all_stat_list.append(cur_stat_int/10e5)
        print cur_stat_int
    except:
        pass

plt.plot(range(0,len(qlist)),all_stat_list)
plt.plot(range(0,len(qlist)),all_stat_list,'ro')
plt.ylabel('Results in Millions')
plt.title('Google Query Results')
for i in range(len(qlist)):
    plt.annotate(qlist[i], (i,all_stat_list[i]))
#plt.axis([1, len(qlist), 1, max(all_stat_list)])
    
plt.show()    
    
