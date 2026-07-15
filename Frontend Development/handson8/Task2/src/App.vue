<template>

<nav>

  <RouterLink to="/">Home</RouterLink> |

  <RouterLink to="/courses">Courses</RouterLink> |

  <RouterLink to="/profile">Profile</RouterLink>

</nav>

<hr>

<RouterView />

</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>