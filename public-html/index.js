var root = document.body
var target = document.createElement("div")

const developlment  = "http://localhost:8000/"
const production    = "http://ilmare.familjenberger.com:8000/"

var SpotifyData = { list: [] }
var YoutubeData = { list: [] }
var PDFData     = { list: [] }
var AllitemsData ={ list: [] }
var APIData     = { list: [] }
var ErrorData   = { list: [] }

var Points     = {
    list: [ "/" ,
            "/Spotify",
            "/Youtube",
            "/PDF",
            "/Allitems",
            "/ErrorTest"
    ]
}


function getData(uri, struct) {
    m.request({
        url: uri ,
        method: "GET",
    })
    .then(function(result) {
        //console.log(result)
        /*
        console.log(JSON.parse(JSON.stringify(result.message[0])))
        console.log(result.message[0])
        result.message.forEach(element => {
            console.log(element)
        });
        */
        struct.list = result
    })
    .catch(function(e) {
        struct.error = e
        //console.log(struct.error.code)
        //console.log(struct.error.response.detail)
    })
}

function createParagraph(item) {
    var paragraph = document.createElement("P")
    paragraph.innerHTML = "<a target=\"_blank\" rel=\"noopener noreferrer\" href=\"" + item[1] + "\">" + item[0] + "</a>"
    document.getElementById("main").appendChild(paragraph)
}

function createErrorParagraph(code, details) {
    // console.log(item)
    var paragraph = document.createElement("P")
    paragraph.innerHTML = "The back end is probably on coffee break and static fall back pages are still not implemented. " + 
    "The Error code is " + code + "."
    //" and the message " + details
    document.getElementById("main").appendChild(paragraph)
}

function foo(){
}

var Start = {
    oninit: foo(),
    view: function(vnode) {
        document.getElementById("navbar").innerHTML = ""

        return Points.list.map(function(item) {
            //document.getElementById("main").innerHTML = "";
            //console.log(item)
            link = "#!/" + item
            title = item.split("/")
            title = title[1]
            var paragraph = document.createElement("div")
            paragraph.innerHTML = "<a href=\"" + link + "\">" + title + "</a>"
            document.getElementById("navbar").appendChild(paragraph)
    })
}
}

var Spotify = {
	oninit: getData(developlment + "Spotify", SpotifyData),
    view: function(vnode) {
        document.getElementById("main").innerHTML = ""
        return SpotifyData.list.map(function(item) {
            createParagraph(item)
        })
    }
}

var Youtube = {
	oninit: getData(developlment + "Youtube", YoutubeData),
    view: function(vnode) {
        document.getElementById("main").innerHTML = ""
        return YoutubeData.list.map(function(item) {
            createParagraph(item)
        })
    }
}

var PDFs = {
    oninit: getData(developlment + "PDF", PDFData),
    view: function(vnode) {
        if(PDFData.list.length == 0) {
            document.getElementById("main").innerHTML = ""
            createErrorParagraph(PDFData.error.code, PDFData.error.response.detail)
        }
        else {
            document.getElementById("main").innerHTML = ""
            return PDFData.list.map(function(item) {
                createParagraph(item)
            })
        }
    }
}

var Allitems = {
    oninit: getData(developlment + "Allitems", AllitemsData),
    view: function(vnode) {
        if(AllitemsData.list.length == 0) {
            document.getElementById("main").innerHTML = ""
            createErrorParagraph(AllitemsData.error.code, AllitemsData.error.response.detail)
        }
        else {
            document.getElementById("main").innerHTML = ""
            return AllitemsData.list.map(function(item) {
                createParagraph(item)
            })
        }
    }
}

var ErrorTest = {
    oninit: getData(developlment + "PDFs", ErrorData),
    view: function(vnode) {
        //console.log(ErrorData.error.code)
        if(ErrorData.list.length == 0) {
            //console.log(ErrorData)
            document.getElementById("main").innerHTML = ""
            createErrorParagraph(ErrorData.error.code, ErrorData.error.response.detail)
        }
        else {
            document.getElementById("main").innerHTML = ""
            return ErrorData.list.map(function(item) {
                createParagraph(item)
            })
        }
    }
}

//m.route(target, "/", {
m.route(target, "/", {
    "/": Start,
    "/Youtube": Youtube ,
    "/Spotify" : Spotify,
    "/PDF": PDFs,
    "/Allitems": Allitems,
    "/ErrorTest": ErrorTest
})
 

/*
    return m("a", {href: item[1]}, item[0])
    return m("a", {href: link}, title)
    return m("button", {onclick: function() {location.assign(link)}}, title ) //Fungerar
    return m.render(document.body, m("a", {href: item[1]}, item[0]))
    return m(m.route.Link, {href: item}, title)
    return m("div", item)
*/

/* Create a list.
    var node = document.createElement("LI")
    var textnode = document.createTextNode(item[0])
    node.appendChild(textnode)
    document.getElementById("links").appendChild(node)
*/

