var root = document.body

function getData() {
m.request({
    url: "http://ilmare.familjenberger.com:8000",   //Works
    method: "GET",
})
.then(function(result) {
    //console.log(JSON.parse(JSON.stringify(result.message[0])))
    //console.log(result.message[0])
    result.message.forEach(element => {
        console.log(element)
    });
})
}

var Data = {
    todos: {
        list: [],
        fetch: function() {
            m.request({
                method: "GET",
                url: "http://ilmare.familjenberger.com:8000",   //Works
            })
            .then(function(items) {
                Data.todos.list = items.message
                //console.log(Data.todos.list)
            })
        }
    }
}

var Todos = {
    oninit: Data.todos.fetch,
    view: function(vnode) {
        return Data.todos.list.map(function(item) {
            //console.log(item[0])    // Name
            //console.log(item[1])    // URL
            return m("div", item)
        })
    }
}

m.route(document.body, "/", {
    "/": Todos
})