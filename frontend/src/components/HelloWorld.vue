<script setup lang="ts">
import { ref } from 'vue'

const message = ref("")
</script>

<template>
  <input v-model="message" />
  <br />
  {{  message }}
</template>
