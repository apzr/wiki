#!/usr/bin/python2
#coding:utf-8
"""
Usage:
  moinconvert URL

Retrives the given URL and convert it to MoinMoin markup. The result is
written to stdout.
"""

import htmlentitydefs, sys

from HTMLParser import HTMLParser

class HTML2MoinMoin(HTMLParser):

    start_tags = {
        "a"     : " [%(0)s ",
        "b"     : "'''",
        "em"    : "''",
        "tt"    : "{{{",
        "pre"   : "\n{{{",
        "p"     : "\n\n",
        "br"    : "\n\n",
        "h1"    : "\n\n= ",
        "h2"    : "\n\n== ",
        "h3"    : "\n\n=== ",
        "h4"    : "\n\n==== ",
        "h5"    : "\n\n===== ",
        "title" : "TITLE: ",
        "table" : "\n",
        "tr"    : "",
        "td"    : "||"
        }

    end_tags = {
        "a"     : ']',
        "b"     : "'''",
        "em"    : "''",
        "tt"    : "}}}",
        "pre"   : "}}}\n",
        "p"     : "",
        "h1"    : " =\n\n",
        "h2"    : " ==\n\n",
        "h3"    : " ===\n\n",
        "h4"    : " ====\n\n",
        "h5"    : " =====\n\n",
        "table" : "\n", 
        "tr"    : "||\n",
        "dt"    : ":: "
        }

    def __init__(self):
        HTMLParser.__init__(self)
        self.output = sys.stdout
        self.list_mode = []
        self.preformatted = False
        self.verbose = 0

    def write(self, text):
        self.output.write(text)

    def do_ul_start(self, attrs, tag):
        self.list_mode.append("*")

    def do_ol_start(self, attrs, tag):
        self.list_mode.append("1.")

    def do_dl_start(self, attrs, tag):
        self.list_mode.append("")

    def do_ul_end(self, tag):
        self.list_mode = self.list_mode[:-1]

    do_ol_end = do_ul_end
    do_dl_end = do_ul_end

    def do_li_start(self, args, tag):
        self.write("\n" + " " * len(self.list_mode) + self.list_mode[-1])

    def do_dt_start(self, args, tag):
        self.write("\n" + " " * len(self.list_mode) + self.list_mode[-1])

    def do_pre_start(self, args, tag):
        self.preformatted = True
        self.write(self.start_tags["pre"])

    def do_pre_end(self, tag):
        self.preformatted = False
        self.write(self.end_tags["pre"])

    def handle_starttag(self, tag, attrs):
        func = HTML2MoinMoin.__dict__.get("do_%s_start" % tag,
                                         HTML2MoinMoin.do_default_start)
        if ((func == HTML2MoinMoin.do_default_start) and
            self.start_tags.has_key(tag)):
            attr_dict = {}
            i = 0
            for a in attrs:
                attr_dict[a[0]] = a[1]
                attr_dict[str(i)] = a[1]
                i += 1
            self.write(self.start_tags[tag] % attr_dict)
        else:
            func(self, attrs, tag)

    def handle_endtag(self, tag):
        func = HTML2MoinMoin.__dict__.get("do_%s_end" % tag,
                                         HTML2MoinMoin.do_default_end)
        if ((func == HTML2MoinMoin.do_default_end) and
            self.end_tags.has_key(tag)):
            self.write(self.end_tags[tag])
        else:
            func(self, tag)

    def handle_data(self, data):
        if self.preformatted:
            self.write(data)
        else:
            self.write(data.replace("\n", " "))

    def handle_charref(self, name):
        self.write(name)

    def handle_entityref(self, name):
        if htmlentitydefs.entitydefs.has_key(name):
            self.write(htmlentitydefs.entitydefs[name])
        else:
            self.write("&" + name)

    def do_default_start(self, attrs, tag):
        if self.verbose:
            print "Encountered the beginning of a %s tag" % tag
            print "Attribs: %s" % attrs
            
    def do_default_end(self, tag):
        if self.verbose:
            print "Encountered the end of a %s tag" % tag


