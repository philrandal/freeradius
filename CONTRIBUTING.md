# Contributing

If you have any issues or ideas for improvement you can contact me in the [CMK forum](https://forum.checkmk.com/) by sending me a direct message to `@thl-cmk` (this is the prefered way) or send an email to _thl-cmk[at]outlook[dot]com_.

Please include:
- your CMK version/edition
- your environment (stand alone or distributed)
- the OS of your CMK server(s)
- the version of the plugin
- the crash report (if any)

For active checks I might need the output of the check command. I.e.

```
~$ ./local/lib/nagios/plugins/check_ntp -H ares
Stratum: 3, Reference ID: 194.25.134.196, Time: Sun Apr  7 13:38:52 2024
 ....
 | ntp_offset=-0.005115509033203125;0.2;0.5; ntp_delay=0.02794170379638672;0.2;0.5; ntp_root_dispersion=0.0051116943359375;200;500;

```

For agent based plugins I might need also the agent output of the plugin.
```
$ /omd/sites/build/local/share/check_mk/agents/special/agent_cisco_meraki Meraki_Cloud 
<<<cisco_meraki_org_organisations:sep(0)>>>
...
...
...

```

For SNMP based plugins I migth need a snmpwalk fom the device in question. This must contain
```
.1.3.6.1.2.1.1.1 sysDescr
.1.3.6.1.2.1.1.2 sysObjectID
```
and all the SNMP OIDs used in the plugin.
If you run the snmpwalk command, please uses these options -ObentU in addition to your snmp options like community, version etc.
For example:

```
snmpwalk -v2c -c public -ObentU 10.10.10.10 .1.3.6.1.2.1.1.1 > hostname.snmpwalk
snmpwalk -v2c -c public -ObentU 10.10.10.10 .1.3.6.1.2.1.1.2 >> hostname.snmpwalk
snmpwalk -v2c -c public -ObentU 10.10.10.10 .1.0.8802.1.1.2.1.4.1.1 >> hostname.snmpwalk
snmpwalk -v2c -c public -ObentU 10.10.10.10 .1.0.8802.1.1.2.1.3.7.1.3 >> hostname.snmpwalk
```

