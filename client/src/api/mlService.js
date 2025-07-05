// src/api/mlService.js

export async function getSuggestions(inputText) {
  try {
    const response = await fetch('http://localhost:5050/generate', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ input: inputText }),
    });

    if (!response.ok) {
      throw new Error('ML service not responding');
    }

    const data = await response.json();
    console.log("✅ Response received from Flask:", data);

    if (Array.isArray(data)) {
      return { products: data, trending: [] };
    }

    // 📦 Now supporting both products and trending from backend
    if (Array.isArray(data.products)) {
      return {
        products: data.products,
        trending: Array.isArray(data.trending) ? data.trending : []
      };
    }

    return { products: [], trending: [] };

  } catch (error) {
    console.error("❌ Error in mlService:", error.message);
    return { error: error.message, products: [], trending: [] };
  }
}
