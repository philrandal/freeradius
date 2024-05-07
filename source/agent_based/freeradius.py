#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# License: GNU General Public License v2
#
# Author: thl-cmk[at]outlook[dot]com
# URL   : https://thl-cmk.hopto.org
# Date  : 2024-04-29
# File  : freeradius.py (check plugin)

# 2024-05-06: fixed crash in _rate_attributes (missing values to unpack)
#             changed time output to render.datetime
# 2024-05-07: changed max CMK version in package info to 2.3.0b1

from _collections_abc import Mapping, Sequence
from json import loads as json_loads, JSONDecodeError
from time import time as now_tine
# from time import localtime, mktime, strftime, strptime, time as now_tine


from cmk.base.plugins.agent_based.agent_based_api.v1 import (
    Result,
    Service,
    State,
    check_levels,
    register,
    render,
    get_rate,
    GetRateError,
    get_value_store,
)
from cmk.base.plugins.agent_based.agent_based_api.v1.type_defs import (
    CheckResult,
    DiscoveryResult,
    StringTable,
)

# _CMK_TIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%m %Z'
# _FREERADIUS_TIME_FORMAT = "%b %d %Y %H:%M:%S %Z"

# Authentication attributes
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
# Accounting attributes
_FreeRADIUS_Total_Accounting_Requests = 'FreeRADIUS-Total-Accounting-Requests'
_FreeRADIUS_Total_Accounting_Responses = 'FreeRADIUS-Total-Accounting-Responses'
_FreeRADIUS_Total_Acct_Duplicate_Requests = 'FreeRADIUS-Total-Acct_Duplicate-Requests'
_FreeRADIUS_Total_Acct_Malformed_Requests = 'FreeRADIUS-Total-Acct-Malformed-Requests'
_FreeRADIUS_Total_Acct_Invalid_Requests = 'FreeRADIUS-Total-Acct-Invalid-Requests'
_FreeRADIUS_Total_Acct_Dropped_Requests = 'FreeRADIUS-Total-Acct-Dropped-Requests'
_FreeRADIUS_Total_Acct_Unknown_Types = 'FreeRADIUS-Total-Acct-Unknown-Types'
_FreeRADIUS_Total_Acct_Conflicts = 'FreeRADIUS-Total-Acct-Conflicts'
# Internal Attributes
_FreeRADIUS_Stats_Start_Time = 'FreeRADIUS-Stats-Start-Time'
_FreeRADIUS_Stats_HUP_Time = 'FreeRADIUS-Stats-HUP-Time'
_FreeRADIUS_Queue_Len_Internal = 'FreeRADIUS-Queue-Len-Internal'
_FreeRADIUS_Queue_Len_Proxy = 'FreeRADIUS-Queue-Len-Proxy'
_FreeRADIUS_Queue_Len_Auth = 'FreeRADIUS-Queue-Len-Auth'
_FreeRADIUS_Queue_Len_Acct = 'FreeRADIUS-Queue-Len-Acct'
_FreeRADIUS_Queue_Len_Detail = 'FreeRADIUS-Queue-Len-Detail'
_FreeRADIUS_Queue_PPS_In = 'FreeRADIUS-Queue-PPS-In'
_FreeRADIUS_Queue_PPS_Out = 'FreeRADIUS-Queue-PPS-Out'
# Proxy-Authentication attributes
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
# Proxy-Accounting attributes
_FreeRADIUS_Total_Proxy_Accounting_Requests = 'FreeRADIUS-Total-Proxy-Accounting-Requests'
_FreeRADIUS_Total_Proxy_Accounting_Responses = 'FreeRADIUS-Total-Proxy-Accounting-Responses'
_FreeRADIUS_Total_Proxy_Acct_Duplicate_Requests = 'FreeRADIUS-Total-Proxy-Acct-Duplicate-Requests'
_FreeRADIUS_Total_Proxy_Acct_Malformed_Requests = 'FreeRADIUS-Total-Proxy-Acct-Malformed-Requests'
_FreeRADIUS_Total_Proxy_Acct_Invalid_Requests = 'FreeRADIUS-Total-Proxy-Acct-Invalid-Requests'
_FreeRADIUS_Total_Proxy_Acct_Dropped_Requests = 'FreeRADIUS-Total-Proxy-Acct-Dropped-Requests'
_FreeRADIUS_Total_Proxy_Acct_Unknown_Types = 'FreeRADIUS-Total-Proxy-Acct-Unknown-Types'

