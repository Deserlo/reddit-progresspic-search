import './App.css';
import Main from './components/Main';
import './main.css';

/*
function List({ items, fallback }) {
  if (!items || items.length === 0) {
    return fallback;
  } else {
    //console.log("type of ", typeof(items.data[0]));
    //console.log(items.data[0]);
    return items.map(item => {
      return <div key={item.post_id}><img src={item.post_thumbnail}/>{item.post_title}</div>;
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
      <Main/>
      <List items={items} fallback={"Loading..."} />
    </div>
  );
}

*/

function App(){
  return(
    <Main></Main>
  )
}


export default App;

