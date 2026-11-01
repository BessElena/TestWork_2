import { useState } from 'react';
import Header from './Header';
import ParticipantCard from './ParticipantCard';
import './App.css';

function App() {
  const [participants] = useState([
    { id: 1, name: 'Никита Анисимов', email: 'anisimovich.nikita0604@gmail.com' },
    
  ]);

  return (
    <>
      <Header />

      <main>
        <h1>Участники проекта</h1>

        {participants.map((participant) => (
          <ParticipantCard
            key={participant.id}
            name={participant.name}
            email={participant.email}
          />
        ))}
      </main>
    </>
  );
}

export default App;