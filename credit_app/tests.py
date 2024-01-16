from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from credit_app.models import Contract, LoanApplication, Producer, Product


class TestAPI(TestCase):
    def setUp(self):
        self.producer_1 = Producer.objects.create(name="Apple")
        self.producer_2 = Producer.objects.create(name="Samsung")

        product_1_1 = Product.objects.create(
            name="iPhone 15", producer=self.producer_1
        )
        product_1_2 = Product.objects.create(
            name="iPhone 15 Pro", producer=self.producer_1
        )
        product_2_1 = Product.objects.create(
            name="Galaxy S23 Ultra", producer=self.producer_2
        )

        self.contract_1 = Contract.objects.create(number="contract-1")
        self.contract_2 = Contract.objects.create(number="contract-2")

        loan_application_1 = LoanApplication.objects.create(
            number="loan-1", contract=self.contract_1
        )
        loan_application_2 = LoanApplication.objects.create(
            number="loan-2", contract=self.contract_2
        )
        loan_application_1.products.add(product_1_1)
        loan_application_1.products.add(product_2_1)
        loan_application_2.products.add(product_1_2)
        self.client = APIClient()

    def test_producer_ids_api(self):
        contract_id = self.contract_1.pk
        url = reverse("producer-ids", kwargs={"contract_id": contract_id})
        response = self.client.get(url)

        assert response.status_code == 200
        assert set(response.data["producer_ids"]) == set(
            [self.producer_1.pk, self.producer_2.pk]
        )

        contract_id = self.contract_2.pk
        url = reverse("producer-ids", kwargs={"contract_id": contract_id})
        response = self.client.get(url)

        assert response.status_code == 200
        assert list(response.data["producer_ids"]) == [self.producer_1.pk]

        contract_id = self.contract_2.pk + 1
        url = reverse("producer-ids", kwargs={"contract_id": contract_id})
        response = self.client.get(url)

        assert response.status_code == 200
        assert list(response.data["producer_ids"]) == []
