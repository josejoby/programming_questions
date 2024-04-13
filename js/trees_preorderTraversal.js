class Node {
    constructor(value, left, right) {
        this.value = value;
        this.left = left;
        this.right = right;
    }
}

/*

   1
  / \
 6   2
    /
   3

expected output = 1 6 2 3
*/

rootNode = new Node(1)
rootNode.left = new Node(6)
r1 = new Node(2)
r1.left = new Node(3)
rootNode.right = r1

function processNode(node) {
    console.log(node.value)
}

function preorderTraversal(node) {
    if (node) {
        processNode(node)
        preorderTraversal(node.left)
        preorderTraversal(node.right)
    }
}

preorderTraversal(rootNode)
