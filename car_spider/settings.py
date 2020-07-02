# Scrapy settings for car_spider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from car_spider.constant import SpiderConstant

BOT_NAME = SpiderConstant.BOT_NAME

SPIDER_MODULES = ['car_spider.spiders']
NEWSPIDER_MODULE = 'car_spider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'car_spider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = SpiderConstant.ROBOTSTXT_OBEY

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = SpiderConstant.CONCURRENT_REQUESTS

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = SpiderConstant.DOWNLOAD_DELAY
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = SpiderConstant.COOKIES_ENABLED

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = SpiderConstant.DEFAULT_REQUEST_HEADERS

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = SpiderConstant.SPIDER_MIDDLEWARES

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'car_spider.middlewares.CarSpiderDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = SpiderConstant.ITEM_PIPELINES

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = SpiderConstant.AUTOTHROTTLE_MAX_DELAY
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
AUTOTHROTTLE_DEBUG = SpiderConstant.AUTOTHROTTLE_DEBUG

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# redis
# REDIS_HOST = '127.0.0.1'
# REDIS_URL = 'redis://127.0.0.1'
# REDIS_PORT = 6379
# REDIS_ENCODING = 'utf-8'
# # REDIS_PARAMS = {‘password’:’123456’}
#
#
# # 使用scrapy-redis组件的去重队列
# DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# # 使用scrapy-redis组件自己的调度器
# SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# # 是否允许暂停
# SCHEDULER_PERSIST = True