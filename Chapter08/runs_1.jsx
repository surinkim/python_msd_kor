/* Chapter08 */
/* runs_1.jsx */
var Run = React.createClass( {
  render: function() {
    return (
      <div>{this.props.title} ({this.props.type})</div>
    );
  }
} );

var Runs = React.createClass( {
  render: function() {
    var runNodes = this.props.data.map(function (run) {
      return (
        <Run
          title= {run.title}
          type= {run.type}
        />
      );
    } );
    
    return (
      <div>
        {runNodes}
      </div>
    );
  }
} );
  