# -*- coding: utf-8 -*-

import re
from openerp import netsvc
from openerp.osv import osv, fields

class import(osv.osv):
    """"""
    
    _name = 'epicor.import'
    _description = 'import'
    _inherits = {  }
    _inherit = [ 'mail.thread' ]

    _states_ = [
        # State machine: untitle
        ('draft','draft'),
        ('running','running'),
        ('done','done'),
        ('error','error'),
    ]
    _track = {
        'state': {
            'epicor.import_draft': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'draft',
            'epicor.import_running': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'running',
            'epicor.import_done': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'done',
            'epicor.import_error': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'error',
        },
    }


    _columns = {
        'name': fields.char(string='name'),
        'datetime': fields.datetime(string='datetime'),
        'log': fields.text(string='log'),
        'state': fields.selection(_states_, "State"),
    }

    _defaults = {
        'state': 'draft',
    }


    _constraints = [
    ]


    def execute(self, cr, uid, ids, context=None):
        """"""
        parent = super(import,self)
        result = parent.execute(cr, uid, ids, context=None) if hasattr(parent, 'execute') else False
        return result



import()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
