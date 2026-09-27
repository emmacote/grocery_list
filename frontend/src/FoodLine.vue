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
    <div class="row">
        <div class="col-sm-4"> {{  food.name }} </div>
        <div class="col-sm-4">{{  food.price }}</div>
        <div class="col-sm-4"><button type="button" class="btn btn-danger" @click="deleteFood">Delete</button></div>
    </div>
</template>

<style scoped>
</style>