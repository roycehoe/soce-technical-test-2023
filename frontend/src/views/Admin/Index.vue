<script setup lang="ts">
import { onBeforeMount, ref } from "vue";
import { ShopItemIn, useItem } from "../../composables/useItem";
import { useItems } from "../../composables/useItems";
import { DEFAULT_PRICE_DECIMAL_PLACES } from "../../constants";
import NewItem from "./NewItem.vue";

const { getItems } = useItems();
const { createItem, updateItem, deleteItem, isLoading } = useItem();

const shopItems = ref([] as ShopItemIn[]);

async function fetchShopItemData() {
  const { ok: isSuccessful, val: response } = await getItems();
  if (isSuccessful) {
    shopItems.value = response as ShopItemIn[];
    return;
  }
  console.log(response);
}

onBeforeMount(fetchShopItemData);
</script>

<template>
  <div class="w-screen h-screen flex flex-col">
    <div class="flex flex-wrap mx-24 text-center current-store--group">
      <div v-for="item in shopItems" class="w-96 m-6 curent-store--cards">
        <div class="card bg-base-100 shadow-xl">
          <div class="card-body">
            <input
              type="text"
              placeholder="Name"
              class="input input-ghost p-0 card-title text-center"
              :value="item.name"
            />
            <input
              type="text"
              placeholder="Description"
              class="input input-ghost w-full max-w-xs p-0 text-center"
              :value="item.description"
            />
            <div class="divider m-0"></div>
            <p class="card-title block">
              $
              <input
                type="text"
                placeholder="Price"
                class="input input-bordered w-16 p-0 text-center"
                :value="item.price.toFixed(DEFAULT_PRICE_DECIMAL_PLACES)"
              />
            </p>
            <div class="card-actions justify-between mt-4">
              <input
                type="text"
                placeholder="Qty"
                class="input input-bordered w-12 p-0 text-center"
                :value="item.quantity"
              />
              <div class="admin-mod-selection">
                <button
                  :disabled="isLoading"
                  @click="
                    async (event) => {
                      await deleteItem(item.id);
                      await fetchShopItemData();
                    }
                  "
                  class="btn btn-primary mx-2"
                >
                  Delete
                </button>
                <button class="btn btn-primary mx-2">Save</button>
              </div>
            </div>
          </div>
        </div>
      </div>
      <NewItem></NewItem>
    </div>
  </div>
</template>
<style scoped></style>
