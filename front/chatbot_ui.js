<style>
  textarea.openai-prompt {
    width: 100%;
  }
</style>

#######

<div>
<form id="openai-form">
  <textarea id="openai-prompt-main" rows="10" col="50" class="openai-prompt">
  Say hello in japanese
  </textarea>

  <div>
    <button type="submit">Submit</button>
  </div>
</form>
<div>
  <p>OpenAI Response</p>
  <textarea id="openai-response-main" rows="2" col="50" class="openai-prompt"></textarea>
</div>
</div>

#######

<script>
  const openaiForm = document.getElementById('openai-form');
  const openaiPrompt = document.getElementById('openai-prompt-main');
  const openaiResponse = document.getElementById('openai-response-main');

  openaiForm.addEventListener('submit', (event) => {
    event.preventDefault();

    fetch('http://localhost:40003/prompt', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        prompt: openaiPrompt.value
      })
    })
    .then(response => response.json())
    .then(data => {
      console.log("response:", data)
      openaiResponse.textContent = data.text;
      openaiResponse.style = "height: 500px;";

    })
    .catch(error => {
      console.error(error);
    });
  });
</script>
