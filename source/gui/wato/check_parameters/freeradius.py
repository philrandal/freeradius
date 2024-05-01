#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# License: GNU General Public License v2
#
# Author: thl-cmk[at]outlook[dot]com
# URL   : https://thl-cmk.hopto.org
# Date  : 2024-04-29
# File  : freeradius.py (WATO)

from cmk.gui.i18n import _
from cmk.gui.plugins.wato.utils import (
    CheckParameterRulespecWithoutItem,
    RulespecGroupCheckParametersApplications,
    rulespec_registry,
)
from cmk.gui.valuespec import (
    Alternative,
    Dictionary,
    FixedValue,
    Integer,
    ListOf,
    Tuple,
    ValueSpec,
)

_list_attributes = (
    'list_attributes',
    FixedValue(
        True, title=_('List response attributes in service details'), totext=_('yes'),
    ))


def _parameter_valuespec_freeradius():
    return Dictionary(
        title=_('FreeRADIUS queue'),
        optional_keys=True,
        elements=[
            _list_attributes,
        ],
        required_keys=['attributes']
    )


def _attributes(_attribute_list, _attribute_type) -> ValueSpec:
    return ('attributes',
            ListOf(
                Alternative(
                    orientation='horizontal',
                    elements=[
                        _attribute_values(attribute, name) for attribute, name in _attribute_list
                    ]
                ),
                title=_(f'{_attribute_type} Attributes'),
                add_label=_('add attribute'),
            ))


rulespec_registry.register(
    CheckParameterRulespecWithoutItem(
        title=lambda: _('FreeRADIUS'),
        check_group_name='freeradius',
        group=RulespecGroupCheckParametersApplications,
        parameter_valuespec=_parameter_valuespec_freeradius,
        match_type='dict',
    )
)

# names
_Accepts = 'Accepts'
_Accounting = 'Accounting'
_Authentication = 'Authentication'
_Challenges = 'Challenges'
_Conflicts = 'Conflicts'
_Detail = 'Detail'
_Dropped = 'Dropped'
_Duplicate = 'Duplicate'
_Internal = 'Internal'
_Invalid = 'Invalid'
_Malformed = 'Malformed'
_PPS_In = 'PPS In'
_PPS_Out = 'PSS Out'
_Proxy = 'Proxy'
_Rejects = 'Rejects'
_Requests = 'Requests'
_Responses = 'Responses'
_Unknown_Types = 'Unknown Types'

# Internal Attributes
_FreeRADIUS_Queue_Len_Internal = 'FreeRADIUS-Queue-Len-Internal'
_FreeRADIUS_Queue_Len_Proxy = 'FreeRADIUS-Queue-Len-Proxy'
_FreeRADIUS_Queue_Len_Auth = 'FreeRADIUS-Queue-Len-Auth'
_FreeRADIUS_Queue_Len_Acct = 'FreeRADIUS-Queue-Len-Acct'
_FreeRADIUS_Queue_Len_Detail = 'FreeRADIUS-Queue-Len-Detail'
_FreeRADIUS_Queue_PPS_In = 'FreeRADIUS-Queue-PPS-In'
_FreeRADIUS_Queue_PPS_Out = 'FreeRADIUS-Queue-PPS-Out'

_FreeRADIUS_Queue = [
    (_FreeRADIUS_Queue_Len_Acct, _Accounting),
    (_FreeRADIUS_Queue_Len_Auth, _Authentication),
    (_FreeRADIUS_Queue_Len_Detail, _Detail),
    (_FreeRADIUS_Queue_Len_Internal, _Internal),
    (_FreeRADIUS_Queue_Len_Proxy, _Proxy),
    (_FreeRADIUS_Queue_PPS_In, _PPS_In),
    (_FreeRADIUS_Queue_PPS_Out, _PPS_Out),
]


