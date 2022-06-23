<script setup>
import WatchHeader from "@/components/WatchHeader.vue"
import WatchFooter from "@/components/WatchFooter.vue"

import {useStore} from "vuex"

const store = useStore()

</script>

<template>
  <el-container>
    <h2>
      <img src="@/assets/images/avatar.png" style="width: 40px"/>
      {{ store.getters.title }} WatchList
    </h2>

    <el-header>
      <WatchHeader :isLogin="store.state.token ? true : false"/>
    </el-header>

    <el-main>
      <router-view/>
    </el-main>

    <el-footer>
      <WatchFooter/>
    </el-footer>
  </el-container>
</template>

<style scoped>
.el-header {
  padding: 0px;
  height: 32px;
}

.el-main {
  padding: 0 3px 0 3px;
}

.el-footer {
  text-align: center;
}

</style>