class Solution {

    public List<List<Integer>> getAncestors(int n, int[][] edges) {
        // Initialize adjacency list for each node and ancestors list
        List<Integer>[] adjacencyList = new ArrayList[n];
        List<List<Integer>> ancestors = new ArrayList<>();

        // Initialize adjacency list and ancestors list for each node
        for (int i = 0; i < n; i++) {
            adjacencyList[i] = new ArrayList<>();
            ancestors.add(new ArrayList<>());
        }

        // Populate the adjacency list with edges
        for (int[] edge : edges) {
            int from = edge[0];
            int to = edge[1];
            adjacencyList[from].add(to);
        }

        // Perform DFS for each node to find all its ancestors
        for (int i = 0; i < n; i++) {
            findAncestorsDFS(i, adjacencyList, i, ancestors);
        }

        return ancestors;
    }

    // Helper method to perform DFS and find ancestors
    private void findAncestorsDFS(
        int ancestor,
        List<Integer>[] adjacencyList,
        int currentNode,
        List<List<Integer>> ancestors
    ) {
        for (int childNode : adjacencyList[currentNode]) {
            // Check if the ancestor is already added to avoid duplicates
            if (
                ancestors.get(childNode).isEmpty() ||
                ancestors
                        .get(childNode)
                        .get(ancestors.get(childNode).size() - 1) !=
                    ancestor
            ) {
                ancestors.get(childNode).add(ancestor);
                findAncestorsDFS(ancestor, adjacencyList, childNode, ancestors);
            }
        }
    }
}