import { useState, useEffect } from 'react'
import ContactList from './ContactList'
import './App.css'

function App() {
  const [contacts, setContacts] = useState([{"id": "1", "firstName": "Tim", "email": "cum man 18"}])

  useEffect(() => {
    // fetchContacts()
}, [])

  const fetchContacts = async () => {
    const response = await fetch('http://localhost:5000/contacts')
    const data = await response.json()
    setContacts(data.contacts)
    console.log(data.contacts)
  }

  return <ContactList contacts={contacts} />
}

export default App
