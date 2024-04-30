#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# License: GNU General Public License v2
#
# Author: thl-cmk[at]outlook[dot]com
# URL   : https://thl-cmk.hopto.org
# Date  : 2024-04-29
# File  : freeradius.py (metrics)

from cmk.gui.i18n import _

from cmk.gui.plugins.metrics.utils import (
    check_metrics,
    graph_info,
    metric_info,
    perfometer_info,
)
#
_color_accepts = '24/a'
_color_challenges = '42/a'
_color_rejects = '32/a'
_color_requests = '16/a'
_color_responses = '35/b'
#
_color_conflicts = '25/a'
_color_dropped = '43/a'
_color_duplicate = '13/a'
_color_invalid = '33/a'
_color_malformed = '23/a'
_color_unknown = '53/a'
# queue
_color_authentication = '11/a'
_color_accounting = '21/a'
_color_detail = '31/a'
_color_internal = '41/a'
_color_proxy = '22/a'
_color_pps_in = '13/a'
_color_pps_out = '23/b'
#
# times
#
metric_info['reload'] = {'title': _('Reload'), 'unit': 's', 'color': '13/b', }
graph_info['freeradius.time'] = {
    'title': _('FreeRADIUS uptime'),
    'metrics': [
        ('reload', 'area'),
        ('uptime', 'area'),
    ],
    'optional_metrics': [
        'uptime',
        'reload',
    ],
}
#
# queue
#
_FreeRADIUS_Queue_Len_Internal = 'freeradius_queue_len_internal'
_FreeRADIUS_Queue_Len_Proxy = 'freeradius_queue_len_proxy'
_FreeRADIUS_Queue_Len_Auth = 'freeradius_queue_len_auth'
_FreeRADIUS_Queue_Len_Acct = 'freeradius_queue_len_acct'
_FreeRADIUS_Queue_Len_Detail = 'freeradius_queue_len_detail'
_FreeRADIUS_Queue_PPS_In = 'freeradius_queue_pps_in'
_FreeRADIUS_Queue_PPS_Out = 'freeradius_queue_pps_out'

metric_info[_FreeRADIUS_Queue_Len_Auth] = {
    'title': _('Authentication'), 'unit': 'count', 'color': _color_authentication
}
metric_info[_FreeRADIUS_Queue_Len_Acct] = {'title': _('Accounting'), 'unit': 'count', 'color': _color_accounting}
metric_info[_FreeRADIUS_Queue_Len_Detail] = {'title': _('Detail'), 'unit': 'count', 'color': _color_detail}
metric_info[_FreeRADIUS_Queue_Len_Internal] = {'title': _('Internal'), 'unit': 'count', 'color': _color_internal}
metric_info[_FreeRADIUS_Queue_Len_Proxy] = {'title': _('Proxy'), 'unit': 'count', 'color': _color_proxy}
metric_info[_FreeRADIUS_Queue_PPS_In] = {'title': _('PPS in'), 'unit': 'count', 'color': _color_pps_in}
metric_info[_FreeRADIUS_Queue_PPS_Out] = {'title': _('PPS out'), 'unit': 'count', 'color': _color_pps_out}

graph_info['freeradius.queue'] = {
    'title': _('FreeRADIUS queue length'),
    'metrics': [
        (_FreeRADIUS_Queue_Len_Acct, 'line'),
        (_FreeRADIUS_Queue_Len_Auth, 'line'),
        (_FreeRADIUS_Queue_Len_Detail, 'line'),
        (_FreeRADIUS_Queue_Len_Internal, 'line'),
        (_FreeRADIUS_Queue_Len_Proxy, 'line'),
    ],
    'optional_metrics': [
        _FreeRADIUS_Queue_Len_Auth,
        _FreeRADIUS_Queue_Len_Acct,
        _FreeRADIUS_Queue_Len_Detail,
        _FreeRADIUS_Queue_Len_Internal,
        _FreeRADIUS_Queue_Len_Proxy,
    ],
}

graph_info['freeradius.pps'] = {
    'title': _('FreeRADIUS queue PPS'),
    'metrics': [
        (_FreeRADIUS_Queue_PPS_In, 'area'),
        (_FreeRADIUS_Queue_PPS_Out, '-area'),
    ],
    'optional_metrics': [
        _FreeRADIUS_Queue_PPS_In,
        _FreeRADIUS_Queue_PPS_Out,
    ],
}

