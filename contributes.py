# -*- coding: utf-8 -*-
# @Author: detailyang
# @Date:   2016-10-16 17:12:16
# @Last Modified by:   detailyang
# @Last Modified time: 2016-10-16 19:38:52

#from https://github.com/users/detailyang/pinned_repositories_modal


import requests
import json

repos = '''
  id-generator 19
  nginx-location-match-visible 11
  lua-resty-socks5-server 6
  pre-commit-shell 10
  awesome-cheatsheet 2,774
  sindresorhus/awesome 44,584
  tiimgreen/github-cheat-sheet 20,048
  wsargent/docker-cheat-sheet 7,811
  audreyr/favicon-cheat-sheet 7,556
  ant-design/ant-design 6,145
  alibaba/tengine 4,750
  haiwen/seafile 4,214
  WebpageFX/emoji-cheat-sheet.com 4,206
  nodejs/http-parser 2,884
  ai/easings.net 2,535
  Jam3/math-as-code 2,506
  foru17/front-end-collect 2,344
  tj/consolidate.js 2,089
  fisherman/fisherman 1,731
  a8m/go-lang-cheat-sheet 1,615
  soulmachine/machine-learning-cheat-sheet 1,428
  rakyll/coop 1,165
  JesseObrien/laravel-cheatsheet 1,056
  iwasrobbed/Objective-C-CheatSheet 834
  SpiderLabs/owasp-modsecurity-crs 724
  thank-you-github/thank-you-github 716
  joemasilotti/UI-Testing-Cheat-Sheet 687
  vuejs/vuejs.org 610
  iwasrobbed/Swift-CheatSheet 530
  nodejs/nodejs.org 486
  openresty/headers-more-nginx-module 478
  dwtkns/gdal-cheat-sheet 474
  linode/docs 469
  tanprathan/MobileApp-Pentest-Cheatsheet 430
  yaoweibin/nginx_upstream_check_module 428
  refinery29/react-native-cheat-sheet 386
  fzzy/radix 339
  p0pr0ck5/lua-resty-waf 249
  openresty/test-nginx 151
  jeremycx/node-LDAP 148
  collective/collective.github.com 110
  youzan/tiny-loader.js 110
  niklongstone/regular-expression-cheat-sheet 98
  hiboma/hiboma 84
  soulteary/Get-D2-2014-Ticket 82
  gnuhpc/All-About-Redis 79
  google/vogon 30
  indutny/ocsp 27
  calio/ragel-cheat-sheet 24
  wireshark-nsq 15
  cas-server 8
  ngx_http_updown 8
  x-v8/ngx_http_cors_filter 5
  cas-x/cas-server 4
  zoneproxy 4
  pre-commit/pre-commit.github.io 4
  awesome-wireshark-dissector 3
  hikarian 3
  luaproxy 3
  nodejs/build-container-sync 3
  cas-nginx_http_auth_module 2
  lua-resty-cors 2
  x-v8/nginx-xmind 2
  x-v8/ngx_http_barcode 2
  cas-x/cas-nginx_http_auth_module 1
  cas-x/lua-resty-cas 1
  awesome 1
  blog 1
  cas-ldap 1
  nginx_upstream_check_module 1
  ngx_http_barcode 1
  ngx_http_cors_filter 1
  ngx_http_qrcode_module 1
  pix 1
  x-v8/ngx_http_qrcode_module 1
  x-v8/ngx_http_reqstat_module 1
  x-v8/ngx_http_updown 1
  1v2/bootstrap 0
  1v2/logo 0
  cas-x/cas-doc 0
  cas-x/cas-exmailqq 0
  cas-x/cas-exwechat 0
  cas-x/cas-gitlab 0
  cas-x/cas-ldap 0
  cas-x/cas-logo 0
  cas-x/cas-nginx_http_ssl_auth_module 0
  cas-x/cas-ssh-auth-server 0
  chenyangdo/webfront 0
  cloudcopy/seafile 0
  All-About-Redis 0
  ant-design 0
  awesome-docker 0
  bifrost 0
  Bootstrap-Admin-Template 0
  build-container-sync 0
  bundler 0
  cas-doc 0
  cas-exmailqq 0
  cas-exwechat 0
  cas-gitlab 0
  consolidate.js 0
  dayofstap 0
  demo_signals 0
  detailyang.github.io 0
  docs 0
  esl 0
  fisherman 0
  fisherman.github.io 0
  github-cheat-sheet 0
  headers-more-nginx-module 0
  http-parser 0
  koa 0
  learn 0
  logger 0
  logo 0
  lua-nginx-module 0
  lua-resty-cookie 0
  lua-resty-dns 0
  lua-resty-http 0
  lua-resty-iputils 0
  lua-resty-upload 0
  lua-resty-waf 0
  ncp 0
  nginx 0
  nginx-auth-request-module 0
  nginx-devel-utils 0
  nginx-systemtap-toolkit 0
  ngx_queue 0
  node-LDAP 0
  nodejs.org 0
  ocsp 0
  openresty 0
  opm 0
  php-barcode 0
  pre-commit-php 0
  pre-commit.github.io 0
  programming-openresty-zh 0
  react-enroute 0
  react-router 0
  reading-code-of-nginx-1.9.2 0
  redis 0
  repo 0
  requests 0
  seafile 0
  stream-lua-nginx-module 0
  tengine 0
  test-nginx 0
  thank-you-github 0
  tiny-loader.js 0
  tsar 0
  utf8_validator.lua 0
  vogon 0
  vuejs.org 0
  ybw 0
  zint 0
  eladiomejutogracia/tech-cheatsheet 0
  golang-mirrors/radix 0
  jkhowland/static-landing 0
  koa-grace/grace-consolidate 0
  x-v8/bkb 0
  x-v8/generator-nginx-http-module 0
  x-v8/nginx-faq 0
  x-v8/ngx-http-stub-status-rt 0
  x-v8/ngx-insides 0
  x-v8/ngx_http_auth_file_module 0
  x-v8/ngx_http_fproxy_module 0
  x-v8/ngx_http_redis_cluster_module 0
  zhangfengbing/front-end 0
'''

data = []
for line in repos.splitlines():
  if '/' not in line:
    continue

  #filter
  if 'cas' in line or 'x-v8' in line:
    continue

  repo_name, star = line.strip().split(' ')
  r = requests.get(
    'https://api.github.com/repos/{repo_name}/commits?author=detailyang'.format(repo_name=repo_name))
  commits = r.json()
  if len(commits) == 0:
    continue

    zhangfengbing/front-end
  r = requests.get(
    'https://api.github.com/repos/{repo_name}'.format(repo_name=repo_name)
    )
  repo = r.json()

  data.append({
    'name': repo['name'],
    'url': repo['html_url'],
    'desc': repo['description'],
  })

with open('./contributes.json', 'w') as f:
  json.dump(data, f)