_FreeRADIUS_Authentication = [
    _FreeRADIUS_Total_Access_Requests,
    _FreeRADIUS_Total_Auth_Responses,
    _FreeRADIUS_Total_Access_Accepts,
    _FreeRADIUS_Total_Access_Rejects,
    _FreeRADIUS_Total_Access_Challenges,
    _FreeRADIUS_Total_Auth_Duplicate_Requests,
    _FreeRADIUS_Total_Auth_Malformed_Requests,
    _FreeRADIUS_Total_Auth_Invalid_Requests,
    _FreeRADIUS_Total_Auth_Dropped_Requests,
    _FreeRADIUS_Total_Auth_Unknown_Types,
    _FreeRADIUS_Total_Auth_Conflicts,
]

_FreeRADIUS_Accounting = [
    _FreeRADIUS_Total_Accounting_Requests,
    _FreeRADIUS_Total_Accounting_Responses,
    _FreeRADIUS_Total_Acct_Duplicate_Requests,
    _FreeRADIUS_Total_Acct_Malformed_Requests,
    _FreeRADIUS_Total_Acct_Invalid_Requests,
    _FreeRADIUS_Total_Acct_Dropped_Requests,
    _FreeRADIUS_Total_Acct_Unknown_Types,
    _FreeRADIUS_Total_Acct_Conflicts
]

_FreeRADIUS_Queue = [
    _FreeRADIUS_Queue_PPS_In,
    _FreeRADIUS_Queue_PPS_Out,
    _FreeRADIUS_Queue_Len_Acct,
    _FreeRADIUS_Queue_Len_Auth,
    _FreeRADIUS_Queue_Len_Detail,
    _FreeRADIUS_Queue_Len_Internal,
    _FreeRADIUS_Queue_Len_Proxy,
]

_FreeRADIUS_Total_Proxy_Authentication = [
    _FreeRADIUS_Total_Proxy_Access_Requests,
    _FreeRADIUS_Total_Proxy_Auth_Responses,
    _FreeRADIUS_Total_Proxy_Access_Accepts,
    _FreeRADIUS_Total_Proxy_Access_Challenges,
    _FreeRADIUS_Total_Proxy_Access_Rejects,
    _FreeRADIUS_Total_Proxy_Auth_Dropped_Requests,
    _FreeRADIUS_Total_Proxy_Auth_Duplicate_Requests,
    _FreeRADIUS_Total_Proxy_Auth_Invalid_Requests,
    _FreeRADIUS_Total_Proxy_Auth_Malformed_Requests,
    _FreeRADIUS_Total_Proxy_Auth_Unknown_Types,
]

_FreeRADIUS_Total_Proxy_Accounting = [
    _FreeRADIUS_Total_Proxy_Accounting_Requests,
    _FreeRADIUS_Total_Proxy_Accounting_Responses,
    _FreeRADIUS_Total_Proxy_Acct_Dropped_Requests,
    _FreeRADIUS_Total_Proxy_Acct_Duplicate_Requests,
    _FreeRADIUS_Total_Proxy_Acct_Invalid_Requests,
    _FreeRADIUS_Total_Proxy_Acct_Malformed_Requests,
    _FreeRADIUS_Total_Proxy_Acct_Unknown_Types,
]


def _get_metric(rwa_attribute: str) -> str:
    return rwa_attribute.lower().replace('-', '_')


