from http import HTTPStatus

import pytest
from django.urls import reverse
from django.contrib.auth.models import User, Permission


def test_contacts_thanks_success(client):
    # Given
    name = "jhon"

    # When
    response = client.get(f"/contacts/thanks/{name}")

    # Then
    assert response.status_code == HTTPStatus.OK
    assert response.content.decode() == f"Obrigado, {name}!"

def test_contact_create_with_unauthenticated_user(client):
    # Given
    url = f'{reverse("accounts:login")}?next={reverse("contacts:create")}'

    # When
    response = client.post(reverse("contacts:create"))

    # Then
    assert response.status_code == HTTPStatus.FOUND
    assert response.url == url

@pytest.mark.django_db
def test_contact_create_success(client, django_user_model):
    # Given
    data = {
        "subject": "subject@testmail.com",
        "message": "Hello world!",
        "sender": "sender@testmail.com",
        "cc_myself": True,
    }
    user = django_user_model.objects.create_user(username='jhon', email='jhon@testmail.com', password='123@mudar')
    user.user_permissions.add(Permission.objects.get(codename='add_contact'))

    # Then
    client.force_login(user)
    #response = client.post(reverse("contacts:create"), data)
    response = client.post(f'{reverse("accounts:login")}?next={reverse("contacts:create")}')

    # When
    assert response.status_code == HTTPStatus.OK
