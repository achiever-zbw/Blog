import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useUserStore = defineStore('user', () => {
    const token = ref('')
    const setToken = newToken => {
        token.value = newToken
    }
    const removeToken = () => {
        token.value = ''
    }
    return {
        token,
        setToken,
        removeToken
    }
},{
    //本地持久化
    persist: {
        paths: ['token']
    }
}) 