def _rate_attributes(params: Mapping[str, any], section: Mapping[str, int], attributes: Sequence):
    def _get_label(raw_attribute: str) -> str:
        raw_attribute = raw_attribute.replace('FreeRADIUS-Total-Proxy-', '')
        raw_attribute = raw_attribute.replace('FreeRADIUS-Total-', '')
        raw_attribute = raw_attribute.replace('Access-', '')
        raw_attribute = raw_attribute.replace('Auth-', '')
        raw_attribute = raw_attribute.replace('Accounting-', '')
        raw_attribute = raw_attribute.replace('Acct-', '')
        raw_attribute = raw_attribute.replace('-', ' ')
        raw_attribute = raw_attribute.replace(' Requests', '')

        return raw_attribute

    attribute_params = {attribute: params for attribute, params in params.get('attributes', [])}
    now = now_tine()
    value_store = get_value_store()

    for attribute, notice_only in attributes:
        if (value := section.get(attribute)) is not None:
            try:
                value = get_rate(value_store, _get_metric(attribute), now, value, raise_overflow=True)
            except GetRateError:
                continue
            yield from check_levels(
                value=value,
                label=_get_label(attribute),
                render_func=lambda v: f'{v:.2f}/s',
                metric_name=_get_metric(attribute),
                notice_only=attribute_params.get(attribute, {}).get('info_line', notice_only),
                levels_upper=attribute_params.get(attribute, {}).get('upper'),
                levels_lower=attribute_params.get(attribute, {}).get('lower'),
            )


def _list_attributes(section: Mapping[str, int], attributes: Sequence[str] | None):
    yield Result(state=State.OK, notice=f'\nAttributes:')
    for key, value in section.items():
        if attributes is None or key in attributes:
            yield Result(state=State.OK, notice=f'{key}:{value}')


def parse_freeradius(string_table: StringTable) -> Mapping[str, int] | None:
    try:
        return json_loads(string_table[0][0])
    except (JSONDecodeError, TypeError):
        return


register.agent_section(
    name="freeradius",
    parse_function=parse_freeradius,
)


def discover_freeradius(section: Mapping[str, int]) -> DiscoveryResult:
    yield Service()


def check_freeradius(params: Mapping[str, any], section: Mapping[str, int]) -> CheckResult:
    if 'error' in section:
        yield Result(state=State.CRIT, summary=section['error'])
        return
    if (start_time := section.get(_FreeRADIUS_Stats_Start_Time)) is None or (
            hup_time := section.get(_FreeRADIUS_Stats_HUP_Time)) is None:
        yield Result(
            state=State.WARN,
            summary=f'Response attributes {_FreeRADIUS_Stats_Start_Time} and {_FreeRADIUS_Stats_Start_Time} not found.'
        )
        return

    # if isinstance(start_time, str):
    #     # str to sec "Apr 29 2024 10:09:54 CEST" -> 1714378194.0
    #     start_time = mktime(strptime(start_time, _FREERADIUS_TIME_FORMAT))
    # if isinstance(hup_time, str):
    #     hup_time = mktime(strptime(hup_time, _FREERADIUS_TIME_FORMAT))

    yield from check_levels(
        value=now_tine() - start_time,
        label='Uptime',
        render_func=render.timespan,
        metric_name='uptime',
    )

    yield from check_levels(
        value=now_tine() - hup_time,
        label='Reload',
        render_func=render.timespan,
        metric_name='reload',
    )

    # yield Result(
    #     state=State.OK,
    #     notice=f'Service started at: {strftime(_CMK_TIME_FORMAT, localtime(start_time))}'
    # )
    yield Result(state=State.OK, notice=f'Service started at: {render.datetime(start_time)}')
    if start_time != hup_time:
        # yield Result(
        #     state=State.OK,
        #     notice=f'Service restarted (HUP) at: {strftime(_CMK_TIME_FORMAT, localtime(hup_time))}'
        # )
        yield Result(state=State.OK, notice=f'Service reloaded (HUP) at: {render.datetime(hup_time)}')
    else:
        yield Result(state=State.OK, notice='Service reloaded (HUP) at: never')

    yield Result(state=State.OK, summary=f'# of status attributes: {len(section)}')

    if params.get('list_attributes'):
        yield from _list_attributes(section, None)


register.check_plugin(
    name='freeradius',
    service_name='FreeRADIUS',
    sections=['freeradius'],
    discovery_function=discover_freeradius,
    check_function=check_freeradius,
    check_default_parameters={},
    check_ruleset_name='freeradius',
)


def discover_freeradius_queue(section: Mapping[str, int]) -> DiscoveryResult:
    for attribute in _FreeRADIUS_Queue:
        if attribute in section:
            yield Service()
            break


