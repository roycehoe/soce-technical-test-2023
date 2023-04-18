<script setup lang="ts">
import { DEFAULT_PRICE_DECIMAL_PLACES } from "../constants";

const PREPOPULATED_ITEMS = [
  {
    name: "Coke Zero",
    quantity: 100,
    price: 1.8,
    description: "A healthier alternative to regular coke",
  },
  {
    name: "Coke Regular",
    quantity: 20,
    price: 1.6,
    description: "An unhealthier alternative to coke zero",
  },
  {
    name: "Twisties",
    quantity: 38,
    price: 1.0,
    description: "A tasty corn-based snack!",
  },
  {
    name: "Liquorice",
    quantity: 22,
    price: 1.2,
    description: "Just why.....",
  },
  {
    name: "Top 10",
    quantity: 8,
    price: 1.5,
    description: "The poor man's Mangum ice cream. Tastes just as great!",
  },
];
</script>

<template>
  <div class="w-screen h-screen flex flex-col">
    <div class="flex flex-wrap mx-24 text-center">
      <div v-for="item in PREPOPULATED_ITEMS" class="w-96 m-6">
        <div class="card bg-base-100 shadow-xl">
          <div class="card-body">
            <p class="card-title text-center block">{{ item.name }}</p>
            <p>{{ item.description }}</p>
            <div class="divider m-0"></div>
            <p class="my-2 card-title block">
              ${{ item.price.toFixed(DEFAULT_PRICE_DECIMAL_PLACES) }}
            </p>
            <div class="card-actions justify-between mt-2">
              <select class="select select-primary">
                <option selected>0</option>
                <option v-for="quantity in item.quantity">
                  {{ quantity }}
                </option>
              </select>
              <button class="btn btn-primary">Add to cart</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<style scoped></style>
