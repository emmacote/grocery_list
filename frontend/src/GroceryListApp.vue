<script setup lang="ts">
import { ref, onMounted, watch, computed } from "vue";
import type { Food } from "./types";
import FoodLine from "./FoodLine.vue";

type SortType = "NAME_ORDER" | "PRICE_ORDER" | "NO_ORDER";

const groceries = ref<Food[]>([
    {id: "1", name: "Apples", price: 0.32},
    {id: "2", name: "Bananas", price: 0.88},
]);

const selectedOrder = ref<SortType>("NO_ORDER");
const searchTerm = ref<string>("");

const newFoodText = ref<string>("");
const newFoodPrice = ref<number>(0.01);






function addFood(){

    if(newFoodText.value.trim().length > 0){
        groceries.value.push(
        {
            id: Date.now().toString(),
            name: newFoodText.value,
            price: newFoodPrice.value
        });

        newFoodText.value = "";
        newFoodPrice.value=0.01;
    }

}

const sortedGroceries = computed(()=>{
    if(selectedOrder.value === "NAME_ORDER"){
        let arrToSort = [...groceries.value];
        arrToSort.sort(  (x,y)=>x.name.localeCompare(y.name) )
        return arrToSort;
    }
    else if(selectedOrder.value === "PRICE_ORDER"){
        let arrToSort = [...groceries.value];
        arrToSort.sort( (x,y)=> x.price - y.price );
        return arrToSort;
    }
    return groceries.value;
});

const searchedGroceries = computed(()=>{
    const searchLambda = (x: Food )=>x.name.toLowerCase().includes(searchTerm.value.toLowerCase());
    let searchFilteredList = sortedGroceries.value.filter(searchLambda);
    return searchFilteredList;
});

function deleteFood(id: string){    
    groceries.value = groceries.value.filter(food=>food.id !== id );
}




watch(groceries, (newGroceries)=> {
    localStorage.setItem("groceries", JSON.stringify(newGroceries))
}, {deep: true });


onMounted(()=> {
    const saved = localStorage.getItem("groceries");
    if( saved ){
        groceries.value = JSON.parse(saved);
    }
});



</script>

<template>

    <b>Add food: </b><input v-model="newFoodText" placeholder="New food item..." />
    <b>Add Price: </b> <input v-model.number="newFoodPrice" placeholder="0.00" />
    <br /><br />

    <button @click="addFood()">Add</button>
    <br />
    <b>Grocery List</b><br />
    <select v-model="selectedOrder">
        <option value="NO_ORDER">No order</option>
        <option value="PRICE_ORDER">Price order</option>
        <option value="NAME_ORDER">Name order</option>
    </select>
    <br />
    <b>Search: </b>
    <input v-model="searchTerm" type="text"/>

    <br />
    <h3>Grocery List</h3>
    <ul>
        <li v-for="food in searchedGroceries" :key="food.id">
            <FoodLine :food="food" @deleted="deleteFood"></FoodLine>
            
        </li>
    </ul>
</template>