def check_freeradius_queue(params: Mapping[str, any], section: Mapping[str, int]) -> CheckResult:
    def _get_label(raw_attribute: str) -> str:
        raw_attribute = raw_attribute.replace('FreeRADIUS-Queue-', '')
        raw_attribute = raw_attribute.replace('Len-', '')
        raw_attribute = raw_attribute.replace('Acct', 'Accounting')
        raw_attribute = raw_attribute.replace('Auth', 'Authentication')
        raw_attribute = raw_attribute.replace('-', ' ')
        return raw_attribute

    attribute_params = {attribute: params for attribute, params in params.get('attributes', [])}
    attributes = [
        # attribute, notice_only
        (_FreeRADIUS_Queue_PPS_In, False),
        (_FreeRADIUS_Queue_PPS_Out, False),
        (_FreeRADIUS_Queue_Len_Acct, True),
        (_FreeRADIUS_Queue_Len_Auth, True),
        (_FreeRADIUS_Queue_Len_Detail, True),
        (_FreeRADIUS_Queue_Len_Internal, True),
        (_FreeRADIUS_Queue_Len_Proxy, True),
    ]
    for attribute, notice_only in attributes:
        if (value := section.get(attribute)) is not None:
            yield from check_levels(
                value=value,
                label=_get_label(attribute),
                render_func=lambda v: f'{v}',
                metric_name=_get_metric(attribute),
                notice_only=attribute_params.get(attribute, {}).get('info_line', notice_only),
                levels_upper=attribute_params.get(attribute, {}).get('upper'),
                levels_lower=attribute_params.get(attribute, {}).get('lower'),
            )
    if params.get('list_attributes'):
        yield from _list_attributes(section, _FreeRADIUS_Queue)


register.check_plugin(
    name='freeradius_queue',
    service_name='FreeRADIUS queue',
    sections=['freeradius'],
    discovery_function=discover_freeradius_queue,
    check_function=check_freeradius_queue,
    check_default_parameters={},
    check_ruleset_name='freeradius_queue',
)


def discover_freeradius_total_authentication(section: Mapping[str, int]) -> DiscoveryResult:
    for attribute in _FreeRADIUS_Authentication:
        if attribute in section:
            yield Service()
            break


def check_freeradius_total_authentication(params: Mapping[str, any], section: Mapping[str, int]) -> CheckResult:
    attributes = [
        # attribute, notice_only
        (_FreeRADIUS_Total_Access_Requests, False),
        (_FreeRADIUS_Total_Auth_Responses, False),
        (_FreeRADIUS_Total_Access_Accepts, True),
        (_FreeRADIUS_Total_Access_Rejects, True),
        (_FreeRADIUS_Total_Auth_Dropped_Requests, True),
        (_FreeRADIUS_Total_Access_Challenges, True),
        (_FreeRADIUS_Total_Auth_Duplicate_Requests, True),
        (_FreeRADIUS_Total_Auth_Malformed_Requests, True),
        (_FreeRADIUS_Total_Auth_Invalid_Requests, True),
        (_FreeRADIUS_Total_Auth_Unknown_Types, True),
        (_FreeRADIUS_Total_Auth_Conflicts, True),
    ]
    yield from _rate_attributes(params, section, attributes)

    if params.get('list_attributes'):
        yield from _list_attributes(section, _FreeRADIUS_Authentication)


register.check_plugin(
    name='freeradius_total_authentication',
    service_name='FreeRADIUS authentication',
    sections=['freeradius'],
    discovery_function=discover_freeradius_total_authentication,
    check_function=check_freeradius_total_authentication,
    check_default_parameters={},
    check_ruleset_name='freeradius_total_authentication',
)


def discover_freeradius_total_accounting(section: Mapping[str, int]) -> DiscoveryResult:
    for attribute in _FreeRADIUS_Accounting:
        if attribute in section:
            yield Service()
            break


