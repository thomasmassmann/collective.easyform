# -*- coding: utf-8 -*-

from actions import IAction
from collective.easyform import config
from collective.easyform import easyformMessageFactory as _  # NOQA
from collective.easyform import vocabularies
from plone.autoform import directives
from plone.supermodel.model import fieldset
from validators import isTALES
from z3c.form.browser.checkbox import CheckBoxFieldWidget

import zope.i18nmessageid
import zope.interface
import zope.schema.interfaces

PMF = zope.i18nmessageid.MessageFactory('plone')
MODIFY_PORTAL_CONTENT = 'cmf.ModifyPortalContent'


class IMailer(IAction):

    """A form action adapter that will e-mail form input."""
#     default_method='getDefaultRecipientName',
    directives.write_permission(recipient_name=config.EDIT_ADDRESSING_PERMISSION)
    directives.read_permission(recipient_name=MODIFY_PORTAL_CONTENT)
    recipient_name = zope.schema.TextLine(
        title=_(u'label_formmailer_recipient_fullname',
                default=u"Recipient's full name"),
        description=_(u'help_formmailer_recipient_fullname',
                      default=u'The full name of the recipient of the mailed form.'),
        default=u'',
        missing_value=u'',
        required=False,
    )
#     default_method='getDefaultRecipient',
#     validators=('isEmail',),
#     TODO defaultFactory
#     TODO IContextAwareDefaultFactory
    directives.write_permission(recipient_email=config.EDIT_ADDRESSING_PERMISSION)
    directives.read_permission(recipient_email=MODIFY_PORTAL_CONTENT)
    recipient_email = zope.schema.TextLine(
        title=_(u'label_formmailer_recipient_email',
                default=u"Recipient's e-mail address"),
        description=_(u'help_formmailer_recipient_email',
                      default=u'The recipients e-mail address.'),
        default=u'',
        missing_value=u'',
        required=False,
    )
    fieldset(u'addressing', label=_('Addressing'), fields=[
             'to_field', 'cc_recipients', 'bcc_recipients', 'replyto_field'])
    directives.write_permission(to_field=config.EDIT_ADVANCED_PERMISSION)
    directives.read_permission(to_field=MODIFY_PORTAL_CONTENT)
    to_field = zope.schema.Choice(
        title=_(u'label_formmailer_to_extract',
                default=u'Extract Recipient From'),
        description=_(u'help_formmailer_to_extract', default=u''
                      u'Choose a form field from which you wish to extract '
                      u'input for the To header. If you choose anything other '
                      u'than "None", this will override the "Recipient\'s e-mail address" '
                      u'setting above. Be very cautious about allowing unguarded user '
                      u'input for this purpose.'),
        required=False,
        vocabulary=vocabularies.fieldsFactory,
    )
#     default_method='getDefaultCC',
    directives.write_permission(cc_recipients=config.EDIT_ADDRESSING_PERMISSION)
    directives.read_permission(cc_recipients=MODIFY_PORTAL_CONTENT)
    cc_recipients = zope.schema.Text(
        title=_(u'label_formmailer_cc_recipients',
                default=u'CC Recipients'),
        description=_(u'help_formmailer_cc_recipients',
                      default=u'E-mail addresses which receive a carbon copy.'),
        default=u'',
        missing_value=u'',
        required=False,
    )
