from contacts.forms import NameForm


def test_name_form_success():
    # Given
    data = {"your_name": "Jhon"}
    form = NameForm(data=data)

    # When
    result = form.is_valid()

    # Then
    assert result == True

def test_name_form_failure():
    # Given
    data = {}
    form = NameForm(data=data)

    # When
    result = form.is_valid()

    # Then
    assert result == False

def test_name_form_your_name_max_length_failure():
    # Given
    data = {"your_name": "Jhon" * 50}
    form = NameForm(data=data)

    # When
    result = form.is_valid()

    # Then
    assert result == False