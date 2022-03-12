var field = new Field('canvas')
field.render()

function download(){
    field.download()
}

function addItemToField(name){
    let item = null
    switch (name){
        case 'ball':
            item = new Item('ball_32.png', 'Ball', {x: 0, y: 0})
            break
        case  'plot':
            item = new Item('plot_32.png', 'Plot', {x: 0, y: 0})
            break
        case 'player':
            item = new Item('player_32.png', 'Player', {x: 0, y: 0})
            break
    }
    field.addItem(item)
}

field.canvas.onmousedown = function(e){
    var mouseX = e.pageX - this.offsetLeft
    var mouseY = e.pageY - this.offsetTop
    field.mouseDown(mouseX, mouseY)
}

field.canvas.onmousemove = function(e){
    var mouseX = e.pageX - this.offsetLeft
    var mouseY = e.pageY - this.offsetTop
    field.mouseMove(mouseX, mouseY)
}

field.canvas.onmouseup = function(e){
    field.mouseUp()
}

function deleteItem(item){
    field.removeItem(item)
}