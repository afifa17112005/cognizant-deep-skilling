<template>
  <div>
    <h1>Courses</h1>

    <div
      v-for="course in courses"
      :key="course.id"
      style="border:1px solid gray; padding:15px; margin:10px;"
    >
      <h3>{{ course.name }}</h3>

      <p>Credits: {{ course.credits }}</p>

      <button @click="store.enroll(course)">
        Enroll
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useEnrollmentStore } from '../stores/enrollment'

const store = useEnrollmentStore()

const courses = ref([
  {
    id: 1,
    name: 'Data Structures',
    credits: 4
  },
  {
    id: 2,
    name: 'Database Management',
    credits: 3
  },
  {
    id: 3,
    name: 'Operating Systems',
    credits: 4
  },
  {
    id: 4,
    name: 'Computer Networks',
    credits: 3
  },
  {
    id: 5,
    name: 'Artificial Intelligence',
    credits: 5
  }
])
</script>