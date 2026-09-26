<script setup lang="ts">
import type { Food } from "./types";

const props = defineProps<{
    food: Food
}>();

const emit = defineEmits<{
    deleted: [value: string]
}>()

const currencyFormatter =  Intl.NumberFormat("en-US", {style: "currency", currency: "USD"});

function toUSCurrency(price: number) {
    return currencyFormatter.format(price);
}

function deleteFood(){
    emit("deleted", props.food.id);
}


</script>

<template>
    {{  food.name }} -- {{  toUSCurrency(food.price) }}
    <button @click="deleteFood">Delete</button>
</template>

<style scoped>
</style>