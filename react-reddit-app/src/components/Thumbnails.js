import React,{useState,useEffect} from 'react';
import './Thumbnails.css';


function List({ items, fallback }) {
    if (!items || items.length === 0) {
      return fallback;
    } else {
      //console.log("type of ", typeof(items.data[0]));
      //console.log(items.data[0]);
      return items.map(item => {
        /*return <div key={item.post_id}><img src={item.post_thumbnail}/>{item.post_title}</div>;*/
        return <img src={item.post_thumbnail}/>;
      });
    }
  }

const getItems = () => fetch('/home').then(res => res.json());

function Thumbnails() {
const [items, setItems] = useState([]);

useEffect(() => {
    getItems().then(data => setItems(data));
}, []);


return (
    <section id="thumbnails">
    <List items={items} fallback={"Loading..."} />
    </section>
);
}


export default Thumbnails