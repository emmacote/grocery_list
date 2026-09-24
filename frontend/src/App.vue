<script setup lang="ts">
import Counter from './components/Counter.vue';
import {ref} from "vue";

const total = ref<number>(0);

function handleChanged(value: number) {
  total.value += value;
}

</script>

<template>
<Counter label="first button" :step="5" @changed="handleChanged"/>
<Counter label = "second button" @changed="handleChanged"/>
<p>Totl across both: {{ total }}</p>
</template>
