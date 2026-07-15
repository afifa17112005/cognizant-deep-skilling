<template>

  <Header />

  <nav style="padding:15px">

    <RouterLink to="/">Courses</RouterLink>

    |

    <RouterLink to="/profile">Profile</RouterLink>

  </nav>

  <hr>

  <RouterView />

</template>

<script setup>
import Header from './components/Header.vue'
import { RouterLink, RouterView } from 'vue-router'
</script>