perfometer_info.append(('stacked', [
    {
        'type': 'logarithmic',
        'metric': _FreeRADIUS_Queue_PPS_In,
        "half_value": 100,
        "exponent": 3,
    },
    {
        'type': 'logarithmic',
        'metric': _FreeRADIUS_Queue_PPS_Out,
        "half_value": 100,
        "exponent": 3,
    }
]))
#
# authentication
#
_FreeRADIUS_Total_Access_Requests = 'freeradius_total_access_requests'
_FreeRADIUS_Total_Access_Accepts = 'freeradius_total_access_accepts'
_FreeRADIUS_Total_Access_Rejects = 'freeradius_total_access_rejects'
_FreeRADIUS_Total_Access_Challenges = 'freeradius_total_access_challenges'
_FreeRADIUS_Total_Auth_Responses = 'freeradius_total_auth_responses'
_FreeRADIUS_Total_Auth_Duplicate_Requests = 'freeradius_total_auth_duplicate_requests'
_FreeRADIUS_Total_Auth_Malformed_Requests = 'freeradius_total_auth_malformed_requests'
_FreeRADIUS_Total_Auth_Invalid_Requests = 'freeradius_total_auth_invalid_requests'
_FreeRADIUS_Total_Auth_Dropped_Requests = 'freeradius_total_auth_dropped_requests'
_FreeRADIUS_Total_Auth_Unknown_Types = 'freeradius_total_auth_unknown_types'
_FreeRADIUS_Total_Auth_Conflicts = 'freeradius_total_auth_conflicts'

metric_info[_FreeRADIUS_Total_Access_Requests] = {'title': _('Requests'), 'unit': '1/s', 'color': _color_requests}
metric_info[_FreeRADIUS_Total_Access_Accepts] = {'title': _('Accepts'), 'unit': '1/s', 'color': _color_accepts}
metric_info[_FreeRADIUS_Total_Access_Rejects] = {'title': _('Rejects'), 'unit': '1/s', 'color': _color_rejects}
metric_info[_FreeRADIUS_Total_Access_Challenges] = {'title': _('Challenges'), 'unit': '1/s', 'color': _color_challenges}
metric_info[_FreeRADIUS_Total_Auth_Responses] = {'title': _('Responses'), 'unit': '1/s', 'color': _color_responses}
metric_info[_FreeRADIUS_Total_Auth_Duplicate_Requests] = {
    'title': _('Duplicate'), 'unit': '1/s', 'color': _color_duplicate
}
metric_info[_FreeRADIUS_Total_Auth_Malformed_Requests] = {
    'title': _('Malformed'), 'unit': '1/s', 'color': _color_malformed
}
metric_info[_FreeRADIUS_Total_Auth_Invalid_Requests] = {'title': _('Invalid'), 'unit': '1/s', 'color': _color_invalid}
metric_info[_FreeRADIUS_Total_Auth_Dropped_Requests] = {'title': _('Dropped'), 'unit': '1/s', 'color': _color_dropped}
metric_info[_FreeRADIUS_Total_Auth_Unknown_Types] = {
    'title': _('Unknown tyoes'), 'unit': '1/s', 'color': _color_unknown
}
metric_info[_FreeRADIUS_Total_Auth_Conflicts] = {'title': _('Conflicts'), 'unit': '1/s', 'color': _color_conflicts}

graph_info['freeradius.authentication'] = {
    'title': _('FreeRADIUS Authentications'),
    'metrics': [
        (_FreeRADIUS_Total_Access_Accepts, 'line'),
        (_FreeRADIUS_Total_Access_Challenges, 'line'),
        (_FreeRADIUS_Total_Access_Rejects, 'line'),
        (_FreeRADIUS_Total_Access_Requests, 'area'),
        (_FreeRADIUS_Total_Auth_Responses, '-area'),
    ],
    'optional_metrics': [
        _FreeRADIUS_Total_Access_Requests,
        _FreeRADIUS_Total_Access_Accepts,
        _FreeRADIUS_Total_Access_Rejects,
        _FreeRADIUS_Total_Access_Challenges,
        _FreeRADIUS_Total_Auth_Responses,
    ],
}

graph_info['freeradius.authentication.errors'] = {
    'title': _('FreeRADIUS Authentication Errors'),
    'metrics': [
        (_FreeRADIUS_Total_Auth_Conflicts, 'line'),
        (_FreeRADIUS_Total_Auth_Dropped_Requests, 'line'),
        (_FreeRADIUS_Total_Auth_Duplicate_Requests, 'line'),
        (_FreeRADIUS_Total_Auth_Invalid_Requests, 'line'),
        (_FreeRADIUS_Total_Auth_Malformed_Requests, 'line'),
        (_FreeRADIUS_Total_Auth_Unknown_Types, 'line'),
    ],
    'optional_metrics': [
        _FreeRADIUS_Total_Auth_Conflicts,
        _FreeRADIUS_Total_Auth_Dropped_Requests,
        _FreeRADIUS_Total_Auth_Duplicate_Requests,
        _FreeRADIUS_Total_Auth_Invalid_Requests,
        _FreeRADIUS_Total_Auth_Malformed_Requests,
        _FreeRADIUS_Total_Auth_Unknown_Types,
    ],
}

