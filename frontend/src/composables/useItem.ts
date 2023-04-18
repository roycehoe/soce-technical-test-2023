import { Err, Result } from "ts-results";
import { ref } from "vue";
import { client } from "../services";

export interface ShopItemOut {
  name: string;
  quantity: number;
  price: number;
  description: string;
}

export interface ShopItemIn extends ShopItemOut {
  id: number;
}

export function useItem() {
  const isLoading = ref(false);

  async function createItem(
    newItem: ShopItemOut
  ): Promise<Result<void, string>> {
    try {
      return await client.post("/item/", newItem);
    } catch (error) {
      console.log(error);
      return Err("error occured creating item");
    }
  }

  async function updateItem(
    itemId: number,
    updatedItem: ShopItemOut
  ): Promise<Result<void, string>> {
    try {
      return await client.put(`/item/${itemId}`, updatedItem);
    } catch (error) {
      console.log(error);
      return Err("error occured updating item");
    }
  }

  async function deleteItem(itemId: number): Promise<Result<void, string>> {
    isLoading.value = true;
    try {
      return await client.delete(`/item/${itemId}`);
    } catch (error) {
      console.log(error);
      return Err("error occured deleting item");
    } finally {
      isLoading.value = false;
    }
  }

  return { createItem, updateItem, deleteItem, isLoading };
}
