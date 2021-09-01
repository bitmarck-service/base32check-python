[![Release Notes](https://img.shields.io/github/release/bitmarck-service/base32check-python.svg)](https://github.com/bitmarck-service/base32check-python/releases/latest)
[![Apache License 2.0](https://img.shields.io/github/license/bitmarck-service/base32check-python.svg)](https://www.apache.org/licenses/LICENSE-2.0)
[![Test Workflow](https://github.com/bitmarck-service/base32check-python/workflows/test/badge.svg)](https://github.com/bitmarck-service/base32check-python/actions?query=workflow%3Atest)

# base32check-python

This project is a Python 3 implementation of the [Base32Check1](https://base32check.org/) algorithm.
The minimum requirement is Python 3.6.
There are no additional requirements/dependencies.

## License

This project is covered by the [Apache License, Version 2](LICENSE).

## Release

For an easy release process and upload to PyPI [zest.releaser]
(https://github.com/zestsoftware/zest.releaser) can be used.

First you have to configure your `~/.pypirc` with your credentials. ([doc]
(https://zestreleaser.readthedocs.io/en/latest/uploading.html#pypi-configuration-file-pypirc))
Then you can start the release process.


````bash
$ python3.9 -m venv venv
$ venv/bin pip install zest.releaser[recommended]
$ venv/bin/fullrelease

```
