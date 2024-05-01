#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# License: GNU General Public License v2
#
# Author: thl-cmk[at]outlook[dot]com
# URL   : https://thl-cmk.hopto.org
# Date  : 2024-04-29
# File  : agent_freeradius.py (special agent)

# /etc/freeradius/3.0/radiusd.conf
# security {
#     status_server = yes
# }

#
# /etc/freeradius/3.0/sites-enabled/status
#
# server status {
#         listen {
#                 type = status
#                 # ipaddr = 127.0.0.1
#                 ipaddr = 0.0.0.0
#                 port = 18121
#         }
#         client cmkbuild {
#                 ipaddr = 192.168.10.99
#                 secret = adminsecret
#         }
# }
#

import socket
import pyrad.client
from argparse import Namespace
from collections.abc import Mapping, Sequence
from json import dumps as json_dumps
from os import environ
from sys import (
    exit as sys_exit,
    stdout as sys_stdout,
)

from cmk.special_agents.utils.agent_common import (
    special_agent_main,
)
from cmk.special_agents.utils.argument_parsing import create_default_argument_parser

no_radiuslib = False
try:
    from pyrad.client import Client as radClient
    from pyrad.dictionary import Dictionary as radDictionary
    from pyrad.packet import AccessAccept, AccessReject, AccessRequest, StatusServer
    from pyrad.client import Timeout as pyTimeout
except ModuleNotFoundError:
    no_radiuslib = True

VERSION = '0.1.1-20240430'


class Args(Namespace):
    host: str
    secret: str
    username: str
    password: str
    auth_port: int
    timeout: int


def write_section(message: Mapping[str, any]):
    sys_stdout.write('\n<<<freeradius:sep(0)>>>\n')
    sys_stdout.write(json_dumps(message))
    sys_stdout.write('\n<<<>>>\n')


def parse_arguments(argv: Sequence[str] | None) -> Args:
    parser = create_default_argument_parser(__doc__)
    parser.description = 'This is a CMK special agent to collect stats data from FreeRADIS servers.'
    parser.epilog = (
        f'(c) thl-cmk[at]outlook[dot], Version: {VERSION}, '
        f'For more information see: https://thl-cmk.hopto.org'
    )

    parser.add_argument(
        '-H', '--host', required=True,
        help='Host/IP-Address of RADIUS server to query (required)',
    )
    parser.add_argument(
        '--secret', required=True,
        help='secret RADIUS key',
    )
    parser.add_argument(
        '--auth-port', type=int, default=18121,
        help='RADIUS authentication port to use.',
    )
    parser.add_argument(
        '--timeout', type=int, default=1,
        help='RADIUS server timeout',
    )

    return parser.parse_args(argv)


def agent_freeradius_main(args: Args) -> int:
    if no_radiuslib:
        write_section(
            {
                'error': 'To use this special agent, you must install the Python '
                         'library “pyrad” in your CMK Python environment.'
            }
        )
        sys_exit(0)

    omd_root = environ["OMD_ROOT"]
    path_to_dict = f'{omd_root}/local/lib/check_mk/special_agents'
    # status request
    status_srv = radClient(
        server=args.host.strip(),  # not sure where the leading spce comes from
        authport=args.auth_port,
        secret=args.secret.encode('utf-8'),
        dict=radDictionary(f"{path_to_dict}/dictionary"),
        retries=1,
        timeout=args.timeout,
    )
    status = status_srv.CreateAuthPacket(
        code=StatusServer,
        NAS_Identifier="checkmk",
    )
    # https://freeradius.org/documentation/freeradius-server/3.2.4/howto/monitoring/statistics.html
    # status.AddAttribute("FreeRADIUS-Statistics-Type", "Authentication")
    # status.AddAttribute("FreeRADIUS-Statistics-Type", "Accounting")
    # status.AddAttribute("FreeRADIUS-Statistics-Type", "Proxy-Authentication")
    # status.AddAttribute("FreeRADIUS-Statistics-Type", "Proxy-Accounting")
    # status.AddAttribute("FreeRADIUS-Statistics-Type", "Internal")
    # status.AddAttribute("FreeRADIUS-Statistics-Type", "Client")
    # status.AddAttribute('FreeRADIUS-Stats-Client-IP-Address', "192.168.10.99")
    # status.AddAttribute("FreeRADIUS-Statistics-Type", "Server")
    # status.AddAttribute("FreeRADIUS-Stats-Server-IP-Address", "192.168.10.95")
    # status.AddAttribute("FreeRADIUS-Stats-Server-Port", "1645")
    # status.AddAttribute("FreeRADIUS-Statistics-Type", "Home-Server")
    status.AddAttribute("FreeRADIUS-Statistics-Type", "All")

    status.add_message_authenticator()
    try:
        response = status_srv.SendPacket(status)
    except pyrad.client.Timeout as e:
        write_section({'error': f'Special agent request timeout, check configuration!. ({e})'})
        sys_exit()
    except socket.gaierror as e:
        write_section(({'error': f'Special agent network error, check Configuration. ({e})'}))
        sys_exit()

    if response.code == AccessAccept:
        attributes = {
            attribute: response.get(attribute)[0]
            for attribute in response.keys() if isinstance(attribute, str)}
        write_section(attributes)
    else:
        write_section({'error': 'Response access reject, check configuration'})

    return 0


def main() -> int:
    return special_agent_main(parse_arguments, agent_freeradius_main)
