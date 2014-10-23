 /** @jsx React.DOM */

      var data = [
        {author: "Pete Hunt", text:"This is one comment."},
        {author: "Jordan White", text:"This is *another* comment."},
      ]

      var CommentBox = React.createClass({
        loadComments:function(){
          var url = "jobs/"
            this.setState({data: this.state.data});
        },
        handleCommentSubmit: function(comment){
          var comments = this.state.data;
          var newComments = comments.concat([comment]);
          this.setState({data: newComments});
        },

        getInitialState: function(){
          return {data: data};
        },
        componentDidMount: function(){
          this.loadComments();
          setInterval(this.loadComments, this.props.pollInterval);
        },
        render: function(){
          return (
              <div className="commentBox">
                <h1>Comments</h1>
                <h1>{this.props.jobPK}</h1>
                <CommentList data={this.state.data}/>
                <CommentForm onCommentSubmit={this.handleCommentSubmit}/>
              </div>
            );
        }
      });

      var CommentList = React.createClass({
        render: function(){
          var commentNodes = this.props.data.map(function(comment){
            return (
                <Comment author={comment.author}>
                  {comment.text}
                </Comment>
              );
          })

          return (
          <div className="CommentList">
            {commentNodes}
          </div>
          );
        }
      });

      var CommentForm = React.createClass({
        handleSubmit: function(e){
          e.preventDefault();
              var author = this.refs.author.getDOMNode().value.trim();
              var text = this.refs.text.getDOMNode().value.trim();

              if (!text || !author) {
                return;
              }

              this.props.onCommentSubmit({author: author, text: text});

              this.refs.author.getDOMNode().value = '';
              this.refs.text.getDOMNode().value = '';
              return;
        },

        render: function(){
          return (
          <form className="CommentForm" onSubmit={this.handleSubmit}>
             <input type="text" placeholder="Your name" ref="author"/>
             <input type="text" placeholder="Say something..." ref="text"/>
             <input type="submit" value="Post"/>
          </form>
          );
        }
      });

      var Comment = React.createClass({
        render: function(){
          return (
            <div className="comment">
              <h2 className="commentAuthor">{this.props.author}</h2>
            </div>
          );
        }
      });

      React.renderComponent(
        <CommentBox pollInterval={2000} jobPK={document.getElementById('hiddenData').innerHTML} />,
        document.getElementById('react-commentbox'))
