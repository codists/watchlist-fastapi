<script setup>
import {computed, ref} from 'vue'
import {reactive} from 'vue'
import {useRouter} from 'vue-router'
import {useStore} from 'vuex'

import {getMovieList, addMovie, delMovie} from "@/apis/movie"

// ref 参考：https://vuejs.org/guide/essentials/reactivity-fundamentals.html#limitations-of-reactive
const movies = ref({})
const store = useStore()
const router = useRouter()

// 不涉及到组件传递的值存到vuex里面
const isLogin = store.state.token ? true : false

const imdbURL = computed(() => {
  return function imdbSearch(movieName) {
    // https://www.imdb.com/find?q=
    return `https://www.imdb.com/find?q=${movieName}`
  }
})

/*
1.getMovieList() 得到的是一个Promise
2.接着解析Promise
3.参考资料MDN Promise：https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise
 */

getMovieList()
    .then(
        (res) => {
          // ref对象赋值只能使用其value属性
          movies.value = res
        }
    ).catch(
    (err) => console.log(err)
)

const addMovieForm = reactive({
  name: '',
  year: ''
})

// 校验
const ruleForm = ref()
const rules = reactive({
  name: [
    {required: true, message: '请输入电影名', trigger: 'blur'},
    {min: 1, message: '电影名不能为空', trigger: 'blur'},
  ],
  year: [
    {required: true, message: '请输入电影上映年份', trigger: 'blur'},
    {min: 4, max: 4, message: '电影上映时间为四位数字，如 2022', trigger: 'blur'},
  ]
})
const submitForm = () => {
  // todo: ruleForm和rules是怎么关联起来的?
  ruleForm.value.validate((valid) => {
        // 如果验证通过
        if (valid) {
          addMovie(addMovieForm).then(() => {
                // 请求成功后在赋值一次，实现数据刷新
                getMovieList().then((response) => {
                      movies.value = response
                    }
                ).catch((err) => console.log(err))
              }
          ).catch((error) => {
            console.log(error)
          })
        } else {
          // console.log('error submit')
          return false
        }
      }
  )
}

const editBtnClick = (movie) => {
  // 如何传值给edit页面何
  router.push({
    name: 'edit',
    // 编辑:这里不能使用params进行传参，否则刷新页面的时候会丢失数据,要使用query
    query: movie,
  })

}
// 删除
const delBtnClick = (id) => {
  delMovie(id).then(() => {
    getMovieList().then((res) => {
      movies.value = res
    }).catch((error) => {
      console.log(error)
    })
  }).catch((error) => {
    console.log(error)
  })
}
</script>

<template>
  <p>{{ movies.total }} Titles</p>
  <!--  inline form(行内表单)-->
  <template v-if="isLogin">
    <el-form
        :inline="true"
        :model="addMovieForm"
        :rules="rules"
        ref="ruleForm"
        class="demo-form-inline"
    >
      <!-- prop： 绑定 Item 与 Rule     -->
      <el-form-item label="name" prop="name">
        <el-input v-model="addMovieForm.name" placeholder="电影名字"/>
      </el-form-item>
      <el-form-item label="year" prop="year">
        <el-input v-model="addMovieForm.year" placeholder="上映时间"/>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submitForm">提交
        </el-button>
      </el-form-item>
    </el-form>
  </template>

  <ul class="movie-list">
    <li v-for="movie in movies.movies" v-bind:key="movie">
      {{ movie.name }}-{{ movie.year }}
      <span class="float-right">
         <template v-if="this.$store.state.token">
            <el-button @click="editBtnClick(movie)">编辑</el-button>
            <el-button @click="delBtnClick(movie.id)">删除</el-button>
         </template>
         <a :href="imdbURL(movie.name)" class="imdb" target="_blank">IMDB</a>
       </span>
    </li>
  </ul>
  <img class="totoro" src="@/assets/images/totoro.gif" alt="totoro.gif">

</template>

<style scoped>
.movie-list {
  list-style-type: none;
  padding: 0px;
  margin-bottom: 10px;
  box-shadow: 0 2px 10px 0 rgb(0 0 0 / 12%), 0 2px 10px 0 rgb(0 0 0 / 12%);

}

.movie-list li {
  padding: 12px 24px;
  border-bottom: 1px solid #ddd;
}

.totoro {
  display: block;
  margin: 0 auto;
  height: 100px;
}

.float-right {
  float: right;
}

.imdb {
  font-size: 12px;
  font-weight: bold;
  color: black;
  text-decoration: none;
  background: #F5C518;
  border-radius: 5px;
  padding: 3px 5px
}

.el-form-item {
  margin-right: 1px;
}

.el-form {
  padding: 0;
}
</style>