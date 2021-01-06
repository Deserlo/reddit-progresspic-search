import React from 'react'
import Header from './Header';
import Thumbnails from './Thumbnails';
import Viewer from './Viewer';



function Main() {
    return (
        <div>
            <div id="main">
                <h1>Progress Pic Search</h1>
            <Header/>
            <Thumbnails/>
            </div>
            <Viewer/>
        </div>
    )
}

export default Main