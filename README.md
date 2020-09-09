# tochka_test

Run with run_docker.sh script

# Requests example:

# /api/ping

Empty /GET request

# /api/status

/POST request:
{
  "operation": "status",
  "uuid": "user_uuid"
}

# /api/add

/POST request:
{
  "operation": "add",
  "amount": your amount, int, 200, for example,
  "uuid": "user_uuid"
}

# /api/substract

/POST request:
{
  "operation": "substract",
  "amount": your amount, int, 200, for example,
  "uuid": "user_uuid"
}
