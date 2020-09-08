import json

from django.http import JsonResponse

from api.models import Account


def ping(request):
    if request.method == 'GET':
        return JsonResponse(data={
            'status': 200,
            'result': True,
            'addition': '',
            'description': 'API /ping method returned 200, service is stable and running',
        })

    return JsonResponse(data={
        'status': 400,
        'result': False,
        'addition': '',
        'description': 'Bad request, check type of your HTTP-request, must be GET',
    })


def add(request):
    if request.method == 'POST':
        try:
            request_data = json.loads(request.body)
        except Exception as ex:
            return JsonResponse(data={
                'status': 500,
                'result': False,
                'addition': '',
                'description': 'Internal server error when decoding JSON',
            })

        else:
            if any([x not in list(request_data.keys()) for x in ['operation', 'uuid', 'amount']]):
                return JsonResponse(data={
                    'status': 400,
                    'result': False,
                    'addition': {x: y for x, y in request_data.items()},
                    'description': f"Check all the fields in your request, received fields were {list(request_data.keys())}, "
                                   f"must have 'operation', 'uuid', 'amount'",
                    }
                )
            if request_data['operation'] == 'add':
                try:
                    user_account = Account.objects.get(id=request_data['uuid'])
                except Exception as ex:
                    return JsonResponse(data={
                        'status': 400,
                        'result': False,
                        'addition': {x: y for x, y in request_data.items()},
                        'description': f"uuid: {request_data['uuid']} does not exist"
                    })
                else:
                    if user_account.is_opened is True:
                        user_account.current_balance += request_data['amount']
                        user_account.save()
                    else:
                        return JsonResponse(data={
                            'status': 400,
                            'result': False,
                            'addition': {x: y for x, y in request_data.items()},
                            'description': f"Client's account is blocked for transactions"
                        })
                    return JsonResponse(data={
                        'status': 200,
                        'result': True,
                        'addition': {x: y for x, y in request_data.items()},
                        'description': f"Client's uuid {request_data['uuid']} balance were increased by {request_data['amount']}"
                    })
            return JsonResponse(
                data={
                    'status': 400,
                    'result': False,
                    'addition': {x: y for x, y in request_data.items()},
                    'description': f"Check operation type, your was: '{request_data['operation']}', "
                                   f"but you called /add endpoint"
                }
            )
    return JsonResponse(data={
        'status': 400,
        'result': False,
        'addition': '',
        'description': 'Bad request, check type of your HTTP-request, must be POST',
    })


def substract(request):
    if request.method == 'POST':
        try:
            request_data = json.loads(request.body)
        except Exception as ex:
            return JsonResponse(data={
                'status': 500,
                'result': False,
                'addition': '',
                'description': 'Internal server error when decoding JSON',
            })

        else:
            if any([x not in list(request_data.keys()) for x in ['operation', 'uuid', 'amount']]):
                return JsonResponse(data={
                    'status': 400,
                    'result': False,
                    'addition': {x: y for x, y in request_data.items()},
                    'description': f"Check all the fields in your request, received fields were {list(request_data.keys())}, "
                                   f"must have 'operation', 'uuid', 'amount'",
                })

            if request_data['operation'] == 'substract':
                try:
                    user_account = Account.objects.get(id=request_data['uuid'])
                except Exception as ex:
                    return JsonResponse(data={
                        'status': 400,
                        'result': False,
                        'addition': {x: y for x, y in request_data.items()},
                        'description': f"uuid: {request_data['uuid']} does not exist"
                    })
                else:
                    if user_account.is_opened is True:
                        result = user_account.current_balance - user_account.reserved_operations - request_data['amount']
                        if result < 0:
                            is_possible = False
                        else:
                            is_possible = True

                        if is_possible is True:
                            user_account.current_balance = result
                            hold = user_account.reserved_operations
                            user_account.reserved_operations = 0
                            user_account.save()
                            return JsonResponse(data={
                                'status': 200,
                                'result': True,
                                'addition': {x: y for x, y in request_data.items()},
                                'description': f"Client's uuid {request_data['uuid']} balance were substracted by"
                                               f" {hold + request_data['amount']}"
                            })
                    else:
                        return JsonResponse(data={
                            'status': 400,
                            'result': False,
                            'addition': {x: y for x, y in request_data.items()},
                            'description': f"Client's account is blocked for transactions"
                        })
                    return JsonResponse(data={
                        'status': 400,
                        'result': False,
                        'addition': {x: y for x, y in request_data.items()},
                        'description': f"Insufficient funds on account for substract"
                    })

            return JsonResponse(
                data={
                    'status': 400,
                    'result': False,
                    'addition': {x: y for x, y in request_data.items()},
                    'description': f"Check operation type, your was: '{request_data['operation']}', "
                                   f"but you called /substract endpoint"
                }
            )
    return JsonResponse(data={
        'status': 400,
        'result': False,
        'addition': '',
        'description': 'Bad request, check type of your HTTP-request, must be POST',
    })


def status(request):
    if request.method == 'POST':
        try:
            request_data = json.loads(request.body)
        except Exception as ex:
            return JsonResponse(data={
                'status': 500,
                'result': False,
                'addition': '',
                'description': 'Internal server error when decoding JSON',
            })
        else:
            if any([x not in list(request_data.keys()) for x in ['operation', 'uuid']]):
                return JsonResponse(data={
                    'status': 400,
                    'result': False,
                    'addition': {x: y for x, y in request_data.items()},
                    'description': f"Check all the fields in your request, received fields were {list(request_data.keys())}, "
                                   f"must have 'operation', 'uuid' ",
                })
            if request_data['operation'] == 'status':
                try:
                    user_account = Account.objects.get(id=request_data['uuid'])
                except Exception as ex:
                    return JsonResponse(data={
                        'status': 400,
                        'result': False,
                        'addition': {x: y for x, y in request_data.items()},
                        'description': f"uuid: {request_data['uuid']} does not exist"
                    })
                else:
                    account_status = {**{x: y for x, y in request_data.items()}, **{
                                'current_balance': user_account.current_balance,
                                'reserved_operations': user_account.reserved_operations,
                                'is_opened': user_account.is_opened,
                    }}
                    return JsonResponse(data={
                        'status': 200,
                        'result': True,
                        'addition': account_status
                    })
            return JsonResponse(
                data={
                    'status': 400,
                    'result': False,
                    'addition': {x: y for x, y in request_data.items()},
                    'description': f"Check operation type, your was: '{request_data['operation']}', "
                                   f"but you called /status endpoint"
                }
            )
    return JsonResponse(data={
        'status': 400,
        'result': False,
        'addition': '',
        'description': 'Bad request, check type of your HTTP-request, must be POST',
    })
