import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [count, setCount] = useState(0)
  const [greeting, setGreeting] = useState('')
  const [file, setFile] = useState(null)
  const [name, setName] = useState('')

  // Handle file change
  const handleFileChange = (e) => {
    setFile(e.target.files[0])  // Store selected file
  }

  // Handle name change
  const handleNameChange = (e) => {
    setName(e.target.value)  // Store entered name
  }

  // Function to call the API with file upload
  const uploadFile = async () => {
    if (!file) {
      alert("Please select an MP3 file first")
      return
    }

    const formData = new FormData()
    formData.append('file', file)  // Add file to the form data

    try {
      const response = await fetch('https://test-function-1011726187231.us-central1.run.app', {
        method: "POST",
        body: formData,
      })
      const text = await response.text()
      setGreeting(text)
    } catch (error) {
      console.error('Error calling API:', error)
    }
  }

  // Function to call the API with name parameter
  const sendName = async () => {
    try {
      const response = await fetch('https://test-function-1011726187231.us-central1.run.app', {
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        method: "POST",
        body: JSON.stringify({ name: name || 'World' })  // Default to 'World' if name is empty
      })
      const text = await response.text()
      setGreeting(text)
    } catch (error) {
      console.error('Error calling API:', error)
    }
  }

  return (
    <>
      <div>
        <a href="https://vite.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        <input type="file" accept=".mp3" onChange={handleFileChange} />
        <button onClick={uploadFile}>Upload MP3 and Call API</button>
        <br />
        <input
          type="text"
          placeholder="Enter a name"
          value={name}
          onChange={handleNameChange}
        />
        <button onClick={sendName}>Send Name and Call API</button>
        <p>{greeting}</p>
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.jsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App
