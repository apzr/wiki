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
    htmldata = urllib.urlopen(sys.argv[1]).read()
    
    p = HTML2MoinMoin()
    p.feed(htmldata)
    p.close()


if __name__ == "__main__":
    main()
