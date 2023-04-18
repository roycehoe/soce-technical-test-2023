<script setup lang="ts">

import { ref, toRefs } from "vue";
import { ShopItemIn, useItem } from "../../composables/useItem";
import { currentItems, useItems } from "../../composables/useItems";

const { updateCurrentItems } = useItems();
const { updateItem, deleteItem } = useItem();
const { item } = defineProps<{ item: ShopItemIn }>();

const itemForm = toRefs(item);
const isLoading = ref(false);

async function submitUpdateItemRequest() {
  isLoading.value = true;
  await updateItem(itemForm.id.value, {
    name: itemForm.name.value,
    quantity: itemForm.quantity.value,
    price: itemForm.price.value,
    description: itemForm.description.value,
  });
  await updateCurrentItems();
  isLoading.value = false;
}

async function submitDeleteItemRequest() {
  isLoading.value = true;
  await deleteItem(itemForm.id.value);
  await updateCurrentItems();
  console.log(currentItems);
  isLoading.value = false;
}
</script>

<template>
  <form @submit.prevent="submitUpdateItemRequest">
    <div class="card bg-base-100 shadow-xl w-96 m-6">
      <div class="card-body">
        <input
          type="text"
          placeholder="Name"
          class="input input-ghost p-0 card-title text-center"
          v-model="itemForm.name.value"
          required
        />
        <input
          type="text"
          placeholder="Description"
          class="input input-ghost w-full max-w-xs p-0 text-center"
          v-model="itemForm.description.value"
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
            v-model="itemForm.price.value"
            required
          />
        </p>
        <div class="card-actions justify-between mt-4">
          <input
            type="number"
            placeholder="Qty"
            class="input input-bordered w-12 p-0 text-center"
            :value="itemForm.quantity.value"
            required
          />
          <div class="admin-mod-selection">
            <button
              type="button"
              :disabled="isLoading"
              @click="submitDeleteItemRequest"
              class="btn btn-error mx-2"
            >
              Delete
            </button>
            <button
              type="submit"
              :disabled="isLoading"
              class="btn btn-success mx-2"
            >
              Save
            </button>
          </div>
        </div>
      </div>
    </div>
  </form>
</template>
<style scoped></style>
