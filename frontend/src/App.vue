<script setup lang="ts">
import Body from "./components/Body.vue";
import Header from "./components/Header.vue";

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
    <Header></Header>
    <Body></Body>
  </div>
</template>
<style scoped></style>
