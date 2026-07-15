import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

export const getInteractions = () => {
  return API.get("/interactions");
};

export const createInteraction = (interactionData) => {
  return API.post("/interactions", interactionData);
};

export const updateInteraction = (interactionId, interactionData) => {
  return API.put(`/interactions/${interactionId}`, interactionData);
};

export const searchHCP = (name) => {
  return API.get("/hcps/search", {
    params: {
      name: name,
    },
  });
};

export const sendChatMessage = (message) => {
  return API.post("/chat", {
    message: message,
  });
};

export default API;