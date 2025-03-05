import requests
from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from transactions.models import Transactions
from users.models import Profile
from django.conf import settings
from decimal import Decimal
from django.views.decorators.csrf import csrf_exempt
from .serializers import TransactionsSerializers
from django.http import JsonResponse
from django.db import IntegrityError

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def top_up(request):

    user = request.user
    amount = request.data.get('amount')

    if not amount:
        return Response({"error": "Amount is required"}, status=HTTP_400_BAD_REQUEST)

    url = "https://api.cryptocloud.plus/v2/invoice/create"
    data = {
        "shop_id": settings.CRYPTOCLOUD_SHOP_ID,
        "amount": amount
    }

    headers = {
        "Authorization": f'Token {settings.CRYPTOCLOUD_API_KEY}',
        "Content-Type": "application/json"
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
    except requests.RequestException as e:
        return Response({"error": f"Failed to create payment link: {str(e)}"}, status=HTTP_400_BAD_REQUEST)

    response_data = response.json()
    result = response_data.get('result', {})
    uuid = result["uuid"]
    
    if uuid and uuid.startswith('INV-'):
        uuid = uuid[4:]
        
    transaction = Transactions.objects.create(
        user=user,
        amount=Decimal(result["amount"]),
        uuid=uuid
    )

    payload = {
        "payment_link": result["link"]
    }
    return Response(payload, status=HTTP_200_OK)


@csrf_exempt
def postback(request):
    if request.method == 'POST':

        status = request.POST.get('status')
        invoice_id = request.POST.get('invoice_id')
        amount_crypto = request.POST.get('amount_crypto')
        currency = request.POST.get('currency')
        order_id = request.POST.get('order_id')
        token = request.POST.get('token')
        
        print(f"Received postback: {status}, {invoice_id}, {amount_crypto}, {currency}, {order_id}, {token}")
        if status == 'success':
            try:
                transaction = Transactions.objects.get(uuid=invoice_id)
                
                transaction.update_status('COMPLETED')
                transaction.save()
                
                profile = Profile.objects.get(user=transaction.user)
                profile.balance += Decimal(amount_crypto)
                profile.save()
            
            except Transactions.DoesNotExist:
                return JsonResponse({'error': f'Transaction with UUID {invoice_id} not found'}, status=404)
            except Profile.DoesNotExist:
                return JsonResponse({'error': f'Profile for user {transaction.user.username} not found'}, status=404)
            except IntegrityError:
                return JsonResponse({'error': 'Database error occurred while updating the balance'}, status=500)

        
        return JsonResponse({'message': 'Postback received'}, status=200)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)



class TransactionPagination(PageNumberPagination):
    page_size = 10  # Number of transactions per page
    page_size_query_param = 'page_size'
    max_page_size = 100

class UserTransactions(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = request.user
        transactions = Transactions.objects.filter(user=user)
        
        # Apply pagination
        paginator = TransactionPagination()
        result_page = paginator.paginate_queryset(transactions, request)
        
        if result_page is not None:
            serializer = TransactionsSerializers(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        
        # If no pagination is applied, just return all results
        serializer = TransactionsSerializers(transactions, many=True)
        return Response(serializer.data)