#     default_method='getDefaultBCC',
    directives.write_permission(bcc_recipients=config.EDIT_ADDRESSING_PERMISSION)
    directives.read_permission(bcc_recipients=MODIFY_PORTAL_CONTENT)
    bcc_recipients = zope.schema.Text(
        title=_(u'label_formmailer_bcc_recipients',
                default=u'BCC Recipients'),
        description=_(u'help_formmailer_bcc_recipients',
                      default=u'E-mail addresses which receive a blind carbon copy.'),
        default=u'',
        missing_value=u'',
        required=False,
    )
    directives.write_permission(replyto_field=config.EDIT_ADVANCED_PERMISSION)
    directives.read_permission(replyto_field=MODIFY_PORTAL_CONTENT)
    replyto_field = zope.schema.Choice(
        title=_(u'label_formmailer_replyto_extract',
                default=u'Extract Reply-To From'),
        description=_(u'help_formmailer_replyto_extract', default=u''
                      u'Choose a form field from which you wish to extract '
                      u'input for the Reply-To header. NOTE: You should '
                      u'activate e-mail address verification for the designated '
                      u'field.'),
        required=False,
        vocabulary=vocabularies.fieldsFactory,
    )
    fieldset(u'message', label=PMF('Message'), fields=[
             'msg_subject', 'subject_field', 'body_pre', 'body_post',
             'body_footer', 'showAll', 'showFields', 'includeEmpties'])
    directives.read_permission(msg_subject=MODIFY_PORTAL_CONTENT)
    msg_subject = zope.schema.TextLine(
        title=_(u'label_formmailer_subject', default=u'Subject'),
        description=_(u'help_formmailer_subject', default=u''
                      u'Subject line of message. This is used if you '
                      u'do not specify a subject field or if the field '
                      u'is empty.'),
        default=u'Form Submission',
        missing_value=u'',
        required=False,
    )
    directives.write_permission(subject_field=config.EDIT_ADVANCED_PERMISSION)
    directives.read_permission(subject_field=MODIFY_PORTAL_CONTENT)
    subject_field = zope.schema.Choice(
        title=_(u'label_formmailer_subject_extract',
                default=u'Extract Subject From'),
        description=_(u'help_formmailer_subject_extract', default=u''
                      u'Choose a form field from which you wish to extract '
                      u'input for the mail subject line.'),
        required=False,
        vocabulary=vocabularies.fieldsFactory,
    )
#     accessor='getBody_pre',
    directives.read_permission(body_pre=MODIFY_PORTAL_CONTENT)
    body_pre = zope.schema.Text(
        title=_(u'label_formmailer_body_pre', default=u'Body (prepended)'),
        description=_(u'help_formmailer_body_pre',
                      default=u'Text prepended to fields listed in mail-body'),
        default=u'',
        missing_value=u'',
        required=False,
    )
    directives.read_permission(body_post=MODIFY_PORTAL_CONTENT)
    body_post = zope.schema.Text(
        title=_(u'label_formmailer_body_post', default=u'Body (appended)'),
        description=_(u'help_formmailer_body_post',
                      default=u'Text appended to fields listed in mail-body'),
        default=u'',
        missing_value=u'',
        required=False,
    )
    directives.read_permission(body_footer=MODIFY_PORTAL_CONTENT)
    body_footer = zope.schema.Text(
        title=_(u'label_formmailer_body_footer',
                default=u'Body (signature)'),
        description=_(u'help_formmailer_body_footer',
                      default=u'Text used as the footer at '
                      u'bottom, delimited from the body by a dashed line.'),
        default=u'',
        missing_value=u'',
        required=False,
    )
    directives.read_permission(showAll=MODIFY_PORTAL_CONTENT)
    showAll = zope.schema.Bool(
        title=_(u'label_mailallfields_text', default=u'Include All Fields'),
        description=_(u'help_mailallfields_text', default=u''
                      u'Check this to include input for all fields '
                      u'(except label and file fields). If you check '
                      u'this, the choices in the pick box below '
                      u'will be ignored.'),
        default=True,
        required=False,
    )
    directives.read_permission(showFields=MODIFY_PORTAL_CONTENT)
    showFields = zope.schema.List(
        title=_(u'label_mailfields_text', default=u'Show Responses'),
        description=_(u'help_mailfields_text',
                      default=u'Pick the fields whose inputs you\'d like to include in the e-mail.'),
        unique=True,
        required=False,
        value_type=zope.schema.Choice(vocabulary=vocabularies.fieldsFactory),
    )
    directives.read_permission(includeEmpties=MODIFY_PORTAL_CONTENT)
    includeEmpties = zope.schema.Bool(
        title=_(u'label_mailEmpties_text', default=u'Include Empties'),
        description=_(u'help_mailEmpties_text', default=u''
                      u'Check this to include titles '
                      u'for fields that received no input. Uncheck '
                      u'to leave fields with no input out of the e-mail.'),
        default=True,
        required=False,
    )
    fieldset(u'template', label=PMF(
        'Template'), fields=['body_pt', 'body_type'])
