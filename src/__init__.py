"""Financial Services - Claude AI Integration Package.

This package provides tools and utilities for integrating Claude AI
into financial services workflows, including document analysis,
risk assessment, and compliance checking.
"""

__version__ = "0.1.0"
__author__ = "Anthropic"
__license__ = "MIT"

from .client import FinancialServicesClient
from .exceptions import FinancialServicesError, AuthenticationError, RateLimitError

__all__ = [
    "FinancialServicesClient",
    "FinancialServicesError",
    "AuthenticationError",
    "RateLimitError",
]
