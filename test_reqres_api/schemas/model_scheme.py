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


single_user = S({
    "data": {
        "id": int,
        "email": str,
        "first_name": str,
        "last_name": str,
        "avatar": str
    },
    "support": {
        "url": str,
        "text": str
    }
})






