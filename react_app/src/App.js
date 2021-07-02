import React, {useState, useEffect} from 'react';
import axios from 'axios'
import './App.css';
import List from './components/List';
import ListLoading from './components/ListLoading';

function App() {
  const ListsLoading = ListLoading(List);
  const [appState, setAppState] = useState({
    loading: false,
    pokemons: null
  });

  useEffect(() => {
    setAppState({loading: true});
    const apiUrl = 'http://127.0.0.1:5000/get-pokemon';
    axios.get(apiUrl).then((pokemons) => {
      const Allpokemons = pokemons.data.pokemons;
      setAppState({loading: false, pokemons: Allpokemons})
    });
  }, [setAppState])

  return (
    <div className="App">
      <h2>Pokemons beginning with 'S'</h2>
      <div>
        <ListsLoading isLoading={appState.loading} pokemons={appState.pokemons} />
      </div>
    </div>
  );
}

export default App;