#     ZPTField('body_pt',
#     default_method='getMailBodyDefault',
#     validators=('zptvalidator',),
    directives.write_permission(body_pt=config.EDIT_TALES_PERMISSION)
    directives.read_permission(body_pt=MODIFY_PORTAL_CONTENT)
    body_pt = zope.schema.Text(
        title=_(u'label_formmailer_body_pt', default=u'Mail-Body Template'),
        description=_(u'help_formmailer_body_pt', default=u''
                      u'This is a Zope Page Template '
                      u'used for rendering of the mail-body. You don\'t need to modify '
                      u'it, but if you know TAL (Zope\'s Template Attribute Language) '
                      u'you have the full power to customize your outgoing mails.'),
        default=config.MAIL_BODY_DEFAULT,
        missing_value=u'',
    )
#     default_method='getMailBodyTypeDefault',
    directives.write_permission(body_type=config.EDIT_ADVANCED_PERMISSION)
    directives.read_permission(body_type=MODIFY_PORTAL_CONTENT)
    body_type = zope.schema.Choice(
        title=_(u'label_formmailer_body_type', default=u'Mail Format'),
        description=_(u'help_formmailer_body_type', default=u''
                      u'Set the mime-type of the mail-body. '
                      u'Change this setting only if you know exactly what you are doing. '
                      u'Leave it blank for default behaviour.'),
        default=u'html',
        vocabulary=vocabularies.MIME_LIST,
    )
    fieldset(u'headers', label=_('Headers'),
             fields=['xinfo_headers', 'additional_headers'])
    directives.widget(xinfo_headers=CheckBoxFieldWidget)
#     default_method='getDefaultXInfo',
    directives.write_permission(xinfo_headers=config.EDIT_ADVANCED_PERMISSION)
    directives.read_permission(xinfo_headers=MODIFY_PORTAL_CONTENT)
    xinfo_headers = zope.schema.List(
        title=_(u'label_xinfo_headers_text', default=u'HTTP Headers'),
        description=_(u'help_xinfo_headers_text', default=u''
                      u'Pick any items from the HTTP headers that '
                      u'you\'d like to insert as X- headers in the message.'),
        unique=True,
        required=False,
        default=[u'HTTP_X_FORWARDED_FOR', u'REMOTE_ADDR', u'PATH_INFO'],
        missing_value=[u'HTTP_X_FORWARDED_FOR', u'REMOTE_ADDR', u'PATH_INFO'],
        value_type=zope.schema.Choice(vocabulary=vocabularies.XINFO_HEADERS),
    )
#     default_method='getDefaultAddHdrs',
    directives.write_permission(additional_headers=config.EDIT_ADVANCED_PERMISSION)
    directives.read_permission(additional_headers=MODIFY_PORTAL_CONTENT)
    additional_headers = zope.schema.List(
        title=_(u'label_formmailer_additional_headers',
                default=u'Additional Headers'),
        description=_(u'help_formmailer_additional_headers',
                      default=u'Additional e-mail-header lines. Only use RFC822-compliant headers.'),
        unique=True,
        required=False,
        value_type=zope.schema.TextLine(
            title=_(u'extra_header',
                    default=u'${name} Header', mapping={u'name': u'HTTP'}),
        ),
    )
