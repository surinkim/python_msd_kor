/* Chapter08 */
/* runs_2.jsx */
var RunsBox = React.createClass( {
    loadRunsFromServer: function()  {
      var xhr = new XMLHttpRequest();
      xhr.open('get', this.props.url, true);
      xhr.withCredentials = true;
      xhr.onload = function()  {
        var data = JSON.parse(xhr.responseText);
        this.setState( { data: data } );
      } .bind(this);
      xhr.send();
    } ,
  
    getInitialState: function()  {
      return  {data: []} ;
    } ,
  
    componentDidMount: function()  {
      this.loadRunsFromServer();
    } ,
  
    render: function()  {
      return (
        <div>
          <h2>Runs</h2>
          <Runs data= {this.state.data}  />
        </div>
      );
    }
} );

/* RunsBox를 전역으로 노출한다. */
window.RunsBox = RunsBox;