# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the BSD License. See the LICENSE file in the root of this repository
# for complete details.

import typing

from cryptography.hazmat.primitives.asymmetric.types import PRIVATE_KEY_TYPES
from cryptography.hazmat.primitives import hashes
from cryptography.x509 import Extension
from cryptography.x509.ocsp import (
    OCSPRequest,
    OCSPRequestBuilder,
    OCSPResponse,
    OCSPResponseStatus,
    OCSPResponseBuilder,
)

def load_der_ocsp_request(data: bytes) -> OCSPRequest: ...
def load_der_ocsp_response(data: bytes) -> OCSPResponse: ...
def create_ocsp_request(builder: OCSPRequestBuilder) -> OCSPRequest: ...
def create_ocsp_response(
    status: OCSPResponseStatus,
    builder: typing.Optional[OCSPResponseBuilder],
    private_key: typing.Optional[PRIVATE_KEY_TYPES],
    hash_algorithm: typing.Optional[hashes.HashAlgorithm],
) -> OCSPResponse: ...
