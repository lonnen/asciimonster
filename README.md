# asciimonster

a cli tool for ingesting a file and vomiting out ascii character stats.

This is not intended to be a robust or general tool. It can probably be replaced with a bash one-liner. This is a quick 'n dirty tool for deriving a dataset to help with solving the [cryptopals](https://www.cryptopals.com/) challenge sets.

The Project Gutenberg text of Don Quixote is included in the `data/` folder and licensed under the Project Gutenberg License.

## Installation

Install this tool using `pip`:
```bash
pip install asciimonster
```
## Usage

```bash
asciimonster data/pg996.txt > pg996.csv
```

results in the output file:

```csv
32,  , 395378, 17.05
33, !, 665, 0.03
34, ", 0, 0.00
35, #, 1, 0.00
36, $, 2, 0.00
37, %, 1, 0.00
38, &, 1, 0.00
39, ', 0, 0.00
40, (, 573, 0.02
41, ), 573, 0.02
42, *, 12, 0.00
43, +, 0, 0.00
44, ,, 36919, 1.59
45, -, 1802, 0.08
46, ., 8416, 0.36
47, /, 7, 0.00
48, 0, 189, 0.01
49, 1, 417, 0.02
50, 2, 257, 0.01
51, 3, 269, 0.01
52, 4, 213, 0.01
53, 5, 182, 0.01
54, 6, 161, 0.01
55, 7, 131, 0.01
56, 8, 127, 0.01
57, 9, 118, 0.01
58, :, 370, 0.02
59, ;, 6059, 0.26
60, <, 0, 0.00
61, =, 0, 0.00
62, >, 0, 0.00
63, ?, 967, 0.04
64, @, 0, 0.00
65, A, 4004, 0.17
66, B, 1239, 0.05
67, C, 2371, 0.10
68, D, 4732, 0.20
69, E, 3586, 0.15
70, F, 1548, 0.07
71, G, 1490, 0.06
72, H, 3091, 0.13
73, I, 9614, 0.41
74, J, 187, 0.01
75, K, 627, 0.03
76, L, 1840, 0.08
77, M, 1591, 0.07
78, N, 2179, 0.09
79, O, 2504, 0.11
80, P, 1415, 0.06
81, Q, 2460, 0.11
82, R, 2306, 0.10
83, S, 5061, 0.22
84, T, 5694, 0.25
85, U, 752, 0.03
86, V, 539, 0.02
87, W, 1506, 0.06
88, X, 509, 0.02
89, Y, 402, 0.02
90, Z, 163, 0.01
91, [, 1, 0.00
92, \, 0, 0.00
93, ], 1, 0.00
94, ^, 0, 0.00
95, _, 220, 0.01
96, `, 0, 0.00
97, a, 145072, 6.26
98, b, 24352, 1.05
99, c, 39043, 1.68
100, d, 76884, 3.32
101, e, 216339, 9.33
102, f, 40477, 1.75
103, g, 33143, 1.43
104, h, 122293, 5.27
105, i, 112558, 4.85
106, j, 1841, 0.08
107, k, 12267, 0.53
108, l, 65473, 2.82
109, m, 44255, 1.91
110, n, 121943, 5.26
111, o, 144498, 6.23
112, p, 25469, 1.10
113, q, 1754, 0.08
114, r, 97884, 4.22
115, s, 109991, 4.74
116, t, 163823, 7.07
117, u, 49667, 2.14
118, v, 18165, 0.78
119, w, 39133, 1.69
120, x, 4058, 0.18
121, y, 32865, 1.42
122, z, 1204, 0.05
123, {, 0, 0.00
124, |, 0, 0.00
125, }, 0, 0.00
126, ~, 0, 0.00
```


For help, run:
```bash
asciimonster --help
```
You can also use:
```bash
python -m asciimonster --help
```
## Development

To contribute to this tool, first checkout the code. Then create a new virtual environment:
```bash
cd asciimonster
python -m venv venv
source venv/bin/activate
```
Now install the dependencies and test dependencies:
```bash
pip install -e '.[test]'
```
To run the tests:
```bash
python -m pytest
```
