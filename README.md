# ip_query
ip_quey是一个用来查询相关ip信息的工具。

功能逻辑

1.将IP地址放入txt文件中，通过调用api接口进行批量查询

2.在当前目录下生成查询成功文件夹，文件夹内按照时间生产对应文件夹，文件夹中保存对应ip的查询结果。

3.当查询失败时会将失败的ip存入当前目录下的查询失败文件夹内（大概率是未登录限制查询次数）

4.利用格式化字符串将json中对应的结果保存到txt文件中


结果样列

ip(查询的ip)： 218.190.235.217  
geocode(地理编码): 344081001001 
asn(所属路由)： HUTCHISON-AS-AP HGC Global Communications Limited  
asnCode(路由编码): AS9304  
iana(互联网数字分配国家): 中国香港  
ianaEn(互联网数字分配国家代码)： HK  
country(国家)： 中国  
province（省份）： 香港  
city(城市)： 香港岛  
districts(区县)： 中西区  
isp(运营商): 香港环球全域电讯  
netWorkType(网络类型)： 移动数据  
score(真人概率-不准确)： 63
latitude(纬度)： 30.311684
longitude(经度): 120.343001  
radius(覆盖半经-单位:米): 46.0  
mbRate(秒拨概率): 暂未发现  
continent(所属大陆): AS  
timezone(所属时区)： +0800  
countryCode(国家代码): HK  
provinceCode(省代码): 810000  
cityCode(城市代码): 810100  
districtCode(地区代码)： 810101  
vpn(是否VPN-不准确): False  
tor(是否tor-不准确): False  
proxy(是否代理-不准确)： False  
spider(是否爬虫-不准确) ： False  



