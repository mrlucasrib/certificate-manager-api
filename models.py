from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import DateTime

from database import Base


class Certificates(Base):
    __tablename__ = "certificates"

    def __init__(self,
                 issued_to, issued_by,
                 expiration_date,
                 intended_purposes,
                 status,
                 certificate_template, *args, **kwargs
                 ) -> None:
        self.issued_to = issued_to
        self.issued_by = issued_by
        self.expiration_date = expiration_date
        self.intended_purposes = intended_purposes
        self.status = status
        self.certificate_template = certificate_template

        super().__init__()

    id = Column(Integer, primary_key=True, index=True)
    issued_to = Column(String)
    issued_by = Column(String)
    expiration_date = Column(String)
    intended_purposes = Column(String)
    status = Column(String)
    certificate_template = Column(String)
