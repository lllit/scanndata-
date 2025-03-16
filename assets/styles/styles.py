import flet as ft


PADDING_TOP = 3



colors = [
    "#424454",
    "#393b52",
    "#33354a",
    "#2f3143",
    "#292b3c",
    "#222331",
    "#1a1a25",
    "#1a1b26",
    "#21222f",
    "#1d1e2a"
]

css = """
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f4;
}
.container {
    width: 80%;
    margin: auto;
    overflow: hidden;
}
header {
    background: #333;
    color: #fff;
    padding-top: 30px;
    min-height: 70px;
    border-bottom: #77aaff 3px solid;
}
header a {
    color: #fff;
    text-decoration: none;
    text-transform: uppercase;
    font-size: 16px;
}
.main {
    padding: 20px;
    background: #fff;
    margin-top: 20px;
}
table {
    width: 100%;
    margin-bottom: 20px;
    border-collapse: collapse;
}
table, th, td {
    border: 1px solid #ddd;
}
th, td {
    padding: 8px;
    text-align: left;
}
th {
    background-color: #f2f2f2;
}
.total {
    text-align: right;
    padding-right: 20px;
}

"""