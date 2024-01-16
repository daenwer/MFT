from credit_app.models import Producer


def get_producer_ids(contract_id):
    try:
        producer_ids = (
            Producer.objects.filter(
                products__loan_applications__contract__id=contract_id
            )
            .values_list("id", flat=True)
            .distinct()
        )
        return producer_ids
    except Producer.DoesNotExist:
        return []
