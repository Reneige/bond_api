from pydantic import BaseModel
import datetime

class Bond(BaseModel):
    Issuer: str | None
    Ticker: str | None
    Coupon: float | None
    Maturity: datetime.datetime | None
    IssueDate: datetime.datetime | None
    ISIN: str | None
    PreferredRIC: str | None
    PrincipalCurrency: str | None
    CountryofIssue: str | None
    IssuerType: str | None
    InstrumentType: str | None
    CouponType: str | None
    BondGrade: str | None
    Sector: str | None
    GreenBond: str | None
    Putable: str | None
    Callable: str | None
    HasSinkingFund: str | None
    CouponFrequency: float | None
    CapitalTier: float | None
    IsCallable: str | None
    IsPutable: str | None
    SeniorityType: str | None
    SeniorityTypeShortDescription: str | None
    SIC: float | None
    GuarantorType: str | None
    OptionAdjustedSpread: float | None
    BidAskSpread: float | None
    TypeofSinkingFund: float | None
    NegativePledgeFlag: str | None
    DebtIncurrenceLimitationFlag: str | None
    CrossDefaultFlag: str | None
    ChangeOfControlPutFlag: str | None
    SaleOfAssetsFlag: str | None
    AffiliateTransactionsFlag: str | None
    MergerFlag: str | None
    SaleLeasebackFlag: str | None
    CollectiveActionClausesFlag: float | None
    ForceMajeureFlag: str | None
    DefaultEventsFlag: str | None
    KeepwellAgreementFlag: float | None
    PariPassuFlag: str | None
    GreenBondFlag: str | None
    FirstCouponDate: str | None
    MaturityYearsToRedem: float | None
    DayCount: str | None
    AssetStatus: str | None
    AssetStatusDescription: str | None

class Prices(BaseModel):
    Date: datetime.datetime | None
    Bid: float | None
    Ask: float | None
    BidYld: float | None
    AskYld: float | None
    BidYChg: float | None
    Calculated_DirtyPrice: float | None
    ZSpread: float | None
    Calculated_ZSpread: float | None
    RedemptionDate: str | None
    ID: str | None
    ISIN: str | None
    