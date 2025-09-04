import instance from "@/utils/request"

export function login_api(data) {
    return instance.post('/user/login', data)
}