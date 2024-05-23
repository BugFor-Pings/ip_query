# Pings 2024-05-23

import argparse
import requests
import os
from datetime import datetime

# 创建解析器
parser = argparse.ArgumentParser(description='查询IP信息，并将查询结果保存为txt文件.')
# 添加参数
parser.add_argument('-t', '--target', help='查询单个IP地址.')
parser.add_argument('-f', '--file', help='批量查询txt文件中的ip地址，每行一个.')
# 解析命令行参数
args = parser.parse_args()

# API的基础URL
base_url = "https://cz88.net/api/cz88/ip/accurate?ip="

# 请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
}

# 确保目录存在，如果不存在则创建
def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# 函数用于查询单个IP地址并保存结果
def query_ip(ip):
    response = requests.get(base_url + ip, headers=headers)
    if response.status_code == 200:
        json_data = response.json()
        if json_data.get("success"):
            data = json_data.get("data", {})
            locations = data.get("locations", [{}])
            if locations:  
                location = locations[0]
            else:
                location = {"latitude": "无", "longitude": "无", "radius": "无"}
            data["latitude"] = location.get("latitude", "无")
            data["longitude"] = location.get("longitude", "无")
            data["radius"] = location.get("radius", "无")
            return data
        else:
            print(f"Query failed for IP: {ip} with message: {json_data.get('message')}")
            return None
    else:
        print(f"Failed to get data for IP: {ip} with status code: {response.status_code}")
        return None

# 函数用于格式化数据并保存到txt文件
def save_formatted_data(data, ip, dir_path):
    formatted_data = (
       f"ip(查询的ip)： {data.get('ip')}  \n"
            f"geocode(地理编码): {data.get('geocode')} \n"
            f"asn(所属路由)： {data.get('asn')}  \n"
            f"asnCode(路由编码): {data.get('asnCode')}  \n"
            f"iana(互联网数字分配国家): {data.get('iana')}  \n"
            f"ianaEn(互联网数字分配国家代码)： {data.get('ianaEn')}  \n"
            f"country(国家)： {data.get('country')}  \n"
            f"province（省份）： {data.get('province')}  \n"
            f"city(城市)： {data.get('city')}  \n"
            f"districts(区县)： {data.get('districts') or '无'}  \n"
            f"isp(运营商): {data.get('isp')}  \n"
            f"netWorkType(网络类型)： {data.get('netWorkType')}  \n"
            f"score(真人概率-不准确)： {data.get('score')} \n"
            f"latitude(纬度)： {data.get('latitude')} \n"
            f"longitude(经度): {data.get('longitude')}  \n"
            f"radius(覆盖半经-单位:米): {data.get('radius')}  \n"
            f"mbRate(秒拨概率): {data.get('mbRate')}  \n"
            f"continent(所属大陆): {data.get('continent')}  \n"
            f"timezone(所属时区)： {data.get('timezone')}  \n"
            f"countryCode(国家代码): {data.get('countryCode')}  \n"
            f"provinceCode(省代码): {data.get('provinceCode')}  \n"
            f"cityCode(城市代码): {data.get('cityCode')}  \n"
            f"districtCode(地区代码)： {data.get('districtCode', '无')}  \n"
            f"vpn(是否VPN-不准确): {data.get('vpn')}  \n"
            f"tor(是否tor-不准确): {data.get('tor')}  \n"
            f"proxy(是否代理-不准确)： {data.get('proxy')}  \n"
            f"spider(是否爬虫-不准确) ： {data.get('spider')}  \n"
    )
    filename = f"ip_{data.get('ip')}_查询成功.txt"
    file_path = os.path.join(dir_path, filename)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(formatted_data)
    print(f"Data for IP {data.get('ip')} has been saved to {file_path}")

# 保存错误信息到error.txt
def save_error(ip, dir_path):
    error_message = f"Query failed for IP: {ip} on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    file_path = os.path.join(dir_path, "error.txt")
    with open(file_path, 'a', encoding='utf-8') as file:  # 使用'a'模式来追加内容
        file.write(error_message + "\n")
    print(f"Error for IP {ip} has been saved to {file_path}")

# 处理单个IP查询
if args.target:
    ip = args.target
    data = query_ip(ip)
    if data:
        dir_path = os.path.join('查询成功', datetime.now().strftime('%Y_%m_%d'))
        ensure_dir(dir_path)
        save_formatted_data(data, ip, dir_path)
    else:
        dir_path = os.path.join('查询失败', datetime.now().strftime('%Y_%m_%d'))
        ensure_dir(dir_path)
        save_error(ip, dir_path)

# 处理文件中的IP列表查询
elif args.file:
    ips_file_path = args.file
    if not os.path.isfile(ips_file_path):
        print(f"The file {ips_file_path} does not exist.")
        exit(1)
    
    with open(ips_file_path, 'r', encoding='utf-8') as file:
        ips = file.readlines()
    for ip in ips:
        ip = ip.strip()
        if ip:
            data = query_ip(ip)
            if data:
                dir_path = os.path.join('查询成功', datetime.now().strftime('%Y_%m_%d'))
                ensure_dir(dir_path)
                save_formatted_data(data, ip, dir_path)
            else:
                dir_path = os.path.join('查询失败', datetime.now().strftime('%Y_%m_%d'))
                ensure_dir(dir_path)
                save_error(ip, dir_path)

# 如果没有提供-t或-f参数，显示帮助信息
else:
    parser.print_help()