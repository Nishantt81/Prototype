let inputValue = "Your input here"; // Assign the actual input value
const apiToken = "your_actual_api_token"; // Replace with your actual token
const apiKey = "your_actual_api_key";    // Replace with your actual API key

fetch("http://127.0.0.1:7860/api/v1/run/prototype?stream=false", {
  method: "POST",
  headers: {
    Authorization: `Bearer ${apiToken}`,
    "Content-Type": "application/json",
    "x-api-key": apiKey, // Replace with your API key
  },
  body: JSON.stringify({
    input_value: inputValue,
    output_type: "chat",
    input_type: "chat",
    tweaks: {
      "ChatInput-w7erC": {},
      "AstraDB-XZAmC": {},
      "GoogleGenerativeAIModel-9FoAi": {},
      "ChatOutput-gm65H": {},
    },
  }),
})
  .then((res) => {
    if (!res.ok) {
      throw new Error(`HTTP error! status: ${res.status}`);
    }
    return res.json();
  })
  .then((data) => console.log("Response:", data))
  .catch((error) => console.error("Error:", error));
