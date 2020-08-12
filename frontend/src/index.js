import React from 'react';
import ReactDOM from 'react-dom';


class App extends React.Component {
    reder () {
        return (
            <div>hello</div>
        )
    }
}

ReactDOM.render(<App/>, document.getElementById('app'));