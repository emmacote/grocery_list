<script setup lang="ts">
import { ref, computed, watch, onMounted } from "vue";

const props = defineProps<{
    label: string
    step?: number
}>()

const count = ref<number>(0);

const emit = defineEmits<{
    changed: [value: number]
}>();
const message = ref<string>("loading...");

const isEven = computed(()=> count.value % 2 == 0 );

function increment() {
    const changeDelta = props.step ?? 1;
    count.value += changeDelta;
    emit("changed", changeDelta);
}

watch(count, (newVal, oldVal)=>{
    console.log(`count changed from ${oldVal} to ${newVal}`);
})

onMounted(async () => {
    const response = await fetch("/data.json");
    const data = await response.json();
    message.value = data.message;
});

</script>

<template>
    <button @click="increment">{{ label }} : {{  count  }}</button>
    <p>{{  isEven? "Even": "Odd" }}</p>
    <p> {{  message  }}</p>
</template>