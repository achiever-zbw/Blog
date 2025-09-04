import axios from 'axios'
import { useUserStore } from '@/stores'

//设置请求的基地址
const baseURL = 'http:127.0.0.1:8000'

//创建axios实例
const instance = axios.create({
    baseURL,
    timeout: 10000
})

//请求拦截器
instance.interceptors.request.use(
    config => {
        const token = useUserStore().token
        if (!token)
            config.headers.Authorization = ''
        else
            config.headers.Authorization = `Bearer ${token}`
        return config   
    },
    error => {
        return Promise.reject(error)
    }
)

//响应拦截器
instance.interceptors.response.use(
    res => {
        return res
    },
    error => {
        return Promise.reject(error)
    }
)

//导出axios实例
export default instance