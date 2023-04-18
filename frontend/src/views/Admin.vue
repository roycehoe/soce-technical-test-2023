<script setup lang="ts">
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
    <div class="flex flex-wrap mx-24">
      <div v-for="item in PREPOPULATED_ITEMS" class="w-96 m-6">
        <div class="card bg-base-100 shadow-xl">
          <div class="card-body">
            <input
              type="text"
              placeholder="Name"
              class="input input-ghost w-full max-w-xs p-0 card-title"
              :value="item.name"
            />
            <input
              type="text"
              placeholder="Description"
              class="input input-ghost w-full max-w-xs p-0"
              :value="item.description"
            />
            <div class="card-actions justify-between mt-4">
              <input
                type="text"
                placeholder="Qty"
                class="input input-bordered w-12 p-0 text-center"
                :value="item.quantity"
              />
              <div class="admin-mod-selection">
                <button class="btn btn-primary mx-2">Delete</button>
                <button class="btn btn-primary mx-2">Save</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<style scoped></style>
