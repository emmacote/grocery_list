<script setup lang="ts">
import type { Food } from "./types";

defineProps<{
    food: Food
}>();

const currencyFormatter =  Intl.NumberFormat("en-US", {style: "currency", currency: "USD"});

function toUSCurrency(price: number) {
    return currencyFormatter.format(price);
}

</script>

<template>{{  food.name }} -- {{  toUSCurrency(food.price) }}</template>

<style scoped>
</style>