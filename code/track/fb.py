def merge(A, B):
    i = 0
    j = 0
    res = []
    while i < len(A) or j < len(B):
        if i==len(A):
            curr = B[j]
            j+=1
        elif j==len(B):
            curr = A[i]
            i+=1
        elif A[i][0] < B[j][0]:
            curr = A[i]
            i+=1
        else:
            curr = B[j]
            j+=1
        if res and res[-1][-1] >= curr[0]:
            res[-1][-1] = max(res[-1][-1],curr[-1])
        else:
            res.append(curr)
    return res

print(merge([[1,5],[10,14],[16,18]], [[2,6],[8,10],[11,20]]))

'''
sorted list iterator
'''
class GentNextMin:
    def __init__(self, l1, l2, l3):
        self.heap = []
        
        if l1:
            l1.sort(key=lambda x : -x)
            heapq.heappush(self.heap, (l1.pop(), l1))
        if l2:
            l2.sort(key=lambda x : -x)
            heapq.heappush(self.heap, (l2.pop(), l2))
        if l3:
            l3.sort(key=lambda x : -x)
            heapq.heappush(self.heap, (l3.pop(), l3))
    
    def has_next(self):
        if self.heap:
            return True
        return False
    
    def next(self):
        if not self.has_next():
            raise Exception()
        
        e, l = heapq.heappop(self.heap)
        if l:
            heapq.heappush(self.heap, (l.pop(), l))
        return e

'''
validate signal binary tree

1. There can be one and only one root
2. All nodes should have only one indegree, except the root node, which has zero indegree
3. Check if there any node missed from the given list (example 5)


    public boolean isBinaryTree(List<TreeNode> nodes) {
        Map<TreeNode, Integer> degree = new HashMap<>();
        for (TreeNode node : nodes) { 
            if (node.left != null) degree.put(node.left, degree.getOrDefault(node.left, 0) + 1);
            if (node.right != null) degree.put(node.right, degree.getOrDefault(node.right, 0) + 1);         
        }
        TreeNode root = null;
        for (TreeNode node : nodes) {
            if (!degree.containsKey(node)) {
                if (root == null) root = node;
                else return false; 
            } else if (degree.get(node) != 1) 
                return false; 
        }
        return root != null && nodes.size() == degree.keySet().size() + 1;
'''

##########################
'''
task schedular 计算时间的版本

tasks: ["1", "2", "1", "1", "3", "4"]

1, 2, _, 1, _, _, 1, 3, 4 = 9
'''
def schedule(tasks, cooldown):
    if not tasks:
        return 0
    time = {}

    curtime = 0
    for task in tasks:
        ## 说明当前时间没到cooldown, 那么就把当前时间直接跳到cool down的时间
        if task in time and time[task] > curtime:
            curtime = time[task]
        ## 下一次再执行此任务时的时间
        time[task] = curtime + cooldown + 1
        ## 执行此任务，时间 + 1
        curtime += 1
    return curtime

'''
task schedular 输出字符串版本

tasks: ["1", "2", "1", "1", "3", "4"]

1, 2, _, 1, _, _, 1, 3, 4 = 9
'''
def schedule2(tasks, cooldown):
    if not tasks:
        return 0
    time = {}
    res = []
    curtime = 0
    for task in tasks:
        ## 说明当前时间没到cooldown, 那么就把当前时间直接跳到cool down的时间
        if task in time and time[task] > curtime:
            waitingTime = time[task] - curtime
            while waitingTime > 0:
                res.append("_")
                waitingTime -= 1
            curtime = time[task]
        ## 下一次再执行此任务时的时间
        time[task] = curtime + cooldown + 1
        ## 执行此任务，时间 + 1
        curtime += 1
        res.append(task)
    return ", ".join(res)

print(schedule2(["1", "2", "1", "1", "3", "4"], 3))

