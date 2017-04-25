# OCI Watson Tools
Contains a Python library for using the Watson API Services

## Configuration

The configuration file "config.txt" must be created in the configuration directory.  Below is the format:

```
[GlobalInformation]
url = The Request URL for the Watson API
userName = User credential for the API
password = Password credential for the API
```

## Usage
Ensure the object you are passing is a "file-like" class.

The included test.py file shows a simple use case for the get functions.

The included testHeader.csv and testBody.csv shows the input file formats for their respective functions.

The output file format is as follows:

```
Body ID,anger,disgust,fear,joy,sadness
```
