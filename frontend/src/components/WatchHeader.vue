<script setup>
import {useRouter, useRoute} from 'vue-router'
import {ElMessage} from "element-plus"

import router from '@/router'
import store from '@/store'


// getRoutes()参考：https://router.vuejs.org/api/#getroutes
const routers = useRouter()
const currentRouters = routers.getRoutes()

defineProps({
  isLogin: {
    type: Boolean,
    default: false,
    required: true,
  },
});

// 当前路由对象
const routes = useRoute();

// 菜单点击事件
const handleSelect = (index) => {

  if (index === "/logout") {

    window.localStorage.clear();
    console.log(store)
    store.commit("changeToken", "")
    store.commit("changeNickname", "")
    ElMessage({
      message: "退出登录.",
      type: "success",
    });

    router.push("/login");
  }
};
</script>

<template>
  <!-- default-active设置当前激活的链接 -->
  <el-menu
      :default-active="routes.path"
      class="el-menu-demo"
      mode="horizontal"
      @select="handleSelect"
      router
  >

    <template v-for="currentRouter in currentRouters" v-bind:key="currentRouter">
      <!-- 无论什么情况Home都显示 -->
      <template v-if="currentRouter.name == 'home'">
        <el-menu-item :index="currentRouter.path">{{ currentRouter.name }}</el-menu-item>
      </template>
      <!-- 登录后login不能显示 -->
      <template v-else-if="isLogin && currentRouter.name != 'login' && currentRouter.meta.isNav ">
        <el-menu-item :index="currentRouter.path">{{ currentRouter.name }}</el-menu-item>
      </template>
      <!-- 未登录setting和logout不能显示 -->
      <template v-else-if="!isLogin && currentRouter.meta.isNav && !currentRouter.meta.requiresAuth">
        <el-menu-item :index="currentRouter.path">{{ currentRouter.name }}</el-menu-item>
      </template>
    </template>

  </el-menu>
</template>

<style scoped>
.el-menu {
  background-color: black;
  height: 32px;
}

.el-menu-item {
  color: white;
}
</style>