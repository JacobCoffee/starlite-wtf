import asyncio

import pytest
from starlite import Starlite
from starlite.testing import TestClient
from wtforms import BooleanField, FileField, StringField
from wtforms.validators import DataRequired, ValidationError
from wtforms.widgets import CheckboxInput

from starlite_wtf.form import StarliteForm


@pytest.fixture
def app():
    """Create Starlite app instance"""
    return Starlite()


@pytest.fixture
def client(app):
    """Create Starlite test client"""
    return TestClient(app)


@pytest.fixture
def BasicForm():
    """Return BasicForm class"""

    class BasicForm(StarliteForm):
        name = StringField(validators=[DataRequired()])
        avatar = FileField()
        checkbox = BooleanField(widget=CheckboxInput(), default=True)

    return BasicForm


@pytest.fixture
def FormWithCustomValidators():
    """Return FormWithCustomValidators class"""

    class FormWithCustomValidators(StarliteForm):
        field1 = StringField()
        field2 = StringField()

        def validate_field1(self, field):
            if not field.data == "value1":
                raise ValidationError("Field value is incorrect.")

        def validate_field2(self, field):
            if not field.data == "value2":
                raise ValidationError("Field value is incorrect.")

    return FormWithCustomValidators


@pytest.fixture
def form_with_async_validators():
    """Return FormWithAsyncValidators class"""

    class FormWithAsyncValidators(StarliteForm):
        field1 = StringField()
        field2 = StringField(validators=[DataRequired()])

        async def async_validate_field1(self, field):
            # test wait
            await asyncio.sleep(0.01)

            # raise exception
            if not field.data == "value1":
                raise ValidationError("Field value is incorrect.")

        async def async_validate_field2(self, field):
            # test wait
            await asyncio.sleep(0.02)

            # raise exception
            if not field.data == "value2":
                raise ValidationError("Field value is incorrect.")

    return FormWithAsyncValidators


@pytest.fixture
def form_with_async_exception():
    """Return FormWithAsyncException class"""

    class FormWithAsyncException(StarliteForm):
        field1 = StringField()

        async def async_validate_field1(self, field):
            await asyncio.sleep(0.01)
            raise Exception("test")

    return FormWithAsyncException
