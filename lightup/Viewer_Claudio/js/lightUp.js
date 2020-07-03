class Board {
    constructor(s) {
        this.selector = s;
        this.board = [];
        this.validContent = ['.', '*', '0', '1', '2', '3', '4', 'W', 'B'];
    }

    adjacentBulbs(r, c) {
        let self = this;
        let n = 0;
        if (r > 0 && self.board[r-1][c].content == 'B') n++;
        if (r < self.height-1 && self.board[r+1][c].content == 'B') n++;
        if (c > 0 && self.board[r][c-1].content == 'B') n++;
        if (c < self.width-1 && self.board[r][c+1].content == 'B') n++;
        return n;
    }

    adjacentUnknowns(r, c) {
        let self = this;
        let n = 0;
        if (r > 0 && self.isUnknown(r-1, c)) n++;
        if (r < self.height-1 && self.isUnknown(r+1, c)) n++;
        if (c > 0 && self.isUnknown(r, c-1)) n++;
        if (c < self.width-1 && self.isUnknown(r, c+1)) n++;
        return n;
    }

    allLitUp() {
        let self = this;
        for (let r = 0; r < self.height; r++) {
            for (let c = 0; c < self.width; c++) {
                let cell = self.board[r][c];
                if ((cell.content == '.' || cell.content =='*') && cell.dark) {
                    return false;
                }
            }
        }
        return true;
    }

    create(w, h) {
        let self = this;

        self.width = w;
        self.height = h;
        self.board = [];

        for (let i = 0; i < self.height; i++) {
            self.board[i] = [];
            for (let j = 0; j < self.width; j++) {
                self.board[i][j] = {
                    content: '.',
                    dark: true,
                    error: false
                };
            }
        }
    }

    draw(reset) {
        let self = this;

        if (reset) $(self.selector).empty().append('<table class="lightUpBoard"><tbody></tbody></table>');
        let $board = $('tbody', self.selector);
        let tdClass = '';

        self.board.forEach(function(row, r) {
            let $tr;
            if (reset) $tr = $(`<tr><th>${r}</th></tr>`);
            row.forEach(function(cell, c) {
                let $td, content;
                if (reset) $td = $(`<td id="cell-${r}-${c}" />`);
                else $td = $(`#cell-${r}-${c}`);
                if (cell.content == '0' || cell.content == '1' || cell.content == '2' || cell.content == '3' || cell.content == '4') {
                    tdClass = 'wall';
                    content = cell.content;
                } else if (cell.content == 'W') {
                    tdClass = 'wall';
                    content = '';
                } else if (cell.content == 'B') {
                    tdClass = 'bulb';
                    content = '<i class="fas fa-lightbulb"></i>';
                } else if (cell.content == '*') {
                    tdClass = 'text-muted';
                    content = '&bullet;';
                } else if (cell.content == '.') {
                    tdClass = '';
                    content = '';
                } else {
                    tdClass = '';
                    content = cell.content;;
                }
                $td.addClass(tdClass).html(content);
                if (!cell.dark) $td.addClass('light');
                if (cell.error) {
                    $td.addClass('error');
                    if ($td.html() == '') $td.text('E');
                }
                if (reset) $tr.append($td);
            })
            if (reset) {
                $tr.append(`<th>${r}</th>`);
                $board.append($tr);
            }
        })
        if (reset) {
            let $tr;
            $tr = $(`<tr><th></th></tr>`);
            for (let c = 0; c < self.width; c++)
                $tr.append(`<th>${c}</th>`);
            $tr.append(`<th></th>`);
            $board.prepend($tr.html()).append($tr.html());
        }
    }

    error(r, c, verbose, message) {
        message = message || '';
        this.board[r][c].error = true;
        if (verbose) console.error(`Error at ${r} ${c} ${message}`);
    }

    exportASC() {
        let self = this;
        let s = '';

        for (let i = 0; i < self.height; i++) {
            for (let j = 0; j < self.width; j++) {
                if (self.board[i][j].content == '*') s += '.';
                else s += self.board[i][j].content;
            }
            s += '\n';
        }
        return s;
    }

    importASC(s) {
        let self = this;
        let row;

        self.board = [];
        s.split('\n').forEach(function(row, r) {
            row = row.trim();
            if (row.length > 0 ) {
                self.board[r] = [];
                row.split('').forEach(function(content, c) {
                    self.board[r][c] = {
                        content: content,
                        dark: true,
                        error: false
                    };
                    if ($.inArray(content, self.validContent) == -1) self.error(r, c, true, `Invalid content "${content}"`);
                });
            }
        });
        self.height = self.board.length;
        self.width = self.board[0].length;
        // light ways
        self.board.forEach(function(row, r) {
            row.forEach(function(cell, c) {
                if (cell.content == 'B') self.lightUpWay(r, c);
            })
        })
    }

    isUnknown(r, c) {
        return (this.board[r][c].content == '.' && this.board[r][c].dark);
    }

    isWall(r, c) {
        let content = this.board[r][c].content;
        return (content == 'W' || content == '0' || content == '1' || content == '2' || content == '3' || content == '4');
    }

    lightUpWay(r, c) {
        let self = this;
        let i, j;
        let cell;

        // light up
        i = r - 1; j = c;
        while (i >= 0 && !self.isWall(i, j)) {
            self.board[i][j].dark = false;
            i--;
        }
        // light down
        i = r + 1; j = c;
        while (i < self.height && !self.isWall(i, j)) {
            self.board[i][j].dark = false;
            i++;
        }
        // light left
        i = r; j = c - 1;
        while (j >= 0 && !self.isWall(i, j)) {
            self.board[i][j].dark = false;
            j--;
        }
        // light right
        i = r; j = c + 1;
        while (j < self.width && !self.isWall(i, j)) {
            self.board[i][j].dark = false;
            j++;
        }
    }

    valid(verbose) {
        let self = this;
        let errors = 0;
        self.board.forEach(function(row, r) {
            row.forEach(function(cell, c) {
                let content = cell.content * 1;
                if (cell.error) errors++;
                else if (!isNaN(content)) {
                    // Celulas com numero versus lampadas adjacentes
                    let bAdjacent = self.adjacentBulbs(r, c);
                    let uAdjacent = self.adjacentUnknowns(r, c);
                    if (content - bAdjacent > uAdjacent) {
                        self.error(r, c, verbose, "Can't set all bulbs required!");
                        errors++;
                    } else if (bAdjacent > content) {
                        self.error(r, c, verbose, "More Bulbs than allowed!");
                        errors++;
                    }
                } else if (cell.content == 'B' && !cell.dark) {
                    // Duas lampadas se iluminando
                    self.error(r, c, verbose, "I am a bulb and there's another bulb lighting me!");
                    errors++;
                }
            })
        })
        return (errors == 0);
    }

}
