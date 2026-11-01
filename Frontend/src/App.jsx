
import { useState, useEffect } from 'react';
import Header from './Header';
import ParticipantCard from './ParticipantCard';
import './App.css';

function App() {
  const [participants, setParticipants] = useState([]);
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [wish, setWish] = useState('');

  useEffect(() => {
    fetch('http://localhost:5000/api/participants')
      .then((response) => response.json())
      .then((data) => {
        setParticipants(data.data);
      })
      .catch((error) => {
        console.error('Ошибка загрузки участников:', error);
      });
  }, []);

  function handleSubmit(event) {
    event.preventDefault();

    fetch('http://localhost:5000/api/participants', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ name, email, wish }),
    })
      .then((response) => response.json())
      .then((result) => {
        if (result.success) {
          setParticipants([...participants, result.data]);
          setName('');
          setEmail('');
          setWish('');
        } else {
          alert(result.error);
        }
      })
      .catch((error) => {
        console.error('Ошибка добавления участника:', error);
      });
  }

  return (
    <>
      <Header />

      <main>
        <h1>Участники проекта</h1>

        <form onSubmit={handleSubmit}>
          <input
            type="text"
            placeholder="Ваше имя"
            value={name}
            onChange={(event) => setName(event.target.value)}
            required
          />

          <input
            type="email"
            placeholder="Ваша почта"
            value={email}
            onChange={(event) => setEmail(event.target.value)}
            required
          />

          <textarea
            placeholder="Ваше пожелание"
            value={wish}
            onChange={(event) => setWish(event.target.value)}
          />

          <button type="submit">Добавить участника</button>
        </form>

        {participants.map((participant) => (
          <ParticipantCard
            key={participant.id}
            name={participant.name}
            email={participant.email}
            wish={participant.wish}
          />
        ))}
      </main>
    </>
  );
}

export default App;
