const generatePlan = async () => {
  try {
    const response = await fetch(
      "http://127.0.0.1:8000/generate-plan?skill=Python&level=Beginner&time_per_day=15",
      {
        method: "POST",
      }
    );

    const data = await response.json();
    console.log(data); // 🔥 SEE RESPONSE

    return data;
  } catch (error) {
    console.error(error);
  }
};