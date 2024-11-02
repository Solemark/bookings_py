from pytest import fixture
from src.booking import Booking, Luxury


@fixture
def booking() -> Booking:
    return Booking(
        "100-abd-543-123",
        "01/01/2020",
        1,
        "Obi-Wan Kenobi",
        "0123 456 789",
        "111 Test St",
        5,
        100,
    )


@fixture
def luxury() -> Luxury:
    return Luxury(
        "100-abd-543-123",
        "01/01/2020",
        1,
        "Obi-Wan Kenobi",
        "0123 456 789",
        "111 Test St",
        5,
        100,
        True,
        True,
    )


def test_get_booking_data(booking: Booking) -> None:
    assert "100-abd-543-123" == booking.get_id()
    assert "01/01/2020" == booking.get_date()
    assert 1 == booking.get_weeks()
    assert "Obi-Wan Kenobi" == booking.get_owner()
    assert "0123 456 789" == booking.get_number()
    assert "111 Test St" == booking.get_address()
    assert 5 == booking.get_rooms()
    assert 100 == booking.get_area()


def test_get_luxury_data(luxury: Luxury) -> None:
    assert "100-abd-543-123" == luxury.get_id()
    assert "01/01/2020" == luxury.get_date()
    assert 1 == luxury.get_weeks()
    assert "Obi-Wan Kenobi" == luxury.get_owner()
    assert "0123 456 789" == luxury.get_number()
    assert "111 Test St" == luxury.get_address()
    assert 5 == luxury.get_rooms()
    assert 100 == luxury.get_area()
    assert True is luxury.get_alarm()
    assert True is luxury.get_pool()
