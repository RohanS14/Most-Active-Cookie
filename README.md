# Quantcast Technical Challenge: Most Active Cookie

[![build](https://github.com/RohanS14/Most-Active-Cookie/actions/workflows/python-tests.yml/badge.svg)](https://github.com/RohanS14/Most-Active-Cookie/actions/workflows/python-tests.yml)

<br>This code finds the most active cookie on a specified day.</br>


Files:

`cookie_logic.py`: Contains core functionality

`most_active_cookie`: Contains command line executable functionality

`cookie_test.py`: Testing with Pytest. Pytest testing is automated using GitHub Actions.


<br>This can be run using:
```$ ./most_active_cookie <cookie log filename> -d <date>```
</br>

The cookie log file is ideally in csv format and the date should be in YYYY-MM-DD format.

If the execution does not work, first run `chmod +x most_active_cookie`.

