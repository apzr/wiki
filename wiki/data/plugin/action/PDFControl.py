# -*- coding: iso-8859-1 -*-
"""
    MoinMoin - PDFControl macro to control the PDF action plugin output

    Dedicated for HTMLDOC aspecially for the PDF action plugin this macro
    allow to control the processing of HTMLDOC.

    A overview about available features gives the HTMLDOC documentation:
    http://www.htmldoc.org/documentation.php/Comments.html#COMMENTS

    @copyright: 2006  Raphael Bossek <raphael.bossek@solutions4linux.de>
    @license: GNU GPL, see COPYING for details.

    2006-11-14  Raphael Bossek
    * Release v1.0.1
    * Moin 1.6 support added.

    2006-08-31  Raphael Bossek
    * Initial release v1.0.0
"""

def execute (macro, args):
	msg = u''
	if args:
		msg += u'<!-- %s -->' % (args,)
		if macro.request.form.has_key(u'button_preview'):
			msg += u'<span style="cursor: help; border-bottom: 1px dashed;" title="PDFControl: %s">&nbsp;&para;</span>' % (args,)
	elif macro.request.form.has_key(u'button_preview'):
		_ = macro.request.getText
		msg += macro.formatter.paragraph (1, css_class='error')
		msg += macro.formatter.smiley(u'/!\\')
		msg += macro.formatter.text(u' ')
		msg += macro.formatter.strong(1)
		msg += macro.formatter.text(_(u'Empty PDFControl macro option.'))
		msg += macro.formatter.text(u' ')
		msg += macro.formatter.text(_(u'To get an overview about HTMLDOC\'s control options please refer to the online help:'))
		msg += macro.formatter.text(u' ')
		msg += macro.formatter.url (1, u'http://www.htmldoc.org/documentation.php/Comments.html#COMMENTS')
		msg += macro.formatter.text(_(u'HTMLDOC help'))
		msg += macro.formatter.url(0)
		msg += macro.formatter.linebreak(0)
		msg += macro.formatter.smiley(u'(!)')
		msg += macro.formatter.text(u' ')
		msg += macro.formatter.text(_(u'To start a new page within the PDF document enter:'))
		msg += macro.formatter.text(u' ')
		msg += macro.formatter.code(1)
		msg += macro.formatter.text(u'[[PDFControl(NEW PAGE)]]')
		msg += macro.formatter.code(0)
		msg += macro.formatter.strong(0)
		msg += macro.formatter.paragraph(0)

	return msg

