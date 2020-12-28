import React,{useState,useEffect} from 'react';
import './App.css';


function List({ items, fallback }) {
  if (!items || items.length === 0) {
    return fallback;
  } else {
    console.log("type of ", typeof(items.data[0]));
    console.log(items.data[0]);
    return items.data.map(item => {
      return <div key={item.id}>{item.title}</div>;
    });
  }
}

const getItems = () => fetch('/home').then(res => res.json());

function App() {
  const [items, setItems] = useState([]);

  useEffect(() => {
    getItems().then(data => setItems(data));
  }, []);

  return (
    <div>
      <List items={items} fallback={"Loading..."} />
    </div>
  );
}


export default App;
