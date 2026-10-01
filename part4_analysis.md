Let:
* $n$ = grid size (number of rows and columns)
* $a$ = number of currently active (ringing) strings

## 1. Running time summary
**Table 1. Summary of optimized methods running time.**
| Operation | Original Time | Optimized Time |
|-|-|-|
| `__init__` | $O(n)$ | $O(n)$ |
| `next_sample()` | $O(n)$ | $O(a)$ |
| `pluck_column(col)` | $O(n)$ | $O(n)$ |
| `_retire_quiet_row()` | N/A | $O(1)$ |
| `clear()` | $O(n^2)$ | $O(n^2)$ |
| `resize(new_size)` | $O(n_{min}^2 + n_{new}^2)$ | $O(n_{min}^2 + n_{new}^2)$ |

## 2. Arguments for each bound
#### `__init__`
* **Original:** $O(n^2)$
* **Optimized:** $O(n^2)$
* **Explanation:** Both the original and optimized versions use a 1D grid array of size $n^2$ and instantiate $n$ `StringInstrument` objects, which requirs $O(n^2)$ time. While the optimized version stores extra attributes (`self.active_rows`, `self._energy_check_index`), these take $O(1)$ and do not change the Big O bound.

#### `clear`
* **Original:** $O(n^2)$
* **Optimized:** $O(n^2)$
* **Explanation:** Both versions iterate $n^2$ times to set every cell in `self.grid` to `False`. The optimized version does call `self.active_rows.clear()`, but this executes in $O(1)$ constant time and does not change Big O bound.

#### `next_sample`
* **Original:** $O(n)$
* **Optimized:** $O(a)$
* **Explanation:** The original implementation iterates through all $n$ instruments on every single sample frame. The optimized version loops exclusively over $a$ instruments in `self.active_rows`, reducing the number of iterations to $O(a)$ iterations. Overall, the Big O is reduced from $n$ to $a$.

#### `pluck_column`
* **Original:** $O(n)$
* **Optimized:** $O(n)$
* **Explanation:** Both methods execute a loop of $n$ iterations (one for each row in the given column). For the optimized version, lit cells are checked for `row not in self.active_rows`, which requires an $O(a)$ to iterate through the active strings. However, the Big O is unchanged since $n \ge a$.

#### `_retire_quiet_row`
* **Original:** does not exist
* **Optimized:** $O(1)$
* **Explanation:** In the original version, this method does not exist. In the optimized version, retire_quiet_row checks the energy of one row at a time. If the row is quiet, it removes it from `self.active_rows` using `pop()` on the last element and replaces the removed position with the last row, avoiding the element shifting that would occur with a normal list removal. All operations performed by the method take constant time, so the method runs in $O(1)$ time.

#### `resize`
* **Original:** $O(n_{min}^2 + n_{new}^2)$
* **Optimized:** $O(n_{min}^2 + n_{new}^2)$
* **Explanation:** Copying the existing active cells requires iterating through the $n_{min} \times n_{min}$ overlap region with ($O(n_{min}^2$ time). Allocating the new flat grid and rebuilding the instrument list requires $O(n_{min}^2  + n_{min})$ steps. In the optimized version, repopulating `self.active_rows` takes an extra $O(n_{min})$ check, which is completely dominated by $O(n_{\text{new}}^2)$. Therefore, Big O is the same for the original and optimized implementations.

## 3. Benchmark results of the original and optimized implementations
**Table 2. Benchmark results for the original and optimized implementations.**
| Size | Density | Original:<br>μs/sample | Optimized:<br>μs/sample | Original: x realtime | Optimized: x realtime |
|-|-|-|-|-|-|
| 8 | 0.05 | 4.992  | 0.426 | 4.54 | 53.27 |
| 8 | 0.25 | 5.138  | 3.878 | 4.41 | 5.85 |
| 16 | 0.05 | 9.918  | 2.877 | 2.29 | 7.88 |
| 16 | 0.25 | 9.921  | 8.601 | 2.29 | 2.64 |
| 32 | 0.05 | 19.527 | 11.025 | 1.16 | 2.06 |
| 32 | 0.25 | 16.671 | 17.729 | 1.15 | 1.28 |
| 64 | 0.05 | 39.883 | 26.922 | 0.57 | 0.84 |
| 64 | 0.25 | 41.109 | 37.485 | 0.55 | 0.60 |

\
**Table 3. Extended benchmark results (density 0.5, 0.75, and 1.0) for the original and optimized implementations.**
| Size | Density | Original:<br>μs/sample | Optimized:<br>μs/sample | Original: x realtime | Optimized: x realtime |
|-|-|-|-|-|-|
| 8    | 0.50 | 4.956  | 4.490 | 4.58 | 5.05 |
| 8    | 0.75 | 5.039  | 5.009 | 4.50 | 4.53 |
| 8    | 1.00 | 5.224  | 5.073 | 4.34 | 4.47 |
| 16   | 0.50 | 9.705  | 9.614 | 2.34 | 2.36 |
| 16   | 0.75 | 9.578  | 9.721 | 2.37 | 2.33 |
| 16   | 1.00 | 9.630  | 9.891 | 2.35 | 2.29 |
| 32   | 0.50 | 19.025 | 18.827 | 1.19 | 1.20 |
| 32   | 0.75 | 19.137 | 19.142 | 1.18 | 1.18 |
| 32   | 1.00 | 19.322 | 19.438 | 1.17 | 1.17 |
| 64   | 0.50 | 37.572 | 38.951 | 0.60 | 0.58 |
| 64   | 0.75 | 38.172 | 39.425 | 0.59 | 0.58 |
| 64   | 1.00 | 38.061 | 39.600 | 0.60 | 0.57 |

## 4. When the optimized version is worse
* For sure faster when a = n, but in some cases 0.5 density, greater na si 32. ewan basta.