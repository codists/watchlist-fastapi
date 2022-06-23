<script setup>
import {reactive, ref} from 'vue'
import {useRoute} from 'vue-router'
import {useRouter} from 'vue-router'

import {updateMovie} from '@/apis/movie'

const route = useRoute()
const router = useRouter()

const formInline = reactive({
  name: route.query.name,
  year: route.query.year,
});

const rules = {
  name: [
    {
      required: true,
      message: "请输入电影名称",
      trigger: "blur",
    },
    {
      min: 3,
      message: "Length should 3 ",
      trigger: "blur",
    },
  ],
  year: [
    {
      required: true,
      message: "请输入电影年份",
      trigger: "blur",
    },
    {
      min: 4,
      max: 4,
      message: "Length should 4 ",
      trigger: "blur",
    },
  ],
}

const ruleForm = ref()

const onSubmit = () => {
  ruleForm.value.validate((valid) => {
    if (valid) {
      updateMovie(route.query.id, formInline)
          .then(() => router.push("/"))
          .catch((err) => console.log(err))
    } else {
      return false
    }
  })
}
</script>

<template>
  <h3>Edit Item</h3>
  <el-form
      :inline="true"
      :model="formInline"
      class="demo-form-inline"
      :rules="rules"
      ref="ruleForm"
  >
    <el-form-item label="name" prop="name">
      <el-input v-model="formInline.name"></el-input>
    </el-form-item>
    <el-form-item label="year" prop="year">
      <el-input v-model="formInline.year"></el-input>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="onSubmit">提交</el-button>
    </el-form-item>
  </el-form>
</template>

<style></style>