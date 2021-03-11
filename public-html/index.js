var root = document.body

function getData(uri, struct) {
    m.request({
        url: uri ,
        method: "GET",
    })
    .then(function(result) {
        //console.log(result)

        /*console.log(JSON.parse(JSON.stringify(result.message[0])))
        console.log(result.message[0])
        result.message.forEach(element => {
            console.log(element)
        });
        */
        struct.list = result
    })
}

var SpotifyData = {
        list: []
}

var YoutubeData = {
    list: []
}

var PDFData = {
    list: []
}

var AllitemsData = {
    list: []
}

var APIData = {
    list: ["/" ,
        "/Spotify",
        "/Youtube",
        "/PDF",
        "/Allitems"
    ]
}

//var count = 0;
var Start = {
    //oninit: getData("http://localhost:8000/openapi.json", APIData),
    view: function(vnode) {
        return APIData.list.map(function(item){
            link = "#!/" + item
            title = item.split("/")
            //return m("a", {href: link}, title) //Fungerar
            //return m("button", {onclick: function() {location.assign(link)}}, title ) //Fungerar
            return m(m.route.Link, {href: item}, title)
        })
    }
}

var Spotify = {
    oninit: getData("http://localhost:8000/Spotify",SpotifyData),
    view: function(vnode) {
        return SpotifyData.list.map(function(item) {
            //console.log(item[0])    // Name
            //console.log(item[1])    // URL
            //return m("div", item)
            return m("a", {href: item[1]}, item[0])
        })
    }
}


var Youtube = {
    oninit: getData("http://localhost:8000/Youtube", YoutubeData),
    view: function(vnode) {
        return YoutubeData.list.map(function(item) {
            //console.log(YoutubeData)
            //console.log(item[0])    // Name
            //console.log(item[1])    // URL
            return m("a", {href: item[1]}, item[0])  //Fungerar
            //return m.render(document.body, m("a", {href: item[1]}, item[0]))
        })
    }
}

var PDFs = {
    oninit: getData("http://localhost:8000/PDF", PDFData),
    view: function(vnode) {
        return PDFData.list.map(function(item) {
            //console.log(item[0])    // Name
            //console.log(item[1])    // URL
            //return m("div", item)
            return m("a", {href: item[1]}, item[0])
        })
    }
}

var Allitems = {
    oninit: getData("http://localhost:8000/Allitems", AllitemsData),
    view: function(vnode) {
        return AllitemsData.list.map(function(item) {
            //console.log(item[0])    // Name
            //console.log(item[1])    // URL
            //return m("div", item)
            return m("a", {href: item[1]}, item[0])
        })
    }
}

m.route(document.body, "/", {
    "/": Start,
    "/Youtube": Youtube ,
    "/Spotify" : Spotify,
    "/PDF": PDFs,
    "/Allitems": Allitems
})