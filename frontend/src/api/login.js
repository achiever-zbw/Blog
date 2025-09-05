import instance from "@/utils/request"

export function login_api(data) {
    return instance.post('/user/login/', data)
}

export function signup_api(data) {
    return instance.post('/user/register/', data)
}