'''
- Find an efficient way to represent a vector (1,1,1,1,1,1,22,2,2,2,2,2,2,2,3,4,4,5,6,6,7,7,7,8,8,8,9,9,9,99,9,,1,1,1,1,1,1,2,3,34,3,4,,3,3,3,3....)
- Use the representation you come up with to compute dot product of two vectors
Ex: If you come up with MyDataStructure to represent a vector, then your function signature will be
int dotProduct(MyDataStructure vector1, MyDataStructure vector2)
// dot product of two vectors [1,2,3,4] and [5,6,7,8] is 1 * 5 + 2 * 6 + 3 * 7 + 4 * 8
Take advantage of your "efficient" representation to compute the dot product faster.

'''
## A: [1, 1, 4, 4, 4, 4, 7, 7, 7, 7, 7, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
## B: [2, 2, 5, 5, 5, 5, 5, 5, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
class compressVector:
    def __init__(self, vec):
        self.compressed = self.compress(vec)

    def compress(self, vec):

        res = []
        i = 0
        while i < len(vec):
            val = vec[i]
            count = 1

            while i < len(vec) - 1 and vec[i + 1] == val:
                count += 1
                i += 1
            
            res.append([count, val])
            i += 1
        return res

def calculate(vector1, vector2):
    vector1 = compressVector(vector1).compressed
    vector2 = compressVector(vector2).compressed
    ### vector1 = [[2, 1], [4, 4], [5, 7], [10, 2]]
    ### vector2 = [[2, 2], [7, 5], [12, 3]]

    dotProduct = 0
    i = 0
    j = 0
    while i < len(vector1) and j < len(vector2):
        a = vector1[i]
        b = vector2[j]

        multiplier = min(a[0], b[0])
        a[0] -= multiplier
        b[0] -= multiplier

        dotProduct += multiplier * a[1] * b[1]

        if a[0] == 0:
            i += 1
        if b[0] == 0:
            j += 1
    return dotProduct

print(calculate([1, 1, 4, 4, 4, 4, 7, 7, 7, 7, 7, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 5, 5, 5, 5, 5, 5, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]))

'''
intersection (one list) https://leetcode.com/discuss/interview-question/338948/Facebook-or-Onsite-or-Schedule-of-Tasks

You are given a shcedule of tasks to work on. Each tasks has a start and an end time [start, end] where end > start. 
Find out for the given schedule:

in what intervals you are working (at least 1 task ongoing)
in what intervals you are multitasking (at least 2 tasks ongoing)

    |--------------|
    3             12
  |----|
  2    6
|-----------|
1           10
以上应该是 [2, 10]

cases: 
[[1,10], [2,6], [9,12], [14,16], [16,17]] multiTasking=[[2,6], [9,10]]}
[[1,10], [2,6], [3,7], [4,8]] multiTasking=[[2,8]]}
[[1,2], [3,4], [5,6], [7,8]] multiTasking=[]}
'''

def intersection(intervals):
    if not intervals:
        return []

    intervals.sort()
    prevStart = intervals[0][0]
    prevEnd = intervals[0][1]

    i = 1
    ans = []
    while i < len(intervals):
        curStart = intervals[i][0]
        curEnd = intervals[i][1]

        low = max(prevStart, curStart)
        high = min(prevEnd, curEnd)

        # intersection found
        if low < high: # 没有等于
            if ans and ans[-1][1] == low: # merge intersection with previous intersection if needed
                ans[-1][1] = high

            else:
                ans.append([low, high])
            
            prevStart = high
            prevEnd = max(prevEnd, curEnd) # important!
        else:
            prevStart = curStart
            prevEnd = curEnd
        
        i += 1
    return ans

print(intersection([[1,10], [2,6], [3,12], [4,8]]))


'''
Calculate tax if Salary and Tax Brackets are given as: calculateTax(double salary, Double[][] brackets)
e.g. Salary = 35000
Brackets = [ [10000, 0.1],[20000, 0.2], [10000, 0.3], [null, .4]]
null being rest of the salary


  static double calculateTax2(Map<Double, Double> itSlabMap, double income) {
        double tax = 0d;

        for (Map.Entry<Double, Double> entry : itSlabMap.entrySet()) {
            if (income >= entry.getKey()) {
                tax += entry.getValue() * entry.getKey();
                income -= entry.getKey();
            } 
            // final residual of tax on highest slab
            else if (tax != 0) {
                tax += entry.getValue() * income;
                break;
            } 
            // when income is lesser than first slab
             else {
                return tax;
            }
        }
        return tax;
    }
'''

'''

Given a matrix, return all elements of the matrix in antidiagonal order as shown in the below image.
https://leetcode.com/discuss/interview-question/346342/

vector<vector<int>> solve(vector<vector<int>>&a, int row, int col) {
    if (a.size() == 0)
        return {};
    vector<vector<int>> result(a.size() + a[0].size());
    
    for (int i = 0; i < a.size(); ++i) {
        for (int j = 0; j < a[0].size(); ++j) {
            result[i + j].push_back(a[i][j]);
        }
    }
    return result;
}
'''
'''
n-ary Tree with each node having a boolean flag. 
Traverse all the nodes with only boolean flag = True. Return the total distance traveled from root to all those nodes.

int traverseNodes(const Node *&node)
{
      if(node->val == false)
          return 0;

      int result = 1;
      for(int i = 0; i < node->subnodes.size(); ++i)
      {
        result += traverseNodes(node->subnodes[i]);
      }
      return result;
}

traverseNodes(root);
'''

