from pytest_voluptuous import S

register = S({
    "id": int,
    "token": str
})

login = S({
    "token": str
})

create = S({
    "name": str,
    "job": str,
    "id": str,
    "createdAt": str
})

update = S({
    "name": str,
    "job": str,
    "updatedAt": str
})









