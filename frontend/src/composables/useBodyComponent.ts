import { ref } from "vue";

export enum BodyComponent {
  Admin,
  Shop,
}

export const currentBodyComponent = ref(BodyComponent.Shop as BodyComponent);
