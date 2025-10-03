export async function analyzeResume(formData) {
  const response = await fetch("http://127.0.0.1:8000/upload-resume", {
    method: "POST",
    body: formData,
  });
  return response.json();
}