def main():
    import urllib
    
    #htmldata = urllib.urlopen(sys.argv[1]).read().decode('UTF-8')
    
    #print sys.getdefaultencoding() 
    reload(sys)
    sys.setdefaultencoding('utf8')  
    #print sys.getdefaultencoding() 
    htmldata = '<section class="ouvJEz"><h1 class="_1RuRku">给Docker容器添加端口映射</h1><div class="rEsl9f"><div class="_2mYfmT"><a class="_1qp91i _1OhGeD" href="/u/e929466cfe77" target="_blank" rel="noopener noreferrer"><img class="_13D2Eh" src="https://upload.jianshu.io/users/upload_avatars/15519803/22a567f4-d800-4388-a041-58e0eac6578d.jpg?imageMogr2/auto-orient/strip|imageView2/1/w/96/h/96/format/webp" alt=""></a><div style="margin-left: 8px;"><div class="_3U4Smb"><span class="FxYr8x"><a class="_1OhGeD" href="/u/e929466cfe77" target="_blank" rel="noopener noreferrer">ThinkJava</a></span><button data-locale="zh-CN" type="button" class="_3kba3h _1OyPqC _3Mi9q9 _34692-"><span>关注</span></button></div><div class="s-dsoj"><span class="_3tCVn5"><i aria-label="ic-diamond" class="anticon"><svg width="1em" height="1em" fill="currentColor" aria-hidden="true" focusable="false" class=""><use xlink:href="#ic-diamond"></use></svg></i><span>0.167</span></span><time datetime="2019-03-19T01:48:12.000Z">2019.03.19 09:48:12</time><span>字数 110</span><span>阅读 2,349</span></div></div></div></div><article class="_2rhmJa"><h2>前言</h2><p>给docker正在运行的容器加端口映射</p><h3>方式一（提交当前容器为镜像，使用run -p映射）</h3><div class="_2Uzcx_"><button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em" fill="currentColor" aria-hidden="true"><path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button><pre class="line-numbers  language-bash"><code class="  language-bash">#指令会将容器的80端口映射到宿主机的8000端口上。docker run -p 8000:80 -it centos /bin/bash<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span></span></code></pre></div><h3>方式二（防火墙层处理）</h3><p>如果没有<code>/etc/sysconfig/iptables</code>这个文件，可以参考文章<a href="https://www.jianshu.com/p/c08d27c48cf8" target="_blank">centos创建iptables文件</a><br><strong><em>一、添加规则</em></strong></p><ul><li>获取到docker容器的ip地址</li></ul><div class="_2Uzcx_"><button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em" fill="currentColor" aria-hidden="true"><path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button><pre class="line-numbers  language-bash"><code class="  language-bash">docker ps #查看运行中的容器，查看容器iddocker inspect c5ea97ccc82d | grep IPAddress ##其中 c5ea97ccc82d 为容器id<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span></span></code></pre></div><ul><li>将docker容器的80端口映射到宿主机主机的8091端口</li<div class="_2Uzcx_"><button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em" fill="currentColor" aria-hidden="true"><path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button><pre class="line-numbers  language-css"><code class="  language-css">#将docker容器的80端口映射到宿主机主机的8091端口iptables -t nat -A  DOCKER -p tcp --dport 8091 -j DNAT --to-destination 172.17.0.19<span class="token punctuation">:</span>80#保存防火墙service iptables save<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span></span></code></pre></div><p><strong><em>二、测试规则</em></strong></p><div class="_2Uzcx_"><button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em" fill="currentColor" aria-hidden="true"><path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button><pre class="line-numbers  language-css"><code class="  language-css">#192.168.1.208 为宿主机ip#8091为以上配置宿主机portcurl 192.168.1.208<span class="token punctuation">:</span>8091#80端口是web服务器默认端口，即访问到docker nginx 欢迎页面。<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span><span></span><span></span></span></code></pre></div></article><div></div><div class="_1kCBjS"><div class="_18vaTa"><div class="_3BUZPB"><div class="_2Bo4Th" role="button" tabindex="-1" aria-label="给文章点赞"><i aria-label="ic-like" class="anticon"><svg width="1em" height="1em" fill="currentColor" aria-hidden="true" focusable="false" class=""><use xlink:href="#ic-like"></use></svg></i></div><span class="_1LOh_5" role="button" tabindex="-1" aria-label="查看点赞列表">1人点赞<i aria-label="icon: right" class="anticon anticon-right"><svg viewBox="64 64 896 896" focusable="false" class="" data-icon="right" width="1em" height="1em" fill="currentColor" aria-hidden="true"><path d="M765.7 486.8L314.9 134.7A7.97 7.97 0 0 0 302 141v77.3c0 4.9 2.3 9.6 6.1 12.6l360 281.1-360 281.1c-3.9 3-6.1 7.7-6.1 12.6V883c0 6.7 7.7 10.4 12.9 6.3l450.8-352.1a31.96 31.96 0 0 0 0-50.4z"></path></svg></i></span></div><div class="_3BUZPB"><div class="_2Bo4Th" role="button" tabindex="-1"><i aria-label="ic-dislike" class="anticon"><svg width="1em" height="1em" fill="currentColor" aria-hidden="true" focusable="false" class=""><use xlink:href="#ic-dislike"></use></svg></i></div></div></div><div class="_18vaTa"><a class="_3BUZPB _1x1ok9 _1OhGeD" href="/nb/34334676" target="_blank" rel="noopener noreferrer"><i aria-label="ic-notebook" class="anticon"><svg width="1em" height="1em" fill="currentColor" aria-hidden="true" focusable="false" class=""><use xlink:href="#ic-notebook"></use></svg></i><span>技术实战</span></a><div class="_3BUZPB ant-dropdown-trigger"><div class="_2Bo4Th"><i aria-label="ic-others" class="anticon"><svg width="1em" height="1em" fill="currentColor" aria-hidden="true" focusable="false" class=""><use xlink:href="#ic-others"></use></svg></i></div></div></div></div><div class="_19DgIp" style="margin-top:24px;margin-bottom:24px"></div><div class="d0hShY"><a class="_1bPVBH _1OhGeD" href="/u/e929466cfe77" target="_blank" rel="noopener noreferrer"><img class="_27NmgV" src="https://upload.jianshu.io/users/upload_avatars/15519803/22a567f4-d800-4388-a041-58e0eac6578d.jpg?imageMogr2/auto-orient/strip|imageView2/1/w/100/h/100/format/webp" alt="  "></a><div class="Uz-vZq"><div class="Cqpr1X"><a class="HC3FFO _1OhGeD" href="/u/e929466cfe77" title="ThinkJava" target="_blank" rel="noopener noreferrer">ThinkJava</a><span class="_2WEj6j" title="欢迎关注订阅号「学堂二三事」，分享孩子们在学校里的小故事，在记录、沟通和思考中更全面地认识孩子...">欢迎关注订阅号「学堂二三事」，分享孩子们在学校里的小故事，在记录、沟通和思考中更全面地认识孩子...</span></div><div class="lJvI3S"><span>总资产8 (约0.55元)</span><span>共写了2.5W字</span><span>获得108个赞</span><span>共19个粉丝</span></div></div><button data-locale="zh-CN" type="button" class="_1OyPqC _3Mi9q9"><span>关注</span></button></div></section>'.encode().decode('utf8')
    
    p = HTML2MoinMoin()
    p.feed(htmldata)
    p.close()


if __name__ == "__main__":
    main()
