[PACKAGE]: ../../raw/master/mkp/freeradius-0.1.3-20240617.mkp "freeradius-0.1.3-20240617.mkp"
[PYRADLIB]: ../../raw/master/mkp/pyrad-2.4.0-240421.mkp "pyrad-2.4.0-240421.mkp"
# FreeRADIUS

This is a special agent to monitor FreeRADIUS servers. It will connect to the FreeRADIUS status server using the RADIUS protocol.

---
### Download
* [Download latest mkp file][PACKAGE]
* [pyrad-2.4.0-240421.mkp][PYRADLIB] The pyrad lib as MKP (contains pyrad 2.4, six 1.16.0, netaddr 1.2.1).

**Note**: before you update to a newer version, always check the [CHANGELOG](CHANGELOG). There migth be incompatible changes.
                        
---
### Installation

You can install the package by uploading it to your CheckMK site and as site user run 
```
mkp add PAKAGE_NAME.mkp
mkp enable PAKAGE_NAME VERSION
```

In the Enterprise/Free/Cloud edition of CheckMK you can use the GUI to install the package (_Setup_ -> _Extension Packages_ -> _Upload package_)

**Note**: before you can use this plugin you need to install the python lib [**_pyrad_**](https://github.com/pyradius/pyrad) into your CMK site. This can be done by issuing the command `pip3 install pyrad` as site user, as long as your CMK server has internet access. If you prefer not to download the pyrad lib from the internet you can also use the additional MKP package **_pyrad-2.4.0-240421.mkp_** (see above).

To use this plugin the `status` module of the FreeRADIUS server must be enabled und accessible from the CheckMK site (see [Status of FreeRADIUS](https://wiki/freeradius.org/config/Status))

---
### Want to Contribute?

Nice ;-) Have a look at the [contribution guidelines](CONTRIBUTING.md "Contributing")

---
### Check Info

The plugin creates the services
- FreeRADIUS
- FreeRADIUS accounting
- FreeRADIUS authentication
- FreeRADIUS proxy accounting
- FreeRADIUS proxy authentication
- FreeRADIUS queue

<details><summary>Montoring states</summary>

The state is always OK, except for configured levels.

</details>

<details><summary>Perfdata</summary>

| Metric | Unit | Perfometer |
| ------ | ------ | ------ |
| Uptime | s | yes |
| Reload | s | no |
| Queue: PPS In/Out | count | yes |
| Queue: Accounting/Authentication/Detail/Internal/Proxy | count | no |
| (Proxy) Accounting/Authentication: Requests/Responses | 1/s | yes |
| (Proxy) Accounting/Authentication: Conflicts/Dropped/Malformed/Invalid/Unknown Types | 1/s | no |
| (Proxy) Authentication: Accepts/Rejects/Dropped/Challenges | 1/s | no |


</details>

---
### WATO
<details><summary>Special agent rule</summary>

| Section | Rule name |
| ------ | ------ |
| Other integrations -> Applications | FreeRADIUS  |

| Option | Defailt value |
| ------ | ------ |
| Authentication port | 18121 |
| Shared secret | none |
| Request timeout | 2 seconds |

</details> 

<details><summary>Service monitoring rules</summary>

| Section | Rule name |
| ------ | ------ |
| Applications, Processes & Services | FreeRADIUS  |
| Applications, Processes & Services | FreeRADIUS  acconting |
| Applications, Processes & Services | FreeRADIUS  authentication |
| Applications, Processes & Services | FreeRADIUS  proxy accounting |
| Applications, Processes & Services | FreeRADIUS  proxy authentication |
| Applications, Processes & Services | FreeRADIUS  queue |

| Option | Defailt value | Comment |
| ------ | ------ | ---- | 
| List response attributes in service details | No | for each servise |
| Upper Levels | none | for each monitored attribute |
| Lower Levels | none | for each monitored attribute |
| Show on info line | no | for each monitored attribute |

</details> 

<details><summary>Discovery rule</summary>
There is no discovery rule.
</details> 

<details><summary>HW/SW inventory rules</summary>
There is no inventory rule.
</details> 

<details><summary>Special agent CLI usage</summary>

```
:~$ ~/local/share/check_mk/agents/special/agent_freeradius -h
usage: agent_freeradius [-h] [--debug] [--verbose] [--vcrtrace TRACEFILE] -H HOST --secret SECRET [--auth-port AUTH_PORT] [--timeout TIMEOUT]

This is a CMK special agent to collect stats data from FreeRADIS servers.

options:
  -h, --help            show this help message and exit
  --debug, -d           Enable debug mode (keep some exceptions unhandled)
  --verbose, -v
  --vcrtrace TRACEFILE, --tracefile TRACEFILE
                            If this flag is set to a TRACEFILE that does not exist yet, it will be created and
                            all requests the program sends and their corresponding answers will be recorded in said file.
                            If the file already exists, no requests are sent to the server, but the responses will be
                            replayed from the tracefile. 
  -H HOST, --host HOST  Host/IP-Address of RADIUS server to query (required)
  --secret SECRET       secret RADIUS key
  --auth-port AUTH_PORT
                        RADIUS authentication port to use.
  --timeout TIMEOUT     RADIUS server timeout

(c) thl-cmk[at]outlook[dot], Version: 0.1.1-20240430, For more information see: https://thl-cmk.hopto.org

```
</details>

---
### Sample Output

Sample output

![sample output](img/sample.png?raw=true "sample output")

Sample output details

![sample output details](img/sample-details.png?raw=true "sample output details")