def check_freeradius_total_accounting(params: Mapping[str, any], section: Mapping[str, int]) -> CheckResult:
    attributes = [
        # attribute, notice_only
        (_FreeRADIUS_Total_Accounting_Requests, False),
        (_FreeRADIUS_Total_Accounting_Responses, False),
        (_FreeRADIUS_Total_Acct_Dropped_Requests, True),
        (_FreeRADIUS_Total_Acct_Duplicate_Requests, True),
        (_FreeRADIUS_Total_Acct_Malformed_Requests, True),
        (_FreeRADIUS_Total_Acct_Invalid_Requests, True),
        (_FreeRADIUS_Total_Acct_Unknown_Types, True),
        (_FreeRADIUS_Total_Acct_Conflicts, True),
    ]
    yield from _rate_attributes(params, section, attributes)

    if params.get('list_attributes'):
        yield from _list_attributes(section, _FreeRADIUS_Accounting)


register.check_plugin(
    name='freeradius_total_accounting',
    service_name='FreeRADIUS accounting',
    sections=['freeradius'],
    discovery_function=discover_freeradius_total_accounting,
    check_function=check_freeradius_total_accounting,
    check_default_parameters={},
    check_ruleset_name='freeradius_total_accounting',
)


def discover_freeradius_total_proxy_authentication(section: Mapping[str, int]) -> DiscoveryResult:
    for attribute in _FreeRADIUS_Total_Proxy_Authentication:
        if attribute in section:
            yield Service()
            break


def check_freeradius_total_proxy_authentication(params: Mapping[str, any], section: Mapping[str, int]) -> CheckResult:
    attributes = [
        # attribute, notice_only
        (_FreeRADIUS_Total_Proxy_Access_Requests, False),
        (_FreeRADIUS_Total_Proxy_Auth_Responses, False),
        (_FreeRADIUS_Total_Proxy_Access_Accepts, True),
        (_FreeRADIUS_Total_Proxy_Access_Rejects, True),
        (_FreeRADIUS_Total_Proxy_Access_Challenges, True),
        (_FreeRADIUS_Total_Proxy_Auth_Duplicate_Requests, True),
        (_FreeRADIUS_Total_Proxy_Auth_Malformed_Requests, True),
        (_FreeRADIUS_Total_Proxy_Auth_Invalid_Requests, True),
        (_FreeRADIUS_Total_Proxy_Auth_Dropped_Requests, True),
        (_FreeRADIUS_Total_Proxy_Auth_Unknown_Types, True),
    ]
    yield from _rate_attributes(params, section, attributes)

    if params.get('list_attributes'):
        yield from _list_attributes(section, _FreeRADIUS_Total_Proxy_Authentication)


register.check_plugin(
    name='freeradius_total_proxy_authentication',
    service_name='FreeRADIUS proxy authentication',
    sections=['freeradius'],
    discovery_function=discover_freeradius_total_proxy_authentication,
    check_function=check_freeradius_total_proxy_authentication,
    check_default_parameters={},
    check_ruleset_name='freeradius_total_proxy_authentication',
)


def discover_freeradius_total_proxy_accounting(section: Mapping[str, int]) -> DiscoveryResult:
    for attribute in _FreeRADIUS_Total_Proxy_Accounting:
        if attribute in section:
            yield Service()
            break


def check_freeradius_total_proxy_accounting(params: Mapping[str, any], section: Mapping[str, int]) -> CheckResult:
    attribute = [
        # attribute, notice_only
        (_FreeRADIUS_Total_Proxy_Accounting_Requests, False),
        (_FreeRADIUS_Total_Proxy_Accounting_Responses, False),
        (_FreeRADIUS_Total_Proxy_Acct_Duplicate_Requests, True),
        (_FreeRADIUS_Total_Proxy_Acct_Malformed_Requests, True),
        (_FreeRADIUS_Total_Proxy_Acct_Invalid_Requests, True),
        (_FreeRADIUS_Total_Proxy_Acct_Dropped_Requests, True),
        (_FreeRADIUS_Total_Proxy_Acct_Unknown_Types, True),
    ]
    yield from _rate_attributes(params, section, attribute)

    if params.get('list_attributes'):
        yield from _list_attributes(section, _FreeRADIUS_Total_Proxy_Accounting)


register.check_plugin(
    name='freeradius_total_proxy_accounting',
    service_name='FreeRADIUS proxy accounting',
    sections=['freeradius'],
    discovery_function=discover_freeradius_total_proxy_accounting,
    check_function=check_freeradius_total_proxy_accounting,
    check_default_parameters={},
    check_ruleset_name='freeradius_total_proxy_accounting',
)
