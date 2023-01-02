import React, { useState } from 'react'; 

const Search = () => {
    const [string, setString] = useState(''); 
    
    function handleSubmit(e){
        e.preventDefault();
        
        //pass data to backend 
    }

    

    return (
        <form onSubmit={handleSubmit}>
            <input type="text" value={string} onChange={(e) => setString(e.target.value)}></input>
            <button type="submit">Go!</button>
        </form>

    ); 
}

export default Search; 