perfometer_info.append(('stacked', [
    {
        'type': 'logarithmic',
        'metric': _FreeRADIUS_Total_Access_Requests,
        "half_value": 400,
        "exponent": 3,
    },
    {
        'type': 'logarithmic',
        'metric': _FreeRADIUS_Total_Auth_Responses,
        "half_value": 400,
        "exponent": 3,
    }
]))
#
# accounting
#
_FreeRADIUS_Total_Accounting_Requests = 'freeradius_total_accounting_requests'
_FreeRADIUS_Total_Accounting_Responses = 'freeradius_total_accounting_responses'
_FreeRADIUS_Total_Acct_Duplicate_Requests = 'freeradius_total_acct_duplicate_requests'
_FreeRADIUS_Total_Acct_Malformed_Requests = 'freeradius_total_acct_malformed_requests'
_FreeRADIUS_Total_Acct_Invalid_Requests = 'freeradius_total_acct_invalid_requests'
_FreeRADIUS_Total_Acct_Dropped_Requests = 'freeradius_total_acct_dropped_requests'
_FreeRADIUS_Total_Acct_Unknown_Types = 'freeradius_total_acct_unknown_types'
_FreeRADIUS_Total_Acct_Conflicts = 'freeradius_total_acct_conflicts'

metric_info[_FreeRADIUS_Total_Accounting_Requests] = {'title': _('Requests'), 'unit': '1/s', 'color': _color_responses}
metric_info[_FreeRADIUS_Total_Accounting_Responses] = {
    'title': _('Responses'), 'unit': '1/s', 'color': _color_responses
}
metric_info[_FreeRADIUS_Total_Acct_Duplicate_Requests] = {
    'title': _('Duplicate'), 'unit': '1/s', 'color': _color_duplicate
}
metric_info[_FreeRADIUS_Total_Acct_Malformed_Requests] = {
    'title': _('Malformed'), 'unit': '1/s', 'color': _color_malformed
}
metric_info[_FreeRADIUS_Total_Acct_Invalid_Requests] = {'title': _('Invalid'), 'unit': '1/s', 'color': _color_invalid}
metric_info[_FreeRADIUS_Total_Acct_Dropped_Requests] = {'title': _('Dropped'), 'unit': '1/s', 'color': _color_dropped}
metric_info[_FreeRADIUS_Total_Acct_Unknown_Types] = {'title': _('Unknown type'), 'unit': '1/s', 'color': _color_unknown}
metric_info[_FreeRADIUS_Total_Acct_Conflicts] = {'title': _('Conflict'), 'unit': '1/s', 'color': _color_conflicts}

graph_info['freeradius.accounting'] = {
    'title': _('FreeRADIUS Accounting'),
    'metrics': [
        (_FreeRADIUS_Total_Accounting_Requests, 'line'),
        (_FreeRADIUS_Total_Accounting_Responses, '-line'),
    ],
    'optional_metrics': [
        _FreeRADIUS_Total_Accounting_Requests,
        _FreeRADIUS_Total_Accounting_Responses,
    ],
}

graph_info['freeradius.accounting.errors'] = {
    'title': _('FreeRADIUS Accounting Errors'),
    'metrics': [
        (_FreeRADIUS_Total_Acct_Conflicts, '-line'),
        (_FreeRADIUS_Total_Acct_Dropped_Requests, 'line'),
        (_FreeRADIUS_Total_Acct_Duplicate_Requests, 'line'),
        (_FreeRADIUS_Total_Acct_Invalid_Requests, 'line'),
        (_FreeRADIUS_Total_Acct_Malformed_Requests, 'line'),
        (_FreeRADIUS_Total_Acct_Unknown_Types, 'line'),
    ],
    'optional_metrics': [
        _FreeRADIUS_Total_Acct_Conflicts,
        _FreeRADIUS_Total_Acct_Dropped_Requests,
        _FreeRADIUS_Total_Acct_Duplicate_Requests,
        _FreeRADIUS_Total_Acct_Invalid_Requests,
        _FreeRADIUS_Total_Acct_Malformed_Requests,
        _FreeRADIUS_Total_Acct_Unknown_Types
    ],
}

