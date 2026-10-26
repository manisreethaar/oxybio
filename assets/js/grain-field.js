// Grain field: a canvas of small grain-shaped particles that move between target shapes.
// A field holds several named shape sets; `progress` (0..n-1) blends between consecutive sets,
// so scroll position can drive the morph. The cursor gently pushes grains aside.
(function () {
    var PALETTE = ['#DCE6F1', '#C2D3EA', '#A9C0E3', '#7F9DD0', '#4F74BF'];

    function rand(a, b) {
        return a + Math.random() * (b - a);
    }

    function GrainField(canvas, options) {
        this.palette = (options && options.palette) || PALETTE;
        this.canvas = canvas;
        this.ctx = canvas.getContext('2d');
        this.options = options || {};
        this.shapes = [];
        this.progress = 0;
        this.mouse = { x: -9999, y: -9999 };
        this.running = false;
        this.visible = true;
        this.time = 0;
        this.particles = [];
        this.resize();
        this.bind();
    }

    GrainField.prototype.count = function () {
        var area = this.width * this.height;
        var density = this.options.density || 0.0021;
        var max = this.options.max || 2600;
        return Math.max(500, Math.min(max, Math.round(area * density)));
    };

    GrainField.prototype.resize = function () {
        var rect = this.canvas.getBoundingClientRect();
        var dpr = Math.min(window.devicePixelRatio || 1, 2);
        this.width = rect.width;
        this.height = rect.height;
        this.canvas.width = Math.round(rect.width * dpr);
        this.canvas.height = Math.round(rect.height * dpr);
        this.ctx.setTransform(dpr, 0, 0, dpr, 0, 0);

        var n = this.count();
        while (this.particles.length < n) {
            this.particles.push({
                x: rand(0, this.width),
                y: rand(0, this.height),
                vx: 0,
                vy: 0,
                size: rand(1.1, 2.6),
                rot: rand(0, Math.PI),
                spin: rand(-0.01, 0.01),
                phase: rand(0, Math.PI * 2),
                color: Math.floor(Math.random() * this.palette.length),
                alpha: rand(0.45, 0.95)
            });
        }
        this.particles.length = n;
        if (this.shapeBuilders) this.buildShapes();
    };

    // Each builder returns an array of {x, y} for n particles at the current size.
    GrainField.prototype.setShapes = function (builders) {
        this.shapeBuilders = builders;
        this.buildShapes();
    };

    GrainField.prototype.buildShapes = function () {
        var self = this;
        var n = this.particles.length;
        this.shapes = this.shapeBuilders.map(function (build) {
            return build(n, self.width, self.height);
        });
    };

    GrainField.prototype.bind = function () {
        var self = this;
        var host = this.options.pointerTarget || this.canvas;
        host.addEventListener('pointermove', function (e) {
            var r = self.canvas.getBoundingClientRect();
            self.mouse.x = e.clientX - r.left;
            self.mouse.y = e.clientY - r.top;
        });
        host.addEventListener('pointerleave', function () {
            self.mouse.x = -9999;
            self.mouse.y = -9999;
        });
        var resizeTimer;
        window.addEventListener('resize', function () {
            clearTimeout(resizeTimer);
            resizeTimer = setTimeout(function () {
                self.resize();
                if (!self.running) self.draw();
            }, 150);
        });
        if ('IntersectionObserver' in window) {
            new IntersectionObserver(function (entries) {
                self.visible = entries[0].isIntersecting;
                if (self.visible && self.running) self.loop();
            }).observe(this.canvas);
        }
    };

    GrainField.prototype.targetFor = function (i) {
        var shapes = this.shapes;
        if (!shapes.length) return null;
        var p = Math.max(0, Math.min(shapes.length - 1, this.progress));
        var a = Math.floor(p);
        var b = Math.min(shapes.length - 1, a + 1);
        var t = p - a;
        // Ease each particle's switch a little differently so morphs ripple rather than snap.
        var pi = this.particles[i];
        var local = Math.max(0, Math.min(1, (t - (pi.phase / (Math.PI * 2)) * 0.35) / 0.65));
        local = local * local * (3 - 2 * local);
        var pa = shapes[a][i], pb = shapes[b][i];
        return { x: pa.x + (pb.x - pa.x) * local, y: pa.y + (pb.y - pa.y) * local };
    };

    GrainField.prototype.step = function () {
        this.time += 0.016;
        var mx = this.mouse.x, my = this.mouse.y;
        var radius = this.options.pushRadius || 110;
        var r2 = radius * radius;
        for (var i = 0; i < this.particles.length; i++) {
            var p = this.particles[i];
            var tgt = this.targetFor(i);
            if (tgt) {
                var bx = Math.sin(this.time * 0.9 + p.phase) * 1.6;
                var by = Math.cos(this.time * 0.7 + p.phase) * 1.6;
                p.vx += (tgt.x + bx - p.x) * 0.045;
                p.vy += (tgt.y + by - p.y) * 0.045;
            }
            var dx = p.x - mx, dy = p.y - my, d2 = dx * dx + dy * dy;
            if (d2 < r2 && d2 > 0.01) {
                var f = (1 - d2 / r2) * 2.4;
                var d = Math.sqrt(d2);
                p.vx += (dx / d) * f;
                p.vy += (dy / d) * f;
            }
            p.vx *= 0.82;
            p.vy *= 0.82;
            p.x += p.vx;
            p.y += p.vy;
            p.rot += p.spin + p.vx * 0.02;
        }
    };

    GrainField.prototype.draw = function () {
        var ctx = this.ctx;
        ctx.clearRect(0, 0, this.width, this.height);
        for (var c = 0; c < this.palette.length; c++) {
            ctx.fillStyle = this.palette[c];
            for (var pass = 0; pass < 2; pass++) {
                ctx.globalAlpha = pass ? 0.9 : 0.55;
                ctx.beginPath();
                for (var i = 0; i < this.particles.length; i++) {
                    var p = this.particles[i];
                    if (p.color !== c || (p.alpha > 0.7) !== !!pass) continue;
                    ctx.moveTo(p.x + p.size * 1.7, p.y);
                    ctx.ellipse(p.x, p.y, p.size * 1.7, p.size, p.rot, 0, Math.PI * 2);
                }
                ctx.fill();
            }
        }
        ctx.globalAlpha = 1;
    };

    GrainField.prototype.loop = function () {
        var self = this;
        if (this.frame) return;
        function tick() {
            self.frame = null;
            if (!self.running || !self.visible) return;
            self.step();
            self.draw();
            self.frame = requestAnimationFrame(tick);
        }
        this.frame = requestAnimationFrame(tick);
    };

    GrainField.prototype.start = function () {
        this.running = true;
        this.loop();
    };

    // Static render for reduced motion: place every grain on its target and draw once.
    GrainField.prototype.still = function () {
        for (var i = 0; i < this.particles.length; i++) {
            var t = this.targetFor(i);
            if (t) {
                this.particles[i].x = t.x;
                this.particles[i].y = t.y;
            }
        }
        this.draw();
    };

    // Shape builders --------------------------------------------------------

    var Shapes = {
        // The O2 mark: a thick open ring with a column of short dashes in its opening.
        // Pass ratios, or a function (w, h) => {cx, cy, R} to anchor the ring to page layout.
        ring: function (cxRatio, cyRatio, rRatio) {
            return function (n, w, h) {
                var geo = typeof cxRatio === 'function' ? cxRatio(w, h) : {
                    cx: w * cxRatio, cy: h * cyRatio, R: Math.min(w, h) * rRatio
                };
                var cx = geo.cx, cy = geo.cy, R = geo.R;
                var pts = [];
                var dashN = Math.round(n * 0.22);
                for (var i = 0; i < n - dashN; i++) {
                    var a = rand(Math.PI * 0.32, Math.PI * 1.86);
                    var rr = R * (0.7 + Math.sqrt(Math.random()) * 0.3);
                    pts.push({ x: cx + Math.cos(a) * rr, y: cy - Math.sin(a) * rr });
                }
                var rows = [R * 0.78, R * 0.95];
                var segs = [[-0.30, -0.17], [-0.10, 0.03], [0.10, 0.23], [0.30, 0.42]];
                for (var j = 0; j < dashN; j++) {
                    var row = rows[j % 2];
                    var s = segs[Math.floor(Math.random() * segs.length)];
                    var ang = Math.PI * rand(s[0], s[1]);
                    var rad = row + rand(-R * 0.04, R * 0.04);
                    pts.push({ x: cx + Math.cos(ang) * rad, y: cy - Math.sin(ang) * rad });
                }
                return pts;
            };
        },
        // Loose grains spread across the whole area.
        field: function () {
            return function (n, w, h) {
                var pts = [];
                for (var i = 0; i < n; i++) pts.push({ x: rand(-20, w + 20), y: rand(-20, h + 20) });
                return pts;
            };
        },
        // Grains drifting down past the bottom edge, used as the hero scrolls away.
        fall: function () {
            return function (n, w, h) {
                var pts = [];
                for (var i = 0; i < n; i++) pts.push({ x: rand(0, w), y: h + rand(20, h * 0.8) });
                return pts;
            };
        },
        // One dense disc: the base.
        disc: function (cxRatio, cyRatio, rRatio) {
            return function (n, w, h) {
                var cx = w * cxRatio, cy = h * cyRatio, R = Math.min(w, h) * rRatio;
                var pts = [];
                for (var i = 0; i < n; i++) {
                    var a = rand(0, Math.PI * 2), rr = R * Math.sqrt(Math.random());
                    pts.push({ x: cx + Math.cos(a) * rr, y: cy + Math.sin(a) * rr });
                }
                return pts;
            };
        },
        // Two rounded vessels side by side: the two formats.
        pair: function (gapRatio, cyRatio, sizeRatio) {
            return function (n, w, h) {
                var s = Math.min(w, h) * sizeRatio;
                var cy = h * cyRatio;
                var centers = [w / 2 - w * gapRatio, w / 2 + w * gapRatio];
                var pts = [];
                for (var i = 0; i < n; i++) {
                    var cx = centers[i % 2];
                    var bw = s * 0.62, bh = s;
                    var x = rand(-bw, bw), y = rand(-bh, bh);
                    var corner = bw * 0.55;
                    var ex = Math.max(0, Math.abs(x) - (bw - corner)), ey = Math.max(0, Math.abs(y) - (bh - corner));
                    if (ex * ex + ey * ey > corner * corner) {
                        x *= 0.8;
                        y *= 0.8;
                    }
                    pts.push({ x: cx + x, y: cy + y });
                }
                return pts;
            };
        }
    };

    // Grains that spell out a short piece of text, sampled from an offscreen render.
    Shapes.text = function (text, fontFamily) {
        return function (n, w, h) {
            var off = document.createElement('canvas');
            off.width = Math.max(1, Math.round(w));
            off.height = Math.max(1, Math.round(h));
            var c = off.getContext('2d');
            var size = h * 0.78;
            c.font = '600 ' + size + 'px ' + fontFamily;
            while (c.measureText(text).width > w * 0.9 && size > 10) {
                size *= 0.92;
                c.font = '600 ' + size + 'px ' + fontFamily;
            }
            c.textAlign = 'center';
            c.textBaseline = 'middle';
            c.fillStyle = '#000';
            c.fillText(text, w / 2, h / 2 + size * 0.04);
            var data = c.getImageData(0, 0, off.width, off.height).data;
            var hits = [];
            var step = Math.max(2, Math.round(size / 60));
            for (var y = 0; y < off.height; y += step) {
                for (var x = 0; x < off.width; x += step) {
                    if (data[(y * off.width + x) * 4 + 3] > 128) hits.push({ x: x, y: y });
                }
            }
            var pts = [];
            for (var i = 0; i < n; i++) {
                var p = hits.length ? hits[Math.floor(Math.random() * hits.length)] : { x: w / 2, y: h / 2 };
                pts.push({ x: p.x + rand(-step, step) * 0.6, y: p.y + rand(-step, step) * 0.6 });
            }
            return pts;
        };
    };

    window.GrainField = GrainField;
    window.GrainShapes = Shapes;
})();