def _attribute_values(attribute, name):
    return Tuple(
        title=name,
        elements=[
            FixedValue(attribute, totext=name),
            Dictionary(
                # title=_('Settings'),
                elements=[
                    ('upper',
                     Tuple(
                         title='Upper Levels',
                         orientation='horizontal',
                         elements=[
                             Integer(title='Warning at'),
                             Integer(title='Critical at'),
                         ])),
                    ('lower',
                     Tuple(
                         title='Lower Levels',
                         orientation='horizontal',
                         elements=[
                             Integer(title='Warning below', unit='count'),
                             Integer(title='Critical below', unit='count'),
                         ])),
                    ('info_line',
                     FixedValue(False, title='Show on info line', totext='yes')
                     )
                ],
            )])


def _parameter_valuespec_freeradius_queue():
    return Dictionary(
        title=_('FreeRADIUS queue'),
        optional_keys=True,
        elements=[
            _list_attributes,
            _attributes(_FreeRADIUS_Queue, 'Queue'),
        ],
        required_keys=['attributes']
    )


rulespec_registry.register(
    CheckParameterRulespecWithoutItem(
        title=lambda: _('FreeRADIUS queue'),
        check_group_name='freeradius_queue',
        group=RulespecGroupCheckParametersApplications,
        parameter_valuespec=_parameter_valuespec_freeradius_queue,
        match_type='dict',
    )
)

_FreeRADIUS_Total_Access_Requests = 'FreeRADIUS-Total-Access-Requests'
_FreeRADIUS_Total_Access_Accepts = 'FreeRADIUS-Total-Access-Accepts'
_FreeRADIUS_Total_Access_Rejects = 'FreeRADIUS-Total-Access-Rejects'
_FreeRADIUS_Total_Access_Challenges = 'FreeRADIUS-Total-Access-Challenges'
_FreeRADIUS_Total_Auth_Responses = 'FreeRADIUS-Total-Auth-Responses'
_FreeRADIUS_Total_Auth_Duplicate_Requests = 'FreeRADIUS-Total-Auth-Duplicate-Requests'
_FreeRADIUS_Total_Auth_Malformed_Requests = 'FreeRADIUS-Total-Auth-Malformed-Requests'
_FreeRADIUS_Total_Auth_Invalid_Requests = 'FreeRADIUS-Total-Auth-Invalid-Requests'
_FreeRADIUS_Total_Auth_Dropped_Requests = 'FreeRADIUS-Total-Auth-Dropped-Requests'
_FreeRADIUS_Total_Auth_Unknown_Types = 'FreeRADIUS-Total-Auth-Unknown-Types'
_FreeRADIUS_Total_Auth_Conflicts = 'FreeRADIUS-Total-Auth-Conflicts'

_FreeRADIUS_Total_Authentication = [
    (_FreeRADIUS_Total_Access_Accepts, _Accepts),
    (_FreeRADIUS_Total_Access_Challenges, _Challenges),
    (_FreeRADIUS_Total_Auth_Conflicts, _Conflicts),
    (_FreeRADIUS_Total_Auth_Dropped_Requests, _Dropped),
    (_FreeRADIUS_Total_Auth_Duplicate_Requests, _Duplicate),
    (_FreeRADIUS_Total_Auth_Invalid_Requests, _Invalid),
    (_FreeRADIUS_Total_Auth_Malformed_Requests, _Malformed),
    (_FreeRADIUS_Total_Access_Rejects, _Rejects),
    (_FreeRADIUS_Total_Access_Requests, _Requests),
    (_FreeRADIUS_Total_Auth_Responses, _Responses),
    (_FreeRADIUS_Total_Auth_Unknown_Types, _Unknown_Types),
]


def _parameter_valuespec_freeradius_total_authentication():
    return Dictionary(
        title=_('FreeRADIUS authentication'),
        optional_keys=True,
        elements=[
            _list_attributes,
            _attributes(_FreeRADIUS_Total_Authentication, 'Authentication'),
        ],
        required_keys=['attributes']
    )


rulespec_registry.register(
    CheckParameterRulespecWithoutItem(
        title=lambda: _('FreeRADIUS authentication'),
        check_group_name='freeradius_total_authentication',
        group=RulespecGroupCheckParametersApplications,
        parameter_valuespec=_parameter_valuespec_freeradius_total_authentication,
        match_type='dict',
    )
)

