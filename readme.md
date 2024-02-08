# Pi-hole adlist

![update](https://github.com/Pyenb/Pi-hole-adlist/actions/workflows/generate.yml/badge.svg)
![statistics](https://github.com/Pyenb/Pi-hole-adlist/actions/workflows/statistics.yml/badge.svg)
![last commit](https://img.shields.io/github/last-commit/Pyenb/Pi-hole-adlist)

![VALID_BADGE](https://img.shields.io/badge/Valid-99.918%25-green)
![INVALID_BADGE](https://img.shields.io/badge/Invalid-0.082%25-red)

This is the blocklist I use with my Pi-hole. It's compiled out of the individual lists I use, but in a single file. **Updated daily.**

It may not be perfect for everyone, but it's a good starting point. It mostly contains ads, telemetry and other questionable websites.

The list currently contains around *2.2* million unique domains.

The blocklist generator already cleans up a lot of the data. Still, after each update, the list is checked for domain validity and the results are displayed in the badges above.

## Usage

To use this list, simply add the following URL to your Pi-hole:

```text
https://raw.githubusercontent.com/Pyenb/Pi-hole-adlist/main/blocklist.txt
```

## Images

![Pi-hole dashboard](images/pic.png)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

## Disclaimer

This repository is for research purposes only, the use of this code is your responsibility.

I take NO responsibility and/or liability for how you choose to use any of the source code available here. By using any of the files available in this repository, you understand that you are AGREEING TO USE AT YOUR OWN RISK. Once again, ALL files available here are for EDUCATION and/or RESEARCH purposes ONLY.