perfometer_info.append(('stacked', [
    {
        'type': 'logarithmic',
        'metric': _FreeRADIUS_Total_Accounting_Requests,
        "half_value": 400,
        "exponent": 3,
    },
    {
        'type': 'logarithmic',
        'metric': _FreeRADIUS_Total_Accounting_Responses,
        "half_value": 400,
        "exponent": 3,
    }
]))
#
# Proxy-Authentication
#
_FreeRADIUS_Total_Proxy_Access_Requests = 'freeradius_total_proxy_access_requests'
_FreeRADIUS_Total_Proxy_Access_Accepts = 'freeradius_total_proxy_access_accepts'
_FreeRADIUS_Total_Proxy_Access_Rejects = 'freeradius_total_proxy_access_rejects'
_FreeRADIUS_Total_Proxy_Access_Challenges = 'freeradius_total_proxy_access_challenges'
_FreeRADIUS_Total_Proxy_Auth_Responses = 'freeradius_total_proxy_auth_responses'
_FreeRADIUS_Total_Proxy_Auth_Duplicate_Requests = 'freeradius_total_proxy_auth_duplicate_requests'
_FreeRADIUS_Total_Proxy_Auth_Malformed_Requests = 'freeradius_total_proxy_auth_malformed_requests'
_FreeRADIUS_Total_Proxy_Auth_Invalid_Requests = 'freeradius_total_proxy_auth_invalid_requests'
_FreeRADIUS_Total_Proxy_Auth_Dropped_Requests = 'freeradius_total_proxy_auth_dropped_requests'
_FreeRADIUS_Total_Proxy_Auth_Unknown_Types = 'freeradius_total_proxy_auth_unknown_types'

check_metrics['check_mk-freeradius_total_proxy_authentication'] = {
    _FreeRADIUS_Total_Proxy_Access_Requests: {'name': _FreeRADIUS_Total_Access_Requests},
    _FreeRADIUS_Total_Proxy_Access_Accepts: {'name': _FreeRADIUS_Total_Access_Accepts},
    _FreeRADIUS_Total_Proxy_Access_Rejects: {'name': _FreeRADIUS_Total_Access_Rejects},
    _FreeRADIUS_Total_Proxy_Access_Challenges: {'name': _FreeRADIUS_Total_Access_Challenges},
    _FreeRADIUS_Total_Proxy_Auth_Responses: {'name': _FreeRADIUS_Total_Auth_Responses},
    _FreeRADIUS_Total_Proxy_Auth_Duplicate_Requests: {'name': _FreeRADIUS_Total_Auth_Duplicate_Requests},
    _FreeRADIUS_Total_Proxy_Auth_Malformed_Requests: {'name': _FreeRADIUS_Total_Auth_Malformed_Requests},
    _FreeRADIUS_Total_Proxy_Auth_Invalid_Requests: {'name': _FreeRADIUS_Total_Auth_Invalid_Requests},
    _FreeRADIUS_Total_Proxy_Auth_Dropped_Requests: {'name': _FreeRADIUS_Total_Auth_Dropped_Requests},
    _FreeRADIUS_Total_Proxy_Auth_Unknown_Types: {'name': _FreeRADIUS_Total_Auth_Unknown_Types},
}
#
# Proxy-Accounting
#
_FreeRADIUS_Total_Proxy_Accounting_Requests = 'freeradius_total_proxy_accounting_requests'
_FreeRADIUS_Total_Proxy_Accounting_Responses = 'freeradius_total_proxy_accounting_responses'
_FreeRADIUS_Total_Proxy_Acct_Duplicate_Requests = 'freeradius_total_proxy_acct_duplicate_requests'
_FreeRADIUS_Total_Proxy_Acct_Malformed_Requests = 'freeradius_total_proxy_acct_malformed_requests'
_FreeRADIUS_Total_Proxy_Acct_Invalid_Requests = 'freeradius_total_proxy_acct_invalid_requests'
_FreeRADIUS_Total_Proxy_Acct_Dropped_Requests = 'freeradius_total_proxy_acct_dropped_requests'
_FreeRADIUS_Total_Proxy_Acct_Unknown_Types = 'freeradius_total_proxy_acct_unknown_types'

check_metrics['check_mk-freeradius_total_proxy_accounting'] = {
    _FreeRADIUS_Total_Proxy_Accounting_Requests: {'name': _FreeRADIUS_Total_Accounting_Requests},
    _FreeRADIUS_Total_Proxy_Accounting_Responses: {'name': _FreeRADIUS_Total_Accounting_Responses},
    _FreeRADIUS_Total_Proxy_Acct_Duplicate_Requests: {'name': _FreeRADIUS_Total_Acct_Duplicate_Requests},
    _FreeRADIUS_Total_Proxy_Acct_Malformed_Requests: {'name': _FreeRADIUS_Total_Acct_Malformed_Requests},
    _FreeRADIUS_Total_Proxy_Acct_Invalid_Requests: {'name': _FreeRADIUS_Total_Acct_Invalid_Requests},
    _FreeRADIUS_Total_Proxy_Acct_Dropped_Requests: {'name': _FreeRADIUS_Total_Acct_Dropped_Requests},
    _FreeRADIUS_Total_Proxy_Acct_Unknown_Types: {'name': _FreeRADIUS_Total_Acct_Unknown_Types},
}
