
<template>
    <!-- header -->
  <header class="container-fluid ">
    <div class="wrapper box font-sans">
      <nav class=" border-gray-200 bg-blue-300  ">
        <div class="flex flex-wrap justify-between items-center mx-auto max-w-screen-xl p-4">
            <RouterLink to="/" class="flex items-center focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2.5 text-center inline-flex items-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
                <img src="https://flowbite.com/docs/images/logo.svg" class="h-8 mr-3" alt="Flowbite Logo" />
                <span class="self-center text-2xl font-semibold whitespace-nowrap dark:text-white">Institute Management</span>
            </RouterLink>
            <div class="flex items-center">
                <button id="dropdownDefaultButton" data-dropdown-toggle="dropdown" class="focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-2 py-2.5 text-center inline-flex items-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800" type="button">Signup <svg class="w-4 h-4 ml-1" aria-hidden="true" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg></button>
                <!-- Dropdown menu -->
                <div id="dropdown" class="z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow w-44 dark:bg-gray-700">
                    <ul class="py-2 text-sm text-gray-700 dark:text-gray-200" aria-labelledby="dropdownDefaultButton">
                      <li>
                        <RouterLink to="/institute-signup" class="block px-2 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">Institute</RouterLink>
                      </li>
                      <li>
                        <RouterLink to="/student-signup" class="block px-2 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">Student</RouterLink>
                      </li>
                    </ul>
                </div>
                <RouterLink to="/login" class="focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm  py-2.5 text-center inline-flex items-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Login</RouterLink>
            </div>
        </div>
    </nav>
    <nav class="bg-gray-200 ">
        <div class="max-w-screen-xl py-3 mx-auto">
            <div class="flex items-center">
                <ul class="flex flex-row font-bold font-medium mt-0  space-x-4 text-sm">
                    <li>
                        <RouterLink to="/" class="text-gray-900 dark:text-white hover:underline" aria-current="page">Home</RouterLink>
                    </li>
                    <li>
                        <RouterLink to="/about" class="text-gray-900 dark:text-white hover:underline">About</RouterLink>
                    </li>
                    <li>
                        <a href="#" class="text-gray-900 dark:text-white hover:underline">Contact us</a>
                    </li>
                    <li>
                        <a href="#" class="text-gray-900 dark:text-white hover:underline">Services</a>
                    </li>
                </ul>
            </div>
        <!-- marquee -->
        <marquee class="text-red-600 bg-gray-200 not-italic font-medium mt-2 mb-1">
            <spaan>Wel come to this website will come soon</spaan>
        </marquee>
        </div>
    </nav>
    </div>
  </header>

  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>
