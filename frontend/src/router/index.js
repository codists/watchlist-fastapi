import {createRouter, createWebHistory} from 'vue-router'

const routes = [
    {
        path: '/',
        name: 'home',
        component: () => import('@/views/MovieListView'),
        meta: {
            requiresAuth: false,
            // 标记是否为导航栏
            isNav: true
        }
    },
    {
        path: '/setting',
        name: 'setting',
        component: () => import('@/views/SettingsView'),
        meta: {
            // 标记是否登录才能访问
            requiresAuth: true,
            isNav: true
        }
    },
    {
        path: '/login',
        name: 'login',
        component: () => import('@/views/LoginView'),
        meta: {
            requiresAuth: false,
            isNav: true
        }
    },
    {
        path: '/logout',
        name: 'logout',
        meta: {
            requiresAuth: true,
            isNav: true
        }
    },
    {
        path: '/edit',
        name: 'edit',
        component: () => import('@/views/EditView'),
        meta: {
            requiresAuth: true,
        }
    },
    {
        path: '/:pathMatch(.*)*',
        name: 'NotFound',
        component: () => import('@/views/NotFoundView')
    },
    // 重定向
    {
        path: '/home',
        redirect: '/'
    }

]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

router.beforeEach((to, from, next) => {
    // 多行注释参考：https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#comments
    /*
      1.页面：
        1.1 登录才能访问（如：个人信息设置页）
        1.2 不登录也能访问(如：首页)
        注：1.判断路由是否需要登录才能访问，通过Routr Meta Field进行设置。
           2.使用token判断用户是否已经登录
     */
    const token = localStorage.getItem("token")
    const isLogin = !!token

    if (to.meta.requiresAuth){   //需要登录
        console.log('需要登录')
        if (isLogin) { //已经登录的 直接通过
            if (to.name === 'login') {
                next({name: 'home'});
            } else {
                next();
            }
            return
        }
        if (!isLogin && to.name === 'login') {  //未登录，但是要去登录页
            next()
        }
        if (!isLogin && to.name !== 'login') { //未登录，去的也不是登录页
            next({name: 'login'});
        }
    } else {
        next()
    }
})

export default router
