#!/usr/bin/env python3
"""Generate true-pixel banner, divider, and icons. Nearest-neighbor scale only."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
ICONS = ASSETS / "icons"
PROFILE_ASSETS = ROOT / "profile" / "assets"
PROFILE_ICONS = PROFILE_ASSETS / "icons"

INK = (13, 13, 16, 255)
CREAM = (232, 224, 208, 255)
GOLD = (196, 165, 116, 255)
SLATE = (61, 74, 92, 255)
DIM = (36, 38, 44, 255)
CLEAR = (0, 0, 0, 0)

PALETTE = {
    ".": CLEAR,
    "k": INK,
    "c": CREAM,
    "g": GOLD,
    "s": SLATE,
    "d": DIM,
}

# 5x7 caps for the banner
FONT_5X7 = {
    "A": ["01110", "10001", "10001", "11111", "10001", "10001", "10001"],
    "B": ["11110", "10001", "10001", "11110", "10001", "10001", "11110"],
    "C": ["01110", "10001", "10000", "10000", "10000", "10001", "01110"],
    "D": ["11110", "10001", "10001", "10001", "10001", "10001", "11110"],
    "E": ["11111", "10000", "10000", "11110", "10000", "10000", "11111"],
    "F": ["11111", "10000", "10000", "11110", "10000", "10000", "10000"],
    "G": ["01110", "10001", "10000", "10111", "10001", "10001", "01110"],
    "H": ["10001", "10001", "10001", "11111", "10001", "10001", "10001"],
    "I": ["11111", "00100", "00100", "00100", "00100", "00100", "11111"],
    "K": ["10001", "10010", "10100", "11000", "10100", "10010", "10001"],
    "L": ["10000", "10000", "10000", "10000", "10000", "10000", "11111"],
    "M": ["10001", "11011", "10101", "10101", "10001", "10001", "10001"],
    "N": ["10001", "11001", "10101", "10011", "10001", "10001", "10001"],
    "O": ["01110", "10001", "10001", "10001", "10001", "10001", "01110"],
    "P": ["11110", "10001", "10001", "11110", "10000", "10000", "10000"],
    "R": ["11110", "10001", "10001", "11110", "10100", "10010", "10001"],
    "S": ["01111", "10000", "10000", "01110", "00001", "00001", "11110"],
    "T": ["11111", "00100", "00100", "00100", "00100", "00100", "00100"],
    "U": ["10001", "10001", "10001", "10001", "10001", "10001", "01110"],
    "W": ["10001", "10001", "10001", "10101", "10101", "10101", "01010"],
    "Y": ["10001", "10001", "01010", "00100", "00100", "00100", "00100"],
    " ": ["00000", "00000", "00000", "00000", "00000", "00000", "00000"],
    "&": ["01000", "10100", "01000", "01101", "10010", "10010", "01101"],
    "-": ["00000", "00000", "00000", "11111", "00000", "00000", "00000"],
    "/": ["00001", "00010", "00100", "01000", "10000", "00000", "00000"],
    "V": ["10001", "10001", "10001", "10001", "10001", "01010", "00100"],
    ".": ["00000", "00000", "00000", "00000", "00000", "01100", "01100"],
}


def new_canvas(w, h, color=INK):
    return Image.new("RGBA", (w, h), color)


def px(img, x, y, color):
    if 0 <= x < img.width and 0 <= y < img.height:
        img.putpixel((x, y), color)


def blit_glyph(img, ch, x, y, color, scale=1):
    rows = FONT_5X7.get(ch, FONT_5X7[" "])
    for j, row in enumerate(rows):
        for i, bit in enumerate(row):
            if bit == "1":
                for dy in range(scale):
                    for dx in range(scale):
                        px(img, x + i * scale + dx, y + j * scale + dy, color)


def blit_text(img, text, x, y, color, scale=1, tracking=1):
    cursor = x
    for ch in text:
        blit_glyph(img, ch, cursor, y, color, scale)
        cursor += 5 * scale + tracking
    return cursor


def text_width(text, scale=1, tracking=1):
    if not text:
        return 0
    return len(text) * 5 * scale + (len(text) - 1) * tracking


def scale_nn(img, factor):
    return img.resize((img.width * factor, img.height * factor), Image.NEAREST)


def parse_sprite(rows, mapping=None):
    mapping = mapping or PALETTE
    h = len(rows)
    w = max(len(r) for r in rows)
    img = Image.new("RGBA", (w, h), CLEAR)
    for y, row in enumerate(rows):
        for x, ch in enumerate(row):
            img.putpixel((x, y), mapping.get(ch, CLEAR))
    return img


def paste(dst, src, x, y):
    dst.alpha_composite(src, (x, y))


# --- icons: 16x16 cream-on-clear, then framed ---

ICONS_16 = {
    "mail": [
        "................",
        "................",
        ".cccccccccccccc.",
        ".c............c.",
        ".cc..........cc.",
        ".c.c........c.c.",
        ".c..c......c..c.",
        ".c...c....c...c.",
        ".c....cccc....c.",
        ".c............c.",
        ".c............c.",
        ".c............c.",
        ".cccccccccccccc.",
        "................",
        "................",
        "................",
    ],
    "github": [
        "................",
        ".....cccccc.....",
        "...cc......cc...",
        "..c..c....c..c..",
        ".c............c.",
        ".c............c.",
        ".c.....cc.....c.",
        ".cc..........cc.",
        "..c..c....c..c..",
        "..c..........c..",
        "...c........c...",
        "....c......c....",
        ".....c....c.....",
        ".....c....c.....",
        "....cc....cc....",
        "................",
    ],
    "about": [
        "................",
        "......cccc......",
        ".....c....c.....",
        ".....c....c.....",
        "......cccc......",
        "................",
        "....cccccccc....",
        "...c........c...",
        "..c..........c..",
        "..c..........c..",
        ".c............c.",
        ".c............c.",
        ".cccccccccccccc.",
        "................",
        "................",
        "................",
    ],
    "now": [
        "................",
        "................",
        "........c.......",
        ".......ccc......",
        "......c.c.c.....",
        ".....c..c..c....",
        "....c...c...c...",
        "...c....c....c..",
        "....c...c...c...",
        ".....c..c..c....",
        "......c.c.c.....",
        ".......ccc......",
        "........c.......",
        "................",
        "................",
        "................",
    ],
    "news": [
        "................",
        "..ccc......ccc..",
        "..c.c......c.c..",
        ".cccccccccccccc.",
        ".c............c.",
        ".c..cccccc....c.",
        ".c............c.",
        ".c..cccccccc..c.",
        ".c............c.",
        ".c..cccccccc..c.",
        ".c............c.",
        ".c..cccc......c.",
        ".c............c.",
        ".cccccccccccccc.",
        "................",
        "................",
    ],
    "robot": [
        "................",
        "......c..c......",
        ".......cc.......",
        "....cccccccc....",
        "...c........c...",
        "...c..c..c..c...",
        "...c........c...",
        "...c..cccc..c...",
        "....c......c....",
        ".c..cccccccc..c.",
        ".c.c........c.c.",
        "..c..........c..",
        "..c...c..c...c..",
        "..c...c..c...c..",
        "..c...c..c...c..",
        "................",
    ],
    "research": [
        "................",
        "..ccccccccccc...",
        "..c.........c...",
        "..c.ccccccc.c...",
        "..c.c.....c.c...",
        "..c.c.....c.c...",
        "..c.c.....c.c...",
        "..c.ccccccc.c...",
        "..c.........c...",
        "..c.........c...",
        "...c.......c....",
        "....c.....c.....",
        ".....c...c......",
        "......ccc.......",
        "................",
        "................",
    ],
    "linkedin": [
        "................",
        ".cccccccccccccc.",
        ".c............c.",
        ".c..ccc.......c.",
        ".c...c........c.",
        ".c...c..cccc..c.",
        ".c...c.c...c..c.",
        ".c...c.c...c..c.",
        ".c...c.c...c..c.",
        ".c...c.c...c..c.",
        ".c............c.",
        ".cccccccccccccc.",
        "................",
        "................",
        "................",
        "................",
    ],
}


def make_icon_tile(name, scale=3):
    rows = ICONS_16[name]
    if len(rows) != 16 or any(len(r) != 16 for r in rows):
        raise ValueError(f"{name} must be 16x16, got {[len(r) for r in rows]}")
    sprite = parse_sprite(rows, {".": CLEAR, "c": CREAM})
    tile = new_canvas(20, 20, INK)
    for x in range(20):
        px(tile, x, 0, SLATE)
        px(tile, x, 19, SLATE)
        px(tile, 0, x, SLATE)
        px(tile, 19, x, SLATE)
    paste(tile, sprite, 2, 2)
    return scale_nn(tile, scale)


def make_plain_icon(name, scale=2):
    rows = ICONS_16[name]
    sprite = parse_sprite(rows, {".": CLEAR, "c": CREAM})
    return scale_nn(sprite, scale)


def make_banner(w=256, h=80):
    img = new_canvas(w, h, INK)

    for x in range(w):
        px(img, x, 0, GOLD)
        px(img, x, 1, SLATE)
        px(img, x, h - 2, SLATE)
        px(img, x, h - 1, GOLD)
    for y in range(h):
        px(img, 0, y, GOLD)
        px(img, 1, y, SLATE)
        px(img, w - 2, y, SLATE)
        px(img, w - 1, y, GOLD)

    for x in range(4, w - 4, 8):
        for y in range(4, h - 4, 8):
            px(img, x, y, DIM)

    robot = parse_sprite(
        [
            "....c..c....",
            ".....cc.....",
            "..cccccccc..",
            ".c........c.",
            ".c..c..c..c.",
            ".c........c.",
            ".c..cccc..c.",
            "..c......c..",
            "c.cccccccc.c",
            "c.c......c.c",
            ".c........c.",
            ".c...cc...c.",
            ".c..c..c..c.",
            ".c..c..c..c.",
            ".c..c..c..c.",
            "............",
        ],
        {".": CLEAR, "c": CREAM},
    )
    paste(img, robot, 12, h // 2 - 10)

    title = "YUKUN WANG"
    tw = text_width(title, scale=2, tracking=2)
    tx = (w - tw) // 2 + 10
    blit_text(img, title, tx, 12, CREAM, scale=2, tracking=2)

    school = "UCL MENG ROBOTICS & AI"
    sw = text_width(school, scale=1, tracking=1)
    sx = (w - sw) // 2 + 10
    for x in range(sx - 4, sx + sw + 4):
        px(img, x, 32, SLATE)
    blit_text(img, school, sx, 36, GOLD, scale=1, tracking=1)

    roles = "ROBOT LEARNING / EMBODIED AI"
    rw = text_width(roles, scale=1, tracking=1)
    rx = (w - rw) // 2 + 10
    blit_text(img, roles, rx, 50, CREAM, scale=1, tracking=1)

    return scale_nn(img, 5)


# macOS ships one true 16 px bitmap CJK font; render it without antialiasing.
CJK_FONT = "/System/Library/Fonts/Supplemental/NISC18030.ttf"
CJK_SIZE = 16


def cjk_mask(text, bold=False):
    font = ImageFont.truetype(CJK_FONT, CJK_SIZE)
    mask = Image.new("L", (CJK_SIZE * len(text) + 2, CJK_SIZE + 2), 0)
    draw = ImageDraw.Draw(mask)
    draw.fontmode = "1"
    draw.text((0, 0), text, fill=255, font=font)
    if bold:
        draw.text((1, 0), text, fill=255, font=font)
    return mask.crop(mask.getbbox())


def blit_mask(img, mask, x, y, color):
    for j in range(mask.height):
        for i in range(mask.width):
            if mask.getpixel((i, j)):
                px(img, x + i, y + j, color)


def blit_mixed(img, parts, x, y, line_h=CJK_SIZE):
    """Draw (text, color, is_cjk) parts on one baseline-centred line; returns end x."""
    cursor = x
    for text, color, is_cjk in parts:
        if is_cjk:
            mask = cjk_mask(text)
            blit_mask(img, mask, cursor, y + (line_h - mask.height) // 2, color)
            cursor += mask.width + 6
        else:
            end = blit_text(img, text, cursor, y + (line_h - 7) // 2, color)
            cursor = end + 5
    return cursor - 6


def mixed_width(parts):
    probe = new_canvas(512, 32, CLEAR)
    return blit_mixed(probe, parts, 0, 0)


def make_banner_zh():
    """Chinese nameplate on the same frame, dot grid and robot as the English banner."""
    w, h = 320, 100
    img = make_banner(w, h).resize((w, h), Image.NEAREST)
    # Clear the English text area, keeping frame, dots and robot.
    for x in range(30, w - 4):
        for y in range(4, h - 4):
            px(img, x, y, INK)
    for x in range(28, w - 4, 8):
        for y in range(4, h - 4, 8):
            px(img, x, y, DIM)

    # Name at 2x like the English title, glyph by glyph with the same wide tracking.
    glyphs = [scale_nn(cjk_mask(ch).convert("RGBA"), 2).getchannel("R") for ch in "王宇堃"]
    tw = sum(g.width for g in glyphs) + 8 * (len(glyphs) - 1)
    tx = (w - tw) // 2 + 10
    for g in glyphs:
        blit_mask(img, g, tx, 12 + (30 - g.height) // 2, CREAM)
        tx += g.width + 8

    school = [("UCL MENG ROBOTICS & AI", GOLD, False)]
    sw = mixed_width(school)
    sx = (w - sw) // 2 + 10
    for x in range(sx - 4, sx + sw + 4):
        px(img, x, 50, SLATE)
    blit_mixed(img, school, sx, 58, line_h=7)

    roles = [("机器人学习", CREAM, True), ("/", CREAM, False), ("具身智能", CREAM, True)]
    rw = mixed_width(roles)
    rx = (w - rw) // 2 + 10
    blit_mixed(img, roles, rx, 76, line_h=15)

    return scale_nn(img, 5)


def make_divider():
    w, h = 160, 5
    img = new_canvas(w, h, CLEAR)
    for x in range(0, w, 4):
        px(img, x, 2, SLATE)
        px(img, x + 1, 2, GOLD)
    return scale_nn(img, 3)


def write_png(img, path):
    path.parent.mkdir(parents=True, exist_ok=True)
    img.save(path, "PNG")
    print(f"wrote {path.relative_to(ROOT)} ({img.width}x{img.height})")


def main():
    banner = make_banner()
    divider = make_divider()
    write_png(banner, ASSETS / "banner.png")
    write_png(make_banner_zh(), ASSETS / "banner-zh.png")
    write_png(divider, ASSETS / "divider.png")
    write_png(banner, PROFILE_ASSETS / "banner.png")
    write_png(divider, PROFILE_ASSETS / "divider.png")

    for name in ICONS_16:
        tile = make_icon_tile(name, scale=3)
        plain = make_plain_icon(name, scale=2)
        write_png(tile, ICONS / f"{name}.png")
        write_png(tile, PROFILE_ICONS / f"{name}.png")
        write_png(plain, ICONS / "plain" / f"{name}.png")
        write_png(plain, PROFILE_ICONS / "plain" / f"{name}.png")


if __name__ == "__main__":
    main()
