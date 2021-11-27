public class SingleLinkedList<T> {
    public Node<T> head = null;

    public class Node<T> {
        T data;
        Node<T> next = null;

        public Node(T data) {
            this.data = data;
        }
    }

    // 링크드 리스트에 데이터 추가하기
    public void addNode (T data) {
        if (head == null) {
            head = new Node<T>(data);
        } else {
            Node<T> node = this.head;
            while (node.next != null) {
                node = node.next;
            }
            node.next = new Node<T>(data);
        }
    }

    public void printAll() {
        if (head == null) {
            return;
        }

        Node<T> node = this.head;
        while (node != null) {
            System.out.println(node.data);
            node = node.next;
        }
    }

    public Node<T> search(T data) {
        if (this.head == null) {
            return null;
        } else {
            Node<T> tmpNode = this.head;
            while (tmpNode != null && tmpNode.data != data) {
                tmpNode = tmpNode.next;
            }
            return tmpNode;
        }
    }

    public void addNodeInside(T data, T preData) {
        Node<T> searchedNode = this.search(preData);

        if (searchedNode == null) {
            this.addNode(data);
        } else {
            Node<T> nextNode = searchedNode.next;
            Node<T> insertNode = new Node<T>(data);
            searchedNode.next = insertNode;
            insertNode.next = nextNode;
        }
    }

    public boolean delNode(T tarData) {
        if (this.head == null) {
            return false;
        }
        if (this.head.data == tarData) {
            Node<T> nodeToRemove = this.head;
            this.head = this.head.next;
            nodeToRemove = null;
        }

        Node<T> preNode = this.head;
        Node<T> curNode = this.head.next;
        while (true) {
            if (curNode.data == tarData) {
                // 삭제
                node<T> nextNode = curNode.next;
                preNode.next = nextNode;
                curNode = null;
                return true;
            }
            preNode = curNode;
            curNode = curNode.next;
            if (curNode == null) {
                return false;
            }
        }
    }
}