# IT橘子抓取
##实现：
框架：`scrapy`

实现思路：

1. 根据`url = http://itjuzi.com/company/{}`产生1000个连续页面，分别抓取需要信息和额外的公司网址
2. 去公司页面抓取所有链接，找到包含关键词(如hire, career, zhaopin)的地址存入列表
3. 将所有结果存入json

##时间统计:

学习框架约1小时，实现约1小时，找规律约30分钟，学习xpath等临时使用知识约1小时，debug约2小时

##改进:

1. 未加异常处理
2. 未加入多线程(只使用了scrapy的默认线程)
3. 未加入代理或自动变更user agent，抓多可能会被ban
4. 追求质量可从已上市或其他筛选页面开始抓取，毕竟许多公司质量很低或无招聘页面
5. 有些公司招聘页面可能不在首页，这时候可以尝试搜索站点地图或拼url或从搜索引擎结果抓取（如搜索36kr 招聘 site:36kr.com）
6. 国外访问国内站点速度较慢，放在国内服务器上抓可能会快很多
7. 对于有些hire url不含base url的分别取到,尚未组合
8. 生成json中的中文为Unicode,未解码
9. 未对抓取失败的站点建立log
10. 未对结果去重


##使用:

`scrapy crawl dmoz -o itjuzi.json`
结果存在`itjuzi.json`

`product`为产品
`company`为公司
`location`为地址
`website`为网站
`hire_urls`为招聘地址
