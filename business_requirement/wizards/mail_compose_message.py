# -*- coding: utf-8 -*-
# © 2016 Elico Corp (https://www.elico-corp.com).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models


class MailComposeMessage(models.TransientModel):
    _inherit = 'mail.compose.message'

    def default_get(self, cr, uid, fields, context=None):
        res = super(MailComposeMessage, self).default_get(cr, uid,
            fields, context=context)
        if context.get('default_model') == 'business.requirement' and \
            context.get('default_res_id'):
            br_rec = self.pool.get(
                context.get('default_model')
            ).browse(cr, uid, context['default_res_id'])
            res['subject'] = 'Re: %s-%s' % (br_rec.name, br_rec.description)
        return res
