# -*- coding: iso-8859-1 -*-
"""
    MoinMoin - ImageLink Macro

    This macro is used to make a link that displays an image (can be given
    as either attachment or URL) and links to either an URL or a wiki page.
    Optionally the size of the image can be adjusted.
    If no target is given the link will point to the image itself.
   
    Since MoinMoin 1.6.0 this macro is replaced by builin markup, see HelpOnLinking 
 
    Syntax:
        <<ImageLink(image, [target,] [width=width, [height=height>>)>>

    Parameters:
        image: image attachment file name or the URL of an image
        target: link target wiki page or URL (optional)

    Keyword Parameters:
        width: rendered image width (optional)
        height: rendered image heigth (optional)
        alt: text for img tag "alt" attribute

    Examples:
        <<ImageLink(M?nchen.png,M?nchen,height=100)>>
        <<ImageLink(Images/M?nchen.png,M?nchen,height=100)>>
        <<ImageLink(http://webcam.portalmuc.de/images/webcam/webcam_marienplatz.jpg,M?nchen Marienplatz)>>
        <<ImageLink(plot.png,width=200)>>
        <<ImageLink(plot.png,height=200)>>
        <<ImageLink(plot.png)>>
        <<ImageLink(http://webcam.portalmuc.de/images/webcam/webcam_marienplatz.jpg,http://www.muenchen.de,width=150)>>
        <<ImageLink(m?nchen.png,http://www.muenchen.de,width=50)>>
        <<ImageLink(http://webcam.portalmuc.de/images/webcam/webcam_marienplatz.jpg)>>
        <<ImageLink(example.png,alt=whateveryouwant(???))>>
        <<ImageLink(http://moinmo.in/OliverSiemoneit?action=AttachFile&do=get&target=screenshot.png,width=647,height=517,alt=OliverSiemoneit?action=AttachFile&do=get&target=screenshot,FrontPage)>>

    History:
        Jeff Kunce: 
            wrote the first published version of this macro in 2001.
        
        Reimar Bauer:
            2004 intitial new version for MoinMoin 1.2
        
        Marcin Zalewski:   
            Implemented wikiutil.link_tag and macro.formatter.pagelink.
            Added title attribute to the created link. One could generalize that to
            add arbitrary attributes.

            One could also add class attributes to <a> and/or <img> elements.
            I do not see the need for such modifications. If however this is
            to be done in the future one would need to add 'html_class' key to the kw dictionary
            with a corresponding value to add class to <img> element. To add class to <a> element
            one needs to add 'css_class' key with a corresponding value to the dictionary passed to
            pagelink call.
        
       Reimar Bauer:    
            2004-12-23 Adapted to MoinMoin Version 1.3.1-1
            2004-12-23 Syntax change Version 1.3.1-2
                   width and height and probably other keywords must be given as keywords (e.g. height=20)
            2004-12-31 Version 1.3.1-3 code clean up
            2005-01-16 Bug fixed in the errorhandler - found and patched by Malte Helmert
            2005-03-05 Version 1.3.3-5 Bug fixed found by cypress ("If I put <<ImageLink(moinmoin.png)>> it bombs")
            2005-03-28 Version 1.3.3-6 feature request added by CDPark:
                       "Can we use an external image? And an external target?"
            2005-04-16 Version 1.3.3-7 no default alt tag definition as requested by CDPark and AlexanderSchremmer
       
       Chong-Dae Park:
            2005-04-17 Version 1.3.3-8 code refactored
                       IMG with no alt tag is not recommended in the HTML standard.
                       It keeps a user specified alt tag. If there is none, it tries to make on using the WikiName
                       or image name instead.
       
       Reimar Bauer:
            2005-04-21 Version 1.3.3-9 bug fixed
                       When the image does not exist yet, it gives you a "Upload Image" link, this link does not
                       work. I suspect that this only is a problem on sub-pages, caused by incorrect escaping of
                        "/". -- CraigJohnson
 
            2005-12-19 Versiom 1.5.0-10 feature added to link to images on different wiki pages
            2006-02-14 Version 1.5.2-11 bug fixed for filename of attached image is Chinese (encode added)
            2006-02-22 Version 1.5.2-12 code refactored

      Thomas Waldmann
            2006-03-10 code refactored
            
      Reimar Bauer
             2006-09-22 bug fix of image linked to attachment and inline
             2006-10-08 patch of DavidLinke added and keys now only lowercase used
             2006-12-16 interwikilink for pages added

    @copyright: 2001 by Jeff Kunce,
                2004 by Marcin Zalewski,
                2006 by MoinMoin:ThomasWaldmann,
                2004-2007 by MoinMoin:ReimarBauer
                
    @license: GNU GPL, see COPYING for details.
"""

from MoinMoin import wikiutil
from MoinMoin.action import AttachFile

