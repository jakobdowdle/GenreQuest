import { useState } from 'react'
import { IonIcon } from '@ionic/react'
import { musicalNotesOutline, arrowForwardCircle, arrowForwardOutline } from 'ionicons/icons';
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
      const response = await fetch('https://us-central1-genrequest-440522.cloudfunctions.net/function-1', {
        method: "POST",
        body: formData,
      })
      const data = await response.json();  // Use .json() instead of .text()
      setGreeting(data);  // Assuming the response is in JSON format
      
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
      <h1 className='logo'>GenreQuest</h1>
      <button className='clicky'onClick={() => setCount((count) => count + 1)}>
      <IonIcon icon={musicalNotesOutline} style={{ fontSize: '24px' }}/> 
      </button>
      
      <div className="card">
        <h4>Select a .mp3 file located on your computer and hit "Upload." Our system will analyze the audio file to estimate it's genre.</h4>
        <input type="file" accept=".mp3" onChange={handleFileChange} />
        <button onClick={uploadFile}>
          Upload MP3 and Call API 
          <IonIcon
          className='icons' 
          icon={ arrowForwardOutline }
           />
          </button>            
        <br />
        <h4>Enter a musical genre (examples: Rock, Pop, Classical) to generate a playlist of music from that genre</h4>
        <input
          type="text"
          placeholder="Enter a name"
          value={name}
          onChange={handleNameChange}
        />
        <button onClick={sendName}>
          Send Name and Call API
          <IonIcon
          className='icons' 
          icon={ arrowForwardOutline }
           />
           </button>
        <p>{greeting}</p>
      </div>
      <p className="credits">
        Engineered by: JD | DN | SS.
      </p>
      <p className='counter'>
        {count}
      </p>
    </>
  )
}
export default App
