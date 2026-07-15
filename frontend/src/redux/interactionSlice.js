import { createSlice } from "@reduxjs/toolkit";

const interactionSlice = createSlice({
  name: "interactions",

  initialState: {
    interactions: [],
    loading: false,
    error: null,
  },

  reducers: {
    addInteraction: (state, action) => {
      state.interactions.push(action.payload);
    },
  },
});

export const { addInteraction } = interactionSlice.actions;

export default interactionSlice.reducer;
