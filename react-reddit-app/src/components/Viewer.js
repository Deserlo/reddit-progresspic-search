import React,{useState,useEffect} from 'react';


function First({ item, fallback }) {
    //console.log("type of ", typeof(items.data[0]));
    //console.log(items.data[0]);
    /*return <div key={item.post_id}><img src={item.post_thumbnail}/>{item.post_title}</div>;*/
    /*return <img src={item.post_thumbnail} alt={item.post_title}/>;*/
    console.log("hello");
    return <div id="viewer">
        <div className="inner">
            <div className="nav-next"></div>
            <div className="nav-previous"></div>
            <div className="toggle"></div>
        </div>
        <div className="caption">{item.post_title}</div>
        <div className="image"><img src={item.post_thumbnail} alt="jj"/></div>
    </div> 
}

const getItem = () => fetch('/first').then(res => res.json());

function Viewer() {

    const [item, setItem] = useState([]);


    useEffect(() => {
        getItem().then(data => setItem(data));
    }, []);


    return (
        <First item={item}/>
    );
}


export default Viewer