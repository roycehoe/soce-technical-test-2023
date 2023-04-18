<script setup lang="ts">
// import { onBeforeMount } from "vue";

import { ref } from "vue";
import { ShopItemIn, useItem } from "../../composables/useItem";
import { useItems } from "../../composables/useItems";

const { updateCurrentItems } = useItems();
const { updateItem, deleteItem } = useItem();
const { item } = defineProps<{ item: ShopItemIn }>();
const isLoading = ref(false);
</script>

<template>
  <form
    @submit.prevent="
      async (event) => {
        await updateItem(item.id, {
          name: item.name,
          quantity: item.quantity,
          price: item.price,
          description: item.description,
        });
        await updateCurrentItems();
      }
    "
  >
    <div class="card bg-base-100 shadow-xl w-96 m-6">
      <div class="card-body">
        <input
          type="text"
          placeholder="Name"
          class="input input-ghost p-0 card-title text-center"
          v-model="item.name"
          required
        />
        <input
          type="text"
          placeholder="Description"
          class="input input-ghost w-full max-w-xs p-0 text-center"
          v-model="item.description"
          required
        />
        <div class="divider m-0"></div>
        <p class="card-title block">
          $
          <input
            type="number"
            step="0.01"
            placeholder="Price"
            class="input input-bordered w-16 p-0 text-center"
            v-model="item.price"
            required
          />
        </p>
        <div class="card-actions justify-between mt-4">
          <input
            type="text"
            placeholder="Qty"
            class="input input-bordered w-12 p-0 text-center"
            :value="item.quantity"
            required
          />
          <div class="admin-mod-selection">
            <button
              :disabled="isLoading"
              @click="
                async (event) => {
                  await deleteItem(item.id);
                  await updateCurrentItems();
                }
              "
              class="btn btn-error mx-2"
            >
              Delete
            </button>
            <button type="submit" class="btn btn-success mx-2">Save</button>
          </div>
        </div>
      </div>
    </div>
  </form>
</template>
<style scoped></style>
