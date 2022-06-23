import {createStore} from 'vuex'

import {login, userInfo} from '@/apis/user'
// 直接导入router
import router from "@/router"


export default createStore({
    state: {
        token: "",
        nickname: ""
    },
    // getters的作用：充当计算属性，解决“重复调用”冗余问题
    getters: {
        title(state) {
            // !!把其它类型转为Boolean类型，不转也可以，这里只是用法示例
            // const nickname = !!state.nickname
            if (state.nickname) {
                return state.nickname + "'s"
            } else {
                return ""
            }
        }
    },
    mutations: {
        changeToken(state, token) {
            state.token = token
        },
        changeNickname(state, nickname) {
            state.nickname = nickname
        }
    },
    actions: {
        // 注意async/await的使用
        async userLoginAction({commit}, payload) {
            //调用登录接口
            const resLogin = await login(payload)

            // 获取token并将token存储到vuex和localStorage里面
            const token = resLogin.token
            commit("changeToken", token) // 将token存储到vuex
            // localStorage参考：https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage
            localStorage.setItem("token", token)

            // 请求用户信息
            const resUser = await userInfo()
            const nickname = resUser.nickname
            commit("changeNickname", nickname) // 将nickname存储到vuex
            localStorage.setItem("nickname", nickname)

            // 跳转到首页
            await router.push("/");

        },
        // 解决刷新后vuex数据丢失问题
        loadLocalStorage({commit}) {
            const token = window.localStorage.getItem("token")
            if (token) {
                commit("changeToken", token)
            }
            const nickname = window.localStorage.getItem("nickname")
            if (nickname) {
                commit("changeNickname", nickname)
            }
        }
    },
    modules: {}
})
