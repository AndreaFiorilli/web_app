async function submitPhrase() {
    const phrase = document.getElementById('phraseInput').value;
    if (!phrase) return;

    const response = await fetch('http://localhost:8000/add_phrase', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ phrase: phrase })
    });

    const data = await response.json();
    document.getElementById('result').innerText = data.message;
    document.getElementById('phraseInput').value = '';
}

