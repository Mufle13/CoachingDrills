class Item {
    constructor(name, label, coordinates) {
        // generate unique id based on date and time
        this.id = '_' + Math.random().toString(36).substr(2, 9);
        this.name = name
        this.label = label
        this.coordinates = coordinates
        this.draggable = false
        this.selected = null
    }

    render(ctx) {
        let image = new Image()
        image.src = base_asset_url + this.name
        image.onload = () => {
            this.image = image
            ctx.drawImage(this.image, this.coordinates.x, this.coordinates.y)
        }
    }

    draw(ctx) {
        ctx.drawImage(this.image, this.coordinates.x, this.coordinates.y)
    }

    move(mouseX, mouseY) {
        this.coordinates.x = mouseX - this.image.width / 2
        this.coordinates.y = mouseY - this.image.height / 2
    }

    asJson() {
        let data = {
            label: this.label,
            x: this.coordinates.x,
            y: this.coordinates.y,
        }
        return JSON.stringify(data)
    }

    asHtml(){
        return `
            <span class="item-name">${this.label}</span>
            <span class="item-coordinates">x: ${this.coordinates.x}, y:${this.coordinates.y}</span>
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
            </svg>
        `
    }
}

class Arrow {
    constructor(name, color, start_coordinates, end_coordinates) {
        this.id = '_' + Math.random().toString(36).substr(2, 9);
        this.name = name
        this.color = color
        this.start_coordinates = start_coordinates
        this.end_coordinates = end_coordinates
        this.draggable = false
        this.selected = null
        this.width = 2
    }

    asHtml(){
        return `
            <span class="item-name">${this.name}</span>
            <span class="item-coordinates">x: ${this.start_coordinates.x}, y:${this.start_coordinates.y}</span>
            <span class="item-coordinates">x: ${this.end_coordinates.x}, y:${this.end_coordinates.y}</span>
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
            </svg>
        `
    }

    isInside(mouseX, mouseY) {
        let x_direction = this.start_coordinates.x < this.end_coordinates.x ? 'right' : 'left'
        let y_direction = this.start_coordinates.y < this.end_coordinates.y ? 'down' : 'up'
        if (x_direction == 'right') {
            if (mouseX > this.start_coordinates.x && mouseX < this.end_coordinates.x) {
                if (y_direction == 'down') {
                    if (mouseY > this.start_coordinates.y && mouseY < this.end_coordinates.y) {
                        return true
                    }
                } else {
                    if (mouseY < this.start_coordinates.y && mouseY > this.end_coordinates.y) {
                        return true
                    }
                }
            }
        } else {
            if (mouseX < this.start_coordinates.x && mouseX > this.end_coordinates.x) {
                if (y_direction == 'down') {
                    if (mouseY > this.start_coordinates.y && mouseY < this.end_coordinates.y) {
                        return true
                    }
                } else {
                    if (mouseY < this.start_coordinates.y && mouseY > this.end_coordinates.y) {
                        return true
                    }
                }
            }
        }
    }

    move(mouseX, mouseY) {
        this.start_coordinates.x = mouseX
        this.start_coordinates.y = mouseY
    }

    draw(ctx) {
        let headlen = 10
        let lineWidth = 5;
        let fromx = this.start_coordinates.x
        let tox = this.end_coordinates.x
        let fromy = this.start_coordinates.y
        let toy = this.end_coordinates.y
        let angle = Math.atan2(toy - fromy, tox - fromx);

        ctx.lineWidth = this.width;
        ctx.lineCap = "round";
        ctx.strokeStyle = this.color
        
        ctx.beginPath()
        // ctx.translate(0.5,0.5);
        ctx.moveTo(fromx, fromy)
        ctx.lineTo(tox, toy)
        ctx.stroke()
        ctx.lineWidth = 1;

        //starting a new path from the head of the arrow to one of the sides of
        //the point
        ctx.lineWidth = lineWidth;
        ctx.beginPath();
        ctx.moveTo(tox, toy);
        ctx.lineTo(tox-headlen*Math.cos(angle-Math.PI/7),
                toy-headlen*Math.sin(angle-Math.PI/7));
    
        //path from the side point of the arrow, to the other side point
        ctx.lineTo(tox-headlen*Math.cos(angle+Math.PI/7),
                        toy-headlen*Math.sin(angle+Math.PI/7));
    
        //path from the side point back to the tip of the arrow, and then
        //again to the opposite side point
        ctx.lineTo(tox, toy);
        ctx.lineTo(tox-headlen*Math.cos(angle-Math.PI/7),
                toy-headlen*Math.sin(angle-Math.PI/7));
    
        //draws the paths created above
        ctx.stroke();
    }
}

export { Item, Arrow }