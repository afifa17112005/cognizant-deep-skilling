<template>
  <div>
    <h1>Courses</h1>

    <ul>
      <li>
        <RouterLink to="/courses/1">Data Structures</RouterLink>
      </li>

      <li>
        <RouterLink to="/courses/2">Database Management</RouterLink>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'
</script>