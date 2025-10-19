class Solution {
    private String smallest;
    private Set<String> visited;
    private int a, b, n;

    public String findLexSmallestString(String s, int a, int b) {
        smallest = s;
        visited = new HashSet<>();
        this.a = a;
        this.b = b;
        this.n = s.length();
        dfs(s);
        return smallest;
    }

    private void dfs(String s) {
        if (!visited.add(s)) return;  // already visited

        // Update smallest if current string is smaller
        if (s.compareTo(smallest) < 0) {
            smallest = s;
        }

        // Operation 1: Add 'a' to digits at odd indices
        char[] arr = s.toCharArray();
        for (int i = 1; i < n; i += 2) {
            arr[i] = (char) (((arr[i] - '0' + a) % 10) + '0');
        }
        dfs(new String(arr));

        // Operation 2: Rotate right by 'b'
        String rotated = s.substring(n - b) + s.substring(0, n - b);
        dfs(rotated);
    }
}
