import axios from 'axios'
import { useUserStore } from '@/stores'
import { ElMessage  } from 'element-plus'

//设置请求的基地址
const baseURL = 'http://10.25.205.131:8000'

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
        if (res.data.code >= 400){
            console.log(res.data.message)
            ElMessage.error(res.data.message)
        }
        else
            return res.data
    },
    error => {
        console.log(error)
        ElMessage.error('网连接错误，请稍后再试')
        return new Error(error)
    }
)

//导出axios实例
export default instance