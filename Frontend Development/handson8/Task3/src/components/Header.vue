<template>
  <header style="background:#1976d2; color:white; padding:15px;">
    <h2>Student Portal</h2>

    <p>
      Enrolled Courses:
      {{ store.enrolledCourses.length }}
    </p>
  </header>
</template>

<script setup>
import { useEnrollmentStore } from '../stores/enrollment'

const store = useEnrollmentStore()
</script>