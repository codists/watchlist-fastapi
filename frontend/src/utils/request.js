import axios from 'axios'

import {ElMessage} from "element-plus";

export function request(config) {
    const instance = axios.create({
        baseURL: 'http://localhost:8000/api/v1',
        timeout: 1000,
    })

    // 请求拦截器，config对象参考：https://axios-http.com/docs/req_config
    instance.interceptors.request.use((config) => {
            const token = localStorage.getItem("token");
            // 如果已登录，没有都要带上token，以便后端进行认证
            if (token) {
                config.headers.Authorization = token;
            }
            return config
        },
        (error) => {
            console.log(`请求失败：${error}`)
        }
    )
    /*
       1. 响应拦截器，response格式参考：https://axios-http.com/docs/res_schema
       2. 统一消息提示，不用每个函数都调用消息提示接口ElMessage()
     */

    instance.interceptors.response.use((response) => {
            // 显示响应消息
            ElMessage({
                duration:1000,
                message: response.data.msg,
                type: "success"
            })
           // 拦截之后要将response返回回去
            return response.data.data
        },
        (error) => {
            console.log(`响应错误：${error}`)
        }
    )
    return instance(config)
}
