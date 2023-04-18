<script setup lang="ts">
import { ref } from "vue";
import { ShopItemOut, useItem } from "../../composables/useItem";
import { useItems } from "../../composables/useItems";

const { createItem } = useItem();
const { updateCurrentItems } = useItems();

const newItem = ref({
  name: "",
  quantity: 0,
  price: 0,
  description: "",
} as ShopItemOut);

function resetNewItemForm(): void {
  newItem.value = {
    name: "",
    quantity: 0,
    price: 0,
    description: "",
  };
}

async function submitCreateItem(): Promise<void> {
  await createItem(newItem.value);
  resetNewItemForm();
  updateCurrentItems();
  return;
}
</script>

<template>
  <form @submit.prevent="submitCreateItem">
    <div class="w-96 m-6 curent-store--new-item">
      <div class="card bg-base-100 shadow-xl current-store--card">
        <div class="card-body">
          <input
            type="text"
            placeholder="Name"
            class="input input-ghost w-full max-w-xs p-0 card-title text-center"
            v-model="newItem.name"
            required
          />
          <input
            type="text"
            placeholder="Description"
            class="input input-ghost w-full max-w-xs p-0 text-center"
            v-model="newItem.description"
            required
          />
          <div class="divider m-0"></div>
          <p class="card-title block">
            $
            <input
              type="number"
              step="0.01"
              placeholder="Price"
              class="input input-bordered w-20 p-0 text-center"
              v-model="newItem.price"
              required
            />
          </p>
          <div class="card-actions justify-between mt-4">
            <input
              type="number"
              placeholder="Qty"
              class="input input-bordered w-12 p-0 text-center"
              v-model="newItem.quantity"
              required
            />
            <div class="admin-mod-selection">
              <button type="submit" class="btn btn-success mx-2">Save</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </form>
</template>
<style scoped></style>