from typing import List

class Node:
    def __init__(self, char):
        self.char = char
        self.children = [None]*26
        self.isWord = False
        
class Trie:
    def __init__(self):
        self.root = Node("")
        

    def insert(self, word: str) -> None:
        curNode = self.root
        for i, c in enumerate(word):
            nextNode = curNode.children[ord(c) - ord('a')]
            if not nextNode:
                curNode.children[ord(c) - ord('a')] = Node(c)
                nextNode = curNode.children[ord(c) - ord('a')]
            curNode = nextNode
            if i == len(word) - 1:
                curNode.isWord = True
        
    def findPrefixPairs(self) -> List[List[str]]:
        prefixPairs = []
        subWords = []
        self._findPrefixPairs(self.root, '', prefixPairs, subWords)
        return prefixPairs
        
    def _findPrefixPairs(self, node: Node, stringSoFar: str, prefixPairs: List[List[str]], subWords: List[str]) -> None:
        stringSoFar += node.char
        
        for iChar, charNode in enumerate(node.children):
            if charNode:
                subWordsFromHere = []
                self._findPrefixPairs(charNode, stringSoFar, prefixPairs, subWordsFromHere)
                if node.isWord:
                    prefixPairs.extend([[stringSoFar, subWord] for subWord in subWordsFromHere])
                subWords.extend(subWordsFromHere)
                    
        if node.isWord:
            subWords.append(stringSoFar)
            
words = ["abs","app","be","apple","bee","better","bet","absolute"]

trie = Trie()
for word in words:
    trie.insert(word)
    
output = trie.findPrefixPairs()

print(output)

'''
Design a data structure for History Set
Add(element) : Adds an element to the Set and returns a SequenceId
Discard(element): Discards an element from the Set and returns a SequenceId
Member(sequenceId): Return the state of historySet at a given sequenceId

Example:
seq1 = add("a")
seq2 = add("b")
seq3 = add("c")
seq4 = discard("b")

member(seq3) = ("a", "b", "c")
member(seq1) = ("a")
member(seq4) = ("a", "c")
'''
class HistorySet:
    def __init__(self):
        self.history = {}
        self.seq_id = 0

    def add(self, element):
        self.seq_id += 1
        self.history[self.seq_id] = ['add', element]
        return self.seq_id
    
    def discard(self, element):
        self.seq_id += 1
        self.history[self.seq_id] = ['discard', element]
        return self.seq_id
    
    def member(self, seq_id):
        s = set()
        
        # Implementor's choice
        if len(self.history.keys()) < seq_id:
            return None
        
        for key, value in self.history.items():
            if key > seq_id:
                return s
            if value[0] == 'add':
                s.add(value[1])
            elif value[0] == 'discard':
                s.discard(value[1])
        return s

'''

Print All Paths in a 2D Board

public class Solution {
    private int m;
    private int n;
    public int numIslands(char[][] grid) {
        int count=0;
        m=grid.length;
        if(m==0) return 0;
        n=grid[0].length;
        dfs(grid,0,0,"");
    }
    public void dfs(char[][] grid,int i,int j,String s){
        if(i>m||j>n) return;
        if(i==m&&j==n) print(s+grid[i][j]);
        dfs(grid,i,j+1,s+grid[i][j]+"->");
        dfs(grid,i+1,j,s+grid[i][j]+"->");
    }
}
'''
res = []
def printPath(grid):
    global res
    m = len(grid)
    n = len(grid[0])

    dfs(grid, 0, 0, "")

def dfs(grid, x, y, path):
    global res

    if x >= len(grid) or y >= len(grid[0]):
        return
    if x == len(grid) - 1 and y == len(grid[0]) - 1:
        print(path + str(grid[x][y]))
    
    dfs(grid, x, y + 1, path + str(grid[x][y]) + "->")
    dfs(grid, x + 1, y, path + str(grid[x][y]) + "->")

print(printPath([[0,1,2],[3,4,5],[6,7,8]]))