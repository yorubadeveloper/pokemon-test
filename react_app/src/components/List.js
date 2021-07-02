import React from 'react';

const List = (props) => {
    const { pokemons } = props;
    if (!pokemons || pokemons.length  === 0) return <p>No pokemons starting with S found</p>;
    return (
        <div className='menu'>
            <ul>
                {pokemons.map((pokemon) => {
                    return (
                        <li><button>{pokemon}</button></li>
                    );
                }
                )}
            </ul>
        </div>
    )
}

export default List;