# Accounting attributes
_FreeRADIUS_Total_Accounting_Requests = 'FreeRADIUS-Total-Accounting-Requests'
_FreeRADIUS_Total_Accounting_Responses = 'FreeRADIUS-Total-Accounting-Responses'
_FreeRADIUS_Total_Acct_Duplicate_Requests = 'FreeRADIUS-Total-Acct_Duplicate-Requests'
_FreeRADIUS_Total_Acct_Malformed_Requests = 'FreeRADIUS-Total-Acct-Malformed-Requests'
_FreeRADIUS_Total_Acct_Invalid_Requests = 'FreeRADIUS-Total-Acct-Invalid-Requests'
_FreeRADIUS_Total_Acct_Dropped_Requests = 'FreeRADIUS-Total-Acct-Dropped-Requests'
_FreeRADIUS_Total_Acct_Unknown_Types = 'FreeRADIUS-Total-Acct-Unknown-Types'
_FreeRADIUS_Total_Acct_Conflicts = 'FreeRADIUS-Total-Acct-Conflicts'

_FreeRADIUS_Total_Accounting = [
    (_FreeRADIUS_Total_Accounting_Requests, _Requests),
    (_FreeRADIUS_Total_Accounting_Responses, _Responses),
    (_FreeRADIUS_Total_Acct_Duplicate_Requests, _Duplicate),
    (_FreeRADIUS_Total_Acct_Malformed_Requests, _Malformed),
    (_FreeRADIUS_Total_Acct_Invalid_Requests, _Invalid),
    (_FreeRADIUS_Total_Acct_Dropped_Requests, _Dropped),
    (_FreeRADIUS_Total_Acct_Unknown_Types, _Unknown_Types),
    (_FreeRADIUS_Total_Acct_Conflicts, _Conflicts),
]


def _parameter_valuespec_freeradius_total_accounting():
    return Dictionary(
        title=_('FreeRADIUS accounting'),
        optional_keys=True,
        elements=[
            _list_attributes,
            _attributes(_FreeRADIUS_Total_Accounting, 'Accounting'),
        ],
        required_keys=['attributes']
    )


rulespec_registry.register(
    CheckParameterRulespecWithoutItem(
        title=lambda: _('FreeRADIUS acconting'),
        check_group_name='freeradius_total_accounting',
        group=RulespecGroupCheckParametersApplications,
        parameter_valuespec=_parameter_valuespec_freeradius_total_accounting,
        match_type='dict',
    )
)

# Proxy-Authentication
_FreeRADIUS_Total_Proxy_Access_Requests = 'FreeRADIUS-Total-Proxy-Access-Requests'
_FreeRADIUS_Total_Proxy_Access_Accepts = 'FreeRADIUS-Total-Proxy-Access-Accepts'
_FreeRADIUS_Total_Proxy_Access_Rejects = 'FreeRADIUS-Total-Proxy-Access-Rejects'
_FreeRADIUS_Total_Proxy_Access_Challenges = 'FreeRADIUS-Total-Proxy-Access-Challenges'
_FreeRADIUS_Total_Proxy_Auth_Responses = 'FreeRADIUS-Total-Proxy-Auth-Responses'
_FreeRADIUS_Total_Proxy_Auth_Duplicate_Requests = 'FreeRADIUS-Total-Proxy-Auth-Duplicate-Requests'
_FreeRADIUS_Total_Proxy_Auth_Malformed_Requests = 'FreeRADIUS-Total-Proxy-Auth-Malformed-Requests'
_FreeRADIUS_Total_Proxy_Auth_Invalid_Requests = 'FreeRADIUS-Total-Proxy-Auth-Invalid-Requests'
_FreeRADIUS_Total_Proxy_Auth_Dropped_Requests = 'FreeRADIUS-Total-Proxy-Auth-Dropped-Requests'
_FreeRADIUS_Total_Proxy_Auth_Unknown_Types = 'FreeRADIUS-Total-Proxy-Auth-Unknown-Types'

