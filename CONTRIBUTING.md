# Contributing

If you have any issues or ideas for improvement, you can contact me in the [CMK forum](https://forum.checkmk.com/) by sending me a direct message to `@thl-cmk` (this is the prefered way) or send an email to _thl-cmk[at]outlook[dot]com_.

Please include:
- your CMK version/edition
- your environment (stand alone or distributed)
- the OS of your CMK server(s)
- the version of the plugin
- the crash report (if any)

For agent based plugins I might need also the agent output of the plugin.
```
~$ /omd/sites/build/local/share/check_mk/agents/special/agent_freeradius '-H freeradius' --auth-port 18121 --secret bigsecret --debug

<<<freeradius:sep(0)>>>
{"FreeRADIUS-Total-Access-Requests": 6142999, "FreeRADIUS-Total-Access-Accepts": 6072700, "FreeRADIUS-Total-Access-Rejects": 68440, "FreeRADIUS-Total-Access-Challenges": 0, "FreeRADIUS-Total-Auth-Responses": 6141140, "FreeRADIUS-Total-Auth-Duplicate-Requests": 970, "FreeRADIUS-Total-Auth-Malformed-Requests": 0, "FreeRADIUS-Total-Auth-Invalid-Requests": 0, "FreeRADIUS-Total-Auth-Dropped-Requests": 970, "FreeRADIUS-Total-Auth-Unknown-Types": 0, "FreeRADIUS-Total-Auth-Conflicts": 0, "FreeRADIUS-Total-Accounting-Requests": 0, "FreeRADIUS-Total-Accounting-Responses": 0, "FreeRADIUS-Total-Acct-Duplicate-Requests": 0, "FreeRADIUS-Total-Acct-Malformed-Requests": 0, "FreeRADIUS-Total-Acct-Invalid-Requests": 0, "FreeRADIUS-Total-Acct-Dropped-Requests": 0, "FreeRADIUS-Total-Acct-Unknown-Types": 0, "FreeRADIUS-Total-Acct-Conflicts": 0, "FreeRADIUS-Total-Proxy-Access-Requests": 0, "FreeRADIUS-Total-Proxy-Access-Accepts": 0, "FreeRADIUS-Total-Proxy-Access-Rejects": 0, "FreeRADIUS-Total-Proxy-Access-Challenges": 0, "FreeRADIUS-Total-Proxy-Auth-Responses": 0, "FreeRADIUS-Total-Proxy-Auth-Duplicate-Requests": 0, "FreeRADIUS-Total-Proxy-Auth-Malformed-Requests": 0, "FreeRADIUS-Total-Proxy-Auth-Invalid-Requests": 0, "FreeRADIUS-Total-Proxy-Auth-Dropped-Requests": 0, "FreeRADIUS-Total-Proxy-Auth-Unknown-Types": 0, "FreeRADIUS-Total-Proxy-Accounting-Requests": 0, "FreeRADIUS-Total-Proxy-Accounting-Responses": 0, "FreeRADIUS-Total-Proxy-Acct-Duplicate-Requests": 0, "FreeRADIUS-Total-Proxy-Acct-Malformed-Requests": 0, "FreeRADIUS-Total-Proxy-Acct-Invalid-Requests": 0, "FreeRADIUS-Total-Proxy-Acct-Dropped-Requests": 0, "FreeRADIUS-Total-Proxy-Acct-Unknown-Types": 0, "FreeRADIUS-Stats-Start-Time": 1714413687, "FreeRADIUS-Stats-HUP-Time": 1714417601, "FreeRADIUS-Queue-Len-Internal": 0, "FreeRADIUS-Queue-Len-Proxy": 0, "FreeRADIUS-Queue-Len-Auth": 0, "FreeRADIUS-Queue-Len-Acct": 0, "FreeRADIUS-Queue-Len-Detail": 0, "FreeRADIUS-Queue-PPS-In": 0, "FreeRADIUS-Queue-PPS-Out": 0}
<<<>>>

```

