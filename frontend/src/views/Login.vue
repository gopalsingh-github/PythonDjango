<template>
  <!-- Login  -->
  <div class="mx-auto max-w-screen-xl px-4 py-16 sm:px-6 lg:px-8 ">
    <div class="mx-auto max-w-lg">
      <form  class="mt-6 mb-0 space-y-4 rounded-lg p-4 shadow-lg sm:p-6 lg:p-8 box-login font-sans  font-medium">
        <p class="text-center text-lg font-medium">Login</p>
        <div>
          <label for="email" class="sr-only">Email</label>
          <div class="relative">
            <input v-model="LoginData.username" type="email"
              class="w-full rounded-lg border-gray-200 p-4 pr-12 text-sm shadow-sm" placeholder="Enter email" />
            <span class="absolute inset-y-0 right-0 grid place-content-center px-4">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-gray-400" fill="none" viewBox="0 0 24 24"
                stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M16 12a4 4 0 10-8 0 4 4 0 008 0zm0 0v1.5a2.5 2.5 0 005 0V12a9 9 0 10-9 9m4.5-1.206a8.959 8.959 0 01-4.5 1.207" />
              </svg>
            </span>
          </div>
        </div>
        <div>
          <label for="password" class="sr-only">Password</label>
          <div class="relative">
            <input v-model="LoginData.password" type="password"
              class="w-full rounded-lg border-gray-200 p-4 pr-12 text-sm shadow-sm" placeholder="Enter password" />

            <span class="absolute inset-y-0 right-0 grid place-content-center px-4">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-gray-400" fill="none" viewBox="0 0 24 24"
                stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
              </svg>
            </span>
          </div>
        </div>
        <button type="button" class="block w-full rounded-lg bg-blue-400 px-5 py-3 text-sm font-medium text-white"
          v-on:click="submit()">
          Login
        </button>

      </form>
    </div>
  </div>
  <Footer />
</template>
    
<script>
import axios from 'axios'
import Footer from '../components/Footer.vue'

export default {
  name: 'Login',
  components: {
    Footer
  },
  data() {
    return {
      LoginData: {
        username: '',
        password: ''
      }
    }
  },
  methods: {
    submit() {
      console.log(this.LoginData)
      let header = ("Access-Control-Allow-Origin", "*");
      axios.get('http://127.0.0.1:8000/login/', '',  header).then((res)=>{
        console.log('hhh')
      })
    }
  }
}

</script>