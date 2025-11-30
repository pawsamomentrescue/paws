from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal


@dataclass
class PaymentResult:
    success: bool
    transaction_id: str | None = None
    error_message: str | None = None


class MockPaymentProvider:
    """Simple payment provider mock used in development/test.

    In a real deployment, replace this with an integration that talks to
    Stripe/PayPal/etc. while preserving the PaymentResult interface.
    """

    def charge(self, *, amount: Decimal, description: str | None = None) -> PaymentResult:  # noqa: D401
        # Always succeeds for now; attach a dummy transaction id.
        return PaymentResult(success=True, transaction_id="test_txn_0001")


payment_provider = MockPaymentProvider()
