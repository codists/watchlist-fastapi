<script setup>
import {reactive} from 'vue'
// import {useRouter} from 'vue-router'
import {useStore} from 'vuex'
// import {ElMessage} from 'element-plus'
// import login from '@/apis/user'

// const router = useRouter()
const store = useStore()


// do not use same name with ref
const loginForm = reactive({
  username: "test",
  password: "123456",

})


const onSubmit = () => {
  // 表单数据是绑定到form上面的，所以不需要重新获取
  // 不使用vuex的写法
  /*
  login(form).then((response) => {

        router.push('/')
        console.log(response)
      }
  ).catch(error => {
    console.log(error)
  })
  */

  // 使用vuex后的写法: 使用mutation或者action
  store.dispatch("userLoginAction",loginForm)
}
</script>

<template>
  <h2>登录</h2>
  <el-form
      :model="loginForm"
      label-width="120px"
      label-position="top"
  >
    <!-- 用户名   -->
    <el-form-item label="用户名">
      <el-input v-model="loginForm.username"/>
    </el-form-item>

    <!-- 密码   -->
    <el-form-item label="密码">
      <el-input v-model="loginForm.password" show-password/>
    </el-form-item>

    <el-form-item>
      <el-button type="primary" @click="onSubmit">提交</el-button>
    </el-form-item>
  </el-form>
</template>

<style scoped>

</style>