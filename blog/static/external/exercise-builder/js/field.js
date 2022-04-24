import { Item, Arrow } from './item.js'

class Field {
    constructor(div_id, shadow) {
        this.shadow = shadow
        this.canvas = div_id
        this.ctx = this.canvas.getContext('2d')
        this.width = this.canvas.width
        this.height = this.canvas.height
        this.items = []
        this.selected = null
        this.pending_arrow = null

        this.canvas.addEventListener('mousedown', (e) => {
            this.mouseDown(e.offsetX, e.offsetY)
        })
        this.canvas.addEventListener('mousemove', (e) => {
            this.mouseMove(e.offsetX, e.offsetY)
        })
        this.canvas.addEventListener('mouseup', (e) => {
            this.mouseUp()
        })
    }

    drawCorners(){
        this.ctx.strokeStyle = '#FFFFFF'
        this.ctx.lineWidth = 2
    
        // draw top left corner
        this.ctx.beginPath()
        this.ctx.arc(40, 15, 25, 0, 0.5 * Math.PI)
        this.ctx.stroke()
    
        //draw bottom left corner
        this.ctx.beginPath()
        this.ctx.arc(40, 485, 25, 1.5 * Math.PI, 0)
        this.ctx.stroke()
    
        // draw top right corner
        this.ctx.beginPath()
        this.ctx.arc((this.width - 40), 15, 25, 0.5 * Math.PI, Math.PI)
        this.ctx.stroke()
    
        // draw bottom right corner
        this.ctx.beginPath()
        this.ctx.arc((this.width - 40), this.height - 15, 25, 1 * Math.PI, 1.5 * Math.PI)
        this.ctx.stroke()
    
    }
    
    drawGoalzone(){
        this.ctx.strokeStyle = '#FFFFFF'
        this.ctx.lineWidth = 2
    
        this.ctx.beginPath()
        this.ctx.moveTo(40, 140)
        this.ctx.lineTo(170, 140)
        this.ctx.lineTo(170, 365)
        this.ctx.lineTo(40, 365)
        this.ctx.stroke()
    
        this.ctx.beginPath()
        this.ctx.moveTo(40, 180)
        this.ctx.lineTo(90, 180)
        this.ctx.lineTo(90, 330)
        this.ctx.lineTo(40, 330)
        this.ctx.stroke()
    
        this.ctx.beginPath()
        this.ctx.arc(170, 250, 35, 1.5 * Math.PI, 0.5 * Math.PI)
        this.ctx.stroke()
    
        this.ctx.beginPath()
        this.ctx.moveTo(this.width - 40, 140)
        this.ctx.lineTo(this.width - 40 - 130, 140)
        this.ctx.lineTo(this.width - 40 - 130, 365)
        this.ctx.lineTo(this.width - 40, 365)
        this.ctx.stroke()
    
        this.ctx.beginPath()
        this.ctx.moveTo(this.width - 40, 180)
        this.ctx.lineTo(this.width - 40 - 50, 180)
        this.ctx.lineTo(this.width - 40 - 50, 330)
        this.ctx.lineTo(this.width - 40, 330)
        this.ctx.stroke()
    
        this.ctx.beginPath()
        this.ctx.arc(this.width - 40 - 130, 250, 35, 0.5 * Math.PI, 1.5 * Math.PI)
        this.ctx.stroke()
    }
    
    render(){
        this.ctx.fillStyle = 'green'
        this.ctx.fillRect(0, 0, this.width, this.height)
    
        this.drawCorners()
        this.drawGoalzone()
    
        // draw center line
        this.ctx.beginPath()
        this.ctx.moveTo((this.width / 2), 15)
        this.ctx.lineTo((this.width / 2), (this.height - 15))
        this.ctx.stroke()
    
        // draw center circle
        this.ctx.beginPath()
        this.ctx.arc((this.width / 2), (this.height / 2), 75, 0, 2 * Math.PI)
        this.ctx.stroke()

        // draw the field delimitation
        this.ctx.rect(40, 15, this.width - 40*2, this.height -30)
        this.ctx.strokeStyle = '#FFFFFF'
        this.ctx.lineWidth = 2
        this.ctx.stroke()
    }

