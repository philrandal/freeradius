#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# License: GNU General Public License v2
#
#
# Author: thl-cmk[at]outlook[dot]com
# URL   : https://thl-cmk.hopto.org
# Date  : 2024-04-29
# File  : wato/agent_freeradius.py
#


from cmk.gui.i18n import _
from cmk.gui.plugins.wato.special_agents.common import RulespecGroupDatasourceProgramsApps
from cmk.gui.plugins.wato.utils import HostRulespec, IndividualOrStoredPassword, rulespec_registry
from cmk.gui.valuespec import (
    Dictionary,
    Integer,
    # TextInput,
    Transform,
    ValueSpec,
)


def _valuespec_special_agent_freeradius() -> ValueSpec:
    return Transform(
        Dictionary(
            title=_('FreeRADIUS'),
            help=_(''),
            elements=[
                # ('server',
                #  TextInput(
                #      title=_('Server IP-address or name'),
                #      help=_(
                #          'Hostname or IP-address to monitor. Default is the host name/IP-Address of the monitored host.'
                #      ),
                #      size=50,
                #      allow_empty=False,
                #      placeholder='i.e 192.168.10.10 or srvrad01.company.intern'
                #  )),
                ('auth_port',
                 Integer(
                     title=_('Authentication port'),
                     help=_('The RADIUS port to use for authentication. Default is 18121.'),
                     size=5,
                     default_value=18121,
                     minvalue=1,
                     maxvalue=65535,
                 )),
                ('secret',
                 IndividualOrStoredPassword(
                     title=_('Shared secret'),
                     help=_('The shared secret.'),
                     allow_empty=False,
                 )),
                ('timeout',
                 Integer(
                     title=_('Request timeout'),
                     help=_('The timeout for the RADIUS request.'),
                     default_value=2,
                     minvalue=1,
                     maxvalue=30,
                     unit='s',
                 )),
                # ('user_name',
                #  TextInput(
                #      title=_('Username'),
                #      help=_('The username to use in the request.'),
                #      size=50,
                #      placeholder='username to use in the request',
                #      allow_empty=False,
                #  )),
                # ('user_password',
                #  IndividualOrStoredPassword(
                #      title=_('User password'),
                #      help=_('The user password.'),
                #      allow_empty=False
                #  )),
            ],
            required_keys=[
                'secret',
            ]
        ),
    )


rulespec_registry.register(
    HostRulespec(
        group=RulespecGroupDatasourceProgramsApps,
        name="special_agents:freeradius",
        valuespec=_valuespec_special_agent_freeradius,
    )
)