#     if gpg is not None:
#         formMailerAdapterSchema = formMailerAdapterSchema + Schema((
#             StringField('gpg_keyid',
#                 schemata='encryption',
#                 accessor='getGPGKeyId',
#                 mutator='setGPGKeyId',
#                 write_permission=USE_ENCRYPTION_PERMISSION,
#                 read_permission=ModifyPortalContent,
#                 widget=StringWidget(
#                     description=_(u'help_gpg_key_id', default=u"""
#                         Give your key-id, e-mail address or
#                         whatever works to match a public key from current keyring.
#                         It will be used to encrypt the message body (not attachments).
#                         Contact the site administrator if you need to
#                         install a new public key.
#                         Note that you will probably wish to change your message
#                         template to plain text if you're using encryption.
#                         TEST THIS FEATURE BEFORE GOING PUBLIC!
#                        """),
#                    label=_(u'label_gpg_key_id', default=u'Key-Id'),
#                    ),
#                ),
#            ))
    fieldset(u'overrides', label=_('Overrides'), fields=[
             'subjectOverride', 'senderOverride', 'recipientOverride', 'ccOverride', 'bccOverride'])
    directives.write_permission(subjectOverride=config.EDIT_TALES_PERMISSION)
    directives.read_permission(subjectOverride=MODIFY_PORTAL_CONTENT)
    subjectOverride = zope.schema.TextLine(
        title=_(u'label_subject_override_text', default=u'Subject Expression'),
        description=_(u'help_subject_override_text', default=u''
                      u'A TALES expression that will be evaluated to override any value '
                      u'otherwise entered for the e-mail subject header. '
                      u'Leave empty if unneeded. Your expression should evaluate as a string. '
                      u'PLEASE NOTE: errors in the evaluation of this expression will cause '
                      u'an error on form display.'),
        required=False,
        default=u'',
        missing_value=u'',
        constraint=isTALES,
    )
    directives.write_permission(senderOverride=config.EDIT_TALES_PERMISSION)
    directives.read_permission(senderOverride=MODIFY_PORTAL_CONTENT)
    senderOverride = zope.schema.TextLine(
        title=_(u'label_sender_override_text', default=u'Sender Expression'),
        description=_(u'help_sender_override_text', default=u''
                      u'A TALES expression that will be evaluated to override the "From" header. '
                      u'Leave empty if unneeded. Your expression should evaluate as a string. '
                      u'PLEASE NOTE: errors in the evaluation of this expression will cause '
                      u'an error on form display.'),
        required=False,
        default=u'',
        missing_value=u'',
        constraint=isTALES,
    )
    directives.write_permission(recipientOverride=config.EDIT_TALES_PERMISSION)
    directives.read_permission(recipientOverride=MODIFY_PORTAL_CONTENT)
    recipientOverride = zope.schema.TextLine(
        title=_(u'label_recipient_override_text',
                default=u'Recipient Expression'),
        description=_(u'help_recipient_override_text', default=u''
                      u'A TALES expression that will be evaluated to override any value '
                      u'otherwise entered for the recipient e-mail address. You are strongly '
                      u'cautioned against using unvalidated data from the request for this purpose. '
                      u'Leave empty if unneeded. Your expression should evaluate as a string. '
                      u'PLEASE NOTE: errors in the evaluation of this expression will cause '
                      u'an error on form display.'),
        required=False,
        default=u'',
        missing_value=u'',
        constraint=isTALES,
    )
    directives.write_permission(ccOverride=config.EDIT_TALES_PERMISSION)
    directives.read_permission(ccOverride=MODIFY_PORTAL_CONTENT)
    ccOverride = zope.schema.TextLine(
        title=_(u'label_cc_override_text', default=u'CC Expression'),
        description=_(u'help_cc_override_text', default=u''
                      u'A TALES expression that will be evaluated to override any value '
                      u'otherwise entered for the CC list. You are strongly '
                      u'cautioned against using unvalidated data from the request for this purpose. '
                      u'Leave empty if unneeded. Your expression should evaluate as a sequence of strings. '
                      u'PLEASE NOTE: errors in the evaluation of this expression will cause '
                      u'an error on form display.'),
        required=False,
        default=u'',
        missing_value=u'',
        constraint=isTALES,
    )
    directives.write_permission(bccOverride=config.EDIT_TALES_PERMISSION)
    directives.read_permission(bccOverride=MODIFY_PORTAL_CONTENT)
    bccOverride = zope.schema.TextLine(
        title=_(u'label_bcc_override_text', default=u'BCC Expression'),
        description=_(u'help_bcc_override_text', default=u''
                      u'A TALES expression that will be evaluated to override any value '
                      u'otherwise entered for the BCC list. You are strongly '
                      u'cautioned against using unvalidated data from the request for this purpose. '
                      u'Leave empty if unneeded. Your expression should evaluate as a sequence of strings. '
                      u'PLEASE NOTE: errors in the evaluation of this expression will cause '
                      u'an error on form display.'),
        required=False,
        default=u'',
        missing_value=u'',
        constraint=isTALES,
    )