def _is_URL(text):
    """ Answer true if text is an URL.
        The method used here is pretty dumb. Improvements are welcome.
    """
    return '://' in text

def explore_args(args, kwAllowed):
    """ 
    explore args for positional and keyword parameters
    """
    if args:
        args = args.split(',')
        args = [arg.strip() for arg in args]
    else:
        args = []

    kw_count = 0
    kw = {} # create a dictionary for the formatter.image call
    pp = [] # positional parameter

    if not kwAllowed:
        return pp, 0, kw, 0

    for arg in args:
        if '=' in arg:
            key, value = arg.split('=', 1)
            # avoid that urls with "=" are interpreted as keyword
            if key.lower() not in kwAllowed:
                if not kw_count and _is_URL(arg):
                    # assuming that this is the image
                    pp.append(wikiutil.escape(arg, quote=1))
                continue
            kw_count += 1
            kw[str(key.lower())] = wikiutil.escape(value, quote=1)
        else:
            pp.append(wikiutil.escape(arg, quote=1))

    return pp, len(pp), kw, len(kw)

def execute(macro, args):
    request = macro.request
    _ = request.getText
    formatter = macro.formatter

    kwAllowed = ['width', 'height', 'alt']
    pp, pp_count, kw, kw_count = explore_args(args, kwAllowed)

    if not pp_count or pp_count and not pp[0]:
        msg = 'Not enough arguments given to ImageLink macro! Try <<ImageLink(example.png, WikiName, width=200)>>.'
        return "%s%s%s" % (formatter.sysmsg(1), formatter.text(msg), formatter.sysmsg(0))

    image = pp[0]
    if pp_count >= 2 and pp[1]:
        target = pp[1]
        if target.startswith('attachment:') or target.startswith('inline:'):
            if target.startswith('attachment:'):
                target = (target.split('attachment:'))[1]
                pagename, attname = AttachFile.absoluteName(target, formatter.page.page_name)
                target = AttachFile.getAttachUrl(pagename, target, request)
            elif target.startswith('inline:'):
                target = (target.split('inline:'))[1]
                pagename, attname = AttachFile.absoluteName(target, formatter.page.page_name)
                target = AttachFile.getAttachUrl(pagename, target, request, do='view')

            if not AttachFile.exists(request, pagename, attname):
                linktext = _('Upload new attachment "%(filename)s"', formatted=False)
                return wikiutil.link_tag(request,
                                         ('%s?action=AttachFile&rename=%s' % (
                                         wikiutil.quoteWikinameURL(pagename),
                                         wikiutil.url_quote_plus(attname))),
                                         linktext % {'filename': attname})

            kw['src'] = AttachFile.getAttachUrl(pagename, image, request)

    elif pp_count == 1:
        pagename, attname = AttachFile.absoluteName(image, formatter.page.page_name)
        target = AttachFile.getAttachUrl(pagename, image, request)
    else:
        target = None

    if _is_URL(image):
        kw['src'] = image
    else:
        pagename, attname = AttachFile.absoluteName(image, formatter.page.page_name)
        kw['src'] = AttachFile.getAttachUrl(pagename, attname, request)
        if not AttachFile.exists(request, pagename, attname):
            linktext = _('Upload new attachment "%(filename)s"', formatted=False)
            return wikiutil.link_tag(request,
                                     ('%s?action=AttachFile&rename=%s' % (
                                         wikiutil.quoteWikinameURL(pagename),
                                         wikiutil.url_quote_plus(attname))),
                                         linktext % {'filename': attname})

    if 'alt' not in kw:
        if target is None or _is_URL(target):
            if _is_URL(image):
                # Get image name http://here.com/dir/image.png -> image.png
                kw['alt'] = wikiutil.taintfilename(formatter.text(image.split('/')[-1]))
            else:
                kw['alt'] = attname
        else:
            kw['alt'] = target

    if target is None:
        target = kw['src']

    if pp_count == 1:
        return "%s%s%s" % (formatter.url(1, kw['src']),
                           formatter.image(**kw),
                           formatter.url(0))

    if _is_URL(target) or 'action=AttachFile&do=get&target=' in target or 'action=AttachFile&do=view&target=' in target:
        return "%s%s%s" % (formatter.url(1, target),
                           formatter.image(**kw),
                           formatter.url(0))
    else:
        if ":" in target:
            if target.startswith('wiki:'):
                target = target[5:]
            wikitag, wikiurl, wikitail, error = wikiutil.resolve_wiki(request, target)
            url = wikiurl + wikiutil.quoteWikinameURL(wikitail)
            return "%s%s%s" % (formatter.url(1, url),
                               formatter.image(**kw),
                               formatter.url(0))
        else:
            return "%s%s%s" % (formatter.pagelink(1, target),
                               formatter.image(**kw),
                               formatter.pagelink(0))

