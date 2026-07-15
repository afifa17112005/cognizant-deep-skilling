<template>
  <div>

    <Header />

    <h2>Available Courses</h2>

    <input
      type="text"
      placeholder="Search Course"
      v-model="searchTerm"
    />

    <CourseCard
      v-for="course in filteredCourses"
      :key="course.id"
      :name="course.name"
      :code="course.code"
      :credits="course.credits"
      :grade="course.grade"
    />

  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'

import Header from '../components/Header.vue'
import CourseCard from '../components/CourseCard.vue'

const courses = ref([])

const searchTerm = ref('')

onMounted(() => {
  courses.value = [
    {
      id:1,
      name:'Data Structures',
      code:'CS101',
      credits:4,
      grade:'A'
    },
    {
      id:2,
      name:'Database Management',
      code:'CS102',
      credits:3,
      grade:'A+'
    },
    {
      id:3,
      name:'Operating Systems',
      code:'CS103',
      credits:4,
      grade:'B+'
    },
    {
      id:4,
      name:'Computer Networks',
      code:'CS104',
      credits:3,
      grade:'A'
    },
    {
      id:5,
      name:'Artificial Intelligence',
      code:'CS105',
      credits:5,
      grade:'O'
    }
  ]
})

const filteredCourses = computed(() => {
  return courses.value.filter(course =>
    course.name.toLowerCase().includes(searchTerm.value.toLowerCase())
  )
})
</script>