_FreeRADIUS_Total_Proxy_Authentication = [
    (_FreeRADIUS_Total_Proxy_Access_Accepts, _Accepts),
    (_FreeRADIUS_Total_Proxy_Access_Challenges, _Challenges),
    (_FreeRADIUS_Total_Proxy_Auth_Dropped_Requests, _Dropped),
    (_FreeRADIUS_Total_Proxy_Auth_Duplicate_Requests, _Duplicate),
    (_FreeRADIUS_Total_Proxy_Auth_Invalid_Requests, _Invalid),
    (_FreeRADIUS_Total_Proxy_Auth_Malformed_Requests, _Malformed),
    (_FreeRADIUS_Total_Proxy_Access_Rejects, _Rejects),
    (_FreeRADIUS_Total_Proxy_Access_Requests, _Requests),
    (_FreeRADIUS_Total_Proxy_Auth_Responses, _Responses),
    (_FreeRADIUS_Total_Proxy_Auth_Unknown_Types, _Unknown_Types),
]


def _parameter_valuespec_freeradius_total_proxy_authentication():
    return Dictionary(
        title=_('FreeRADIUS proxy authentication'),
        optional_keys=True,
        elements=[
            _list_attributes,
            _attributes(_FreeRADIUS_Total_Proxy_Authentication, 'Proxy Authentication'),
        ],
        required_keys=['attributes']
    )


rulespec_registry.register(
    CheckParameterRulespecWithoutItem(
        title=lambda: _('FreeRADIUS proxy authentication'),
        check_group_name='freeradius_total_proxy_authentication',
        group=RulespecGroupCheckParametersApplications,
        parameter_valuespec=_parameter_valuespec_freeradius_total_proxy_authentication,
        match_type='dict',
    )
)

# Proxy-Accounting
_FreeRADIUS_Total_Proxy_Accounting_Requests = 'FreeRADIUS-Total-Proxy-Accounting-Requests'
_FreeRADIUS_Total_Proxy_Accounting_Responses = 'FreeRADIUS-Total-Proxy-Accounting-Responses'
_FreeRADIUS_Total_Proxy_Acct_Duplicate_Requests = 'FreeRADIUS-Total-Proxy-Acct-Duplicate-Requests'
_FreeRADIUS_Total_Proxy_Acct_Malformed_Requests = 'FreeRADIUS-Total-Proxy-Acct-Malformed-Requests'
_FreeRADIUS_Total_Proxy_Acct_Invalid_Requests = 'FreeRADIUS-Total-Proxy-Acct-Invalid-Requests'
_FreeRADIUS_Total_Proxy_Acct_Dropped_Requests = 'FreeRADIUS-Total-Proxy-Acct-Dropped-Requests'
_FreeRADIUS_Total_Proxy_Acct_Unknown_Types = 'FreeRADIUS-Total-Proxy-Acct-Unknown-Types'

_FreeRADIUS_Total_Proxy_Accounting = [
    (_FreeRADIUS_Total_Proxy_Acct_Dropped_Requests, _Dropped),
    (_FreeRADIUS_Total_Proxy_Acct_Duplicate_Requests, _Duplicate),
    (_FreeRADIUS_Total_Proxy_Acct_Invalid_Requests, _Invalid),
    (_FreeRADIUS_Total_Proxy_Acct_Malformed_Requests, _Malformed),
    (_FreeRADIUS_Total_Proxy_Accounting_Requests, _Requests),
    (_FreeRADIUS_Total_Proxy_Accounting_Responses, _Responses),
    (_FreeRADIUS_Total_Proxy_Acct_Unknown_Types, _Unknown_Types),
]


def _parameter_valuespec_freeradius_total_proxy_accounting():
    return Dictionary(
        title=_('FreeRADIUS proxy accounting'),
        optional_keys=True,
        elements=[
            _list_attributes,
            _attributes(_FreeRADIUS_Total_Proxy_Accounting, 'Proxy Accounting'),
        ],
        required_keys=['attributes']
    )


rulespec_registry.register(
    CheckParameterRulespecWithoutItem(
        title=lambda: _('FreeRADIUS proxy accounting'),
        check_group_name='freeradius_total_proxy_accounting',
        group=RulespecGroupCheckParametersApplications,
        parameter_valuespec=_parameter_valuespec_freeradius_total_proxy_accounting,
        match_type='dict',
    )
)
