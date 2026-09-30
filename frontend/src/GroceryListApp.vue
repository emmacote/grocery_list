<script setup lang="ts">
import { ref, onMounted, watch, computed } from "vue";
import type { Food } from "./types";
import FoodLine from "./FoodLine.vue";
import "bootstrap/dist/css/bootstrap.css"
import "bootstrap/dist/js/bootstrap.bundle.js"
import axios from "axios";

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
    <div class="container">
        <div class="row">
            <div class="col-sm-3"><b>Add food: </b></div>
            <div class="col-sm-3"><input v-model="newFoodText" placeholder="New food item..." /></div>
            <div class="col-sm-3"> <b>Add Price: </b></div>
            <div class="col-sm-3"><input v-model.number="newFoodPrice" placeholder="0.00" /></div>
        </div>

        <div class="row">
            <div class="col-sm-12 d-grid gap-2"> <br /><button type="button" class="btn btn-primary" @click="addFood()">Add</button></div>
        </div>
        
        <div class="row">
            <div class="col-sm-12"><hr /></div>
        </div>

        <div class="row">
            <div class="col-sm-3">Order</div>
            <div class="col-sm-3">
                    <select v-model="selectedOrder">
                        <option value="NO_ORDER">No order</option>
                        <option value="PRICE_ORDER">Price order</option>
                        <option value="NAME_ORDER">Name order</option>
                    </select>
            </div>
            <div class="col-sm-3">Search</div>
            <div class="col-sm-3">
                <input v-model="searchTerm" type="text"/>
            </div>
        </div>

        <div class="row">
            <div class="col-sm-12"><hr /></div>
        </div>

        <div class="row">
            <div class="col-sm-12">
                <br />
                <h3>Grocery List</h3>
            </div>
        </div>
        <div class="row">
            <div class="col-sm-12">
                <ul class="list-group">
                    <li class="list-group-item" v-for="food in searchedGroceries" :key="food.id">
                        <FoodLine  :food="food" @deleted="deleteFood"></FoodLine>   
                    </li>
                </ul>
            </div>
        </div>
    </div>
</template>