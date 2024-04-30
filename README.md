[PACKAGE]: ../../raw/master/packagee-0.1.2-20230706.mkp "package-0.1.2-20230706.mkp"
# Title

A short description about the plugin

if there are more than on plugin put it in collapsable sections
<details><summary>check_plugin_1</summary>

</details>
<details><summary>check_pluhin_2</summary>

</details>

---
### Download
* [Download latest mkp file][PACKAGE]

**Note**: before you update to a newer version, always check the [CHANGELOG](CHANGELOG). There migth be incompatible changes.
                        
---
### Installation

You can install the package by uploading it to your CheckMK site and as site user run 
```
mkp add PAKAGE_NAME.mkp
mkp enable PAKAGE_NAME VERSION
```

In the Enterprise/Free/Cloud edition of CheckMK you can use the GUI to install the package (_Setup_ -> _Extension Packages_ -> _Upload package_)

---
### Want to Contribute?

Nice ;-) Have a look at the [contribution guidelines](CONTRIBUTING.md "Contributing")

---
### Check Info

The plugin creates the service **_SERVICENAME_** for each discovered FOR WHAT with the **_HOW_TO_BUILD_THE_ITEM_** as item

<details><summary>Montoring states</summary>

| State | condition | WATO | 
| ------ | ------ | ------ |
| WARN | condition 1 | yes |
| CRIT | condition 2 | no |
| WARN/CRIT | condition 3 | no |

</details>

<details><summary>Perfdata</summary>

| Metric | Unit | Perfometer |
| ------ | ------ | ------ |
| METRIC 1 | bit/s | yes |
| METRIC 2 | C | yes |
| METRIC 3 | V | no |

</details>

---
### WATO
<details><summary>Service monitoring rule</summary>

| Section | Rule name |
| ------ | ------ |
| Networking | NAME_OF_THE_RULE  |

| Option | Defailt value |
| ------ | ------ |
| OPTION 1 | 10/50|
| OPTION 2 | 70/90 |
| OPTION 3 | CHOICE 1 |
| OPTION 4 | disabled |

</details> 

<details><summary>Discovery rule</summary>

| Section | Rule name |
| ------ | ------ |
| Discovery of individual services | NAME_OF_THE_RULE  |

| Option | Defailt value |
| ------ | ------ |
| OPTION 1 | disabled |

</details> 

<details><summary>HW/SW inventory rules</summary>
The inventory plugin is not configurable.
</details> 

---
### Sample Output

Sample output

![sample output](/img/sample.png?raw=true "sample output")

Sample output details

![sample output details](/img/sample-details.png?raw=true "sample output details")