    download(){
        var image = this.canvas.toDataURL("image/png").replace("image/png", "image/octet-stream");
        var link = document.createElement('a')
        link.download = 'image.png'
        link.href = image
        link.click()
    }
    addItem(item){
        if (this.items.length == 0){
            item.coordinates.x = 0
            item.coordinates.y = 0
        } else {
            for (var i = 0; i < this.width - 32; i+= 32){
                var has_item = this.items.find( it => it instanceof Item && it.coordinates.x >= i && it.coordinates.x <= i + 32)
                if (has_item == undefined){
                    item.coordinates.x = i
                    item.coordinates.y = 0
                    break
                }
            }
        }
        this.items.push(item)
        item.render(this.ctx)
        this.writeItemList()
    }

    addArrow(arrow) {
        arrow.start_coordinates = null
        arrow.end_coordinates = null
        this.pending_arrow = arrow
    }

    drawArrow(arrow){
        if (arrow.start_coordinates && arrow.end_coordinates){
            arrow.draw(this.ctx)
            this.items.push(arrow)
            this.pending_arrow = null
        }
    }

    removeItem(item_id){
        let item_by_id = this.items.find(it => it.id === item_id)
        this.items.splice(this.items.indexOf(item_by_id), 1)
        this.render()
        for (var i=0 ; i < this.items.length; i++){
            this.items[i].draw(this.ctx)
        }
        this.writeItemList()
    }
    
    writeItemList(){
        let div = this.shadow.querySelector('#eb__canvas-items')
        div.innerHTML = ''
        for (let i = 0; i < this.items.length; i++) {
            let item_div = document.createElement('div')
            item_div.classList.add('item')
            if (this.selected != null
                && this.items[i] instanceof Item
                && this.selected.coordinates.x == this.items[i].coordinates.x
                && this.selected.coordinates.y == this.items[i].coordinates.y){
                    item_div.classList.add('selected')
            }
            item_div.innerHTML = this.items[i].asHtml()
            item_div.addEventListener('click', (e) => {
                this.removeItem(this.items[i].id)
            })
            div.appendChild(item_div)
        }
    }
    mouseDown(mouseX, mouseY){
        console.log(mouseX, mouseY)

        let item_clicked = this.items.find(item => {
            return item instanceof Item
                && mouseX >= item.coordinates.x
                && mouseX <= item.coordinates.x + item.image.width
                && mouseY >= item.coordinates.y
                && mouseY <= item.coordinates.y + item.image.height
        })
        let arrow_clicked = this.items.find(item => {
            return item instanceof Arrow && item.isInside(mouseX, mouseY)
        })
        console.log(arrow_clicked)
        if (item_clicked || arrow_clicked){
            this.selected = item_clicked || arrow_clicked
        } else {
            this.selected = null
        }
        // this.selected = item_clicked ? item_clicked : null
        if (this.selected != null){
            this.selected.draggable = true
        } else if (this.pending_arrow != null){
            if(this.pending_arrow.start_coordinates == null){
                this.pending_arrow.start_coordinates = {
                    x: mouseX,
                    y: mouseY
                }
            } else {
                this.pending_arrow.end_coordinates = {
                    x: mouseX,
                    y: mouseY
                }
                this.drawArrow(this.pending_arrow)
            }
        }
        this.writeItemList()
    }
    mouseMove(mouseX, mouseY){
        if (this.selected != null){
            if (this.selected.draggable == true){
                this.render()
                this.selected.move(mouseX, mouseY)
                this.selected.draw(this.ctx)
                for (var i=0 ; i < this.items.length; i++){
                    this.items[i].draw(this.ctx)
                    // if (this.items[i] instanceof Arrow) {
                    //     this.items[i].draw(this.ctx)
                    // }
                    // else if (this.items[i] instanceof Item) {
                    //     this.items[i].draw(this.ctx)
                    // }
                }
            }
        }
    }
    mouseUp(){
        if (this.selected != null){
            this.selected.draggable = false
        }
        this.writeItemList()
    }
}

export { Field }