<script setup>
import {ref} from 'vue'
import {useStore} from 'vuex'
import {ElMessage} from "element-plus"

import {updateUser} from "@/apis/user"


const store = useStore()
// 在script setup中，必须使用ref对象，否则无法实时更新
const nickname = ref(store.state.nickname)


// 将点击事件绑定到函数上面
const saveBtnClick = () => {
  updateUser(nickname.value).then(() => {
    // 输入校验: todo

    // 副作用：需要更新store.state.nickname, localStorage
    store.state.nickname = nickname.value
    localStorage.setItem("nickname", nickname.value);
    store.commit("changeNickname", nickname.value)
    ElMessage({
      message: "修改成功",
      type: "success"
    })
  }).catch(error => {
    ElMessage({
      message: "修改失败： " + error,
      type: "error"
    })
  })
}

</script>


<template>
  <h3>Settings</h3>
  <!-- 按Enter键进行提交：https://vuejs.org/guide/essentials/event-handling.html -->
  Your Name <input v-model="nickname" @keyup.enter="saveBtnClick" required="required"/>
  <button @click="saveBtnClick" style="margin-left: 3px">save</button>
</template>

<style scoped>
.el-input {
  /*width: 100px;*/
}
</style>